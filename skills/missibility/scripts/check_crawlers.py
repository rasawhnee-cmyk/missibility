#!/usr/bin/env python3
"""Check robots.txt rules for search and AI crawlers on one or more hosts.

Usage:
    python3 check_crawlers.py example.com [docs.example.com ...] [--path /products/]

Reports, per host, whether each crawler may fetch "/" and an optional sample path.
robots.txt "allowed" does not prove the crawler can reach the site: WAF/CDN bot
rules can still block it. User-triggered fetchers (ChatGPT-User, Perplexity-User)
may not follow robots.txt at all. Stdlib only.
"""
import argparse
import sys
import urllib.error
import urllib.request
import urllib.robotparser

CRAWLERS = [
    # (user-agent token, platform, purpose)
    ("Googlebot", "Google", "search"),
    ("Google-Extended", "Google", "Gemini training/grounding (not Search)"),
    ("Bingbot", "Microsoft", "search + Copilot grounding"),
    ("OAI-SearchBot", "OpenAI", "ChatGPT Search"),
    ("GPTBot", "OpenAI", "training"),
    ("ChatGPT-User", "OpenAI", "user-triggered (robots may not apply)"),
    ("PerplexityBot", "Perplexity", "search"),
    ("Perplexity-User", "Perplexity", "user-triggered (generally ignores robots)"),
    ("Claude-SearchBot", "Anthropic", "search"),
    ("ClaudeBot", "Anthropic", "training"),
    ("Claude-User", "Anthropic", "user-triggered"),
    ("CCBot", "Common Crawl", "open dataset (used by many models)"),
]


def fetch_robots(host):
    host = host.strip().rstrip("/")
    if not host.startswith("http"):
        host = "https://" + host
    url = host + "/robots.txt"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (missibility robots check)"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return url, resp.status, body
    except urllib.error.HTTPError as e:
        return url, e.code, ""
    except Exception as e:  # network, TLS, DNS
        return url, None, f"ERROR: {e}"


SEARCH_ENGINES = ["Googlebot", "Bingbot", "DuckDuckBot", "Applebot", "YandexBot", "Baiduspider",
                  "PetalBot", "OAI-SearchBot", "PerplexityBot", "Claude-SearchBot"]
KNOWN_DIRECTIVES = {"user-agent", "disallow", "allow", "sitemap", "crawl-delay", "host",
                    "clean-param", "content-signal"}


def lint(body, rp, base):
    """Flag problems a pass/fail table hides."""
    issues = []
    groups, current = [], None
    for n, raw in enumerate(body.splitlines(), 1):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        if ":" not in line:
            issues.append(f"line {n}: not a 'field: value' line -> {raw.strip()!r}")
            continue
        field, value = (s.strip() for s in line.split(":", 1))
        f = field.lower()
        if f not in KNOWN_DIRECTIVES:
            issues.append(f"line {n}: unknown directive '{field}' (ignored by most crawlers)")
        if f == "user-agent":
            if current is None or current["rules"]:
                current = {"agents": [], "rules": []}
                groups.append(current)
            current["agents"].append(value)
        elif f in ("allow", "disallow"):
            if value and not value.startswith(("/", "*")):
                issues.append(f"line {n}: '{field}: {value}' must be a path starting with '/' — "
                              "robots.txt cannot block a hostname or full URL; it is ignored")
            if current is None:
                issues.append(f"line {n}: rule before any User-agent line")
            else:
                current["rules"].append((f, value))
    for g in groups:
        if "*" in g["agents"] and ("disallow", "/") in g["rules"]:
            issues.append("Default-deny: 'User-agent: *' + 'Disallow: /' blocks every crawler not named "
                          "elsewhere, including search engines nobody listed. Confirm this is intended.")
    blocked = [ua for ua in SEARCH_ENGINES if not rp.can_fetch(ua, base + "/")]
    if blocked:
        issues.append("Search/answer crawlers blocked at '/': " + ", ".join(blocked) +
                      " — this removes visibility on those engines.")
    return issues


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("hosts", nargs="+", help="domains or subdomains, e.g. example.com docs.example.com")
    ap.add_argument("--path", default=None, help="extra path to test, e.g. /blog/")
    args = ap.parse_args()

    for host in args.hosts:
        url, status, body = fetch_robots(host)
        print(f"\n=== {url}  (HTTP {status}) ===")
        if status is None:
            print(body)
            print("Could not fetch robots.txt — check DNS/TLS/WAF. A WAF challenge here often blocks bots too.")
            continue
        if status >= 500:
            print("Server error on robots.txt: Google treats persistent 5xx as 'disallow all'. Fix urgently (P0).")
            continue
        if status in (401, 403):
            print("robots.txt is access-restricted (401/403) — likely WAF/bot protection. Verify crawler access.")
            continue
        if status == 404 or not body.strip():
            print("No robots.txt (404/empty): all crawlers allowed by default.")
        rp = urllib.robotparser.RobotFileParser()
        rp.parse(body.splitlines())
        base = url[: -len("/robots.txt")]
        paths = ["/"] + ([args.path] if args.path else [])
        header = f"{'Crawler':<18}{'Platform':<14}{'Purpose':<42}" + "".join(f"{p:<12}" for p in paths)
        print(header)
        print("-" * len(header))
        for ua, platform, purpose in CRAWLERS:
            cells = "".join(f"{('allow' if rp.can_fetch(ua, base + p) else 'BLOCK'):<12}" for p in paths)
            print(f"{ua:<18}{platform:<14}{purpose:<42}{cells}")
        sitemaps = rp.site_maps() or []
        print("Sitemaps declared:", ", ".join(sitemaps) if sitemaps else "none")
        cd = rp.crawl_delay("ClaudeBot")
        if cd:
            print(f"Crawl-delay for ClaudeBot: {cd}")
        issues = lint(body, rp, base)
        print("Lint:" if issues else "Lint: no problems found in raw file.")
        for i in issues:
            print("  !", i)
        print("Raw robots.txt (read it — the table can't show intent, stale rules, or leaked paths):")
        for line in body.splitlines()[:80]:
            print("  |", line)
    print("\nReminder: 'allow' here ≠ reachable. Verify WAF/CDN bot rules against each vendor's published IP ranges.")


if __name__ == "__main__":
    sys.exit(main())

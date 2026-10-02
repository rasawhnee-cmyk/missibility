#!/usr/bin/env python3
"""Missibility score calculator.

Priority Score (inputs 1-5):
    python3 score.py priority --bv 5 --dc 4 --rtw 5 --gap 4 --evidence 3 --effort 3

0-2 rubric scores (pass dimension=value pairs, in any order):
    python3 score.py page Decision_Fit=2 Directness=1 Distinct_Information=0 ...
    python3 score.py citation Eligibility=2 Task_Relevance=2 ...
    python3 score.py list            # show rubrics and dimensions

Scores sort work; they do not replace judgment or predict rankings/citations.
"""
import sys

RUBRICS = {
    "page": ("Page Source Score",
             ["Decision_Fit", "Directness", "Distinct_Information", "Evidence", "Expertise",
              "Structure", "Source_Integrity", "Format_Fit", "Freshness", "Action_Path"],
             [(17, "Strong source"), (13, "Improve"), (9, "Weak source"), (0, "Reconsider the asset")]),
    "citation": ("Citation Readiness Score",
                 ["Eligibility", "Task_Relevance", "Extractability", "Evidence", "Provenance",
                  "Entity_Clarity", "Freshness", "Distinct_Value"],
                 [(14, "Strong readiness"), (10, "Improve"), (6, "Weak readiness"), (0, "Fix fundamentals first")]),
    "entity": ("Entity Consistency Score",
               ["Identity", "Relationships", "Attributes", "Source", "External_Confirmation"], []),
    "completeness": ("Information Completeness Score",
                     ["Decision_Coverage", "Evidence", "Format_Fit", "Relationships", "Commercial_Path"], []),
    "readiness": ("Content Readiness Score",
                  ["Decision", "Source_of_Truth", "Evidence", "Expert_Input", "Asset_Model"],
                  [(8, "Ready for standard commercial production"), (0, "Not ready — fill missing inputs")]),
    "derivative": ("Derivative Value Score",
                   ["Audience", "Format_Advantage", "Distribution", "Business_Value", "Maintenance"],
                   [(8, "Produce"), (5, "Review"), (0, "Skip")]),
    "authority": ("Earned Authority Score",
                  ["Relevance", "Independence", "Source_Quality", "Claim_Support", "Freshness"], []),
    "representation": ("Representation Accuracy Score",
                       ["Identity", "Core_Fact", "Context", "Freshness", "Source_Alignment"],
                       [(9, "Accurate"), (7, "Minor correction opportunity"), (4, "Material weakness"),
                        (0, "Priority remediation")]),
    "system": ("Search Visibility System Score",
               ["Business_Alignment", "Customer_Research", "Technical_Foundation", "Entity_Governance",
                "Source_of_Truth", "Evidence", "Information_Architecture", "AI_Production", "Authority",
                "Cross_Engine_Visibility", "Representation", "Business_Measurement"],
               [(20, "Strong operating system"), (15, "Working system with several gaps"),
                (9, "Fragmented system"), (0, "Foundation first")]),
}


def band(total, bands):
    for floor, label in bands:
        if total >= floor:
            return label
    return ""


def priority(argv):
    vals = {}
    keys = {"--bv": "Business Value", "--dc": "Demand Confidence", "--rtw": "Right to Win",
            "--gap": "Current Gap", "--evidence": "Evidence Strength", "--effort": "Effort"}
    it = iter(argv)
    for a in it:
        if a not in keys:
            sys.exit(f"Unknown arg {a}. Expected {', '.join(keys)}")
        v = int(next(it))
        if not 1 <= v <= 5:
            sys.exit(f"{keys[a]} must be 1-5")
        vals[a] = v
    missing = [k for k in keys if k not in vals]
    if missing:
        sys.exit(f"Missing: {', '.join(missing)}")
    ease = 6 - vals["--effort"]
    total = (vals["--bv"] * 3 + vals["--dc"] * 2 + vals["--rtw"] * 2 + vals["--gap"] * 2
             + vals["--evidence"] + ease)
    for k, label in keys.items():
        print(f"  {label:<20}{vals[k]}")
    print(f"  {'Ease (6-Effort)':<20}{ease}")
    label = band(total, [(45, "Strong priority"), (35, "Good opportunity"), (25, "Needs investigation"),
                         (0, "Usually defer, reject, or revisit")])
    print(f"Priority Score: {total}/55 — {label}")
    print("Apply override rules (compliance risk, no evidence, technical blocker, existing asset, "
          "no business relevance, low Right to Win) before deciding.")


def rubric(name, argv):
    title, dims, bands = RUBRICS[name]
    given = {}
    for pair in argv:
        k, _, v = pair.partition("=")
        match = [d for d in dims if d.lower() == k.lower()]
        if not match:
            sys.exit(f"Unknown dimension '{k}'. Valid: {', '.join(dims)}")
        v = int(v)
        if v not in (0, 1, 2):
            sys.exit(f"{k} must be 0, 1 or 2")
        given[match[0]] = v
    missing = [d for d in dims if d not in given]
    if missing:
        sys.exit(f"Missing dimensions: {', '.join(missing)}")
    total, mx = sum(given.values()), 2 * len(dims)
    for d in dims:
        print(f"  {d.replace('_', ' '):<26}{given[d]}")
    out = f"{title}: {total}/{mx}"
    if bands:
        out += f" — {band(total, bands)}"
    print(out)
    if name == "representation":
        print("Severity overrides the average: any Level 3-4 error is a priority regardless of total.")


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return
    cmd, rest = sys.argv[1], sys.argv[2:]
    if cmd == "priority":
        priority(rest)
    elif cmd == "list":
        for k, (title, dims, _) in RUBRICS.items():
            print(f"{k:<15}{title} (max {2 * len(dims)}): {', '.join(dims)}")
    elif cmd in RUBRICS:
        rubric(cmd, rest)
    else:
        sys.exit(f"Unknown command {cmd}. Use priority, list, or one of: {', '.join(RUBRICS)}")


if __name__ == "__main__":
    main()

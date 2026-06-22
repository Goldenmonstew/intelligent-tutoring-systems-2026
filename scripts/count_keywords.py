#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reproduce the cross-year title-level keyword counts (docs/05-跨年趋势.md).

Usage:
    python3 scripts/count_keywords.py <titles_file>

where <titles_file> contains one paper title per line. Title lists for ITS /
AIED / LAK (2024, 2025) can be reconstructed from the public sources listed in
docs/05-跨年趋势.md (DBLP table-of-contents and the Crossref REST API by volume).

The script prints RAW keyword hits per signal (case-insensitive). Two signals
need an additional documented manual de-biasing step (see
data/cross_year_keywords.csv):
  - signal 5 is a BROAD bundle (SRL / scaffolding / cognitive-load plus
    over-reliance terms); the narrow 'over-reliance / help-timing' sub-topic has
    ~0 title hits, so signal-5 counts should NOT be read as 'over-reliance';
  - signal 6: after excluding generic 'deploy' / 'efficiency', genuine hits are
    0 for ITS and AIED, and 1 each for LAK 2024 / 2025.

Reference genuine counts (after manual de-biasing): data/cross_year_counts.csv
"""
import re
import sys

# Patterns mirror data/cross_year_keywords.csv (matched case-insensitively).
SIGNALS = {
    1: ("Agentic / multi-agent",
        [r"\bagent", r"agentic", r"multi-agent"]),
    2: ("LLM / generative-AI base",
        [r"\bLLM\b", r"\bGPT", r"generative", r"chatbot", r"conversational"]),
    3: ("Trust / responsible / fairness",
        [r"\btrust", r"responsible", r"\bfair", r"\bbias", r"ethic", r"inclusive"]),
    4: ("Knowledge tracing",
        [r"knowledge tracing", r"\bDKT\b", r"\bBKT\b"]),
    5: ("SRL / scaffolding / cognitive-load (broad)",
        [r"over-reliance", r"cognitive load", r"scaffold", r"help-timing",
         r"\bSRL\b", r"self-regulated", r"coaching"]),
    6: ("Local / efficient / on-device deploy",
        [r"\blocal", r"quantiz", r"efficient", r"on-device", r"low-cost",
         r"deploy", r"\bedge\b"]),  # \bedge\b excludes 'knowledge'
    7: ("Affect / multimodal / engagement",
        [r"affect", r"emotion", r"sentiment", r"multimodal", r"\beye", r"gaze",
         r"facial", r"physiological", r"engagement"]),
}


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python3 count_keywords.py <titles_file>")
    titles = [t.strip() for t in open(sys.argv[1], encoding="utf-8") if t.strip()]
    print("titles: %d" % len(titles))
    for sid, (name, pats) in SIGNALS.items():
        rx = re.compile("|".join(pats), re.IGNORECASE)
        hits = sum(1 for t in titles if rx.search(t))
        print("signal %d  %-40s raw_hits=%d" % (sid, name, hits))
    print("\nNote: signals 5 & 6 require the manual de-biasing documented in")
    print("data/cross_year_keywords.csv; genuine counts are in data/cross_year_counts.csv.")


if __name__ == "__main__":
    main()

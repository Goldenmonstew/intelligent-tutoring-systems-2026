# ITS 2026 Conference — Research Analysis

> 中文版本 / Chinese version: [README.md](README.md) · License: text & data [CC BY 4.0](LICENSE), code [MIT](LICENSE)

> The 22nd International Conference on Intelligent Tutoring Systems (**ITS 2026**) was held on 3–5 June 2026 in Paphos, Cyprus (Neapolis University Pafos), under the theme ***Agentic Learning Ecosystems and ITS***.
> This repository is a systematic content analysis of **all 14 public session recordings**, covering **3 keynotes + 71 papers + 8 technical tracks**, with every paper cross-checked against the official conference program.
>
> This is an **independent third-party analysis**; it does not represent the official position of the ITS 2026 organizers, the paper authors, or the publisher.

---

## Key observations

Judging from the conference's **visible agenda**, the evaluative yardstick for intelligent tutoring systems has expanded from "predict more accurately, personalize more strongly" toward "**trustworthy, restrained, affordable, and not harmful to learners**."

- **Large language models (LLMs) are now the most common substrate** — about **49 of 71 papers (69%)** involve an LLM. Among the LLM-related work this year, the focus appears to have shifted from "can we use it" to "**how to use it reliably**" (hallucination control, trustworthy evaluation, local deployment).
- **Agentic / multi-agent designs are the most conspicuous new architectural theme** this year (about **24%**, 17/71), but their high visibility is **substantially amplified by the conference theme** — against ITS's own multi-year title baseline, agentic work has not been rising within ITS itself (see [`docs/05-跨年趋势.md`](docs/05-跨年趋势.md)).
- **The point most worth remembering is not "convergence of directions" but that "evidence from real classrooms, over the long term, with strong causal designs, remains scarce"** — over half of this year's results are still small-sample pilots.

---

## Key figures

> The three coding dimensions (primary track / LLM use / agentic) come from a three-pass coding scheme (see "Method" below); maturity is a single-pass estimate. The full per-paper coding is in [`data/coding.csv`](data/coding.csv).

| Dimension | Finding |
|---|---|
| Scale | 3 keynotes + **71 papers** (18 sessions); fewer were actually presented on the recordings than scheduled (several absent / skipped / title-only) |
| Primary track (single-label) | **T1 Intelligent Tutoring 32% (23/71) ｜ T4 Learning Analytics / Knowledge Tracing 25% (18/71, second-largest) ｜ T7 Generative AI 18% (13/71, third)** |
| LLM penetration | About **69% (49/71)** actually involve an LLM (core method 52%); but only about 28–30% mention it explicitly in the title |
| Agentic | About **24% (17/71)**, the most reliably coded dimension |
| Maturity (single-pass estimate) | Over half are small-sample pilots (n≈5–40 / weak controls); concept-only ~15%; reasonably rigorous evaluation ~25% |

> Note: T7 (18%) is the **single-label primary-track** share, not the share of all papers that use generative AI; hence **T7 18% does not contradict "LLM actually involved 69%"** — many papers use an LLM but have their primary track in T1/T4 etc. Paper IDs follow the official program numbering (not a 1–71 sequence, so there are gaps).

The three keynotes: **Ig Ibert Bittencourt** (from intelligent tutoring to "intelligent caring systems"), **Zachos Anthis** (trust ≠ trustworthiness; "calibrated trust"), **Marco Temperini** (from "search as learning" to "converse for learning").

---

## Repository structure

| File | Contents |
|---|---|
| [`README.md`](README.md) | Chinese version (overview + key figures + navigation) |
| [`README.en.md`](README.en.md) | This file (English) |
| [`docs/01-视频总览.md`](docs/01-视频总览.md) | Overview of the 14 recordings: content, duration, sessions, themes |
| [`docs/02-论文详解.md`](docs/02-论文详解.md) | Per-paper summaries organized by recording/session (71 papers) |
| [`docs/03-研究洞察.md`](docs/03-研究洞察.md) | Research hot topics, technical difficulties, scenario→solution map, integration directions, pitfalls |
| [`docs/04-技术统计.md`](docs/04-技术统计.md) | Precise statistics and agreement for tracks / methods / maturity |
| [`docs/05-跨年趋势.md`](docs/05-跨年趋势.md) | Cross-year calibration against ITS / AIED / LAK 2024–2025 |
| [`docs/06-论文清单与核对.md`](docs/06-论文清单与核对.md) | The 71 papers cross-checked against the official program (ID/title/authors/session) |
| [`data/coding.csv`](data/coding.csv) | Per-paper coding: three coding passes (content / title-A / title-B) + consensus; reproduces all percentages and agreement (κ) |
| [`data/cross_year_keywords.csv`](data/cross_year_keywords.csv) | Keyword rules for the cross-year analysis (7 signals + de-biasing rules) |
| [`data/cross_year_counts.csv`](data/cross_year_counts.csv) | Title-level hit counts across 3 venues × 2 years (with denominators) |
| [`scripts/count_keywords.py`](scripts/count_keywords.py) | Recomputes hits from a title list per the keyword rules (makes the cross-year part reproducible) |

---

## Method & sources

- **Corpus**: the 14 recordings publicly released by the organizers; full subtitle transcripts were extracted (~200k words total). Subtitle timestamps span the full length of each recording (low word counts come from breaks / waiting silence in the live streams, not truncation); however, timeline coverage does not equal semantic completeness, and auto-captions still mis-recognize some names/terms/numbers. **This repository does not redistribute the raw transcripts** — only derived statistics, indexes, and research summaries; the original videos are the copyright of the organizers/platform.
- **Verification**: every paper title, author, and ID was cross-checked against the [official ITS 2026 program](https://iis-international.org/conference-program-2026/).
- **Coding & statistics**: primary track, LLM use, and agentic architecture were coded under **three independent passes** (one informed by report content, two from titles only), with inter-pass agreement reported via **Cohen's κ**; absent/unpresented papers were coded from titles, so track statistics cover all 71 papers. Operational definitions, agreement, and the auditable coding table are in [`docs/04-技术统计.md`](docs/04-技术统计.md) and [`data/coding.csv`](data/coding.csv).
- **Cross-year calibration**: **title-level** keyword matching over the proceedings of ITS (2024/2025), AIED, and LAK, to distinguish "persistent title-level visibility" from "amplification by this year's theme" (not actual full-text adoption rate).

## License

- **Text & data** (docs/, data/, README*): **CC BY 4.0**
- **Code** (scripts/): **MIT**

See [LICENSE](LICENSE). No additional rights are claimed over the underlying recordings, full-text papers, or third-party material; paper titles and author names are included solely for identification and citation, and their pre-existing rights are unaffected.

## Disclaimer

- Subtitles are auto-generated; some names/terms/numbers may be mis-recognized. **Bibliographic details (exact titles/authors) should follow the forthcoming Springer LNCS proceedings.**
- This analysis contains inferences about conference trends, annotated with evidence strength and caveats where possible; conclusions are based on a **single conference**, and extrapolation to long-term field trends should be cautious (see the cross-year document).
- Content is current as of June 2026; for academic reference only.

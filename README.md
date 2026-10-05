<div align="center">

```
  _____               _____       _ _ _               
 |  __ \             / ____|     | (_) |              
 | |  | | _____   __| |     __ _ | |_| |__   ___ _ __ 
 | |  | |/ _ \ \ / /| |    / _` || | | '_ \ / _ \ '__|
 | |__| |  __/\ V / | |___| (_| || | | |_) |  __/ |   
 |_____/ \___| \_/   \_____\__,_||_|_|_.__/ \___|_|   
```

### The Open Source Engineering Seniority & Career Matrix Diagnostic Engine

*Demystify your career ladder. Take a 30-minute sprint or a 2-hour deep dive of adaptive, scenario-based questions, generate interactive radar diagnostics, and chart your promotion roadmap.*

---

[![CI](https://github.com/alisenn/devcaliber/actions/workflows/ci.yml/badge.svg)](https://github.com/alisenn/devcaliber/actions)
[![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[![Live Web Benchmark](https://img.shields.io/badge/Live_App-Launch_DevCaliber_Benchmark-success?style=for-the-badge&logo=googlechrome&logoColor=white)](https://alisenn.github.io/devcaliber/)

[🎓 Live Web App](https://alisenn.github.io/devcaliber/) •
[Features](#-key-features) •
[Quickstart](#-quickstart) •
[Exam Modes](#-examination-modes) •
[Global Leveling](#-global-engineering-leveling-framework) •
[The 5 Pillars](#-the-5-engineering-pillars) •
[CLI Commands](#-cli-reference)

</div>

---

## 💡 Why DevCaliber?

Engineering job titles are notoriously fragmented across tech companies:
- What one startup calls a **"Senior Software Engineer"** is often an **L3 / Mid-level** at Tier-1 tech firms.
- Traditional technical interviews rely on **LeetCode & algorithmic puzzles** that have zero correlation with real engineering craftsmanship, production incident response, or architectural leadership.
- Career progression rubrics are often opaque, political, or buried inside private corporate wikis.

**DevCaliber** bridges this gap as an open-source, community-governed diagnostic engine that benchmarks software engineers through **60 production-style scenario case studies** (12 per pillar), modeled on themes that come up in senior and staff engineering interviews.

---

## ⚡ Key Features

- 🧠 **Computerized Adaptive Testing (CAT) Engine**: Difficulty dynamically adapts step-by-step (+1 / -1) after each question based on your immediate previous response.
- 🏢 **Interview-Style Scenarios**: Case studies including payment idempotency, cache stampede prevention, zero-downtime database migrations, and SLO burn rates.
- 🌐 **Dual-Language Support (English 🇺🇸 & Turkish 🇹🇷)**: Fully bilingual interface with natural Turkish translation while preserving essential industry developer terminology (`Singleflight`, `Expand-Contract`, `Idempotency Key`, `Circuit Breaker`, `SLO`, `Error Budget`).
- ⚡ **30-Minute Sprint (15 Scenarios)**: The recommended default. Three scenarios per pillar, medium result confidence.
- 🎓 **2-Hour Deep Dive (60 Scenarios)**: The full question bank, twelve scenarios per pillar, high result confidence.
- 🔎 **5-Minute Pulse Check (5 Scenarios)**: A quick, low-confidence sanity check.
- 🔀 **Shuffled Options**: Answer order never hints at seniority.
- 📈 **Progress Tracking**: Results are saved locally (CLI: `~/.devcaliber/history.json`, web: browser storage) so a retake shows what changed per pillar.
- 🧪 **Result Confidence & Calibration Notes**: Flags uniformly top-tier answers and inconsistent pillars instead of pretending every score is equally reliable.
- 📊 **Interactive Radar Dashboard**: Zero-dependency single-file HTML report featuring an interactive Chart.js radar chart.
- 🎯 **Domain-Specific Tracks**: Calibrated weighting for **General SWE, Backend & Distributed Systems, Frontend & Web Platform, DevOps & Cloud, and Tech Lead**.
- 📐 **Estimated Percentile**: A rough, hand-tuned curve. It is **not** measured from real test-takers; treat it as indicative only.
- 🧭 **Targeted Promotion Roadmap**: Concrete behavioral milestones and curated book recommendations (e.g. *Designing Data-Intensive Applications*, *Site Reliability Engineering*, *Staff Engineer*).
- 🛡️ **Verified GitHub Profile Badges**: Generate crisp SVG badges to display on your personal GitHub README.

---

## 🌐 Global Engineering Leveling Framework

DevCaliber's L1–L5 standard correlates directly with global Big Tech career ladders and Levels.fyi:

| DevCaliber | Google | Meta | Amazon | Levels.fyi Standard | Scope & Core Responsibility |
|:---|:---|:---|:---|:---|:---|
| **L1** | L3 (SWE II) | E3 (SWE) | SDE I | Entry-Level Engineer | Functional code for well-scoped tasks with guidance |
| **L2** | L4 (SWE III) | E4 (SWE) | SDE II | Mid-Level Software Engineer | Autonomous feature development, testing, and production deployment |
| **L3** | L5 (Senior SWE) | E5 (Senior) | SDE III / Senior | Career Level Senior SWE | Scalable distributed design, SLO ownership, mentoring peers |
| **L4** | L6 (Staff SWE) | E6 (Staff) | Principal SDE | Staff Engineer / Force Multiplier | Multi-team architectural guardrails, cross-org alignment |
| **L5** | L7+ (Senior Staff/Principal) | E7+ (Senior Staff) | Senior Principal | Principal / Tech Fellow | Multi-year company technology strategy, competitive moats |

---

## 🚀 Quickstart

### Installation

Clone the repository and install via pip:

```bash
git clone https://github.com/alisenn/devcaliber.git
cd devcaliber
pip install -e .
```

Verify installation:

```bash
devcaliber version
```

---

## 🧪 Examination Modes

### 1. ⚡ The 30-Minute Sprint (15 Scenarios, recommended)
```bash
devcaliber sprint --name "Jane Doe" --track backend --html report.html --open
devcaliber sprint --lang tr --name "Ahmet Yilmaz"
```

### 2. 🎓 The 2-Hour Deep Dive (60 Scenarios)
The full question bank, twelve scenarios per pillar. Use it when you want a result you can rely on.

```bash
devcaliber deep --name "Jane Doe" --track backend --html report.html --open
```

`devcaliber exam` is kept as an alias for `deep`.

### 3. 🔎 The 5-Minute Pulse Check (5 Scenarios)
```bash
devcaliber quick --name "Alex Smith" --track general
```

| Mode | Time | Questions | Per pillar | Result confidence |
|:---|:---:|:---:|:---:|:---:|
| `quick` | ~5 min | 5 | 1 | Low |
| `sprint` | ~30 min | 15 | 3 | Medium |
| `deep` | ~2 h | 60 | 12 | High |

Track your progress with `devcaliber history`. Retaking an assessment prints the change versus your last attempt.

### 4. Full Custom Assessment with Badges and Markdown Export
```bash
devcaliber assess \
  --name "Sarah Connor" \
  --track backend \
  --html my-report.html \
  --md seniority-badge.md \
  --json result.json \
  --badge seniority-badge.svg
```

---

## 🏛️ The 5 Engineering Pillars

1. **⚡ Craft & Architecture (25% default weight)**
   - Code elegance, system design, testing discipline, architectural scalability, zero-downtime database migrations.
2. **🛡️ Reliability & Ownership (20% default weight)**
   - Operational excellence, CI/CD, production observability, incident triage, SLOs, and circuit breakers.
3. **🎯 Business & Product Impact (20% default weight)**
   - Translating user needs into engineering deliverables, pragmatic MVP trade-offs, Cloud FinOps, and ROI.
4. **🌟 Leadership & Influence (15% default weight)**
   - Mentorship, technical consensus, RFC authorship, cross-team collaboration, and raising the hiring bar.
5. **🚀 Autonomy & Ambiguity (20% default weight)**
   - Navigating ill-defined problems, setting long-term direction, and executing from 0 to 1 under high uncertainty.

---

## 💻 CLI Reference

| Command | Description | Example |
|:---|:---|:---|
| `devcaliber sprint` | 30-minute, 15-scenario assessment | `devcaliber sprint --lang tr` |
| `devcaliber deep` | 2-hour, 60-scenario assessment (alias: `exam`) | `devcaliber deep` |
| `devcaliber quick` | 5-minute pulse check | `devcaliber quick` |
| `devcaliber history` | Show saved results | `devcaliber history` |
| `devcaliber assess` | Full control (`--mode`, exports, `--no-history`) | `devcaliber assess --mode deep --json r.json` |
| `devcaliber matrix` | View the full engineering competency matrix table | `devcaliber matrix --level L3` |
| `devcaliber compare` | Compare expectations between two seniority levels | `devcaliber compare L2 L3` |
| `devcaliber badge` | Generate an SVG seniority badge for your profile | `devcaliber badge --level L4 -o badge.svg` |
| `devcaliber version` | Show current DevCaliber version | `devcaliber version` |

---

## 🧱 Contributing Questions

The question bank lives in one place: [`devcaliber/data/questions.json`](devcaliber/data/questions.json). After editing it, regenerate the web app and run the tests:

```bash
python scripts/build_web.py   # embeds the bank into docs/index.html
pytest
```

CI fails if `docs/index.html` is out of date or if a question is missing a Turkish translation.

---

## 🛡️ License

MIT License © 2026 DevCaliber Contributors. Free for commercial and private use.

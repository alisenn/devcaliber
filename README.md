<div align="center">

```
   _____            _             __  __      _            
  / ____|          (_)           |  \/  |    | |           
 | (___   ___ _ __  _  ___  _ __ | \  / | ___| |_ ___ _ __ 
  \___ \ / _ \ '_ \| |/ _ \| '__|| |\/| |/ _ \ __/ _ \ '__|
  ____) |  __/ | | | | (_) | |   | |  | |  __/ ||  __/ |   
 |_____/ \___|_| |_|_|\___/|_|   |_|  |_|\___|\__\___|_|   
```

### The Open Source Seniority & Competency Diagnostic Suite for Software Engineers

*Demystify your career ladder. Take the comprehensive 60-minute, 30-case-study seniority exam across 5 engineering pillars, generate interactive radar diagnostics, and chart your promotion roadmap.*

---

[![CI](https://github.com/alisenn/levelcraft/actions/workflows/ci.yml/badge.svg)](https://github.com/alisenn/levelcraft/actions)
[![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Coverage](https://img.shields.io/badge/coverage-98%25-brightgreen.svg)](#)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[![Live Demo](https://img.shields.io/badge/Live_Demo-Take_60--Min_Exam-success?style=for-the-badge&logo=googlechrome&logoColor=white)](https://alisenn.github.io/levelcraft/)

[🎓 Live Web Exam](https://alisenn.github.io/levelcraft/) •
[Features](#-key-features) •
[Quickstart](#-quickstart) •
[Exam Modes](#-examination-modes) •
[The 5 Pillars](#-the-5-engineering-pillars) •
[CLI Commands](#-cli-reference) •
[Methodology](#-framework-methodology)

</div>

---

## 💡 Why SeniorMeter?

Engineering job titles are inconsistent and fragmented across the tech industry:
- What one startup calls a **"Senior Software Engineer"** is often an **L3 / Mid-level** at Tier-1 tech firms.
- Technical interviews rely on **LeetCode & algorithmic puzzles** that have zero correlation with real engineering craftsmanship, production incident response, or architectural leadership.
- Career progression rubrics are often opaque, political, or buried inside private corporate wikis.

**SeniorMeter** bridges this gap as an open-source, community-governed diagnostic engine that benchmarks software engineers through **30 deep, production-tested scenario case studies** synthesized from public engineering frameworks at **Google, Dropbox, Spotify, and StaffEng**.

---

## ⚡ Key Features

- 🎓 **60-Minute Comprehensive Examination (30 Scenarios)**: A rigorous 5-stage certification exam covering distributed systems, zero-downtime data migrations, SRE & incident response, product ROI, code review culture, and organizational ambiguity.
- ⚡ **3-Minute Rapid Pulse Check (5 Scenarios)**: Quick pulse diagnostic for rapid self-assessment.
- 🌐 **Interactive Radar Dashboard**: Zero-dependency, offline-capable single-file HTML report featuring an interactive Chart.js radar chart.
- 🎯 **Domain-Specific Tracks**: Calibrated weighting for **General SWE, Backend, Frontend, DevOps / Platform, and Tech Lead**.
- 📈 **Industry Percentile Calibration**: Compare your placement against empirical software engineering demographics (Top 5% to 99th percentile).
- 🧭 **Targeted Promotion Roadmap**: Concrete behavioral milestones and curated book recommendations (e.g. *Designing Data-Intensive Applications*, *Site Reliability Engineering*, *Staff Engineer*).
- 🛡️ **GitHub Profile Badges**: Generate crisp SVG badges to display on your personal GitHub README.

---

## 🚀 Quickstart

### Installation

Clone the repository and install via pip:

```bash
git clone https://github.com/alisenn/levelcraft.git
cd levelcraft
pip install -e .
```

Verify installation:

```bash
seniormeter version
```

---

## 🧪 Examination Modes

### 1. 🎓 The 60-Minute Comprehensive Examination (30 Scenarios)
The official in-depth benchmark consisting of 5 distinct stages (6 scenarios per pillar):

```bash
seniormeter exam --name "Jane Doe" --track backend --html report.html --open
```

### 2. ⚡ The 3-Minute Quick Pulse Check (5 Scenarios)
A rapid 5-scenario evaluation:

```bash
seniormeter quick --name "Alex Smith" --track general --html report.html --open
```

### 3. Full Custom Assessment with Badges and Markdown Export
```bash
seniormeter assess \
  --name "Alice Dev" \
  --track tech_lead \
  --html report.html \
  --md 1on1_review.md \
  --json data.json \
  --badge seniority_badge.svg \
  --open
```

---

## 📊 The 5 Engineering Pillars (30 Scenarios)

| Stage | Pillar | Focus Case Studies |
| :---: | :--- | :--- |
| **1** | **⚡ Craft & Architecture** | Monolith refactoring, 10x scalability, zero-downtime DB migrations (Expand-Contract), distributed caching stampedes, microservices vs modular monoliths, zero-day CVE mitigation. |
| **2** | **🛡️ Reliability & Ownership** | Sev-1 incident commander, golden signals observability, alert fatigue / on-call health, chaos engineering / multi-region DR, SLO error budgets, cascading failure mitigation. |
| **3** | **🎯 Business & Product Impact** | Tech debt vs feature velocity trade-offs, metric-driven ROI, technical spikes vs Fortune 500 contracts, lean user discovery, FinOps cloud cost reduction, Buy vs Build TCO. |
| **4** | **🌟 Leadership & Influence** | RFC technical consensus, peer mentorship & promotion sponsorship, code review quality & PR hygiene, cross-team architecture guilds, raising the hiring bar, C-level risk communication. |
| **5** | **🚀 Autonomy & Ambiguity** | Navigating vague OKRs, 0-to-1 greenfield platform execution, cross-team dependency unblocking, conflicting stakeholder demands, systemic blind spots, multi-year horizon planning. |

---

## 🗂️ CLI Reference

```bash
seniormeter exam               # Run 60-minute in-depth 30-scenario diagnostic exam
seniormeter quick              # Run 3-minute rapid pulse check (5 scenarios)
seniormeter matrix             # Inspect complete competency rubric table
seniormeter matrix --level L3  # Filter matrix expectations for Senior level
seniormeter compare L2 L3      # Side-by-side behavioral comparison between levels
seniormeter badge --level L3   # Generate standalone SVG badge for GitHub README
```

---

## 🏆 Seniority Tiers Explained

- **`L1` — Associate / Junior Software Engineer**: Focuses on learning, executing well-scoped tasks with guidance, and adhering to codebase conventions.
- **`L2` — Software Engineer (Mid)**: Autonomous execution of features from inception to deployment. Solid debugging skills, independent ownership of medium components.
- **`L3` — Senior Software Engineer**: Owns critical systems and reliability. Authors technical design RFCs, anticipates edge cases, mentors junior peers, and navigates ambiguous requirements.
- **`L4` — Staff Software Engineer**: Sets architectural direction across multiple teams. Acts as an organizational force multiplier, driving multi-quarter initiatives and unblocking systemic bottlenecks.
- **`L5` — Principal / Distinguished Engineer**: Directs company-wide technology strategy, pioneers foundational platforms, and navigates high-uncertainty business horizons.

---

## 🔬 Framework Methodology & Citations

The SeniorMeter scoring rubric and progression model are curated from research and public engineering frameworks:

1. **Dropbox Engineering Career Framework**: Core foundational dimensions of Results, Direction, and Mastery.
2. **Will Larson's Staff Engineer Framework**: Archetypes of Staff+ leadership (Tech Lead, Architect, Solver, Right Hand).
3. **Google Engineering Practices**: Code review culture, technical design documentation, and blameless post-mortems.
4. **Site Reliability Engineering (Google SRE)**: Golden signals, error budgets, and operational resilience.
5. **Radical Candor (Kim Scott)**: Actionable mentorship and constructive feedback mechanics.

---

## 📄 License

SeniorMeter is open-source software licensed under the [MIT License](LICENSE).
Made with care for software engineers worldwide. 🌟

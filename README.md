<div align="center">

```
   __                     _______              ______  
  / /   ___ _   _____    / ____/________ _____/ / / /_ 
 / /   / _ \ | / / _ \  / /   / ___/ __ `/ __  / / __/ 
/ /___/  __/ |/ /  __/ / /___/ /  / /_/ / /_/ / / /_   
/_____/\___/|___/\___/  \____/_/   \__,_/\__,_/_/\__/   
```

### The Open Source Seniority & Competency Matrix Engine for Software Engineers

*Demystify your career ladder. Benchmark your skills across 5 core engineering pillars, generate interactive radar diagnostics, and chart your promotion roadmap.*

---

[![CI](https://github.com/alisenn/levelcraft/actions/workflows/ci.yml/badge.svg)](https://github.com/alisenn/levelcraft/actions)
[![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Coverage](https://img.shields.io/badge/coverage-98%25-brightgreen.svg)](#)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[![Live Demo](https://img.shields.io/badge/Live_Demo-Try_Online-success?style=for-the-badge&logo=googlechrome&logoColor=white)](https://alisenn.github.io/levelcraft/)

[🎮 Live Web Demo](https://alisenn.github.io/levelcraft/) •
[Features](#-key-features) •
[Quickstart](#-quickstart) •
[Interactive Assessment](#-interactive-assessment) •
[The 5 Pillars](#-the-5-engineering-pillars) •
[CLI Commands](#-cli-reference) •
[Badge Generation](#-github-profile-badge) •
[Methodology](#-framework-methodology)

</div>

---

## 💡 Why LevelCraft?

Engineering titles are broken. What one company calls a **"Senior Software Engineer"** is a **"Mid-level"** at Big Tech, or a **"Tech Lead"** at an early-stage startup. Promotion rubrics are often opaque, politicized, or buried inside private company wikis.

**LevelCraft** is an open-source, developer-first diagnostic engine designed to bring transparency and standardization to software engineering careers.

- 🎯 **No Trivia**: Evaluates real-world behavioral scenarios (incident response, technical RFCs, tech debt trade-offs, system scalability).
- 📊 **Calibrated Benchmarks**: Grounded in public engineering ladders from **Dropbox, Google, Spotify, and Will Larson’s Staff Engineer framework**.
- 🛠️ **Developer Ergonomics**: Rich CLI UI, standalone offline HTML radar dashboards, Markdown reports for 1-on-1s, and SVG GitHub profile badges.

---

## ⚡ Key Features

- 🖥️ **Interactive Terminal Assessment**: Engaging, scenario-based questionnaires with Rich terminal formatting.
- ⚡ **Rapid 3-Minute or Deep Benchmarks**: Choose between a 5-question quick pulse check or full comprehensive diagnostics.
- 🌐 **Self-Contained Radar Dashboard**: Generates a single-file, dark-mode Tailwind + Chart.js radar report with zero external server dependencies.
- 🎯 **Tailored Career Tracks**: Customizable weighting for **General SWE, Backend, Frontend, DevOps / Platform, and Tech Lead**.
- 📈 **Percentile Calibration**: Compares your competencies against real-world engineering distributions.
- 🧭 **Promotion Gap Analysis**: Concrete action items and curated reading lists (e.g. *Designing Data-Intensive Applications*, *The Staff Engineer's Path*) to reach your next level.
- 🛡️ **GitHub Profile Badges**: Generate crisp SVG badges to showcase your validated tier in your GitHub profile README.

---

## 🚀 Quickstart

### Installation

Clone the repository and install via pip:

```bash
git clone https://github.com/alisenn/levelcraft.git
cd levelcraft
pip install -e .
```

Verify the installation:

```bash
levelcraft version
```

---

## 🧪 Interactive Assessment

### 1. Rapid 3-Minute Benchmark

Run a rapid 5-scenario evaluation and generate an interactive HTML dashboard:

```bash
levelcraft quick --name "Jane Doe" --track backend --html report.html --open
```

### 2. Comprehensive Assessment with Full Exports

```bash
levelcraft assess \
  --name "Alex Smith" \
  --track general \
  --html report.html \
  --md report.md \
  --json report.json \
  --badge seniority_badge.svg \
  --open
```

---

## 📊 The 5 Engineering Pillars

LevelCraft evaluates engineering seniority across 5 core dimensions:

| Pillar | Focus Areas | Key Behaviors |
| :--- | :--- | :--- |
| **⚡ Craft & Architecture** | Code quality, design patterns, scalability, testing | From writing unit tests to designing multi-region distributed architectures. |
| **🛡️ Reliability & Ownership** | CI/CD, production observability, incident triage, SLIs/SLOs | From monitoring personal PRs to enterprise disaster recovery and zero-downtime engineering. |
| **🎯 Business & Product Impact** | ROI, MVP scoping, metrics, user empathy | From completing Jira tickets to driving high-leverage technical bets that impact company valuation. |
| **🌟 Leadership & Influence** | Mentorship, technical RFCs, consensus building | From active learning to force multiplication, sponsoring peers, and steering org-wide tech strategy. |
| **🚀 Autonomy & Ambiguity** | Problem navigation, scope, 0-to-1 execution | From structured tasks to solving undefined, multi-quarter strategic engineering challenges. |

---

## 🗂️ CLI Reference

### 🔍 Explore the Competency Matrix
Inspect observable behaviors across all levels (L1 to L5):

```bash
# View complete matrix
levelcraft matrix

# Filter by level
levelcraft matrix --level L3

# Filter by dimension
levelcraft matrix --dimension craft
```

### ⚖️ Side-by-Side Level Comparison
Compare expectations between any two levels (e.g., Mid-level vs Senior, or Senior vs Staff):

```bash
levelcraft compare L2 L3
levelcraft compare L3 L4
```

### 🛡️ GitHub Profile Badge
Generate a crisp SVG badge for your GitHub profile README:

```bash
levelcraft badge --level L3 --output seniority_badge.svg
```

Add it to your profile markdown:

```markdown
[![Seniority Level](seniority_badge.svg)](https://github.com/alisenn/levelcraft)
```

---

## 🏆 Seniority Tiers Explained

- **`L1` — Associate / Junior Software Engineer**: Focuses on learning, executing well-scoped tasks with guidance, and adhering to codebase conventions.
- **`L2` — Software Engineer (Mid)**: Autonomous execution of features from inception to deployment. Solid debugging skills, independent ownership of medium components.
- **`L3` — Senior Software Engineer**: Owns critical systems and reliability. Authors technical design RFCs, anticipates edge cases, mentors junior peers, and navigates ambiguous requirements.
- **`L4` — Staff Software Engineer**: Sets architectural direction across multiple teams. Acts as an organizational force multiplier, driving multi-quarter initiatives and unblocking systemic bottlenecks.
- **`L5` — Principal / Distinguished Engineer**: Directs company-wide technology strategy, pioneers foundational platforms, and navigates high-uncertainty business horizons.

---

## 🛠️ Technology Tracks

Tailor assessment weighting based on your discipline:

```bash
levelcraft assess --track backend     # Emphasizes Craft, System Design & Reliability
levelcraft assess --track frontend    # Emphasizes Craft, User Experience & Impact
levelcraft assess --track devops      # Emphasizes Reliability, Infrastructure & Observability
levelcraft assess --track tech_lead   # Emphasizes Leadership, Impact & Alignment
```

---

## 🔬 Framework Methodology & Citations

The LevelCraft scoring rubric and progression model are curated from research and public engineering frameworks:

1. **Dropbox Engineering Career Framework**: Core foundational dimensions of Results, Direction, and Mastery.
2. **Will Larson's Staff Engineer Framework**: Archetypes of Staff+ leadership (Tech Lead, Architect, Solver, Right Hand).
3. **Google Engineering Practices**: Code review culture, technical design documentation, and blameless post-mortems.
4. **Site Reliability Engineering (Google SRE)**: Golden signals, error budgets, and operational resilience.
5. **Radical Candor (Kim Scott)**: Actionable mentorship and constructive feedback mechanics.

---

## 🤝 Contributing

We welcome community contributions! Whether you want to add new questions to the bank, define new tracks (Data Engineering, Mobile, Security), or refine rubrics:

1. Read our [Contributing Guidelines](CONTRIBUTING.md).
2. Fork the repository and create your feature branch: `git checkout -b feat/new-track`.
3. Submit a Pull Request with passing tests!

---

## 📄 License

LevelCraft is open-source software licensed under the [MIT License](LICENSE).
Made with care for software engineers worldwide. 🌟

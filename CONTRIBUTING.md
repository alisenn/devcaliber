# Contributing to LevelCraft

First off, thank you for considering contributing to **LevelCraft**! 🎉

LevelCraft is built by and for the global engineering community. We welcome contributions of all forms:
- 💡 Adding new scenario questions to the question bank
- 🎯 Defining new specialization tracks (e.g., Data Engineering, Security, Mobile)
- 📖 Enhancing career roadmap resources and reading recommendations
- 🛠️ Improving the CLI experience, Terminal UI, or Web Dashboard
- 🧪 Adding test cases and improving code coverage

---

## 🛠️ Local Development Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/alisenn/levelcraft.git
   cd levelcraft
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies in editable mode:**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Run tests:**
   ```bash
   pytest
   ```

---

## 📝 Contribution Guidelines

1. **Adding Scenario Questions:**
   - Keep questions realistic, practical, and grounded in real-world engineering trade-offs.
   - Avoid trivial syntax/trivia questions. Focus on architectural choices, incident response, team communication, and ownership.
   - Add new questions to `levelcraft/matrix.py`.

2. **Code Standards:**
   - Ensure all functions and models have explicit type hints.
   - Maintain 95%+ test coverage. Add corresponding tests in `tests/`.

3. **Submitting a Pull Request:**
   - Use conventional commit messages (`feat: ...`, `fix: ...`, `docs: ...`).
   - Ensure `pytest` passes cleanly across all test suites.

Thank you for helping engineers worldwide demystify their career ladders! 🚀

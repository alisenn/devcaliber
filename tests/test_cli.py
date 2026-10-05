"""
CLI command tests using Typer CliRunner for SeniorMeter.
"""

from typer.testing import CliRunner
from devcaliber.cli import app

runner = CliRunner()


def test_cli_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "DevCaliber version" in result.stdout


def test_cli_matrix():
    result = runner.invoke(app, ["matrix"])
    assert result.exit_code == 0
    assert "Engineering Competency Matrix" in result.stdout
    assert "Craft" in result.stdout
    assert "Architecture" in result.stdout


def test_cli_matrix_filter_level():
    result = runner.invoke(app, ["matrix", "--level", "L3"])
    assert result.exit_code == 0
    assert "L3" in result.stdout


def test_cli_compare():
    result = runner.invoke(app, ["compare", "L2", "L3"])
    assert result.exit_code == 0
    assert "Side-by-Side Comparison: L2 vs L3" in result.stdout


def test_cli_compare_invalid():
    result = runner.invoke(app, ["compare", "L2", "INVALID"])
    assert result.exit_code == 1
    assert "Invalid level codes" in result.stdout


def test_cli_badge(tmp_path):
    badge_file = tmp_path / "test_badge.svg"
    result = runner.invoke(app, ["badge", "--level", "L4", "--output", str(badge_file)])
    assert result.exit_code == 0
    assert badge_file.exists()
    content = badge_file.read_text()
    assert "Seniority: L4" in content


def test_cli_assess_quick(tmp_path):
    html_file = tmp_path / "report.html"
    md_file = tmp_path / "report.md"
    json_file = tmp_path / "report.json"
    badge_file = tmp_path / "badge.svg"

    # Quick has 5 questions; simulate typing 'C' for all 5
    user_inputs = "C\nC\nC\nC\nC\n"
    result = runner.invoke(
        app,
        [
            "assess",
            "--quick",
            "--name", "Dev Tester",
            "--track", "backend",
            "--html", str(html_file),
            "--md", str(md_file),
            "--json", str(json_file),
            "--badge", str(badge_file),
        ],
        input=user_inputs,
    )

    assert result.exit_code == 0
    assert "Dev Tester" in result.stdout
    assert html_file.exists()
    assert md_file.exists()
    assert json_file.exists()
    assert badge_file.exists()


def test_cli_sprint_runs_end_to_end(tmp_path, monkeypatch):
    monkeypatch.setenv("DEVCALIBER_HOME", str(tmp_path))
    result = runner.invoke(app, ["sprint", "--name", "Ada"], input="A\n" * 15)
    assert result.exit_code == 0, result.stdout
    assert "Sprint Assessment" in result.stdout
    assert "(15/15)" in result.stdout

    history = runner.invoke(app, ["history"])
    assert history.exit_code == 0
    assert "Ada" in history.stdout


def test_cli_invalid_mode(tmp_path, monkeypatch):
    monkeypatch.setenv("DEVCALIBER_HOME", str(tmp_path))
    result = runner.invoke(app, ["assess", "--mode", "marathon"])
    assert result.exit_code == 1
    assert "Unknown mode" in result.stdout

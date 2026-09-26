"""
Unit tests for Reporter outputs (Markdown, JSON, HTML, SVG badge).
"""

from io import StringIO
from rich.console import Console

from devcaliber.models import Track
from devcaliber.evaluator import SeniorityEvaluator
from devcaliber.reporter import Reporter
from devcaliber.matrix import QUESTIONS


def get_sample_result():
    evaluator = SeniorityEvaluator(track=Track.GENERAL)
    answers = {q.id: 3.5 for q in QUESTIONS}
    return evaluator.evaluate_answers(answers, candidate_name="Alice Developer")


def test_reporter_terminal_summary():
    result = get_sample_result()
    string_io = StringIO()
    test_console = Console(file=string_io, force_terminal=True, width=100)
    reporter = Reporter(result, console=test_console)
    reporter.print_terminal_summary()

    output = string_io.getvalue()
    assert "Alice Developer" in output
    assert "L3" in output


def test_reporter_markdown():
    result = get_sample_result()
    reporter = Reporter(result)
    md = reporter.generate_markdown()

    assert "Alice Developer" in md
    assert "L3" in md
    assert "Competency Radar Breakdown" in md


def test_reporter_json():
    result = get_sample_result()
    reporter = Reporter(result)
    json_str = reporter.generate_json()

    assert '"candidate_name": "Alice Developer"' in json_str
    assert '"overall_level": "L3 - Senior Software Engineer"' in json_str


def test_reporter_svg_badge():
    result = get_sample_result()
    reporter = Reporter(result)
    svg = reporter.generate_svg_badge()

    assert "<svg" in svg
    assert "Seniority: L3" in svg
    assert "</svg>" in svg


def test_reporter_html_dashboard():
    result = get_sample_result()
    reporter = Reporter(result)
    html = reporter.generate_html_dashboard()

    assert "<!DOCTYPE html>" in html
    assert "Alice Developer" in html
    assert "radarChart" in html
    assert "Chart(ctx," in html

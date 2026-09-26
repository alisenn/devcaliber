"""
SeniorMeter CLI: Command Line Interface for engineering seniority assessment and matrix exploration.
Features 60-minute in-depth benchmarking (30 scenarios) and rapid pulse checks.
"""

import sys
import webbrowser
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich import box

from seniormeter import __version__
from seniormeter.models import SeniorityLevel, DimensionId, Track
from seniormeter.matrix import DIMENSION_METADATA, LEVEL_RUBRIC, QUESTIONS
from seniormeter.evaluator import SeniorityEvaluator
from seniormeter.reporter import Reporter, LEVEL_COLORS

app = typer.Typer(
    name="seniormeter",
    help="🧭 SeniorMeter: Engineering Seniority & Competency Matrix Diagnostic Engine.",
    add_completion=False,
)
console = Console()


def render_banner():
    banner = r"""[bold cyan]
   _____            _             __  __      _            
  / ____|          (_)           |  \/  |    | |           
 | (___   ___ _ __  _  ___  _ __ | \  / | ___| |_ ___ _ __ 
  \___ \ / _ \ '_ \| |/ _ \| '__|| |\/| |/ _ \ __/ _ \ '__|
  ____) |  __/ | | | | (_) | |   | |  | |  __/ ||  __/ |   
 |_____/ \___|_| |_|_|\___/|_|   |_|  |_|\___|\__\___|_|   
[/][dim]The Open Source Engineering Seniority & Career Matrix Engine • seniormeter.com[/]
"""
    console.print(banner)


@app.command()
def assess(
    name: str = typer.Option("Engineer", "--name", "-n", help="Candidate or engineer name"),
    track: Track = typer.Option(Track.GENERAL, "--track", "-t", help="Engineering track (general, backend, frontend, devops, tech_lead)"),
    quick: bool = typer.Option(False, "--quick", "-q", help="Run 5-question rapid pulse check"),
    export_html: Optional[str] = typer.Option(None, "--html", help="Path to save HTML dashboard report"),
    export_md: Optional[str] = typer.Option(None, "--md", help="Path to save Markdown report"),
    export_json: Optional[str] = typer.Option(None, "--json", help="Path to save JSON report"),
    badge: Optional[str] = typer.Option(None, "--badge", help="Path to save SVG GitHub badge"),
    open_browser: bool = typer.Option(False, "--open", help="Open generated HTML report in browser"),
):
    """Run an interactive assessment session to evaluate engineering seniority."""
    render_banner()
    mode_label = "5-Question Rapid Pulse" if quick else f"Comprehensive {len(QUESTIONS)}-Question Diagnostic Exam"
    console.print(f"[bold]Starting Seniority Assessment for [cyan]{name}[/] (Track: [green]{track.value.upper()}[/])[/]")
    console.print(f"[dim]Mode: {mode_label}. Answer each scenario reflecting your natural behavior in production.[/dim]\n")

    eval_questions = [q for q in QUESTIONS if (not quick or q.is_quick)]
    total = len(eval_questions)
    answers = {}

    current_dim = None

    for idx, q in enumerate(eval_questions, start=1):
        dim_info = DIMENSION_METADATA.get(q.dimension, {})

        # Stage transition announcement
        if q.dimension != current_dim:
            current_dim = q.dimension
            stage_idx = list(DimensionId).index(q.dimension) + 1
            console.print(f"\n[bold yellow]━━━ STAGE {stage_idx}/5: {dim_info.get('name', 'Pillar').upper()} ━━━[/]")

        console.print(Panel(
            f"[bold yellow]Scenario ({idx}/{total}):[/] [bold white]{q.title}[/]\n\n"
            f"[italic text-slate-300]{q.scenario}[/]",
            title=f"{dim_info.get('icon', '⚡')} {dim_info.get('name', 'Dimension')}",
            border_style="cyan",
            box=box.ROUNDED,
        ))

        letters = ["A", "B", "C", "D", "E"]
        valid_choices = letters[:len(q.options)]

        for ltr, opt in zip(letters, q.options):
            console.print(f"  [bold cyan]({ltr})[/] {opt.text}")

        console.print("")
        choice = ""
        while choice not in valid_choices:
            choice = Prompt.ask(
                f"[bold]Select option ({'/'.join(valid_choices)})[/]",
                default="A",
                console=console,
            ).strip().upper()

        opt_idx = letters.index(choice)
        selected_option = q.options[opt_idx]
        answers[q.id] = selected_option.score
        console.print(f"[dim]Recorded: {choice}[/]\n")

    # Evaluate
    evaluator = SeniorityEvaluator(track=track)
    result = evaluator.evaluate_answers(
        answers=answers,
        candidate_name=name,
        assessment_mode="rapid" if quick else "comprehensive_exam",
    )

    reporter = Reporter(result, console=console)
    reporter.print_terminal_summary()

    # Exports
    if export_html or open_browser:
        target_html = export_html or f"seniormeter_report_{name.lower().replace(' ', '_')}.html"
        html_path = Path(target_html)
        html_path.parent.mkdir(parents=True, exist_ok=True)
        html_content = reporter.generate_html_dashboard()
        html_path.write_text(html_content, encoding="utf-8")
        console.print(f"\n[bold green]✓[/] HTML Dashboard saved to: [underline]{target_html}[/]")
        if open_browser:
            webbrowser.open(f"file://{html_path.resolve()}")

    if export_md:
        md_path = Path(export_md)
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_content = reporter.generate_markdown()
        md_path.write_text(md_content, encoding="utf-8")
        console.print(f"[bold green]✓[/] Markdown Report saved to: [underline]{export_md}[/]")

    if export_json:
        json_path = Path(export_json)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_content = reporter.generate_json()
        json_path.write_text(json_content, encoding="utf-8")
        console.print(f"[bold green]✓[/] JSON Data saved to: [underline]{export_json}[/]")

    if badge:
        badge_path = Path(badge)
        badge_path.parent.mkdir(parents=True, exist_ok=True)
        svg_content = reporter.generate_svg_badge()
        badge_path.write_text(svg_content, encoding="utf-8")
        console.print(f"[bold green]✓[/] SVG GitHub Badge saved to: [underline]{badge}[/]")


@app.command()
def exam(
    name: str = typer.Option("Engineer", "--name", "-n", help="Candidate name"),
    track: Track = typer.Option(Track.GENERAL, "--track", "-t", help="Engineering track"),
    export_html: Optional[str] = typer.Option(None, "--html", help="Path to save HTML report"),
    open_browser: bool = typer.Option(False, "--open", help="Open HTML report in browser"),
):
    """Run the 60-minute comprehensive 30-scenario seniority examination."""
    assess(
        name=name,
        track=track,
        quick=False,
        export_html=export_html,
        export_md=None,
        export_json=None,
        badge=None,
        open_browser=open_browser,
    )


@app.command()
def quick(
    name: str = typer.Option("Engineer", "--name", "-n", help="Candidate name"),
    track: Track = typer.Option(Track.GENERAL, "--track", "-t", help="Engineering track"),
    export_html: Optional[str] = typer.Option(None, "--html", help="Path to save HTML report"),
    open_browser: bool = typer.Option(False, "--open", help="Open HTML report in browser"),
):
    """Run a rapid 3-minute seniority benchmark (5 core questions)."""
    assess(
        name=name,
        track=track,
        quick=True,
        export_html=export_html,
        export_md=None,
        export_json=None,
        badge=None,
        open_browser=open_browser,
    )


@app.command()
def matrix(
    dimension: Optional[DimensionId] = typer.Option(None, "--dimension", "-d", help="Filter by dimension"),
    level: Optional[str] = typer.Option(None, "--level", "-l", help="Filter by level code (L1, L2, L3, L4, L5)"),
):
    """Inspect the engineering career competency rubric table."""
    render_banner()
    table = Table(title="SeniorMeter Engineering Competency Matrix", box=box.ROUNDED, expand=True)
    table.add_column("Dimension", style="bold cyan", width=22)
    table.add_column("Level", style="bold yellow", width=8)
    table.add_column("Expectations & Observable Behaviors", style="white")

    dims = [dimension] if dimension else list(DimensionId)

    for d in dims:
        meta = DIMENSION_METADATA[d]
        rubrics = LEVEL_RUBRIC[d]
        for lvl_enum, desc in rubrics.items():
            if level and lvl_enum.code.upper() != level.upper():
                continue
            color = LEVEL_COLORS.get(lvl_enum.code, "white")
            table.add_row(
                f"{meta['icon']} {meta['name']}",
                f"[{color}]{lvl_enum.code}[/]",
                desc,
            )

    console.print(table)


@app.command()
def compare(
    level_a: str = typer.Argument(..., help="First level code (e.g. L2)"),
    level_b: str = typer.Argument(..., help="Second level code (e.g. L3)"),
):
    """Side-by-side behavioral comparison between two seniority levels."""
    render_banner()
    code_a = level_a.upper()
    code_b = level_b.upper()

    def get_level(code: str) -> Optional[SeniorityLevel]:
        for lvl in SeniorityLevel:
            if lvl.code == code:
                return lvl
        return None

    lvl_a = get_level(code_a)
    lvl_b = get_level(code_b)

    if not lvl_a or not lvl_b:
        console.print(f"[bold red]Error:[/] Invalid level codes. Use L1, L2, L3, L4, or L5.")
        raise typer.Exit(code=1)

    table = Table(
        title=f"Side-by-Side Comparison: [{LEVEL_COLORS.get(code_a, 'cyan')}]{lvl_a.code}[/] vs [{LEVEL_COLORS.get(code_b, 'green')}]{lvl_b.code}[/]",
        box=box.ROUNDED,
        expand=True,
    )
    table.add_column("Dimension", style="bold white", width=20)
    table.add_column(f"{lvl_a.code} ({lvl_a.title.split(' ')[0]})", style="cyan", width=38)
    table.add_column(f"{lvl_b.code} ({lvl_b.title.split(' ')[0]})", style="green", width=38)

    for dim in DimensionId:
        meta = DIMENSION_METADATA[dim]
        desc_a = LEVEL_RUBRIC[dim][lvl_a]
        desc_b = LEVEL_RUBRIC[dim][lvl_b]
        table.add_row(f"{meta['icon']} {meta['name']}", desc_a, desc_b)

    console.print(table)


@app.command()
def badge(
    level: str = typer.Option("L3", "--level", "-l", help="Seniority code (L1, L2, L3, L4, L5)"),
    output: str = typer.Option("seniority_badge.svg", "--output", "-o", help="Output SVG filepath"),
):
    """Generate a standalone SVG badge for your GitHub profile README."""
    target_level = None
    for lvl in SeniorityLevel:
        if lvl.code.upper() == level.upper():
            target_level = lvl
            break

    if not target_level:
        console.print(f"[bold red]Error:[/] Unknown level '{level}'. Choose from L1, L2, L3, L4, L5.")
        raise typer.Exit(code=1)

    # Mock assessment result for badge rendering
    evaluator = SeniorityEvaluator()
    dummy_answers = {q.id: float(target_level.tier) for q in QUESTIONS}
    result = evaluator.evaluate_answers(dummy_answers)
    result.overall_level = target_level

    reporter = Reporter(result, console=console)
    svg = reporter.generate_svg_badge()
    badge_path = Path(output)
    badge_path.parent.mkdir(parents=True, exist_ok=True)
    badge_path.write_text(svg, encoding="utf-8")
    console.print(f"[bold green]✓[/] Generated badge for [bold]{target_level.code}[/] at: [underline]{output}[/]")


@app.command()
def version():
    """Show SeniorMeter version."""
    console.print(f"[bold cyan]SeniorMeter[/] version [bold white]{__version__}[/]")


def main():
    app()


if __name__ == "__main__":
    main()

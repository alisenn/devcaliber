"""
DevCaliber CLI: Computerized Adaptive Testing (CAT) for Software Engineering Seniority.
Features real-time step-by-step difficulty adaptation, FAANG/Glassdoor real interview questions,
and English / Turkish dual language support.
"""

import random
import webbrowser
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich import box

from devcaliber import __version__
from devcaliber.models import SeniorityLevel, DimensionId, Track
from devcaliber.matrix import DIMENSION_METADATA, LEVEL_RUBRIC, QUESTIONS
from devcaliber.modes import MODES
from devcaliber.history import (
    diff_dimensions,
    load_history,
    previous_entry,
    save_result,
)
from devcaliber.evaluator import SeniorityEvaluator, AdaptiveAssessmentEngine
from devcaliber.reporter import Reporter, LEVEL_COLORS

app = typer.Typer(
    name="devcaliber",
    help="🧭 DevCaliber: Engineering Seniority & Competency Matrix Diagnostic Engine.",
    add_completion=False,
)
console = Console()


def render_banner():
    banner = r"""[bold cyan]
  _____               _____       _ _ _               
 |  __ \             / ____|     | (_) |              
 | |  | | _____   __| |     __ _ | |_| |__   ___ _ __ 
 | |  | |/ _ \ \ / /| |    / _` || | | '_ \ / _ \ '__|
 | |__| |  __/\ V / | |___| (_| || | | |_) |  __/ |   
 |_____/ \___| \_/   \_____\__,_||_|_|_.__/ \___|_|   
[/][dim]The Open Source Engineering Seniority & Competency Benchmark Suite • devcaliber.com[/]
"""
    console.print(banner)


def _print_progress(result, previous, is_tr: bool) -> None:
    deltas = diff_dimensions(result, previous)
    title = "Önceki sonuca göre ilerleme" if is_tr else "Progress since last attempt"
    overall = round(result.overall_score - previous.get("overall_score", result.overall_score), 2)
    label = "Genel" if is_tr else "Overall"
    lines = [f"{label}: {previous.get('overall_score')} -> {result.overall_score} ({overall:+.2f}) [{previous.get('timestamp', '')}]"]
    for dim_id, delta in deltas.items():
        name = DIMENSION_METADATA[DimensionId(dim_id)]["name"]
        color = "green" if delta > 0 else "red" if delta < 0 else "dim"
        lines.append(f"  [{color}]{delta:+.2f}[/]  {name}")
    console.print(Panel("\n".join(lines), title=title, border_style="green", box=box.ROUNDED))


@app.command()
def assess(
    name: str = typer.Option("Engineer", "--name", "-n", help="Candidate name"),
    track: Track = typer.Option(Track.GENERAL, "--track", "-t", help="Engineering track (general, backend, frontend, devops, tech_lead)"),
    lang: str = typer.Option("en", "--lang", "-l", help="Language: 'en' for English or 'tr' for Türkçe (Teknik terimler korunur)"),
    quick: bool = typer.Option(False, "--quick", "-q", help="Shortcut for --mode pulse"),
    mode: str = typer.Option("sprint", "--mode", "-m", help="pulse (5 min), sprint (30 min) or deep (2 hours)"),
    no_history: bool = typer.Option(False, "--no-history", help="Do not save this result to local history"),
    export_html: Optional[str] = typer.Option(None, "--html", help="Path to save HTML dashboard report"),
    export_md: Optional[str] = typer.Option(None, "--md", help="Path to save Markdown report"),
    export_json: Optional[str] = typer.Option(None, "--json", help="Path to save JSON report"),
    badge: Optional[str] = typer.Option(None, "--badge", help="Path to save SVG GitHub badge"),
    open_browser: bool = typer.Option(False, "--open", help="Open generated HTML report in browser"),
):
    """Run an interactive assessment session to evaluate engineering seniority."""
    render_banner()
    is_tr = lang.lower().startswith("tr")

    mode = "pulse" if quick else mode.lower()
    if mode not in MODES:
        console.print(f"[bold red]Error:[/] Unknown mode '{mode}'. Choose from: {', '.join(MODES)}.")
        raise typer.Exit(code=1)
    mode_cfg = MODES[mode]
    pool = mode_cfg.pool(QUESTIONS)

    if is_tr:
        mode_label = f"{mode_cfg.label_tr} (~{mode_cfg.minutes} dk, {len(pool)} soru)"
        console.print(f"[bold][cyan]{name}[/] için Kıdem Değerlendirmesi Başlatılıyor (Track: [green]{track.value.upper()}[/])[/]")
        console.print(f"[dim]Mod: {mode_label}. Her senaryoyu prodüksiyondaki doğal refleksi yansıtacak şekilde yanıtlayın.[/dim]")
        console.print("[italic dim]⚡ Sınav bir önceki soruya verdiğiniz cevabın yetkinliğine göre zorlaşır veya kolaylaşır.[/italic dim]\n")
    else:
        mode_label = f"{mode_cfg.label} (~{mode_cfg.minutes} min, {len(pool)} questions)"
        console.print(f"[bold]Starting Seniority Assessment for [cyan]{name}[/] (Track: [green]{track.value.upper()}[/])[/]")
        console.print(f"[dim]Mode: {mode_label}. Answer each scenario reflecting your natural behavior in production.[/dim]")
        console.print("[italic dim]⚡ Questions adaptively scale up or down based on your previous answer's competency.[/italic dim]\n")

    engine = AdaptiveAssessmentEngine(track=track, questions=pool)
    dimensions = list(DimensionId)
    answers = {}
    q_index = 0
    total_to_ask = len(pool)
    rng = random.Random()

    for stage_idx, dim in enumerate(dimensions, start=1):
        dim_info = DIMENSION_METADATA.get(dim, {})
        stage_label = f"AŞAMA {stage_idx}/5" if is_tr else f"STAGE {stage_idx}/5"
        console.print(f"\n[bold yellow]━━━ {stage_label}: {dim_info.get('name', 'Pillar').upper()} ━━━[/]")

        while True:
            adaptive_result = engine.get_next_question(dimension=dim)
            if not adaptive_result:
                break

            q, adaptation_msg = adaptive_result
            q_index += 1

            if q_index > 1:
                console.print(f"[dim cyan]{adaptation_msg}[/]")

            # Scenario details
            q_title = (q.title_tr if is_tr and q.title_tr else q.title)
            q_scenario = (q.scenario_tr if is_tr and q.scenario_tr else q.scenario)
            source_badge = f" [bold magenta]({q.interview_source})[/]" if q.interview_source else ""

            scenario_word = "Senaryo" if is_tr else "Scenario"
            difficulty_word = "Zorluk" if is_tr else "Difficulty"

            console.print(Panel(
                f"[bold yellow]{scenario_word} ({q_index}/{total_to_ask}) [{difficulty_word}: Tier {q.difficulty}]:[/] [bold white]{q_title}[/]{source_badge}\n\n"
                f"[italic text-slate-300]{q_scenario}[/]",
                title=f"{dim_info.get('icon', '⚡')} {dim_info.get('name', 'Dimension')}",
                border_style="cyan",
                box=box.ROUNDED,
            ))

            letters = ["A", "B", "C", "D", "E"]
            # Shuffle so option position never hints at seniority.
            shuffled = q.options[:]
            rng.shuffle(shuffled)
            valid_choices = letters[:len(shuffled)]

            for ltr, opt in zip(letters, shuffled):
                opt_text = (opt.text_tr if is_tr and opt.text_tr else opt.text)
                console.print(f"  [bold cyan]({ltr})[/] {opt_text}")

            console.print("")
            choice = ""
            select_prompt = f"Seçeneği belirleyin ({'/'.join(valid_choices)})" if is_tr else f"Select option ({'/'.join(valid_choices)})"
            while choice not in valid_choices:
                choice = Prompt.ask(
                    f"[bold]{select_prompt}[/]",
                    default="A",
                    console=console,
                ).strip().upper()

            opt_idx = letters.index(choice)
            selected_option = shuffled[opt_idx]
            answers[q.id] = selected_option.score
            engine.record_answer(q, selected_option.score)
            console.print(f"[dim]Recorded: {choice}[/]\n")

            if mode == "pulse":
                break

    # Evaluate
    evaluator = SeniorityEvaluator(track=track)
    result = evaluator.evaluate_answers(
        answers=answers,
        candidate_name=name,
        assessment_mode=mode,
    )

    reporter = Reporter(result, console=console, lang=lang)
    reporter.print_terminal_summary()

    previous = previous_entry(result)
    if previous:
        _print_progress(result, previous, is_tr)
    if not no_history:
        save_result(result)

    # Exports
    if export_html or open_browser:
        target_html = export_html or f"devcaliber_report_{name.lower().replace(' ', '_')}.html"
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


def _mode_command(mode: str, name, track, lang, export_html, open_browser):
    assess(
        name=name,
        track=track,
        lang=lang,
        quick=False,
        mode=mode,
        no_history=False,
        export_html=export_html,
        export_md=None,
        export_json=None,
        badge=None,
        open_browser=open_browser,
    )


@app.command()
def sprint(
    name: str = typer.Option("Engineer", "--name", "-n", help="Candidate name"),
    track: Track = typer.Option(Track.GENERAL, "--track", "-t", help="Engineering track"),
    lang: str = typer.Option("en", "--lang", "-l", help="Language: 'en' or 'tr'"),
    export_html: Optional[str] = typer.Option(None, "--html", help="Path to save HTML report"),
    open_browser: bool = typer.Option(False, "--open", help="Open HTML report in browser"),
):
    """30-minute sprint assessment (15 adaptive scenarios, medium confidence)."""
    _mode_command("sprint", name, track, lang, export_html, open_browser)


@app.command()
def deep(
    name: str = typer.Option("Engineer", "--name", "-n", help="Candidate name"),
    track: Track = typer.Option(Track.GENERAL, "--track", "-t", help="Engineering track"),
    lang: str = typer.Option("en", "--lang", "-l", help="Language: 'en' or 'tr'"),
    export_html: Optional[str] = typer.Option(None, "--html", help="Path to save HTML report"),
    open_browser: bool = typer.Option(False, "--open", help="Open HTML report in browser"),
):
    """2-hour deep assessment (full question bank, high confidence)."""
    _mode_command("deep", name, track, lang, export_html, open_browser)


@app.command()
def exam(
    name: str = typer.Option("Engineer", "--name", "-n", help="Candidate name"),
    track: Track = typer.Option(Track.GENERAL, "--track", "-t", help="Engineering track"),
    lang: str = typer.Option("en", "--lang", "-l", help="Language: 'en' or 'tr'"),
    export_html: Optional[str] = typer.Option(None, "--html", help="Path to save HTML report"),
    open_browser: bool = typer.Option(False, "--open", help="Open HTML report in browser"),
):
    """Alias for `deep` (kept for backwards compatibility)."""
    _mode_command("deep", name, track, lang, export_html, open_browser)


@app.command()
def quick(
    name: str = typer.Option("Engineer", "--name", "-n", help="Candidate name"),
    track: Track = typer.Option(Track.GENERAL, "--track", "-t", help="Engineering track"),
    lang: str = typer.Option("en", "--lang", "-l", help="Language: 'en' or 'tr'"),
    export_html: Optional[str] = typer.Option(None, "--html", help="Path to save HTML report"),
    open_browser: bool = typer.Option(False, "--open", help="Open HTML report in browser"),
):
    """5-minute pulse check (5 core questions, low confidence)."""
    _mode_command("pulse", name, track, lang, export_html, open_browser)


@app.command()
def history():
    """Show your saved assessment history."""
    entries = load_history()
    if not entries:
        console.print("[dim]No saved results yet. Run `devcaliber sprint` first.[/dim]")
        return
    table = Table(title="Assessment History", box=box.ROUNDED)
    for col in ("Date", "Name", "Track", "Mode", "Level", "Score", "Confidence"):
        table.add_column(col)
    for e in entries:
        table.add_row(
            e.get("timestamp", ""), e.get("name", ""), e.get("track", ""), e.get("mode", ""),
            e.get("level", ""), str(e.get("overall_score", "")), e.get("confidence", ""),
        )
    console.print(table)


@app.command()
def matrix(
    dimension: Optional[DimensionId] = typer.Option(None, "--dimension", "-d", help="Filter by dimension"),
    level: Optional[str] = typer.Option(None, "--level", "-l", help="Filter by level code (L1, L2, L3, L4, L5)"),
):
    """Inspect the engineering career competency rubric table."""
    render_banner()
    table = Table(title="DevCaliber Engineering Competency Matrix", box=box.ROUNDED, expand=True)
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
    """Show DevCaliber version."""
    console.print(f"[bold cyan]DevCaliber[/] version [bold white]{__version__}[/]")


def main():
    app()


if __name__ == "__main__":
    main()

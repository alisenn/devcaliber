"""
Reporting engine: Terminal UI renderers, Markdown reports, JSON exporter,
interactive HTML Radar Dashboard, and SVG GitHub Profile Badges.
"""

import json
from typing import Dict, List, Optional
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress_bar import ProgressBar
from rich.text import Text
from rich import box

from seniormeter.models import AssessmentResult, DimensionId, SeniorityLevel
from seniormeter.matrix import DIMENSION_METADATA


LEVEL_COLORS: Dict[str, str] = {
    "L1": "cyan",
    "L2": "bright_blue",
    "L3": "bright_green",
    "L4": "magenta",
    "L5": "gold1",
}


class Reporter:
    """Renders assessment reports in multiple interactive and static formats."""

    def __init__(self, result: AssessmentResult, console: Optional[Console] = None):
        self.result = result
        self.console = console or Console()

    def print_terminal_summary(self):
        """Prints a stunning, color-rich scorecard to the terminal."""
        lvl_code = self.result.overall_level.code
        lvl_title = self.result.overall_level.title
        color = LEVEL_COLORS.get(lvl_code, "green")

        # Top banner
        header_text = Text()
        header_text.append(" LEVELCRAFT SENIORITY BENCHMARK REPORT \n", style="bold white on dark_blue")
        header_text.append(f"\nCandidate: {self.result.candidate_name}  |  Track: {self.result.track.value.upper()}\n", style="bold")
        header_text.append(f"Assessment Mode: {self.result.assessment_mode} ({self.result.total_questions} scenarios evaluated)\n", style="dim")
        self.console.print(Panel(header_text, border_style="blue", box=box.ROUNDED))

        # Overall Level Card
        card_content = (
            f"[bold {color}]Seniority Tier: {lvl_code}[/]\n"
            f"[bold white]{lvl_title}[/]\n\n"
            f"Overall Score: [bold]{self.result.overall_score:.2f} / 5.00[/]\n"
            f"Global Percentile: [bold {color}]Top {100 - int(self.result.overall_score * 19)}%[/] (Industry benchmark)"
        )
        self.console.print(Panel(card_content, title="[bold]Overall Placement[/]", border_style=color, box=box.DOUBLE))

        # Dimension Breakdown Table
        table = Table(title="Competency Dimensions Breakdown", box=box.ROUNDED, expand=True)
        table.add_column("Dimension", style="bold white", width=26)
        table.add_column("Score", justify="center", width=8)
        table.add_column("Level", justify="center", width=10)
        table.add_column("Visual Benchmark", width=28)
        table.add_column("Percentile", justify="right", width=12)

        for dim_id, dscore in self.result.dimension_scores.items():
            meta = DIMENSION_METADATA.get(dim_id, {"name": dim_id.value, "icon": "•"})
            d_color = LEVEL_COLORS.get(dscore.level.code, "white")
            
            # ASCII / bar visualization
            filled = int(dscore.score * 4)  # 20 chars max
            bar = f"[{d_color}]{'█' * filled}{'░' * (20 - filled)}[/]"
            
            table.add_row(
                f"{meta['icon']} {meta['name']}",
                f"{dscore.score:.2f}",
                f"[{d_color}]{dscore.level.code}[/]",
                bar,
                f"P{dscore.percentile}",
            )

        self.console.print(table)

        # Gap Analysis / Next Steps
        gap_panel_content = Text()
        gap_panel_content.append("TARGET ROADMAP TO ADVANCE TO NEXT LEVEL:\n\n", style="bold yellow")
        for rec in self.result.gap_recommendations[:3]:
            gap_panel_content.append(f"• {rec.dimension_name}: ", style="bold")
            if rec.action_items:
                gap_panel_content.append(f"{rec.action_items[0].description}\n", style="white")
                if rec.recommended_reading:
                    gap_panel_content.append(f"  📖 Reading: {rec.recommended_reading[0]}\n", style="dim italic")

        self.console.print(Panel(gap_panel_content, title="[bold yellow]Career Progression Actions[/]", border_style="yellow", box=box.ROUNDED))

    def generate_markdown(self) -> str:
        """Generates a professional Markdown assessment document."""
        r = self.result
        lvl_code = r.overall_level.code
        lvl_title = r.overall_level.title

        md = [
            f"# 🧭 LevelCraft Engineering Seniority Report",
            f"",
            f"**Candidate:** {r.candidate_name}  ",
            f"**Track:** {r.track.value.capitalize()}  ",
            f"**Assessed At:** {r.timestamp}  ",
            f"**Overall Level:** **`{lvl_code}` - {lvl_title}**  ",
            f"**Composite Score:** `{r.overall_score:.2f} / 5.00`  ",
            f"",
            f"---",
            f"",
            f"## 📊 Competency Radar Breakdown",
            f"",
            f"| Dimension | Score | Seniority Tier | Industry Percentile |",
            f"| :--- | :---: | :---: | :---: |",
        ]

        for dim_id, dscore in r.dimension_scores.items():
            meta = DIMENSION_METADATA.get(dim_id, {"name": dim_id.value, "icon": ""})
            md.append(f"| {meta.get('icon', '')} {meta['name']} | `{dscore.score:.2f}` | **{dscore.level.code}** | `Top {100 - dscore.percentile}%` |")

        md.extend([
            f"",
            f"---",
            f"",
            f"## 🎯 Targeted Growth Roadmap & Action Items",
            f"",
        ])

        for rec in r.gap_recommendations:
            md.append(f"### {rec.dimension_name} (`{rec.current_score:.2f}` ➔ `{rec.target_score:.1f}`)")
            for action in rec.action_items:
                md.append(f"- **{action.title}**: {action.description}")
            if rec.recommended_reading:
                md.append(f"- *Recommended Reading:* {', '.join(rec.recommended_reading)}")
            md.append("")

        md.extend([
            f"---",
            f"*Generated by [LevelCraft](https://github.com/alisenn/levelcraft) — The Open Source Seniority & Competency Matrix Engine.*"
        ])

        return "\n".join(md)

    def generate_json(self) -> str:
        """Returns JSON serialized representation of the results."""
        return self.result.model_dump_json(indent=2)

    def generate_svg_badge(self) -> str:
        """Generates an aesthetic SVG badge for GitHub READMEs."""
        lvl_code = self.result.overall_level.code
        lvl_title = self.result.overall_level.title
        badge_text = f"{lvl_code} • {lvl_title.split(' ')[0]}"

        # Shield SVG template
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="220" height="28" role="img" aria-label="Seniority: {badge_text}">
  <title>Seniority: {badge_text}</title>
  <linearGradient id="s" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <clipPath id="r">
    <rect width="220" height="28" rx="6" fill="#fff"/>
  </clipPath>
  <g clip-path="url(#r)">
    <rect width="80" height="28" fill="#1e293b"/>
    <rect x="80" width="140" height="28" fill="#0284c7"/>
    <rect width="220" height="28" fill="url(#s)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,sans-serif" text-rendering="geometricPrecision" font-size="12">
    <text aria-hidden="true" x="40" y="19" fill="#010101" fill-opacity=".3">Seniority</text>
    <text x="40" y="18" fill="#fff" font-weight="600">Seniority</text>
    <text aria-hidden="true" x="150" y="19" fill="#010101" fill-opacity=".3">{badge_text}</text>
    <text x="150" y="18" fill="#fff" font-weight="bold">{badge_text}</text>
  </g>
</svg>"""
        return svg

    def generate_html_dashboard(self) -> str:
        """Generates a self-contained, interactive HTML Radar Dashboard."""
        labels = [DIMENSION_METADATA[d]["name"] for d in self.result.dimension_scores.keys()]
        scores = [d.score for d in self.result.dimension_scores.values()]
        
        dim_cards_html = ""
        for dim_id, dscore in self.result.dimension_scores.items():
            meta = DIMENSION_METADATA.get(dim_id, {"name": dim_id.value, "icon": "⚡"})
            dim_cards_html += f"""
            <div class="bg-slate-800/80 border border-slate-700/60 rounded-xl p-5 shadow-lg">
                <div class="flex items-center justify-between mb-3">
                    <span class="text-2xl">{meta['icon']}</span>
                    <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-sky-500/20 text-sky-400 border border-sky-500/30">
                        {dscore.level.code}
                    </span>
                </div>
                <h3 class="font-bold text-slate-100 text-lg">{meta['name']}</h3>
                <div class="mt-4 flex items-baseline gap-2">
                    <span class="text-3xl font-extrabold text-white">{dscore.score:.2f}</span>
                    <span class="text-slate-400 text-sm">/ 5.00</span>
                </div>
                <div class="mt-2 text-xs text-emerald-400 font-medium">Percentile: Top {100 - dscore.percentile}%</div>
                <div class="w-full bg-slate-700/60 rounded-full h-2 mt-3">
                    <div class="bg-gradient-to-r from-sky-400 to-indigo-500 h-2 rounded-full" style="width: {(dscore.score / 5.0) * 100}%"></div>
                </div>
            </div>
            """

        roadmap_html = ""
        for rec in self.result.gap_recommendations:
            actions_list = "".join([f"<li class='text-sm text-slate-300 mb-1.5'>• <strong class='text-slate-100'>{a.title}:</strong> {a.description}</li>" for a in rec.action_items])
            reading = f"<div class='mt-2 text-xs text-sky-400 italic'>📖 Recommended: {', '.join(rec.recommended_reading)}</div>" if rec.recommended_reading else ""
            roadmap_html += f"""
            <div class="border-l-2 border-indigo-500 pl-4 py-1">
                <h4 class="font-semibold text-slate-200 text-base">{rec.dimension_name} (Target: {rec.target_score:.1f})</h4>
                <ul class="mt-2 list-none space-y-1">{actions_list}</ul>
                {reading}
            </div>
            """

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LevelCraft Seniority Dashboard — {self.result.candidate_name}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        body {{ font-family: 'Inter', sans-serif; }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen antialiased selection:bg-sky-500 selection:text-white">
    <div class="max-w-6xl mx-auto px-4 py-10">
        <!-- Header -->
        <header class="flex flex-col md:flex-row md:items-center justify-between pb-8 border-b border-slate-800 gap-4">
            <div>
                <div class="flex items-center gap-2">
                    <span class="text-3xl">🧭</span>
                    <h1 class="text-3xl font-extrabold tracking-tight bg-gradient-to-r from-sky-400 via-indigo-300 to-purple-400 bg-clip-text text-transparent">
                        LevelCraft Seniority Matrix
                    </h1>
                </div>
                <p class="text-slate-400 text-sm mt-1">Open-source software engineering career benchmark & diagnostic engine</p>
            </div>
            <div class="flex items-center gap-3">
                <div class="text-right">
                    <div class="font-medium text-slate-200">{self.result.candidate_name}</div>
                    <div class="text-xs text-slate-400">{self.result.track.value.capitalize()} Track • {self.result.timestamp}</div>
                </div>
            </div>
        </header>

        <!-- Main Score Hero -->
        <div class="mt-8 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            <div class="lg:col-span-5 bg-gradient-to-br from-slate-900 to-slate-800 border border-slate-700/80 rounded-2xl p-8 shadow-2xl relative overflow-hidden">
                <div class="absolute -right-10 -bottom-10 w-44 h-44 bg-sky-500/10 rounded-full blur-2xl"></div>
                <span class="px-3 py-1 rounded-full text-xs font-bold tracking-wide uppercase bg-sky-500/20 text-sky-300 border border-sky-500/30">
                    Official Assessment Result
                </span>
                <div class="mt-6">
                    <div class="text-5xl font-black text-white tracking-tight">{self.result.overall_level.code}</div>
                    <div class="text-xl font-semibold text-slate-300 mt-1">{self.result.overall_level.title}</div>
                </div>
                <div class="mt-8 pt-6 border-t border-slate-800 grid grid-cols-2 gap-4">
                    <div>
                        <div class="text-xs text-slate-400 uppercase font-semibold">Composite Score</div>
                        <div class="text-2xl font-bold text-sky-400 mt-1">{self.result.overall_score:.2f} <span class="text-xs text-slate-500">/ 5.0</span></div>
                    </div>
                    <div>
                        <div class="text-xs text-slate-400 uppercase font-semibold">Benchmark Percentile</div>
                        <div class="text-2xl font-bold text-emerald-400 mt-1">Top {100 - int(self.result.overall_score * 19)}%</div>
                    </div>
                </div>
            </div>

            <!-- Radar Chart -->
            <div class="lg:col-span-7 bg-slate-900/90 border border-slate-800 rounded-2xl p-6 shadow-xl flex flex-col items-center justify-center">
                <h3 class="text-sm font-semibold text-slate-300 mb-2 uppercase tracking-wider">Competency Radar Graph</h3>
                <div class="w-full max-w-md h-72">
                    <canvas id="radarChart"></canvas>
                </div>
            </div>
        </div>

        <!-- Dimension Cards Grid -->
        <div class="mt-10">
            <h2 class="text-xl font-bold text-white mb-6">Pillar Diagnostics</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-4">
                {dim_cards_html}
            </div>
        </div>

        <!-- Next Level Roadmap -->
        <div class="mt-10 bg-slate-900/80 border border-slate-800 rounded-2xl p-8">
            <div class="flex items-center gap-3 mb-6">
                <span class="text-2xl">🎯</span>
                <div>
                    <h3 class="text-lg font-bold text-white">Promotion & Growth Roadmap</h3>
                    <p class="text-slate-400 text-xs">Action items curated by Staff+ engineering leaders to unlock your next level.</p>
                </div>
            </div>
            <div class="space-y-6">
                {roadmap_html}
            </div>
        </div>

        <!-- Footer -->
        <footer class="mt-16 pt-8 border-t border-slate-800 flex flex-col md:flex-row items-center justify-between text-xs text-slate-500 gap-4">
            <div>Built with <span class="text-sky-400">LevelCraft</span> • Open Source Software Engineering Ladder Framework</div>
            <div><a href="https://github.com/alisenn/levelcraft" target="_blank" class="hover:text-slate-300 underline">GitHub Repository</a></div>
        </footer>
    </div>

    <script>
        const ctx = document.getElementById('radarChart').getContext('2d');
        new Chart(ctx, {{
            type: 'radar',
            data: {{
                labels: {json.dumps(labels)},
                datasets: [{{
                    label: 'Competency Score',
                    data: {json.dumps(scores)},
                    fill: true,
                    backgroundColor: 'rgba(14, 165, 233, 0.25)',
                    borderColor: 'rgb(14, 165, 233)',
                    pointBackgroundColor: 'rgb(56, 189, 248)',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: 'rgb(14, 165, 233)'
                }}]
            }},
            options: {{
                scales: {{
                    r: {{
                        angleLines: {{ color: 'rgba(255, 255, 255, 0.1)' }},
                        grid: {{ color: 'rgba(255, 255, 255, 0.1)' }},
                        pointLabels: {{
                            color: '#94a3b8',
                            font: {{ size: 11, weight: '600' }}
                        }},
                        ticks: {{
                            display: false,
                            stepSize: 1,
                            min: 0,
                            max: 5
                        }}
                    }}
                }},
                plugins: {{
                    legend: {{ display: false }}
                }},
                maintainAspectRatio: false
            }}
        }});
    </script>
</body>
</html>"""
        return html

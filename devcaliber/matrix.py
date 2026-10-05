"""
DevCaliber: Engineering Competency Matrix definitions, Level Rubrics,
and the scenario question bank (loaded from data/questions.json).
"""

import json
from pathlib import Path
from typing import Dict, List
from devcaliber.models import (
    DimensionId,
    SeniorityLevel,
    Track,
    Question,
    QuestionOption,
)

_QUESTIONS_PATH = Path(__file__).parent / "data" / "questions.json"
_LEVEL_BY_CODE = {lvl.code: lvl for lvl in SeniorityLevel}


def load_questions(path: Path = _QUESTIONS_PATH) -> List[Question]:
    """Load the question bank from the shared JSON source of truth."""
    raw = json.loads(path.read_text(encoding="utf-8"))
    for q in raw:
        for opt in q["options"]:
            opt["level_indicator"] = _LEVEL_BY_CODE[opt["level_indicator"]]
    return [Question(**q) for q in raw]


DIMENSION_METADATA: Dict[DimensionId, Dict[str, str]] = {
    DimensionId.CRAFT: {
        "name": "Craft & Architecture",
        "name_tr": "Mimari & Mühendislik Ustalığı",
        "description": "Code quality, system design, testing discipline, architectural scalability, and technical elegance.",
        "description_tr": "Kod kalitesi, system design, test disiplini, mimari ölçeklenebilirlik ve teknik zarafet.",
        "icon": "⚡",
    },
    DimensionId.OWNERSHIP: {
        "name": "Reliability & Ownership",
        "name_tr": "Güvenilirlik & Sahiplenme",
        "description": "Operational excellence, CI/CD, production observability, incident triage, and zero-downtime mindset.",
        "description_tr": "Operasyonel mükemmellik, CI/CD, production observability, incident müdahalesi ve zero-downtime kültürü.",
        "icon": "🛡️",
    },
    DimensionId.IMPACT: {
        "name": "Business & Product Impact",
        "name_tr": "İş & Ürün Etkisi",
        "description": "Translating user/business needs into engineering deliverables, pragmatic trade-offs, and ROI alignment.",
        "description_tr": "İş ve kullanıcı ihtiyaçlarını mühendislik çıktılarına dönüştürme, pragmatik trade-off dengesi ve ROI uyumu.",
        "icon": "🎯",
    },
    DimensionId.LEADERSHIP: {
        "name": "Leadership & Influence",
        "name_tr": "Liderlik & Etki Alanı",
        "description": "Mentorship, technical consensus, RFC authorship, cross-team collaboration, and raising the team bar.",
        "description_tr": "Mentörlük, teknik consensus, RFC yazımı, takımlar arası iş birliği ve mühendislik çıtasını yükseltme.",
        "icon": "🌟",
    },
    DimensionId.AUTONOMY: {
        "name": "Autonomy & Ambiguity",
        "name_tr": "Otonomi & Belirsizlik Yönetimi",
        "description": "Navigating ill-defined problems, setting long-term direction, and independently executing from 0 to 1.",
        "description_tr": "Ucu açık problemleri yapılandırma, uzun vadeli vizyon belirleme ve 0'dan 1'e bağımsız icra kabiliyeti.",
        "icon": "🚀",
    },
}

LEVEL_RUBRIC: Dict[DimensionId, Dict[SeniorityLevel, str]] = {
    DimensionId.CRAFT: {
        SeniorityLevel.L1: "Writes functional code for well-scoped tasks with guidance. Follows existing code conventions.",
        SeniorityLevel.L2: "Develops modular, tested code independently. Diagnoses bugs and designs small-to-medium components.",
        SeniorityLevel.L3: "Architects scalable systems and anticipates edge cases. Sets code quality standards and leads tech design reviews.",
        SeniorityLevel.L4: "Establishes multi-team architectural standards. Solves systemic performance and scalability bottlenecks.",
        SeniorityLevel.L5: "Defines company-wide technology strategy. Anticipates multi-year paradigm shifts and builds foundational frameworks.",
    },
    DimensionId.OWNERSHIP: {
        SeniorityLevel.L1: "Monitors personal PRs, responds to CI test failures, and learns deployment tooling.",
        SeniorityLevel.L2: "Owns features from development through deployment. Troubleshoots straightforward production alerts.",
        SeniorityLevel.L3: "Owns service-level reliability (SLIs/SLOs). Leads incident post-mortems and drives remediation action items.",
        SeniorityLevel.L4: "Builds organizational resilience. Implements fault-tolerant patterns, disaster recovery, and observability pipelines.",
        SeniorityLevel.L5: "Architects zero-downtime, global-scale infrastructure paradigms. Sets enterprise-wide disaster recovery policies.",
    },
    DimensionId.IMPACT: {
        SeniorityLevel.L1: "Executes assigned sprint tickets accurately according to provided specifications.",
        SeniorityLevel.L2: "Understands user stories, questions ambiguous specs, and delivers features that move team key metrics.",
        SeniorityLevel.L3: "Balances technical debt against feature velocity. Identifies high-ROI technical initiatives for business value.",
        SeniorityLevel.L4: "Aligns engineering investments with departmental strategic goals. Mitigates multi-million dollar technical risks.",
        SeniorityLevel.L5: "Drives top-line company valuation and industry-defining technical innovations. Creates competitive moats.",
    },
    DimensionId.LEADERSHIP: {
        SeniorityLevel.L1: "Active learner, receptive to feedback in code reviews, participates in team discussions.",
        SeniorityLevel.L2: "Provides constructive peer code reviews and onboard newer team members smoothly.",
        SeniorityLevel.L3: "Mentors junior and mid engineers, authors technical RFCs, builds team consensus on contentious topics.",
        SeniorityLevel.L4: "Acts as a force-multiplier across multiple teams. Identifies and cultivates future engineering leaders.",
        SeniorityLevel.L5: "Recognized industry luminary or executive technical advisor. Shapes company culture and attracts top-tier talent.",
    },
    DimensionId.AUTONOMY: {
        SeniorityLevel.L1: "Needs step-by-step guidance on task boundaries, troubleshooting steps, and execution sequence.",
        SeniorityLevel.L2: "Executes clearly scoped projects autonomously; escalates blockers promptly with proposed solutions.",
        SeniorityLevel.L3: "Handles ambiguous problem statements; breaks down multi-month initiatives into iterative execution plans.",
        SeniorityLevel.L4: "Thrives in undefined problem spaces. Identifies blind spots no one is talking about and creates roadmaps.",
        SeniorityLevel.L5: "Operates at the horizon level. Transforms abstract business uncertainties into multi-year engineering execution.",
    },
}

QUESTIONS: List[Question] = load_questions()

GROWTH_ROADMAP: Dict[DimensionId, Dict[SeniorityLevel, List[Dict[str, str]]]] = {
    DimensionId.CRAFT: {
        SeniorityLevel.L2: [
            {"title": "Deep Dive into Software Design", "action": "Study design patterns and write unit/integration tests with >80% coverage.", "reading": "Clean Code by Robert C. Martin"},
            {"title": "Refactoring Practice", "action": "Perform small, safe refactorings with automated test protection.", "reading": "Refactoring by Martin Fowler"},
        ],
        SeniorityLevel.L3: [
            {"title": "Author Technical Design Docs (RFCs)", "action": "Draft 2 technical design proposals before writing complex code, documenting alternatives and trade-offs.", "reading": "Designing Data-Intensive Applications by Martin Kleppmann"},
            {"title": "System Design Mastery", "action": "Study distributed systems patterns: caching, message queues, and database sharding.", "reading": "System Design Interview by Alex Xu"},
        ],
        SeniorityLevel.L4: [
            {"title": "Architectural Governance", "action": "Set multi-team architectural guardrails and deprecate legacy monolith systems cleanly.", "reading": "Software Architecture: The Hard Parts by Ford et al."},
            {"title": "Scale Optimization", "action": "Lead cross-cutting performance profiling, reducing p99 latency or cloud compute spend by >25%.", "reading": "Building Microservices by Sam Newman"},
        ],
        SeniorityLevel.L5: [
            {"title": "Technology Vision", "action": "Pioneer novel technology stacks or open-source infrastructure that creates defensible competitive advantage.", "reading": "The Staff Engineer's Path by Tanya Reilly"},
        ],
    },
    DimensionId.OWNERSHIP: {
        SeniorityLevel.L2: [
            {"title": "Production Exposure", "action": "Pair with seniors on production releases and monitor APM logs during deploys.", "reading": "The DevOps Handbook by Gene Kim"},
        ],
        SeniorityLevel.L3: [
            {"title": "Incident Commander Training", "action": "Volunteer as secondary on-call, then lead incident triage and postmortems.", "reading": "Site Reliability Engineering (Google SRE Book)"},
            {"title": "SLO/SLI Implementation", "action": "Define Error Budgets and latency SLOs for critical user paths.", "reading": "Seeking SRE by David N. Blank-Edelman"},
        ],
        SeniorityLevel.L4: [
            {"title": "Resilience Architecture", "action": "Introduce automated chaos tests, circuit breakers, and disaster recovery drills.", "reading": "Release It! by Michael Nygard"},
        ],
        SeniorityLevel.L5: [
            {"title": "Zero-Downtime Governance", "action": "Build global multi-region active-active redundancy and enterprise disaster standards.", "reading": "Designing Distributed Systems by Brendan Burns"},
        ],
    },
    DimensionId.IMPACT: {
        SeniorityLevel.L2: [
            {"title": "Understand the Business", "action": "Learn the company's North Star metric and how your team's sprint goals impact it.", "reading": "Inspired by Marty Cagan"},
        ],
        SeniorityLevel.L3: [
            {"title": "Pragmatic Scope Negotiation", "action": "Proactively suggest MVP cutbacks that save 40% engineering time while delivering core value.", "reading": "Escaping the Build Trap by Melissa Perri"},
            {"title": "Data-Driven Development", "action": "Ensure all major features have A/B tests or tracking events before merging.", "reading": "Lean Analytics by Alistair Croll"},
        ],
        SeniorityLevel.L4: [
            {"title": "Strategic Roadmapping", "action": "Collaborate directly with Product Directors to craft quarterly/annual OKRs.", "reading": "Good Strategy Bad Strategy by Richard Rumelt"},
        ],
        SeniorityLevel.L5: [
            {"title": "Company Value Creation", "action": "Identify non-obvious technology bets that unlock brand new revenue streams.", "reading": "Zero to One by Peter Thiel"},
        ],
    },
    DimensionId.LEADERSHIP: {
        SeniorityLevel.L2: [
            {"title": "Code Review Quality", "action": "Focus code reviews on architecture, readability, and testability rather than nits.", "reading": "The Art of Readable Code by Boswell & Foucher"},
        ],
        SeniorityLevel.L3: [
            {"title": "Structured Mentorship", "action": "Take formal responsibility for onboarding 1 new hire or mentoring 1 junior dev to promotion.", "reading": "Radical Candor by Kim Scott"},
            {"title": "Technical Alignment", "action": "Organize bi-weekly architecture syncs to align teammates on engineering standards.", "reading": "Crucial Conversations by Patterson et al."},
        ],
        SeniorityLevel.L4: [
            {"title": "Force Multiplication", "action": "Sponsor other engineers for high-visibility projects; lead cross-team tech councils.", "reading": "Staff Engineer by Will Larson"},
        ],
        SeniorityLevel.L5: [
            {"title": "Industry & Cultural Leadership", "action": "Keynote industry conferences, publish engineering blog posts, build open-source visibility.", "reading": "High Output Management by Andy Grove"},
        ],
    },
    DimensionId.AUTONOMY: {
        SeniorityLevel.L2: [
            {"title": "Autonomous Ticket Delivery", "action": "Take tickets from definition to production without needing supervision.", "reading": "The Pragmatic Programmer by Hunt & Thomas"},
        ],
        SeniorityLevel.L3: [
            {"title": "Deconstruct Ambiguity", "action": "Take vague feature requests and break them down into milestones, epics, and risks.", "reading": "Working Effectively with Legacy Code by Michael Feathers"},
        ],
        SeniorityLevel.L4: [
            {"title": "Spotting Unseen Problems", "action": "Identify technical or process blind spots before they impact the organization.", "reading": "The Effective Executive by Peter Drucker"},
        ],
        SeniorityLevel.L5: [
            {"title": "Strategic Horizon Navigation", "action": "Drive multi-year vision, establishing technical direction under high uncertainty.", "reading": "Thinking in Systems by Donella Meadows"},
        ],
    },
}

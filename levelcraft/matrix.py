"""
Competency Matrix definitions, Level Rubrics, and Assessment Question Bank.
Based on industry standards (Dropbox, Google, Spotify, and Staff Engineer frameworks).
"""

from typing import Dict, List
from levelcraft.models import (
    DimensionId,
    SeniorityLevel,
    Track,
    Question,
    QuestionOption,
)

# Human-readable labels and descriptions for each dimension
DIMENSION_METADATA: Dict[DimensionId, Dict[str, str]] = {
    DimensionId.CRAFT: {
        "name": "Craft & Architecture",
        "description": "Code quality, system design, testing discipline, architectural scalability, and technical elegance.",
        "icon": "⚡",
    },
    DimensionId.OWNERSHIP: {
        "name": "Reliability & Ownership",
        "description": "Operational excellence, CI/CD, production observability, incident triage, and zero-downtime mindset.",
        "icon": "🛡️",
    },
    DimensionId.IMPACT: {
        "name": "Business & Product Impact",
        "description": "Translating user/business needs into engineering deliverables, pragmatic trade-offs, and ROI alignment.",
        "icon": "🎯",
    },
    DimensionId.LEADERSHIP: {
        "name": "Leadership & Influence",
        "description": "Mentorship, technical consensus, RFC authorship, cross-team collaboration, and raising the team bar.",
        "icon": "🌟",
    },
    DimensionId.AUTONOMY: {
        "name": "Autonomy & Ambiguity",
        "description": "Navigating ill-defined problems, setting long-term direction, and independently executing from 0 to 1.",
        "icon": "🚀",
    },
}

# The Standard Engineering Matrix Rubric (L1 through L5)
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

# Concrete scenario questions to assess competencies
QUESTIONS: List[Question] = [
    # --- DIMENSION: CRAFT & ARCHITECTURE ---
    Question(
        id="craft_01",
        dimension=DimensionId.CRAFT,
        title="Handling Technical Debt & Architectural Refactoring",
        scenario="You inherit a critical legacy service that is becoming difficult to maintain and has low test coverage. How do you approach it?",
        is_quick=True,
        options=[
            QuestionOption(
                id="c1_a",
                text="I work on assigned tickets within the service, trying not to touch code outside my specific assignment.",
                score=1.0,
                level_indicator=SeniorityLevel.L1,
            ),
            QuestionOption(
                id="c1_b",
                text="I refactor local functions and add unit tests whenever I touch that part of the codebase ('Boy Scout rule').",
                score=2.0,
                level_indicator=SeniorityLevel.L2,
            ),
            QuestionOption(
                id="c1_c",
                text="I draft a technical proposal (RFC) defining strangler fig or modular extraction patterns, balance trade-offs with product, and lead the phased migration.",
                score=3.5,
                level_indicator=SeniorityLevel.L3,
            ),
            QuestionOption(
                id="c1_d",
                text="I establish organization-wide standards for deprecation, decouple systemic domain dependencies across teams, and define architectural boundaries that prevent future debt.",
                score=4.5,
                level_indicator=SeniorityLevel.L4,
            ),
            QuestionOption(
                id="c1_e",
                text="I evaluate whether our core technology paradigm still serves our 5-year business strategy, deciding between paradigm shifts or building next-generation platform foundations.",
                score=5.0,
                level_indicator=SeniorityLevel.L5,
            ),
        ],
    ),
    Question(
        id="craft_02",
        dimension=DimensionId.CRAFT,
        title="System Design & Scalability Planning",
        scenario="Your system is expected to experience a 10x traffic spike over the next two quarters. What is your reaction?",
        is_quick=False,
        options=[
            QuestionOption(
                id="c2_a",
                text="I wait for tasks to be assigned to me by the tech lead and scale server instance counts as instructed.",
                score=1.0,
                level_indicator=SeniorityLevel.L1,
            ),
            QuestionOption(
                id="c2_b",
                text="I run profiling on hot code paths and optimize database queries / caching layers for the endpoints I own.",
                score=2.0,
                level_indicator=SeniorityLevel.L2,
            ),
            QuestionOption(
                id="c2_c",
                text="I conduct load tests, identify bottlenecks (DB connections, contention, stateful services), and redesign architecture (asynchronous queues, partitioning, backpressure).",
                score=3.5,
                level_indicator=SeniorityLevel.L3,
            ),
            QuestionOption(
                id="c2_d",
                text="I design horizontal cross-cutting scaling strategies (distributed rate limiting, multi-region failover, caching topologies) across services with automated degradation modes.",
                score=4.5,
                level_indicator=SeniorityLevel.L4,
            ),
            QuestionOption(
                id="c2_e",
                text="I evaluate foundational infrastructure limits, negotiate budget tradeoffs with executives, and pioneer resilient distributed systems architecture company-wide.",
                score=5.0,
                level_indicator=SeniorityLevel.L5,
            ),
        ],
    ),
    Question(
        id="craft_03",
        dimension=DimensionId.CRAFT,
        title="Zero-Downtime Migrations & High-Risk Breaking Changes",
        scenario="You need to alter a database schema with 50 million rows and change a core entity used across 4 internal services without any maintenance downtime.",
        is_quick=False,
        options=[
            QuestionOption(
                id="c3_a",
                text="I submit an ALTER TABLE script to the DBA team and ask them to run it during off-peak hours.",
                score=1.0,
                level_indicator=SeniorityLevel.L1,
            ),
            QuestionOption(
                id="c3_b",
                text="I test the migration on a staging replica to measure execution time and check for lock timeouts.",
                score=2.0,
                level_indicator=SeniorityLevel.L2,
            ),
            QuestionOption(
                id="c3_c",
                text="I execute an Expand-and-Contract (Parallel Run) migration pattern: add new column, dual-write in application layer, backfill asynchronously in batches, and cleanly deprecate old schema.",
                score=3.6,
                level_indicator=SeniorityLevel.L3,
            ),
            QuestionOption(
                id="c3_d",
                text="I design a distributed event-driven synchronization or CDC (Change Data Capture) pipeline with contract testing (Pact) across downstream teams to eliminate coordination bottlenecks.",
                score=4.6,
                level_indicator=SeniorityLevel.L4,
            ),
            QuestionOption(
                id="c3_e",
                text="I establish enterprise-wide distributed data governance, zero-downtime database tooling (e.g. Gh-ost/Vitess patterns), and fault-isolated tenancy models across product lines.",
                score=5.0,
                level_indicator=SeniorityLevel.L5,
            ),
        ],
    ),
    # --- DIMENSION: RELIABILITY & OWNERSHIP ---
    Question(
        id="own_01",
        dimension=DimensionId.OWNERSHIP,
        title="Production Outage & Incident Response",
        scenario="A critical production incident occurs during peak hours affecting 20% of users. What role do you naturally play?",
        is_quick=True,
        options=[
            QuestionOption(
                id="o1_a",
                text="I follow along in the incident channel, observe senior colleagues, and test proposed fixes in lower environments if asked.",
                score=1.0,
                level_indicator=SeniorityLevel.L1,
            ),
            QuestionOption(
                id="o1_b",
                text="I check error logs and APM dashboards for my feature, pinpoint recent commits, and prepare a rollback or hotfix if it's my area.",
                score=2.2,
                level_indicator=SeniorityLevel.L2,
            ),
            QuestionOption(
                id="o1_c",
                text="I act as Incident Commander or primary responder, mitigate impact first (circuit breaker / rollback), coordinate stakeholders, and facilitate a blameless postmortem with preventative SLOs.",
                score=3.7,
                level_indicator=SeniorityLevel.L3,
            ),
            QuestionOption(
                id="o1_d",
                text="I analyze systemic vulnerabilities across incident trends, implement chaos engineering practices, and redesign the deployment/observability pipeline so this failure class is impossible.",
                score=4.6,
                level_indicator=SeniorityLevel.L4,
            ),
            QuestionOption(
                id="o1_e",
                text="I define enterprise reliability standards, manage executive communications during catastrophic risks, and reshape company-wide operational accountability.",
                score=5.0,
                level_indicator=SeniorityLevel.L5,
            ),
        ],
    ),
    Question(
        id="own_02",
        dimension=DimensionId.OWNERSHIP,
        title="Observability & Production Readiness",
        scenario="How do you ensure a new critical service is truly ready for production?",
        is_quick=False,
        options=[
            QuestionOption(
                id="o2_a",
                text="If it compiles, passes unit tests locally, and works in staging, I consider it ready for production.",
                score=1.0,
                level_indicator=SeniorityLevel.L1,
            ),
            QuestionOption(
                id="o2_b",
                text="I add structured logging, configure basic health check endpoints, and set up alerts for HTTP 500 spikes.",
                score=2.0,
                level_indicator=SeniorityLevel.L2,
            ),
            QuestionOption(
                id="o2_c",
                text="I implement golden signals (latency, traffic, errors, saturation), create canary rollout strategies, runbooks, and defined SLOs with actionable alerts.",
                score=3.5,
                level_indicator=SeniorityLevel.L3,
            ),
            QuestionOption(
                id="o2_d",
                text="I enforce automated production readiness checklists via CI/CD, distributed tracing across service boundaries, and graceful degradation fallback plans.",
                score=4.5,
                level_indicator=SeniorityLevel.L4,
            ),
            QuestionOption(
                id="o2_e",
                text="I champion automated self-healing systems, zero-trust telemetry infrastructure, and organization-wide resilience engineering principles.",
                score=5.0,
                level_indicator=SeniorityLevel.L5,
            ),
        ],
    ),
    Question(
        id="own_03",
        dimension=DimensionId.OWNERSHIP,
        title="Alert Fatigue & On-Call Engineering Health",
        scenario="Your team receives 50+ PagerDuty alerts per week, most of which are non-actionable or resolve themselves. Engineers are exhausted. What do you do?",
        is_quick=False,
        options=[
            QuestionOption(
                id="o3_a",
                text="I snooze or silence the alerts during my shifts and resolve them whenever they pop up.",
                score=1.0,
                level_indicator=SeniorityLevel.L1,
            ),
            QuestionOption(
                id="o3_b",
                text="I adjust threshold limits on the noisy alerts so they trigger less frequently.",
                score=2.0,
                level_indicator=SeniorityLevel.L2,
            ),
            QuestionOption(
                id="o3_c",
                text="I audit alert history, delete all non-actionable alerts, convert informational alerts into dashboards/daily digests, and attach runbooks to all surviving pager alerts.",
                score=3.7,
                level_indicator=SeniorityLevel.L3,
            ),
            QuestionOption(
                id="o3_d",
                text="I calculate on-call operational load (toil vs feature engineering), institute error budgets, and mandate feature freeze when SLO burn rate exceeds healthy limits.",
                score=4.6,
                level_indicator=SeniorityLevel.L4,
            ),
            QuestionOption(
                id="o3_e",
                text="I overhaul engineering on-call culture company-wide: align compensation/incentives with operational excellence, automate self-healing infrastructure, and eliminate systemic toil.",
                score=5.0,
                level_indicator=SeniorityLevel.L5,
            ),
        ],
    ),
    # --- DIMENSION: BUSINESS & PRODUCT IMPACT ---
    Question(
        id="imp_01",
        dimension=DimensionId.IMPACT,
        title="Prioritization & Product Trade-offs",
        scenario="A product manager requests a high-profile feature with a tight deadline, but the engineering design requires shortcuts that incur tech debt. What do you do?",
        is_quick=True,
        options=[
            QuestionOption(
                id="i1_a",
                text="I write the code as quickly as possible according to the PM's specification to meet the deadline.",
                score=1.0,
                level_indicator=SeniorityLevel.L1,
            ),
            QuestionOption(
                id="i1_b",
                text="I alert my tech lead about the deadline risk and ask for advice on which parts can be simplified.",
                score=2.0,
                level_indicator=SeniorityLevel.L2,
            ),
            QuestionOption(
                id="i1_c",
                text="I negotiate a phased MVP delivery: identify the 20% effort delivering 80% user value, explicitly document acceptable tech debt, and schedule remediation in the next sprint.",
                score=3.6,
                level_indicator=SeniorityLevel.L3,
            ),
            QuestionOption(
                id="i1_d",
                text="I partner with product leadership to evaluate the business thesis, explore alternative architectures (like leverage existing APIs/platforms), and prevent wasted engineering quarters.",
                score=4.6,
                level_indicator=SeniorityLevel.L4,
            ),
            QuestionOption(
                id="i1_e",
                text="I reframe the strategic market opportunity, aligning technical investments with multi-year company revenues or competitive market disruption.",
                score=5.0,
                level_indicator=SeniorityLevel.L5,
            ),
        ],
    ),
    Question(
        id="imp_02",
        dimension=DimensionId.IMPACT,
        title="Metric-Driven Engineering",
        scenario="How do you measure the success of an engineering project after shipping?",
        is_quick=False,
        options=[
            QuestionOption(
                id="i2_a",
                text="By having zero immediate crashes and closing all Jira sprint tasks.",
                score=1.0,
                level_indicator=SeniorityLevel.L1,
            ),
            QuestionOption(
                id="i2_b",
                text="By verifying feature adoption in analytics dashboards and monitoring error rates for 48 hours.",
                score=2.0,
                level_indicator=SeniorityLevel.L2,
            ),
            QuestionOption(
                id="i2_c",
                text="By tracking key business and technical KPIs (conversion rates, latency percentiles, cost per query) and running A/B testing experiments.",
                score=3.5,
                level_indicator=SeniorityLevel.L3,
            ),
            QuestionOption(
                id="i2_d",
                text="By establishing experimentation frameworks, measuring long-term user retention impacts, and computing engineering return on investment (ROI).",
                score=4.5,
                level_indicator=SeniorityLevel.L4,
            ),
            QuestionOption(
                id="i2_e",
                text="By measuring macro business outcomes: customer lifetime value, market share acquisition, and sustainable cost structure transformations.",
                score=5.0,
                level_indicator=SeniorityLevel.L5,
            ),
        ],
    ),
    Question(
        id="imp_03",
        dimension=DimensionId.IMPACT,
        title="Technical Spikes & Feasibility vs Hard Deadlines",
        scenario="Leadership wants to promise a prospective Fortune 500 client an enterprise feature in 6 weeks that normally takes 6 months of engineering. How do you handle it?",
        is_quick=False,
        options=[
            QuestionOption(
                id="i3_a",
                text="I commit to working overtime and weekends with the team to write as much code as possible.",
                score=1.0,
                level_indicator=SeniorityLevel.L1,
            ),
            QuestionOption(
                id="i3_b",
                text="I tell my manager it's impossible and quote the standard 6-month estimate.",
                score=2.0,
                level_indicator=SeniorityLevel.L2,
            ),
            QuestionOption(
                id="i3_c",
                text="I run a 2-day technical spike, identify the client's non-negotiable core workflow, strip out all non-essential requirements, and propose a viable Phase 1 pilot within 6 weeks.",
                score=3.6,
                level_indicator=SeniorityLevel.L3,
            ),
            QuestionOption(
                id="i3_d",
                text="I negotiate directly with Sales & Solution Engineering: leverage existing partner integrations or low-code extensions to close the deal without derailing core product roadmap.",
                score=4.6,
                level_indicator=SeniorityLevel.L4,
            ),
            QuestionOption(
                id="i3_e",
                text="I evaluate the macro enterprise strategy: determine if custom enterprise contracts justify pivoting company platform roadmap or if the opportunity cost hurts core business valuation.",
                score=5.0,
                level_indicator=SeniorityLevel.L5,
            ),
        ],
    ),
    # --- DIMENSION: LEADERSHIP & INFLUENCE ---
    Question(
        id="lead_01",
        dimension=DimensionId.LEADERSHIP,
        title="Technical Disagreements & Consensus Building",
        scenario="Two senior engineers strongly disagree on which database/framework to adopt for a new initiative. How do you resolve it?",
        is_quick=True,
        options=[
            QuestionOption(
                id="l1_a",
                text="I stay out of the dispute and wait for someone in charge to pick a decision.",
                score=1.0,
                level_indicator=SeniorityLevel.L1,
            ),
            QuestionOption(
                id="l1_b",
                text="I vote for the technology I personally feel more comfortable with or have used before.",
                score=2.0,
                level_indicator=SeniorityLevel.L2,
            ),
            QuestionOption(
                id="l1_c",
                text="I formulate an objective decision matrix (RACI/RFC) comparing operational cost, developer ergonomics, ecosystem maturity, and benchmark prototypes to reach team consensus.",
                score=3.7,
                level_indicator=SeniorityLevel.L3,
            ),
            QuestionOption(
                id="l1_d",
                text="I de-escalate ideological debates into reversible vs irreversible decisions ('Type 1 vs Type 2'), build cross-departmental alignment, and foster a 'disagree and commit' culture.",
                score=4.6,
                level_indicator=SeniorityLevel.L4,
            ),
            QuestionOption(
                id="l1_e",
                text="I shape the organization's overarching technical values, establish engineering governance models, and coach senior leaders on strategic alignment.",
                score=5.0,
                level_indicator=SeniorityLevel.L5,
            ),
        ],
    ),
    Question(
        id="lead_02",
        dimension=DimensionId.LEADERSHIP,
        title="Mentorship & Force Multiplication",
        scenario="How do you approach team knowledge sharing and mentoring?",
        is_quick=False,
        options=[
            QuestionOption(
                id="l2_a",
                text="I focus on my own learning and ask questions when I get stuck.",
                score=1.0,
                level_indicator=SeniorityLevel.L1,
            ),
            QuestionOption(
                id="l2_b",
                text="I answer questions in Slack and give helpful suggestions on pull requests when reviewing peer code.",
                score=2.0,
                level_indicator=SeniorityLevel.L2,
            ),
            QuestionOption(
                id="l2_c",
                text="I actively mentor junior/mid engineers 1-on-1, organize internal tech talks, and write comprehensive onboarding documentation.",
                score=3.5,
                level_indicator=SeniorityLevel.L3,
            ),
            QuestionOption(
                id="l2_d",
                text="I design career development ladders, run company-wide technical guilds, and coach future tech leads and staff engineers.",
                score=4.5,
                level_indicator=SeniorityLevel.L4,
            ),
            QuestionOption(
                id="l2_e",
                text="I define engineering talent strategy, cultivate an open-source engineering brand for hiring, and inspire the industry through publications and keynotes.",
                score=5.0,
                level_indicator=SeniorityLevel.L5,
            ),
        ],
    ),
    Question(
        id="lead_03",
        dimension=DimensionId.LEADERSHIP,
        title="Code Review Culture & Uplifting Peers",
        scenario="A talented engineer repeatedly submits 1,500-line PRs with no tests and gets defensive when teammates leave comments. How do you handle this?",
        is_quick=False,
        options=[
            QuestionOption(
                id="l3_a",
                text="I approve the PR without reading to avoid interpersonal conflict.",
                score=1.0,
                level_indicator=SeniorityLevel.L1,
            ),
            QuestionOption(
                id="l3_b",
                text="I leave rigorous inline comments pointing out every flaw and request changes until it's fixed.",
                score=2.0,
                level_indicator=SeniorityLevel.L2,
            ),
            QuestionOption(
                id="l3_c",
                text="I have a private 1-on-1 coffee chat, understand their workflow bottlenecks, demonstrate stacked PR / atomic commit workflows, and establish team PR size guidelines (<400 lines).",
                score=3.7,
                level_indicator=SeniorityLevel.L3,
            ),
            QuestionOption(
                id="l3_d",
                text="I introduce automated linters, semantic PR checks, and PR size warnings in CI, removing personal bias from reviews while mentoring senior peers in constructive feedback techniques.",
                score=4.6,
                level_indicator=SeniorityLevel.L4,
            ),
            QuestionOption(
                id="l3_e",
                text="I cultivate a psychologically safe, high-trust engineering culture org-wide where feedback is sought after, continuous learning is rewarded, and high engineering standards are embraced.",
                score=5.0,
                level_indicator=SeniorityLevel.L5,
            ),
        ],
    ),
    # --- DIMENSION: AUTONOMY & AMBIGUITY ---
    Question(
        id="auto_01",
        dimension=DimensionId.AUTONOMY,
        title="Navigating Ambiguous Goals",
        scenario="You receive a high-level goal: 'Improve developer productivity and build speed by next quarter.' There is no specification. What is your first move?",
        is_quick=True,
        options=[
            QuestionOption(
                id="a1_a",
                text="I ask management to provide specific tasks and acceptance criteria before starting work.",
                score=1.0,
                level_indicator=SeniorityLevel.L1,
            ),
            QuestionOption(
                id="a1_b",
                text="I look for obvious low-hanging fruit (like deleting unused tests or updating node/python versions) and ask if that helps.",
                score=2.0,
                level_indicator=SeniorityLevel.L2,
            ),
            QuestionOption(
                id="a1_c",
                text="I instrument telemetry on CI/CD pipelines, survey developers to find top friction points, define a quantitative baseline (P90 build time), and deliver iterative fixes.",
                score=3.6,
                level_indicator=SeniorityLevel.L3,
            ),
            QuestionOption(
                id="a1_d",
                text="I diagnose systemic bottlenecks (remote caching, monorepo tooling, flaky test isolation, local dev environments), form a virtual task force, and transform team developer velocity.",
                score=4.6,
                level_indicator=SeniorityLevel.L4,
            ),
            QuestionOption(
                id="a1_e",
                text="I redefine the organizational engineering workflow: evaluate cloud dev environments, build vs buy tooling investments, and align engineering tooling with multi-year headcount growth.",
                score=5.0,
                level_indicator=SeniorityLevel.L5,
            ),
        ],
    ),
    Question(
        id="auto_02",
        dimension=DimensionId.AUTONOMY,
        title="Project Execution from 0 to 1",
        scenario="You are tasked with kickstarting a brand new domain or Greenfield microservice from scratch. How do you manage execution?",
        is_quick=False,
        options=[
            QuestionOption(
                id="a2_a",
                text="I wait for the architecture skeleton and repository scaffolding to be set up by seniors before picking up tickets.",
                score=1.0,
                level_indicator=SeniorityLevel.L1,
            ),
            QuestionOption(
                id="a2_b",
                text="I set up the repo using standard company templates, write boilerplate CRUD endpoints, and implement the initial feature spec.",
                score=2.0,
                level_indicator=SeniorityLevel.L2,
            ),
            QuestionOption(
                id="a2_c",
                text="I write the Architecture RFC, define domain models, establish testing frameworks, CI/CD pipeline, and coordinate integration with dependent services.",
                score=3.5,
                level_indicator=SeniorityLevel.L3,
            ),
            QuestionOption(
                id="a2_d",
                text="I navigate cross-team dependencies, unblock legal/security approvals, build evolutionary architecture that can adapt to changing product needs, and guarantee smooth rollout.",
                score=4.5,
                level_indicator=SeniorityLevel.L4,
            ),
            QuestionOption(
                id="a2_e",
                text="I identify new product opportunities through technology innovation, assemble strategic teams, and lead high-risk, high-reward ventures that redefine company capabilities.",
                score=5.0,
                level_indicator=SeniorityLevel.L5,
            ),
        ],
    ),
    Question(
        id="auto_03",
        dimension=DimensionId.AUTONOMY,
        title="Cross-Team Friction & Breaking Architectural Blockers",
        scenario="Your team's highest priority initiative is completely blocked because another platform team has delayed building a required API for 2 consecutive quarters.",
        is_quick=False,
        options=[
            QuestionOption(
                id="a3_a",
                text="I put my ticket in 'Blocked' status and wait until the other team finishes.",
                score=1.0,
                level_indicator=SeniorityLevel.L1,
            ),
            QuestionOption(
                id="a3_b",
                text="I ping the other team in Slack every few days asking for updates on their delivery date.",
                score=2.0,
                level_indicator=SeniorityLevel.L2,
            ),
            QuestionOption(
                id="a3_c",
                text="I propose an internal open-source model: I draft the API contract, offer to write the PR directly into their repository, and only request their code review and deployment.",
                score=3.8,
                level_indicator=SeniorityLevel.L3,
            ),
            QuestionOption(
                id="a3_d",
                text="I bring both engineering managers together, demonstrate the company revenue impact of the blockage, realign quarterly roadmap priorities, or architect a temporary decoupling adapter.",
                score=4.7,
                level_indicator=SeniorityLevel.L4,
            ),
            QuestionOption(
                id="a3_e",
                text="I identify the systemic organizational dysfunction (silos, conflicting incentives, misaligned OKRs), partner with VPs of Engineering to redesign team topologies and service boundaries.",
                score=5.0,
                level_indicator=SeniorityLevel.L5,
            ),
        ],
    ),
]

# Actionable career roadmaps and resources for bridging seniority gaps
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

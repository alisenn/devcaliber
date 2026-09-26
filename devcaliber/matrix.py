"""
DevCaliber: Engineering Competency Matrix definitions, Level Rubrics,
and the Comprehensive 30-Scenario Assessment Question Bank with Real Glassdoor / FAANG Scenarios.
"""

from typing import Dict, List
from devcaliber.models import (
    DimensionId,
    SeniorityLevel,
    Track,
    Question,
    QuestionOption,
)

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

QUESTIONS: List[Question] = [
    # =========================================================================
    # DIMENSION 1: CRAFT & ARCHITECTURE (6 Questions)
    # =========================================================================
    Question(
        id="craft_01",
        difficulty=2,
        dimension=DimensionId.CRAFT,
        title="Technical Debt & Refactoring Legacy Monoliths",
        title_tr="Teknik Borç Yönetimi & Legacy Monolith Refactoring",
        scenario="You inherit a critical legacy service that is becoming difficult to maintain and has low test coverage. How do you approach it?",
        scenario_tr="Kritik bir legacy servisi devraldınız; kod tabanı giderek karmaşıklaşıyor ve test coverage oldukça düşük. Bu duruma nasıl yaklaşırsınız?",
        interview_source="Glassdoor: Stripe Senior Backend (Monolith Decomposition & Refactoring)",
        question_type="architecture_tradeoff",
        is_quick=True,
        options=[
            QuestionOption(
                id="c1_a",
                text="I work strictly on assigned tickets within the service, trying not to touch code outside my immediate assignment.",
                text_tr="Bana atanan sprint görevleri dışındaki koda dokunmamaya özen gösterir, sadece acil görevi teslim ederim.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="c1_b",
                text="I refactor local functions and add unit tests whenever I touch that part of the codebase ('Boy Scout rule').",
                text_tr="Boy Scout kuralını uygulayarak dokunduğum lokal fonksiyonları refactor eder ve küçük unit testler eklerim.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="c1_c",
                text="I draft a technical RFC defining strangler fig or modular extraction patterns, balance trade-offs with product, and lead the migration.",
                text_tr="Strangler Fig deseni veya modüler ayrıştırmayı tanımlayan teknik bir RFC hazırlar, product ekibiyle trade-off'ları netleştirip refactoring'e liderlik ederim.",
                score=3.5,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="c1_d",
                text="I establish organization-wide standards for deprecation, decouple systemic domain dependencies across teams, and define architectural boundaries.",
                text_tr="Şirket genelinde deprecation standartları belirler, takımlar arası domain bağımlılıklarını çözer ve net mimari sınırlar çizerim.",
                score=4.5,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="c1_e",
                text="I evaluate whether our core technology paradigm still serves our 5-year business strategy, deciding between paradigm shifts or building platform foundations.",
                text_tr="Temel teknoloji paradigmamızın 5 yıllık iş stratejimize uygunluğunu değerlendirir; radikal bir platform dönüşümü veya temel altyapı inşasına karar veririm.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="craft_02",
        difficulty=3,
        dimension=DimensionId.CRAFT,
        title="System Design & 10x Scalability Planning",
        title_tr="System Design & 10x Ölçeklenebilirlik Planlaması",
        scenario="Your system is expected to experience a 10x traffic spike over the next two quarters. What is your reaction?",
        scenario_tr="Sisteminizin önümüzdeki 6 ay içinde 10 kat trafik artışı yaşaması bekleniyor. İlk tepkiniz ve yaklaşımınız ne olur?",
        interview_source="Glassdoor: Meta E5/E6 Systems (Scalability Bottlenecks & Capacity Planning)",
        question_type="system_design",
        is_quick=False,
        options=[
            QuestionOption(
                id="c2_a",
                text="I wait for tasks to be assigned to me by the tech lead and scale server instance counts as instructed.",
                text_tr="Tech Lead'in görev vermesini bekler ve talimat verildiğinde sunucu instance sayılarını artırırım.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="c2_b",
                text="I run profiling on hot code paths and optimize database queries / caching layers for the endpoints I own.",
                text_tr="Sorumlu olduğum endpoint'lerde hot code path profiling yapar, yavaş veritabanı sorgularını ve indeksleri optimize ederim.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="c2_c",
                text="I conduct load tests, identify bottlenecks (DB connections, state contention), and redesign architecture (queues, partitioning, backpressure).",
                text_tr="Kapsamlı load testleri yapar, darboğazları (DB connection pool, state contention) tespit eder; queue, partitioning ve backpressure ile mimariyi yeniden tasarlarım.",
                score=3.5,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="c2_d",
                text="I design horizontal cross-cutting scaling strategies (distributed rate limiting, multi-region failover, caching topologies) with automated degradation.",
                text_tr="Organizasyon genelinde distributed rate limiting, multi-region failover ve aşamalı degradation (graceful degradation) içeren yatay ölçeklenme stratejisi kurarım.",
                score=4.5,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="c2_e",
                text="I evaluate foundational infrastructure limits, negotiate budget tradeoffs with executives, and pioneer resilient distributed systems architecture org-wide.",
                text_tr="Temel altyapı limitlerini analiz eder, C-level ile bütçe ve risk trade-off'larını müzakere eder, şirket genelinde dayanıklı distributed systems mimarisine öncülük ederim.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="craft_03",
        difficulty=4,
        dimension=DimensionId.CRAFT,
        title="Zero-Downtime Data Migration & High-Risk Breaking Changes",
        title_tr="Zero-Downtime Data Migration & Kritik Şema Dönüşümü",
        scenario="You need to alter a database schema with 50 million rows and change a core entity used across 4 internal services without any maintenance downtime.",
        scenario_tr="50 milyon satırlık bir veritabanı tablosunda şema değişikliği yapmanız ve 4 dahili mikroserviste kullanılan temel bir modeli sıfır kesinti (zero-downtime) ile güncellemeniz gerekiyor.",
        interview_source="Glassdoor: Netflix Senior Platform (Zero-Downtime Database Migration & Dual-Writing)",
        question_type="system_design",
        is_quick=False,
        options=[
            QuestionOption(
                id="c3_a",
                text="I submit an ALTER TABLE script to the DBA team and ask them to run it during off-peak hours.",
                text_tr="ALTER TABLE SQL scriptini DBA ekibine iletir ve gece saatlerinde çalıştırmalarını rica ederim.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="c3_b",
                text="I test the migration on a staging replica to measure execution time and check for lock timeouts.",
                text_tr="Migration'ı staging kopyasında test ederek çalışma süresini ve olası table lock sürelerini ölçerim.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="c3_c",
                text="I execute an Expand-and-Contract (Parallel Run) migration pattern: add new column, dual-write in application layer, backfill asynchronously, and cleanly deprecate.",
                text_tr="Expand-and-Contract (Parallel Run) modelini uygularım: Yeni kolonu ekle, dual-write yap, asenkron backfill çalıştır, okumayı yeni kolona çevir ve eskiyi deprecate et.",
                score=3.6,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="c3_d",
                text="I design a distributed event-driven synchronization or CDC (Change Data Capture) pipeline with contract testing (Pact) across downstream teams.",
                text_tr="Debezium/Kafka CDC (Change Data Capture) ve tüketici kontrat testleri (Pact) ile takımlar arası bağımsızlığı garanti eden asenkron veri senkronizasyonu tasarlarım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="c3_e",
                text="I establish enterprise-wide distributed data governance, zero-downtime database tooling (e.g. Gh-ost/Vitess patterns), and fault-isolated tenancy models.",
                text_tr="Şirket genelinde gh-ost/Vitess desenleri, multi-tenant fault isolation ve kurumsal zero-downtime veri yönetişimi standartlarını kurarım.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="craft_04",
        difficulty=4,
        dimension=DimensionId.CRAFT,
        title="Distributed Caching & Stampede Prevention",
        title_tr="Distributed Caching & Thundering Herd (Stampede) Önleme",
        scenario="During peak load, a cache cluster eviction causes a thundering herd (cache stampede) that nearly brings down the primary database. How do you resolve it?",
        scenario_tr="Pik trafik anında cache kümesindeki eviction nedeniyle thundering herd (cache stampede) meydana geliyor ve ana veritabanı kilitlenme noktasına geliyor. Nasıl çözersiniz?",
        interview_source="Glassdoor: Google L5 Infrastructure (Distributed Caching & Thundering Herd)",
        question_type="system_design",
        is_quick=False,
        options=[
            QuestionOption(
                id="c4_a",
                text="I restart the application pods and increase the Redis memory limit.",
                text_tr="Uygulama pod'larını yeniden başlatır ve Redis bellek limitini artırırım.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="c4_b",
                text="I add a random jitter to cache TTLs so keys do not expire simultaneously.",
                text_tr="Tüm anahtarların aynı anda düşmemesi için cache TTL değerlerine rastgele jitter (sapma) eklerim.",
                score=2.2,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="c4_c",
                text="I implement probabilistic early expiration (XFetch algorithm) or mutex locks (singleflight) around cache misses to prevent redundant database queries.",
                text_tr="Cache miss anında veritabanına sadece tek bir sorgu göndermek için Singleflight / distributed mutex ve XFetch erken yenileme algoritması kurarım.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="c4_d",
                text="I architect a multi-tiered caching topology (local in-memory L1 + distributed L2) with circuit breakers and stale-while-revalidate background refreshers.",
                text_tr="Çok katmanlı caching topolojisi (L1 local in-memory + L2 distributed Redis), stale-while-revalidate arka plan yenilemesi ve circuit breaker mimarisi kurarım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="c4_e",
                text="I redesign the data access paradigm: transition from read-through caching to event-driven materialization views (CQRS/Kafka) with guaranteed sub-millisecond latencies.",
                text_tr="Veri erişim modelini kökten yenilerim: Read-through cache yerine CQRS ve Kafka tabanlı önceden hesaplanmış materialize view'lar ile sub-millisecond gecikme garanti ederim.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="craft_05",
        difficulty=3,
        dimension=DimensionId.CRAFT,
        title="Architectural Boundary: Monolith vs Microservices",
        title_tr="Mimari Sınırlar: Modular Monolith vs Microservices",
        scenario="A debate arises: should your team split a growing monolithic domain into 3 separate microservices?",
        scenario_tr="Takımda hararetli bir tartışma var: Büyüyen monolitik bir domain'i 3 bağımsız microservice'e ayırmalı mıyız?",
        interview_source="Glassdoor: Uber Senior Staff (Architectural Boundaries & Service Decomposition)",
        question_type="architecture_tradeoff",
        is_quick=False,
        options=[
            QuestionOption(
                id="c5_a",
                text="I support whichever option uses newer and more modern technologies.",
                text_tr="Daha yeni ve trend teknolojileri deneyimlememizi sağlayacak seçeneği desteklerim.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="c5_b",
                text="I follow standard microservice tutorials and begin splitting database tables into new repos.",
                text_tr="Standart microservice rehberlerini takip ederek veritabanı tablolarını yeni repolara taşımaya başlarım.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="c5_c",
                text="I analyze domain cohesion (Bounded Contexts) and network boundaries; I advocate for a strictly modular monolith first unless deployment independence is strictly required.",
                text_tr="Domain sınırlarını (Bounded Contexts) analiz ederim; deployment bağımsızlığı ve ölçek ayrımı kesin bir zorunluluk değilse önce Modular Monolith öneririm.",
                score=3.6,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="c5_d",
                text="I evaluate the organizational overhead: distributed transactions, latency budgets, CI/CD operational tax, and team cognitive load before establishing microservice boundaries.",
                text_tr="Distributed transactions (Saga), network gecikme bütçesi, CI/CD operasyonel yükü ve ekip bilişsel kapasitesini hesaplayarak net servis sınırları belirlerim.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="c5_e",
                text="I govern organizational architecture according to Conway's Law: align team boundaries, communication channels, and business agility with system architecture.",
                text_tr="Conway Kanunu doğrultusunda organizasyonel yapıyı, ekip sahiplik sınırlarını ve iş çevikliğini sistem mimarisiyle kusursuz şekilde senkronize ederim.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="craft_06",
        difficulty=5,
        dimension=DimensionId.CRAFT,
        title="Zero-Day Vulnerability & Supply Chain Security",
        title_tr="Zero-Day Zafiyeti & Supply Chain Güvenliği",
        scenario="A critical remote code execution (RCE) vulnerability (like Log4j / XZ Utils) is discovered in a core open-source library used across 30 company repositories. What do you do?",
        scenario_tr="30 şirket reposunda kullanılan açık kaynak bir kütüphanede Log4j / XZ benzeri kritik bir RCE zero-day güvenlik açığı tespit edildi. Aksiyonunuz nedir?",
        interview_source="Glassdoor: Datadog Principal Security (Supply Chain Attacks & Zero-Day Mitigation)",
        question_type="system_design",
        is_quick=False,
        options=[
            QuestionOption(
                id="c6_a",
                text="I wait for security analysts to send a Jira ticket with the exact version bump required.",
                text_tr="Güvenlik ekibinin bana hangi versiyona geçmem gerektiğini belirten bir Jira bileti açmasını beklerim.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="c6_b",
                text="I bump the library version in my immediate repo and trigger a manual deployment to staging.",
                text_tr="Kendi sorumlu olduğum repodaki versiyonu günceller ve staging ortamına deploy ederim.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="c6_c",
                text="I write automated dependency audit scripts, coordinate emergency hotfixes across all affected repositories, and verify patch efficacy with exploit reproduction tests.",
                text_tr="Otomasyon scriptleri ile etkilenen tüm servisleri tarar, acil hotfix koordinasyonu yapar ve exploit doğrulama testleri ile yamanın çalıştığını teyit ederim.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="c6_d",
                text="I implement automated Software Bill of Materials (SBOM) tracking, automated dependency scanning (Dependabot/Snyk) in CI/CD, and WAF virtual patching rules.",
                text_tr="CI/CD'de otomatik SBOM (Software Bill of Materials) takibi, Snyk/Dependabot taraması ve WAF seviyesinde sanal yamalama (virtual patching) kurallarını devreye alırım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="c6_e",
                text="I architect enterprise zero-trust supply chain security: cryptographic artifact signing (Sigstore), sandboxed container runtimes, and company-wide security governance.",
                text_tr="Uçtan uca Zero-Trust supply chain mimarisi kurarım: Kriptografik imzalama (Sigstore), izole runtime sandbox'ları ve şirket çapında tedarik zinciri yönetişimi.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),

    # =========================================================================
    # DIMENSION 2: RELIABILITY & OWNERSHIP (6 Questions)
    # =========================================================================
    Question(
        id="own_01",
        difficulty=3,
        dimension=DimensionId.OWNERSHIP,
        title="Production Sev-1 Outage & Incident Response",
        title_tr="Production Sev-1 Outage & Incident Yönetimi",
        scenario="A critical production incident occurs during peak hours affecting 20% of users. What role do you naturally play?",
        scenario_tr="Pik saatlerde kullanıcıların %20'sini etkileyen kritik bir production kesintisi (Sev-1) yaşanıyor. Bu süreçte doğal olarak nasıl bir rol üstlenirsiniz?",
        interview_source="Glassdoor: Google L5 SRE (Incident Commander & Blameless Postmortems)",
        question_type="scenario",
        is_quick=True,
        options=[
            QuestionOption(
                id="o1_a",
                text="I follow along in the incident channel, observe senior colleagues, and test proposed fixes in lower environments if asked.",
                text_tr="Incident kanalını izler, kıdemli mühendisleri takip eder ve istenirse test ortamında doğrulamalara yardımcı olurum.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="o1_b",
                text="I check error logs and APM dashboards for my feature, pinpoint recent commits, and prepare a rollback or hotfix if it's my area.",
                text_tr="Sorumlu olduğum servisin APM ve hata loglarını inceler, son commit'leri filtreler ve gerekiyorsa hızlıca rollback hazırlarım.",
                score=2.2,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="o1_c",
                text="I act as Incident Commander or primary responder, mitigate impact first (circuit breaker / rollback), coordinate stakeholders, and facilitate a blameless postmortem.",
                text_tr="Incident Commander rolünü üstlenir; önce etkiyi sınırlarım (circuit breaker/rollback), paydaş iletişimini yönetir ve sonrasında blameless postmortem yönetirim.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="o1_d",
                text="I analyze systemic vulnerabilities across incident trends, implement chaos engineering practices, and redesign the deployment/observability pipeline.",
                text_tr="Geçmiş incident trendlerindeki sistemik açıkları analiz eder, Chaos Engineering tatbikatları başlatır ve deployment/canary boru hattını yeniden tasarlarım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="o1_e",
                text="I define enterprise reliability standards, manage executive communications during catastrophic risks, and reshape company-wide operational accountability.",
                text_tr="Kurumsal güvenilirlik standartlarını belirler, felaket anlarında yönetim kurulu iletişimini yürütür ve şirket çapında operasyonel hesap verebilirliği tesis ederim.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="own_02",
        difficulty=2,
        dimension=DimensionId.OWNERSHIP,
        title="Observability & Production Readiness",
        title_tr="Observability & Production Readiness Standartları",
        scenario="How do you ensure a new critical service is truly ready for production?",
        scenario_tr="Yeni geliştirilen kritik bir servisin production ortamına çıkmaya gerçekten hazır olduğundan nasıl emin olursunuz?",
        interview_source="Glassdoor: Spotify Senior Backend (Production Readiness & Golden Signals)",
        question_type="system_design",
        is_quick=False,
        options=[
            QuestionOption(
                id="o2_a",
                text="If it compiles, passes unit tests locally, and works in staging, I consider it ready for production.",
                text_tr="Lokalde testleri geçiyorsa ve staging ortamında sorunsuz çalışıyorsa production için hazır sayarım.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="o2_b",
                text="I add structured logging, configure basic health check endpoints, and set up alerts for HTTP 500 spikes.",
                text_tr="Yapılandırılmış JSON loglama ekler, temel health-check endpoint'i açar ve HTTP 500 hataları için temel alert kurarım.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="o2_c",
                text="I implement golden signals (latency, traffic, errors, saturation), create canary rollout strategies, runbooks, and defined SLOs with actionable alerts.",
                text_tr="4 Golden Signal'ı (Latency, Traffic, Errors, Saturation) kurar; Canary rollout stratejisi, operasyonel runbook'lar ve aksiyon alınabilir SLO alert'leri tanımlarım.",
                score=3.5,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="o2_d",
                text="I enforce automated production readiness checklists via CI/CD, distributed tracing across service boundaries, and graceful degradation fallback plans.",
                text_tr="CI/CD üzerinden otomatik production readiness kontrolü, OpenTelemetry distributed tracing ve sistemik graceful degradation planları zorunlu kılarım.",
                score=4.5,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="o2_e",
                text="I champion automated self-healing systems, zero-trust telemetry infrastructure, and organization-wide resilience engineering principles.",
                text_tr="Otomatik self-healing altyapıları, kurumsal gözlemlenebilirlik platformu ve şirket geneline yayılan dayanıklılık mühendisliği felsefesine liderlik ederim.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="own_03",
        difficulty=3,
        dimension=DimensionId.OWNERSHIP,
        title="Alert Fatigue & On-Call Engineering Health",
        title_tr="Alert Fatigue & On-Call Mühendislik Sağlığı",
        scenario="Your team receives 50+ PagerDuty alerts per week, most of which are non-actionable or resolve themselves. Engineers are exhausted. What do you do?",
        scenario_tr="Takımınız haftada 50'den fazla PagerDuty uyarısı alıyor; çoğu aksiyon gerektirmiyor veya kendiliğinden sönüyor. Mühendisler bitkin durumda. Ne yaparsınız?",
        interview_source="Glassdoor: Amazon SDE III (Operational Excellence & On-Call Health)",
        question_type="scenario",
        is_quick=False,
        options=[
            QuestionOption(
                id="o3_a",
                text="I snooze or silence the alerts during my shifts and resolve them whenever they pop up.",
                text_tr="Nöbetteyken tekrarlayan alarmları sessize alır, bildirim geldikçe ekrandan kapatırım.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="o3_b",
                text="I adjust threshold limits on the noisy alerts so they trigger less frequently.",
                text_tr="Çok sık çalan alarmların eşik (threshold) değerlerini yükselterek daha az bildirim göndermelerini sağlarım.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="o3_c",
                text="I audit alert history, delete all non-actionable alerts, convert informational alerts into dashboards/daily digests, and attach runbooks to all surviving pager alerts.",
                text_tr="Tüm alarm geçmişini denetler, aksiyonu olmayan alarmları siler, bilgilendirme amaçlıları günlük rapora çevirir ve kalan her pager alarmına runbook bağlarım.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="o3_d",
                text="I calculate on-call operational load (toil vs feature engineering), institute error budgets, and mandate feature freeze when SLO burn rate exceeds healthy limits.",
                text_tr="Takımın operasyonel yükünü (toil vs feature) ölçer; Error Budget kurallarını devreye alır ve bütçe tükendiğinde yeni özellik geliştirmesini durdurup stabilite sprinti açarım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="o3_e",
                text="I overhaul engineering on-call culture company-wide: align compensation/incentives with operational excellence, automate self-healing infrastructure, and eliminate toil.",
                text_tr="Şirket genelinde nöbet kültürünü dönüştürürüm: Teşvikleri operasyonel mükemmellikle hizalar, self-healing otomasyonu kurarak insan faktörlü toil'i sıfırlarım.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="own_04",
        difficulty=4,
        dimension=DimensionId.OWNERSHIP,
        title="Disaster Recovery & Chaos Engineering",
        title_tr="Disaster Recovery & Chaos Engineering",
        scenario="How do you validate that your architecture can survive the total loss of an entire cloud availability zone (AZ)?",
        scenario_tr="Mimarinizin bir bulut veri merkezinin (Availability Zone) tamamen çökmesine dayanabileceğini nasıl doğrular ve garanti edersiniz?",
        interview_source="Glassdoor: AWS Principal Architect (Disaster Recovery & Multi-AZ Failover)",
        question_type="system_design",
        is_quick=False,
        options=[
            QuestionOption(
                id="o4_a",
                text="I assume the cloud provider handles multi-AZ failover automatically.",
                text_tr="Bulut sağlayıcısının (AWS/GCP) altyapı çökmelerini arka planda otomatik yönettiğini varsayarım.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="o4_b",
                text="I verify that our Terraform or Kubernetes configs declare multi-AZ deployment replicas.",
                text_tr="Terraform veya Kubernetes pod ayarlarımızda birden fazla AZ seçildiğini konfigürasyondan kontrol ederim.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="o4_c",
                text="I conduct scheduled Chaos Engineering drills (e.g. terminating AZ networking in staging/canary) to measure failover recovery time objective (RTO).",
                text_tr="Düzenli Chaos Engineering tatbikatları yapar; staging veya canary ortamında bir AZ'nin ağ bağlantısını keserek RTO ve RPO sürelerini test ederim.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="o4_d",
                text="I architect automated active-active multi-region failover topologies with asynchronous state reconciliation, cell-based architectures, and automated health checks.",
                text_tr="Hücresel mimari (cell-based architecture), asenkron durum eşitlemesi ve otomatik multi-region active-active failover mekanizması tasarlarım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="o4_e",
                text="I establish the corporate business continuity standard: zero-data-loss geo-redundancy, continuous automated chaos injection in production, and regulatory DR compliance.",
                text_tr="Kurumsal iş sürekliliği standardını belirlerim: Sıfır veri kaybı garantili geo-redundancy, production'da sürekli otonom chaos enjeksiyonu ve regülasyon uyumu.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="own_05",
        difficulty=4,
        dimension=DimensionId.OWNERSHIP,
        title="SLOs, Error Budgets & Velocity Disputes",
        title_tr="SLO, Error Budget & Hız vs Kararlılık Çatışması",
        scenario="Product management wants to push high-risk features rapidly, but the service's monthly Error Budget is 90% burned with two weeks left. How do you handle this?",
        scenario_tr="Product ekibi kritik bir özelliği hızla yayına almak istiyor ancak servisin aylık Error Budget bütçesinin %90'ı tükendi ve ay sonuna 2 hafta var. Ne yaparsınız?",
        interview_source="Glassdoor: Google SRE Manager (SLO Negotiations & Error Budget Policies)",
        question_type="architecture_tradeoff",
        is_quick=False,
        options=[
            QuestionOption(
                id="o5_a",
                text="I let product managers decide; engineering just implements what is scheduled.",
                text_tr="Kararı ürün yöneticisine bırakırım; mühendislik sadece planlanan işleri kodlar.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="o5_b",
                text="I warn the team in a chat message that we might have another outage if we deploy now.",
                text_tr="Slack kanalında yeni deployment yaparsak sistemin tekrar çökebileceğini belirterek uyarıda bulunurum.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="o5_c",
                text="I enforce the agreed Error Budget Policy: halt non-critical feature releases, pivot engineering capacity to reliability hardening, and present burn data to stakeholders.",
                text_tr="Önceden mutabık kalınan Error Budget politikasını işletirim: Kritik olmayan dağıtımları durdurur, kapasiteyi güvenilirlik açıklarına yönlendirir ve verileri sunarım.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="o5_d",
                text="I design Canary releasing pipelines with automated metric-based rollback, isolating blast radiuses so product teams can deploy low-risk changes safely despite budget limits.",
                text_tr="Otomatik metrik analizli canary boru hattı kurarım: Hata alanını (blast radius) mikro parçalara bölerek güvenli parçaların yayına devam etmesini sağlarım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="o5_e",
                text="I negotiate the executive alignment framework between engineering reliability, customer trust, and company revenue velocity at the VP/C-suite level.",
                text_tr="VP ve C-level seviyesinde müşteri güveni, marka itibarı ve inovasyon hızı arasındaki stratejik risk-getiri dengesini yönetecek kurumsal sözleşmeyi tasarlarım.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="own_06",
        difficulty=5,
        dimension=DimensionId.OWNERSHIP,
        title="Cascading Failures & Deadlock Protection",
        title_tr="Cascading Failure, Deadlock & Circuit Breaker Mimarisi",
        scenario="A degraded downstream payment provider starts responding with 15-second latencies, causing thread exhaustion and cascading failures across your entire API gateway.",
        scenario_tr="Alt katmandaki yavaşlayan bir ödeme sağlayıcısı 15 saniyelik gecikmeler üretmeye başlıyor; bu durum thread havuzunu tüketip tüm API Gateway'i zincirleme çökertiyor.",
        interview_source="Glassdoor: Meta Staff Infrastructure (Cascading Failures & Graceful Degradation)",
        question_type="system_design",
        is_quick=False,
        options=[
            QuestionOption(
                id="o6_a",
                text="I restart the gateway pods whenever memory alerts fire.",
                text_tr="Hafıza uyarısı geldikçe API Gateway pod'larını restart ederim.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="o6_b",
                text="I reduce client timeout values to 5 seconds so threads are freed up faster.",
                text_tr="İstemci timeout süresini 5 saniyeye düşürerek thread'lerin daha erken boşalmasını sağlarım.",
                score=2.2,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="o6_c",
                text="I implement circuit breakers (e.g. Resilience4j/Envoy), bulkheads to isolate thread pools, and fallback responses to prevent downstream latency from affecting other routes.",
                text_tr="Circuit Breaker, thread havuzlarını ayıran Bulkhead deseni ve yedek fallback yanıtları devreye alarak diğer servislerin etkilenmesini engellerim.",
                score=3.8,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="o6_d",
                text="I implement proactive load shedding, adaptive concurrency limits (Vegas/TCP BBR algorithms), and queue-based backpressure at the gateway tier.",
                text_tr="Gateway katmanında proaktif load shedding, dinamik eşzamanlılık kısıtlaması (TCP BBR/Vegas uyarlamalı algoritmalar) ve backpressure mekanizması kurarım.",
                score=4.7,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="o6_e",
                text="I architect an asynchronous, fault-isolated payment engine with event-driven reconciliation, guaranteeing zero systemic impact regardless of external partner failures.",
                text_tr="Dış ortakların çöküşlerinden tamamen izole, asenkron ve event-driven mutabakat motoru tasarlayarak sıfır sistemik etki garantisi veririm.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),

    # =========================================================================
    # DIMENSION 3: BUSINESS & PRODUCT IMPACT (6 Questions)
    # =========================================================================
    Question(
        id="imp_01",
        difficulty=2,
        dimension=DimensionId.IMPACT,
        title="Prioritization & Product Trade-offs",
        title_tr="Kapsam Pazarlığı & Pragmatik MVP Çıkışı",
        scenario="Sales commits to a major enterprise customer promising a complex feature in 3 weeks, but engineering estimates 8 weeks. How do you respond?",
        scenario_tr="Satış ekibi stratejik bir kurumsal müşteriye 3 hafta içinde karmaşık bir özellik sözü verdi; ancak teknik tahmin en az 8 hafta gösteriyor. Ne yaparsınız?",
        interview_source="Glassdoor: Stripe Product Engineer (Pragmatic Scope Pruning & Delivery)",
        question_type="scenario",
        is_quick=True,
        options=[
            QuestionOption(
                id="i1_a",
                text="I work extreme overtime to try to rush the full feature through.",
                text_tr="Gece gündüz mesaiye kalarak tüm özelliği 3 haftada yetiştirmeye çalışırım.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="i1_b",
                text="I inform the manager that it's impossible and refuse to work on the tight timeline.",
                text_tr="Yöneticime bunun imkansız olduğunu söyler ve bu süre zarfında çalışmayı reddederim.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="i1_c",
                text="I collaborate with product and sales to identify the core 20% of functionality that satisfies 80% of customer needs, delivering an MVP on time while scheduling the rest.",
                text_tr="Product ve satış ekibiyle oturup müşterinin acil ihtiyacını karşılayan kritik %20'lik çekirdeği belirler; 3 haftada MVP teslim edip kalanını fazlandırırım.",
                score=3.6,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="i1_d",
                text="I restructure delivery using feature toggles, semi-automated backend workflows, and contracts that de-risk the customer commitment without accumulating unmanageable technical debt.",
                text_tr="Feature flags ve yarı-otomatize backend iş akışlarıyla müşteriye değer sunan, teknik borç yaratmayan aşamalı bir mimari teslimat modeli kurgularım.",
                score=4.5,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="i1_e",
                text="I align commercial strategy with engineering roadmaps at the leadership level, preventing asymmetric commitments while enabling enterprise contract acquisition.",
                text_tr="Yönetici düzeyinde ticari taahhüt mekanizması ile mühendislik kapasitesini hizalar; şirketin kurumsal satış gücünü artıran sürdürülebilir bir çerçeve çizerim.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="imp_02",
        difficulty=3,
        dimension=DimensionId.IMPACT,
        title="Metric-Driven Engineering & Measuring ROI",
        title_tr="Metric-Driven Mühendislik & İş Yatırımı Geri Dönüşü (ROI)",
        scenario="Your team wants to spend 2 months refactoring an internal service. How do you justify this investment to leadership?",
        scenario_tr="Takımınız bir iç servisi 2 ay boyunca sıfırdan refactor etmek istiyor. Bu teknik yatırımı şirket yönetimine nasıl gerekçelendirir ve savunursunuz?",
        interview_source="Glassdoor: Airbnb Senior Fullstack (Data-Driven Development & Business ROI)",
        question_type="architecture_tradeoff",
        is_quick=False,
        options=[
            QuestionOption(
                id="i2_a",
                text="I explain that the current code is ugly and poorly written.",
                text_tr="Mevcut kodun çok kötü yazıldığını ve geliştiriciyi yorduğunu söylerim.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="i2_b",
                text="I argue that refactoring will make writing future unit tests easier.",
                text_tr="Refactoring sonrasında gelecekte test yazmanın çok daha kolaylaşacağını savunurum.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="i2_c",
                text="I quantify the impact: showing that current bugs cost 15 hours/week of triage, deployment failures cause k/month churn, and refactoring pays off in 4 months.",
                text_tr="Etkiyi sayısallaştırırım: Mevcut hataların haftada 15 saat mühendislik zamanı çaldığını, kesintilerin müşteri kaybı yarattığını ve yatırımın 4 ayda amorti edeceğini kanıtlarım.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="i2_d",
                text="I link technical health metrics (DORA metrics, MTTR, change failure rate) directly to business conversion and team velocity roadmaps.",
                text_tr="DORA metriklerini (MTTR, Change Failure Rate, Deployment Frequency) doğrudan şirket gelir modellerine ve ürün hızlanma hedeflerine bağlarım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="i2_e",
                text="I establish the capital allocation framework for technical health org-wide, setting portfolio standards for maintenance vs growth investment.",
                text_tr="Şirket genelinde teknik borç ve büyüme dengesini düzenleyen kurumsal sermaye/kaynak tahsis çerçevesini belirlerim.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="imp_03",
        difficulty=3,
        dimension=DimensionId.IMPACT,
        title="Technical Spikes vs Hard Customer Deadlines",
        title_tr="Technical Spike vs Kesin Müşteri Teslim Tarihleri",
        scenario="A critical milestone approaches, but the third-party API your feature relies upon has severe undocumented limitations. How do you proceed?",
        scenario_tr="Kritik bir teslim tarihi yaklaşıyor, ancak kullanmak zorunda olduğunuz üçüncü parti API'de dokümante edilmemiş ağır kısıtlamalar çıktı. Ne yaparsınız?",
        interview_source="Glassdoor: DoorDash Senior Backend (Technical Spikes & Timeline Commitments)",
        question_type="scenario",
        is_quick=False,
        options=[
            QuestionOption(
                id="i3_a",
                text="I wait for their customer support to respond to my open ticket.",
                text_tr="Açtığım destek biletine firmanın yanıt vermesini beklerim.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="i3_b",
                text="I write hacky workarounds in application code to bypass their limits without telling anyone.",
                text_tr="Kimseye haber vermeden kod içinde geçici yamalar (workarounds) yaparak kısıtlamaları aşmaya çalışırım.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="i3_c",
                text="I time-box a 2-day technical spike to benchmark alternative providers, present a risk assessment to PM, and implement an adapter pattern allowing easy swap.",
                text_tr="2 günlük süreli bir Spike açarak alternatif sağlayıcıları test eder, PM'e risk raporu sunar ve kolayca sağlayıcı değiştirmeyi sağlayan Adapter deseni kurarım.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="i3_d",
                text="I design a resilient vendor-agnostic abstraction layer with intelligent failover, caching, and fallback mocks that insulates business deliverables from vendor flaws.",
                text_tr="Dış sağlayıcı bağımlılığını tamamen soyutlayan, akıllı failover ve fallback mock'ları içeren dayanıklı bir entegrasyon katmanı kurarım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="i3_e",
                text="I evaluate strategic partner contracts with legal and procurement, negotiating SLA guarantees or acquiring underlying technology to secure business moats.",
                text_tr="Hukuk ve satın alma ile stratejik tedarikçi sözleşmelerini revize eder; şirketimizin rekabet avantajını korumak için doğrudan teknoloji edinimi veya katı SLA sözleşmeleri yaptırırım.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="imp_04",
        difficulty=2,
        dimension=DimensionId.IMPACT,
        title="Product Discovery & User Empathy",
        title_tr="Kullanıcı Empatisi & Mühendislikte Product Discovery",
        scenario="A proposed feature specification is technically feasible, but you suspect it will confuse end-users and fail to solve their real pain point. What do you do?",
        scenario_tr="Size verilen ürün spesifikasyonu teknik olarak yapılabilir; ancak son kullanıcının kafasını karıştıracağını ve asıl ağrı noktasını çözmeyeceğini fark ettiniz. Ne yaparsınız?",
        interview_source="Glassdoor: Figma Senior Engineer (Customer Empathy & Product Craft)",
        question_type="scenario",
        is_quick=False,
        options=[
            QuestionOption(
                id="i4_a",
                text="I build the spec exactly as written; user experience is the product manager's problem.",
                text_tr="Bana yazılan spesifikasyonu aynen kodlarım; kullanıcı deneyimi PM'in sorumluluğundadır.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="i4_b",
                text="I mention my concern to a colleague during coffee break but don't challenge the ticket.",
                text_tr="Kahve molasında ekip arkadaşıma fikrimi söylerim ama resmi olarak bileti sorgulamam.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="i4_c",
                text="I review user analytics and customer support tickets, bring quantitative data to the PM, and propose a simplified UX alternative that requires 30% less code.",
                text_tr="Kullanıcı analitiği ve destek biletlerini inceler; PM'e veri odaklı kanıtlar sunarak %30 daha az kod gerektiren çok daha sade bir UX alternatifi öneririm.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="i4_d",
                text="I participate in live customer interviews, run rapid prototype experiments with feature flags, and co-design the product roadmap alongside design and product leadership.",
                text_tr="Kullanıcı mülakatlarına katılır, feature flag'lerle hızlı A/B prototip deneyleri yürütür ve ürün yol haritasını ürün yönetimiyle ortaklaşa şekillendiririm.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="i4_e",
                text="I identify latent market opportunities that customers cannot articulate, directing engineering resources to create disruptive features that define our competitive moat.",
                text_tr="Kullanıcıların kelimelerle ifade edemediği pazar fırsatlarını sezer; mühendislik gücünü sektörel ezber bozan ve şirkete tekel avantajı sağlayan ürünlere yönlendiririm.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="imp_05",
        difficulty=4,
        dimension=DimensionId.IMPACT,
        title="Cloud FinOps & Infrastructure Cost Optimization",
        title_tr="Cloud FinOps & Altyapı Maliyet Optimizasyonu",
        scenario="Your company's cloud bill spikes 60% month-over-month due to rapid data ingestion. The VP demands immediate cost remediation. How do you lead this?",
        scenario_tr="Şirketin bulut faturası yüksek veri akışı nedeniyle bir ayda %60 fırladı. Mühendislik VP'si acil maliyet düşürme istiyor. Nasıl yaklaşırsınız?",
        interview_source="Glassdoor: Uber Senior Infrastructure (FinOps & Compute Cost Reduction)",
        question_type="architecture_tradeoff",
        is_quick=False,
        options=[
            QuestionOption(
                id="i5_a",
                text="I shut down a few unused staging development VMs.",
                text_tr="Kullanılmayan birkaç staging sanal makinesini kapatırım.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="i5_b",
                text="I enable AWS Savings Plans or Reserved Instances for the current baseline.",
                text_tr="Mevcut kullanım için AWS Reserved Instance veya Savings Plans satın alırım.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="i5_c",
                text="I build cost allocation dashboards by service, identify the 2 biggest cost culprits (e.g. uncompressed data transfer, oversized compute), and optimize compression and lifecycle policies to cut 35% of costs.",
                text_tr="Servis bazlı FinOps maliyet haritası çıkarır; en büyük 2 maliyet kalemini (sıkıştırılmamış egress veri transferi, aşırı boyutlandırılmış DB) optimize ederek maliyeti %35 düşürürüm.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="i5_d",
                text="I embed automated unit-cost tracking (cost per active user / cost per transaction) into CI/CD pipelines, establishing unit economics governance across all product squads.",
                text_tr="Birim maliyet takibini (kullanıcı başına altyapı maliyeti) CI/CD'ye entegre eder; tüm takımlar için birim ekonomi (unit economics) standartları ve bütçe alarmları kurarım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="i5_e",
                text="I renegotiate multi-million dollar EDP (Enterprise Discount Program) commitments with cloud hyperscalers while architecting portable workload strategies that maintain bargaining leverage.",
                text_tr="Bulut sağlayıcıları ile çok milyon dolarlık kurumsal indirim anlaşmalarını müzakere eder, iş yükü taşınabilirliği ile şirketin pazarlık gücünü korurum.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="imp_06",
        difficulty=4,
        dimension=DimensionId.IMPACT,
        title="Buy vs Build Architectural Decisions",
        title_tr="Buy vs Build (Satın Al vs Kendin Yap) Mimari Kararları",
        scenario="Your team needs an advanced Feature Flagging and A/B experimentation platform. Some engineers want to build it in-house; others want to buy a SaaS solution.",
        scenario_tr="Takımınızın gelişmiş bir Feature Flag ve A/B deney platformuna ihtiyacı var. Bazı mühendisler sıfırdan yazmak, bazıları SaaS satın almak istiyor.",
        interview_source="Glassdoor: Netflix Staff Architect (Buy vs Build Strategy & Core Competency)",
        question_type="architecture_tradeoff",
        is_quick=False,
        options=[
            QuestionOption(
                id="i6_a",
                text="I vote to build it in-house because coding it is more fun and educational for the team.",
                text_tr="Sıfırdan yazalım derim çünkü kodlamak takım için daha eğlenceli ve öğreticidir.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="i6_b",
                text="I vote to buy SaaS immediately so we don't have to write any code.",
                text_tr="Hemen SaaS alalım derim böylece hiç kod yazmamıza gerek kalmaz.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="i6_c",
                text="I produce a Total Cost of Ownership (TCO) analysis: evaluating 3-year engineer maintenance hours, opportunity cost, compliance vs subscription cost, recommending buying unless it's our core competitive differentiator.",
                text_tr="Toplam Sahip Olma Maliyeti (TCO) analizi yaparım: 3 yıllık mühendis bakım maliyeti, fırsat maliyeti ve abonelik giderini karşılaştırır; çekirdek uzmanlığımız değilse satın almayı öneririm.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="i6_d",
                text="I create an open abstraction layer around the chosen SaaS vendor, enabling rapid adoption while protecting our systems from vendor lock-in and allowing future in-house migration if unit economics shift.",
                text_tr="Seçilen SaaS çevresinde kurumsal bir soyutlama katmanı kurarak hızlı entegrasyon sağlar, vendor lock-in riskini önler ve ileride yerli çözüme geçiş kapısını açık tutarım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="i6_e",
                text="I define the enterprise-wide 'Core vs Context' strategy, directing engineering capital exclusively to proprietary competitive advantages while commoditizing context.",
                text_tr="Şirket genelinde 'Core vs Context' stratejisini belirlerim: Mühendislik sermayesini yalnızca şirketi rakiplerinden ayıran çekirdek ürünlere kanalize ederim.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),

    # =========================================================================
    # DIMENSION 4: LEADERSHIP & INFLUENCE (6 Questions)
    # =========================================================================
    Question(
        id="lead_01",
        difficulty=3,
        dimension=DimensionId.LEADERSHIP,
        title="Technical Disagreements & Consensus Building",
        title_tr="Teknik Anlaşmazlıklar & Uzlaşı (Consensus) Kültürü",
        scenario="Two senior engineers strongly disagree on database choice (PostgreSQL vs DynamoDB/NoSQL) for a major new service, stalling the project for 2 weeks. How do you resolve this?",
        scenario_tr="İki kıdemli mühendis yeni bir servis için veritabanı seçimi (Postgres vs DynamoDB) konusunda kilitlendi ve proje 2 haftadır durdu. Nasıl çözersiniz?",
        interview_source="Glassdoor: Google L5 Tech Lead (Reaching Technical Consensus & RFCs)",
        question_type="scenario",
        is_quick=True,
        options=[
            QuestionOption(
                id="l1_a",
                text="I stay out of the dispute and wait for someone else or the manager to make the call.",
                text_tr="Tartışmaya karışmam, yöneticinin veya başkasının karar vermesini beklerim.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="l1_b",
                text="I take a quick team poll and go with whichever option gets the most votes.",
                text_tr="Hızlı bir oylama yapar ve en çok oy alan teknolojiyi seçerim.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="l1_c",
                text="I facilitate an RFC decision matrix with objective criteria (access patterns, consistency needs, operational expertise, latency requirements), drive consensus, and execute 'disagree and commit'.",
                text_tr="Nesnel kriterler (erişim modelleri, consistency gereksinimi, operasyonel tecrübe) içeren bir RFC karar matrisi hazırlar, uzlaşı sağlar ve 'disagree and commit' ilkesini uygulatırım.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="l1_d",
                text="I establish standardized architectural review frameworks across engineering teams, depersonalizing technical debates and creating fast-path escalation mechanisms.",
                text_tr="Teknik tartışmaları kişisellikten arındıran kurumsal Architecture Review kurulları kurar ve mimari kararlar için hızlı eskalasyon mekanizmaları tanımlarım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="l1_e",
                text="I cultivate a culture of pragmatic intellectual honesty and psychological safety where architectural rigor thrives without bureaucratic paralysis.",
                text_tr="Şirket genelinde entelektüel dürüstlük ve psikolojik güvenlik kültürü inşa eder; bürokrasiye boğulmadan yüksek mimari standartların yaşatılmasını sağlarım.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="lead_02",
        difficulty=2,
        dimension=DimensionId.LEADERSHIP,
        title="Mentorship & Force Multiplication",
        title_tr="Mentörlük, Sponsorluk & Ekip Çarpan Etkisi",
        scenario="A mid-level engineer on your team struggles with system design and frequently feels overwhelmed when assigned ambiguous tasks. How do you help them?",
        scenario_tr="Takımınızdaki bir mid-level mühendis sistem tasarımında zorlanıyor ve ucu açık görevlerde bunalmış hissediyor. Ona nasıl destek olursunuz?",
        interview_source="Glassdoor: Meta E5 Engineering (Mentorship & Force Multiplication)",
        question_type="scenario",
        is_quick=False,
        options=[
            QuestionOption(
                id="l2_a",
                text="I take over their difficult tasks and write the code myself so the sprint doesn't slip.",
                text_tr="Sprint aksamasın diye zor görevleri ondan alıp kendim kodlarım.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="l2_b",
                text="I send them a link to a system design book and tell them to read it.",
                text_tr="Bir system design kitabı linki atar ve okumasını tavsiye ederim.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="l2_c",
                text="I set up regular 1-on-1 pairing sessions, co-author technical design docs, teach problem-decomposition frameworks, and sponsor them for a well-scoped stretch project.",
                text_tr="Düzenli pairing oturumları yapar, birlikte RFC yazar, problemleri parçalama yöntemlerini öğretir ve gelişimini destekleyecek bir projede ona sponsor olurum.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="l2_d",
                text="I build systematic engineering growth ladders, structured apprenticeship programs, and internal tech academies that scale mentorship across the engineering division.",
                text_tr="Tüm mühendislik departmanında mentörlüğü kurumsallaştıran kariyer basamakları, çıraklık programları ve teknik akademiler tasarlarım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="l2_e",
                text="I develop future tech executives and Staff+ leaders, shaping an organizational ecosystem where talent development is a core leadership competency.",
                text_tr="Geleceğin Staff+ liderlerini ve teknoloji yöneticilerini yetiştirir, yetenek gelişimini şirketin en temel liderlik metriği haline getiririm.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="lead_03",
        difficulty=2,
        dimension=DimensionId.LEADERSHIP,
        title="Code Review Culture & Uplifting Peers",
        title_tr="Code Review Kültürü & Mühendislik Kalite Çıtası",
        scenario="An engineer submits a massive 1,500-line Pull Request with architectural flaws and no tests, but the sprint deadline is today. How do you handle the review?",
        scenario_tr="Bir ekip arkadaşınız mimari kusurları olan ve hiç test içermeyen 1.500 satırlık devasa bir PR açtı ve sprint bugün bitiyor. İncelemeyi nasıl yönetirsiniz?",
        interview_source="Glassdoor: Stripe Senior Software Engineer (Code Review Standards & Empathy)",
        question_type="scenario",
        is_quick=False,
        options=[
            QuestionOption(
                id="l3_a",
                text="I approve it with 'LGTM' because the sprint deadline is today.",
                text_tr="Sprint yetişsin diye detaylı bakmadan 'LGTM' deyip onaylarım.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="l3_b",
                text="I leave 50 critical nitpick comments and reject the PR without talking to the author.",
                text_tr="PR'a 50 tane sert eleştiri yorumu bırakır ve konuşmadan doğrudan reddederim.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="l3_c",
                text="I hop on a video call with the author with empathy, explain the architectural risks, help them break the PR into 3 smaller digestible PRs, and pair on adding critical tests.",
                text_tr="Ekip arkadaşımla yapıcı bir görüşme yapar; mimari riskleri sakince anlatır, PR'ı 3 küçük mantıksal parçaya bölmesine ve kritik testleri yazmasına pairing ile destek olurum.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="l3_d",
                text="I establish team-wide PR size guidelines (<400 lines), introduce automated linters and CI test gates, and train teams in empathetic, high-leverage code reviews.",
                text_tr="Takımlar için PR boyut limitleri (<400 satır) belirler; otomatik linter ve test kurallarını CI'a bağlar, yapıcı kod inceleme kültürünü yaygınlaştırırım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="l3_e",
                text="I define the engineering cultural ethos: balancing high velocity with uncompromised engineering integrity, fostering psychological safety across hundreds of developers.",
                text_tr="Yüzlerce mühendisin çalıştığı organizasyonda yüksek hız ile tavizsiz mühendislik kalitesini dengeleyen kurumsal mühendislik etiğini tesis ederim.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="lead_04",
        difficulty=4,
        dimension=DimensionId.LEADERSHIP,
        title="Cross-Team Engineering Guilds & Alignment",
        title_tr="Takımlar Arası Mühendislik Guild'leri & Standartlaştırma",
        scenario="Multiple teams are independently inventing divergent solutions for authentication, logging, and API schemas, causing integration friction across the company.",
        scenario_tr="Farklı takımlar birbirinden bağımsız olarak auth, logging ve API şemaları için farklı yöntemler geliştiriyor; şirket içi entegrasyonlar felce uğruyor. Ne yaparsınız?",
        interview_source="Glassdoor: Spotify Chapter Lead (Engineering Guilds & Technical Alignment)",
        question_type="architecture_tradeoff",
        is_quick=False,
        options=[
            QuestionOption(
                id="l4_a",
                text="I focus exclusively on my team and ignore what other teams are building.",
                text_tr="Sadece kendi takımıma odaklanır, diğer takımların ne yaptığıyla ilgilenmem.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="l4_b",
                text="I send an email asking everyone to stop what they're doing and use my team's library.",
                text_tr="Tüm takımlara e-posta atarak herkesin benim takımımın yazdığı kütüphaneyi kullanmasını isterim.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="l4_c",
                text="I found a cross-functional Engineering Guild / Working Group, gather representatives from each team, synthesize common requirements into a shared RFC, and release a standardized internal SDK.",
                text_tr="Takımlar arası bir Mühendislik Guild'i kurar; temsilcileri toplayıp ortak ihtiyaçları tek bir RFC'de birleştirir ve paylaşılan standart bir SDK yayınlarım.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="l4_d",
                text="I establish the Platform Engineering charter, securing dedicated funding and leadership sponsorship to build golden paths that 80%+ of squads willingly adopt.",
                text_tr="Platform Engineering misyonunu başlatır; yönetim desteğiyle tüm takımların isteyerek benimseyeceği kurumsal 'Golden Path' platformlarını inşa ederim.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="l4_e",
                text="I shape organizational topology, aligning team charters, cognitive loads, and platform contracts to eliminate cross-team friction at the enterprise scale.",
                text_tr="Şirket genelinde organizasyonel topolojiyi yeniden düzenler; takım sınırlarını ve bilişsel yükleri optimize ederek sürtünmeleri kökten yok ederim.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="lead_05",
        difficulty=3,
        dimension=DimensionId.LEADERSHIP,
        title="Raising the Technical Hiring Bar",
        title_tr="Teknik İşe Alım & Ekip Kalite Çıtasını Yükseltme",
        scenario="Your hiring committee is split on a senior candidate: strong coding skills, but shows subtle signs of poor collaboration and dismissing feedback.",
        scenario_tr="İşe alım komitesi kıdemli bir aday konusunda ikiye bölündü: Kod yazma becerisi çok yüksek ancak geri bildirimleri küçümsüyor ve iş birliğinde zayıf sinyaller veriyor.",
        interview_source="Glassdoor: Amazon Bar Raiser (Technical Interviewing & Culture Fit)",
        question_type="scenario",
        is_quick=False,
        options=[
            QuestionOption(
                id="l5_a",
                text="I vote to hire them immediately because we need developers urgently.",
                text_tr="Acil geliştiriciye ihtiyacımız olduğu için hemen işe alınması yönünde oy kullanırım.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="l5_b",
                text="I leave my evaluation blank and let the engineering manager decide.",
                text_tr="Değerlendirmemi boş bırakır, kararı doğrudan mühendislik yöneticisine devrederim.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="l5_c",
                text="I act as a Bar Raiser: protect team health by voting 'Strong No-Hire', explaining how toxic brilliance damages psychological safety and creates net negative productivity.",
                text_tr="Bar Raiser rolü üstlenirim: 'Kesin Red' vererek toksik zekanın takım psikolojisini çökerteceğini ve uzun vadede net negatif üretkenlik yaratacağını savunurum.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="l5_d",
                text="I redesign our department's interview rubric: replacing leetcode puzzles with real-world system debugging and collaborative design exercises that measure communication under pressure.",
                text_tr="Tüm departmanın mülakat rubriğini yenilerim: Ezber bulmacaları yerine baskı altında iletişim ve iş birliğini ölçen gerçekçi sistem simülasyonları getiririm.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="l5_e",
                text="I build the company's employer branding and talent magnet identity, attracting world-class engineering luminaries and establishing rigorous hiring standards company-wide.",
                text_tr="Şirketin global mühendislik marka kimliğini inşa eder; dünyanın en iyi yeteneklerini çeken ve kalite çıtasını tavizsiz koruyan işe alım ekosistemini kurarım.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="lead_06",
        difficulty=5,
        dimension=DimensionId.LEADERSHIP,
        title="Executive Communication & Communicating Risk",
        title_tr="Executive İletişim & Yüksek Risklerin İş Diline Tercümesi",
        scenario="Your core payment infrastructure has a subtle data corruption risk under high concurrency. Refactoring takes 9 months, but executives are laser-focused on new product revenue.",
        scenario_tr="Ana ödeme altyapınız yüksek eşzamanlılıkta veri bozulması riski taşıyor. Çözüm 9 ay sürecek ancak yönetim tamamen yeni gelir getirecek özelliklere odaklanmış durumda.",
        interview_source="Glassdoor: Apple Principal Engineer (Executive Technical Communication & High-Stakes Risk)",
        question_type="scenario",
        is_quick=False,
        options=[
            QuestionOption(
                id="l6_a",
                text="I complain to teammates that management doesn't care about code quality.",
                text_tr="Takım arkadaşlarıma yönetimin kod kalitesini hiç önemsemediğinden yakınırım.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="l6_b",
                text="I send a technical architecture diagram to the CEO full of database internals.",
                text_tr="CEO'ya veritabanı iç detaylarıyla dolu karmaşık bir teknik şema gönderirim.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="l6_c",
                text="I translate technical risk into executive language: quantifying legal liability, customer trust destruction, and regulatory fines, proposing a phased 3-stage migration plan that maintains product delivery.",
                text_tr="Teknik riski iş diline çeviririm: Olası regülasyon cezalarını, müşteri güven kaybını ve mali riski sayısallaştırır; ürün teslimatını aksatmayan 3 aşamalı bir yol haritası sunarım.",
                score=3.8,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="l6_d",
                text="I align Board-level risk tolerance with technical investment, framing resilience as a commercial sales enabler that unlocks enterprise and financial sector customers.",
                text_tr="Yönetim kurulu seviyesinde risk iştahı ile teknik yatırımı hizalar; sistem güvenilirliğini kurumsal müşterileri kazandıran ticari bir satış gücüne dönüştürürüm.",
                score=4.7,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="l6_e",
                text="I serve as trusted technical advisor to the C-suite and Board, guiding strategic enterprise governance, M&A due diligence, and existential technology decisions.",
                text_tr="C-Suite ve Yönetim Kurulu'nun baş teknik danışmanı olarak görev yapar; kurumsal teknoloji yönetişimi, birleşme-satın alma (M&A) ve varoluşsal mimari kararları yönlendiririm.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),

    # =========================================================================
    # DIMENSION 5: AUTONOMY & AMBIGUITY (6 Questions)
    # =========================================================================
    Question(
        id="auto_01",
        difficulty=3,
        dimension=DimensionId.AUTONOMY,
        title="Navigating Ambiguous Goals",
        title_tr="Belirsizlik Yönetimi & Ucu Açık Görevleri Yapılandırma",
        scenario="Your VP says: 'Our developer onboarding is too slow. Fix it.' There are no existing specs, tickets, or documentation. What do you do?",
        scenario_tr="Mühendislik VP'si size: 'Geliştirici onboarding sürecimiz çok yavaş, bunu kökten çözün' dedi. Hiçbir doküman, bilet veya spesifikasyon yok. Ne yaparsınız?",
        interview_source="Glassdoor: Meta Staff E6 (Navigating Ambiguity & 0-to-1 Scoping)",
        question_type="scenario",
        is_quick=True,
        options=[
            QuestionOption(
                id="a1_a",
                text="I ask my manager to create specific Jira tickets before I can begin working.",
                text_tr="Çalışmaya başlamadan önce yöneticimin bana detaylı Jira biletleri açmasını isterim.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="a1_b",
                text="I write a quick README with instructions on how I set up my personal laptop.",
                text_tr="Kendi bilgisayarımı nasıl kurduğumu anlatan hızlı bir README dosyası yazarım.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="a1_c",
                text="I interview the last 5 new hires, measure 'time to first PR merge', identify the 3 largest bottlenecks (local env setup, IAM permissions, seed data), and build automated dev container tooling.",
                text_tr="Son 5 yeni katılan mühendisle görüşür, 'ilk PR merge süresi' metriğini ölçer; en büyük 3 engeli (lokal ortam, yetkiler, test verisi) çözmek için dev-container otomasyonu kurarım.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="a1_d",
                text="I establish the company-wide Developer Experience (DevEx) charter: tracking DORA metrics, standardizing cloud dev environments (e.g. Coder/Gitpod), cutting onboarding from 3 weeks to 1 day.",
                text_tr="Şirket genelinde Developer Experience (DevEx) standardı kurarım: Bulut geliştirme ortamları ile onboarding süresini 3 haftadan 1 güne düşüren kurumsal altyapıyı hayata geçiririm.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="a1_e",
                text="I transform company engineering productivity into an industry benchmark, pioneering developer platform innovations that make the company an engineering talent magnet.",
                text_tr="Şirketin mühendislik verimliliğini sektörde örnek gösterilen bir standarda dönüştürür; küresel ölçekte yazılım geliştirici çekim merkezi haline gelmesini sağlarım.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="auto_02",
        difficulty=2,
        dimension=DimensionId.AUTONOMY,
        title="Project Execution from 0 to 1",
        title_tr="Bağımsız İcra & Sıfırdan (0-to-1) Mimari Kurulumu",
        scenario="You are assigned to build a brand new real-time analytics microservice from scratch with no pre-existing templates. How do you approach the build?",
        scenario_tr="Daha önce şirket içinde hiç şablonu olmayan yeni bir gerçek zamanlı analiz mikroservisini sıfırdan kurmanız istendi. Nasıl başlarsınız?",
        interview_source="Glassdoor: Uber Senior Backend (0-to-1 Greenfield Execution)",
        question_type="system_design",
        is_quick=False,
        options=[
            QuestionOption(
                id="a2_a",
                text="I wait for a senior engineer to set up the repository, CI/CD pipeline, and directory structure for me.",
                text_tr="Kıdemli bir mühendisin repoyu, CI/CD boru hattını ve klasör yapısını benim için kurmasını beklerim.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="a2_b",
                text="I copy-paste code from another repository and start building endpoints without documentation.",
                text_tr="Başka bir repodan kodları kopyalar ve dokümantasyon yapmadan endpoint yazmaya başlarım.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="a2_c",
                text="I author a lightweight RFC with architecture options, define schema contracts, set up clean CI/CD pipelines with automated tests and linting, and deliver an MVP within 3 sprints.",
                text_tr="Mimari alternatifleri içeren kısa bir RFC yazar, API kontratlarını belirler, test ve linting içeren sağlam bir CI/CD boru hattı kurarak 3 sprintte MVP teslim ederim.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="a2_d",
                text="I turn this greenfield effort into an organizational archetype: creating a reusable microservice chassis, boilerplate generator, and observability scaffold adopted by all squads.",
                text_tr="Bu sıfırdan projeyi kurumsal bir şablona dönüştürürüm: Tüm takımların kullanabileceği mikroservis iskeleti, boilerplate üreticisi ve gözlemlenebilirlik standardı yaratırım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="a2_e",
                text="I establish the foundational architectural blueprints and multi-runtime platform abstractions that underpin company software delivery for the next decade.",
                text_tr="Önümüzdeki on yıl boyunca şirketin tüm yazılım teslimatını taşıyacak temel mimari standartları ve çoklu çalışma zamanı platform soyutlamalarını kurarım.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="auto_03",
        difficulty=4,
        dimension=DimensionId.AUTONOMY,
        title="Cross-Team Friction & Breaking Architectural Blockers",
        title_tr="Takımlar Arası Bağımlılık Tıkanıklıklarını Çözme",
        scenario="Your critical project is blocked because another core team won't prioritize an API you need for 6 months. How do you unblock yourself?",
        scenario_tr="Kritik projeniz tıkandı çünkü ihtiyaç duyduğunuz API'yi yazması gereken çekirdek ekip bu işi 6 ay sonrasına erteledi. Kendinizi nasıl unblock edersiniz?",
        interview_source="Glassdoor: Google L6 Staff Software Engineer (Cross-Org Dependency Resolution)",
        question_type="scenario",
        is_quick=False,
        options=[
            QuestionOption(
                id="a3_a",
                text="I pause my work and wait 6 months for them to finish their roadmap.",
                text_tr="Çalışmamı durdurur ve o ekibin 6 ay sonra işi bitirmesini beklerim.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="a3_b",
                text="I complain to my manager that the other team is lazy and uncooperative.",
                text_tr="Yöneticime diğer ekibin tembel ve iş birliğinden uzak olduğunu şikayet ederim.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="a3_c",
                text="I negotiate an internal open-source contribution model: my team submits PRs to their codebase following their design standards, or we implement an Anti-Corruption Layer with mock contracts in the interim.",
                text_tr="İç açık kaynak (InnerSource) modeli öneririm: Standartlarına uyarak repolarına PR açarız veya araya geçici bir Anti-Corruption Layer ve mock sözleşmeler koyarak ilerleriz.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="a3_d",
                text="I redefine organizational dependency mapping: replacing synchronous RPC dependencies with decoupled event-driven architectures (Kafka events) to permanently eliminate team-coupling bottlenecks.",
                text_tr="Organizasyonel bağımlılık haritasını yeniden kurgularım: Senkron RPC bağımlılıklarını asenkron event-driven mimarilerle değiştirerek takımlar arası kilitlenmeleri kalıcı olarak bitiririm.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="a3_e",
                text="I realign engineering org design and team topologies at the VP level, ensuring team boundaries reflect decoupled business capabilities that eliminate inter-team gridlock.",
                text_tr="VP seviyesinde organizasyon tasarımını ve takım topolojilerini yeniden düzenler; takım sınırlarının tamamen bağımsız iş kabiliyetlerini temsil etmesini sağlarım.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="auto_04",
        difficulty=4,
        dimension=DimensionId.AUTONOMY,
        title="Balancing Conflicting Stakeholder Demands",
        title_tr="Çelişen Yönetici Taleplerini Dengeleme & Önceliklendirme",
        scenario="The Head of Security mandates strict Zero-Trust compliance requiring 2FA everywhere, while the VP of Growth demands frictionless one-click user signup. What is your path forward?",
        scenario_tr="Güvenlik Direktörü her adımda zorunlu 2FA içeren katı Zero-Trust isterken, Büyüme Direktörü sürtünmesiz tek tıkla üyelik talep ediyor. Nasıl bir yol izlersiniz?",
        interview_source="Glassdoor: Amazon Principal SDE (Balancing Stakeholder Conflicts & Frictionless Security)",
        question_type="architecture_tradeoff",
        is_quick=False,
        options=[
            QuestionOption(
                id="a4_a",
                text="I do whatever the higher-ranking executive tells me to do in person.",
                text_tr="Hiyerarşik olarak daha üst mevkideki yönetici hangisini söylerse onu yaparım.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="a4_b",
                text="I build two completely separate login systems and let users choose.",
                text_tr="İki tamamen ayrı giriş sistemi yapar ve seçimi kullanıcıya bırakırım.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="a4_c",
                text="I architect a Risk-Based Adaptive Authentication model: frictionless one-click signup for low-risk behavior, triggering progressive step-up auth (WebAuthn/Passkeys/2FA) only during anomalous or sensitive operations.",
                text_tr="Risk Tabanlı Adaptif Kimlik Doğrulama mimarisi kurarım: Düşük riskli durumlarda sürtünmesiz kayıt, sadece şüpheli durumlarda veya para transferlerinde kademeli Passkeys/2FA tetiklerim.",
                score=3.8,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="a4_d",
                text="I establish the corporate Security vs Usability decision framework, mediating executive trade-offs with threat modeling and revenue impact models.",
                text_tr="Şirket genelinde Güvenlik vs Kullanılabilirlik karar çerçevesini oluşturur; tehdit modellemesi ve gelir kaybı analizleriyle yönetici uzlaşısını kurumsallaştırırım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="a4_e",
                text="I pioneer industry-leading security-by-design innovations that eliminate security friction as a concept, creating seamless user experiences that surpass regulatory mandates.",
                text_tr="Kullanıcı deneyimini güvenlik sürtünmesinden tamamen arındıran yenilikçi mimarilere öncülük eder; regülasyonları aşarken sektör standartlarını belirlerim.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="auto_05",
        difficulty=5,
        dimension=DimensionId.AUTONOMY,
        title="Identifying Hidden Systemic Blind Spots",
        title_tr="Gizli Sistemik Mimari Kör Noktaları Tespit Etme",
        scenario="Everything appears green on current team dashboards, but you notice subtle architectural patterns that will cause systemic collapse if user base grows 3x next year.",
        scenario_tr="Mevcut dashboard'larda her şey yeşil görünüyor; ancak mimariyi incelediğinizde kullanıcı sayısı gelecek yıl 3 katına çıktığında sistemin çökeceğini fark ediyorsunuz.",
        interview_source="Glassdoor: Netflix Staff Architect (Systemic Blind Spots & Capacity Cliffs)",
        question_type="system_design",
        is_quick=False,
        options=[
            QuestionOption(
                id="a5_a",
                text="I assume senior leadership already knows about it and continue working on current sprint tickets.",
                text_tr="Yönetimin bunu zaten bildiğini varsayar ve mevcut sprint biletlerimi yazmaya devam ederim.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="a5_b",
                text="I mention it casually in a retrospective meeting and see if anyone reacts.",
                text_tr="Bir retrospektif toplantısında laf arasında bahseder ve birinin ilgilenip ilgilenmediğine bakarım.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="a5_c",
                text="I conduct proof-of-concept stress tests, produce a quantitative technical report showing the failure curve, and propose an actionable mitigation epic for the next quarter.",
                text_tr="Kavram kanıtlama (PoC) stres testleri yapar; kırılma eğrisini gösteren teknik bir rapor hazırlayıp gelecek çeyreğin yol haritasına önleyici bir epic ekletirim.",
                score=3.7,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="a5_d",
                text="I identify cross-organizational architectural risks before anyone else spots them, build consensus across affected engineering directors, and secure proactive investment.",
                text_tr="Organizasyon genelindeki mimari riskleri kimse fark etmeden önce tespit eder; etkilenen mühendislik direktörleriyle uzlaşıp proaktif yatırım bütçesi alırım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="a5_e",
                text="I steer organizational future-readiness: anticipate macroeconomic, technological, and regulatory blind spots, positioning the company years ahead of industry rivals.",
                text_tr="Şirketin geleceğe hazır olma yeteneğini yönetirim: Makroekonomik, teknolojik ve yasal kör noktaları yıllar öncesinden öngörerek şirketi rakiplerinin fersah fersah önüne geçiririm.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
    Question(
        id="auto_06",
        difficulty=5,
        dimension=DimensionId.AUTONOMY,
        title="Multi-Year Technical Vision & Direction",
        title_tr="Çok Yıllık Teknik Strateji & North Star Vizyonu",
        scenario="Your engineering organization is transitioning from a startup to a mature enterprise. How do you shape the multi-year technical trajectory?",
        scenario_tr="Mühendislik organizasyonunuz hızlı büyüyen bir startup'tan kurumsal bir yapıya evriliyor. Çok yıllık teknik rotayı ve vizyonu nasıl şekillendirirsiniz?",
        interview_source="Glassdoor: Stripe Principal Systems Architect (Multi-Year Technical Vision & North Star)",
        question_type="architecture_tradeoff",
        is_quick=False,
        options=[
            QuestionOption(
                id="a6_a",
                text="I focus on day-to-day coding tasks and leave long-term vision to the founders.",
                text_tr="Günlük kodlama işlerime odaklanır, uzun vadeli vizyonu kuruculara bırakırım.",
                score=1.0,
                level_indicator=SeniorityLevel.L1
            ),
            QuestionOption(
                id="a6_b",
                text="I propose adopting popular modern technologies that other tech companies are buzzing about.",
                text_tr="Diğer teknoloji şirketlerinin konuştuğu popüler ve trend teknolojileri benimsememizi öneririm.",
                score=2.0,
                level_indicator=SeniorityLevel.L2
            ),
            QuestionOption(
                id="a6_c",
                text="I draft a 1-year technical roadmap for my service domain, planning evolutionary migrations, deprecation of technical debt, and key scalability milestones.",
                text_tr="Kendi servis alanım için 1 yıllık teknik yol haritası hazırlar; kademeli mimari geçişleri, teknik borç tasfiyesini ve kritik ölçeklenme aşamalarını planlarım.",
                score=3.6,
                level_indicator=SeniorityLevel.L3
            ),
            QuestionOption(
                id="a6_d",
                text="I author a 2-3 year Engineering Strategy document across multiple business units, aligning technical architecture with business revenue trajectories and scaling horizons.",
                text_tr="Farklı iş birimlerini kapsayan 2-3 yıllık Mühendislik Strateji belgesini yazar; teknik mimariyi şirketin gelir hedefleri ve ölçeklenme ufkuyla hizalarım.",
                score=4.6,
                level_indicator=SeniorityLevel.L4
            ),
            QuestionOption(
                id="a6_e",
                text="I define the 5-year technological North Star for the enterprise, pioneering platform paradigms that redefine company competitiveness and shape industry standards.",
                text_tr="Şirketin 5 yıllık teknolojik 'Kutup Yıldızı'nı (North Star) belirler; şirket rekabetini yeniden tanımlayan ve sektöre yön veren platform paradigmalarına öncülük ederim.",
                score=5.0,
                level_indicator=SeniorityLevel.L5
            ),
        ],
    ),
]

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

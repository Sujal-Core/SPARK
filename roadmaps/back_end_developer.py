# roadmap/backend_road.py
from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory (project_root/templates)
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

# Backend Developer Roadmap (role-accurate variable)
BACKEND_DEVELOPER_ROADMAP = [
    {
        "title": "Programming Fundamentals",
        "description": "Build strong command over a primary backend language and its ecosystem. Learn core data structures and algorithms, error handling, and concurrency primitives so services are correct, performant, and maintainable.",
        "points": [
            {"name": "Choose a Language", "desc": "Java, Go, Python, Node.js, or .NET based on team and ecosystem"},
            {"name": "Core Concepts", "desc": "DSA, immutability, exceptions, generics/types, interfaces/traits"},
            {"name": "Concurrency", "desc": "Threads/goroutines/async, synchronization, pools, backpressure"},
            {"name": "Testing", "desc": "Unit/integration tests, mocks/stubs, property-based testing"},
            {"name": "Tooling", "desc": "Formatters/linters, build tools, package managers, profiling"}
        ],
        "links": [
            {"name": "Go Tour", "url": "https://go.dev/tour/"},
            {"name": "Effective Java", "url": "https://www.pearson.com/en-us/subject-catalog/p/effective-java/P200000006822/9780134685991"}
        ],
        "other_resources": [
            {"name": "pytest Docs", "url": "https://docs.pytest.org/"},
            {"name": "Jest", "url": "https://jestjs.io/"}
        ]
    },
    {
        "title": "Git, Linux & Shell",
        "description": "Work productively on Linux-based systems and collaborate through Git. Use shell tools to inspect processes, logs, and networks and to automate repetitive tasks during development and ops.",
        "points": [
            {"name": "Git Proficiency", "desc": "Branching models, PR reviews, commit conventions, semantic versioning"},
            {"name": "Shell Skills", "desc": "awk/sed/grep, pipes, environment, tmux, journald/logrotate basics"},
            {"name": "System Basics", "desc": "Processes/signals, service managers, file permissions, ulimit"}
        ],
        "links": [
            {"name": "Git Book", "url": "https://git-scm.com/book/en/v2"},
            {"name": "The Linux Command Line", "url": "https://linuxcommand.org/tlcl.php"}
        ]
    },
    {
        "title": "HTTP, APIs & Web",
        "description": "Understand how the web works to design robust APIs. Master HTTP semantics, caching, idempotency, and safe pagination. Choose REST or gRPC/GraphQL thoughtfully based on clients and contracts.",
        "points": [
            {"name": "HTTP Semantics", "desc": "Methods, status codes, headers, conditional requests, caching"},
            {"name": "API Styles", "desc": "REST, gRPC, GraphQL; versioning, schema-first vs code-first"},
            {"name": "Pagination & Idempotency", "desc": "Cursors vs offset, retry-safe operations, idempotency keys"},
            {"name": "Security Basics", "desc": "TLS, OAuth/OIDC, JWTs, CORS, rate limits, input validation"},
            {"name": "Documentation", "desc": "OpenAPI/Swagger, protobuf schemas, examples, changelogs"}
        ],
        "links": [
            {"name": "RFC 9110 (HTTP Semantics)", "url": "https://www.rfc-editor.org/rfc/rfc9110"},
            {"name": "OpenAPI Spec", "url": "https://swagger.io/specification/"}
        ],
        "other_resources": [
            {"name": "gRPC Docs", "url": "https://grpc.io/docs/"},
            {"name": "GraphQL", "url": "https://graphql.org/learn/"}
        ]
    },
    {
        "title": "Databases & Storage",
        "description": "Select and operate the right data stores for access patterns. Model data carefully, manage transactions and isolation, and reason about indexes, query plans, and consistency trade-offs.",
        "points": [
            {"name": "Relational", "desc": "Postgres/MySQL; indexing, joins, explain plans, isolation levels"},
            {"name": "NoSQL", "desc": "Document, key-value, column, time-series; access patterns first"},
            {"name": "Transactions", "desc": "ACID, distributed transactions vs outbox patterns, idempotency"},
            {"name": "Caching", "desc": "Redis/Memcached, TTLs, cache invalidation and consistency"},
            {"name": "Migrations", "desc": "Schema changes, zero-downtime patterns, backfills and rollbacks"}
        ],
        "links": [
            {"name": "PostgreSQL Docs", "url": "https://www.postgresql.org/docs/"},
            {"name": "Redis Docs", "url": "https://redis.io/docs/"}
        ],
        "other_resources": [
            {"name": "Designing Data-Intensive Applications", "url": "https://dataintensive.net/"}
        ]
    },
    {
        "title": "Architecture & Patterns",
        "description": "Design maintainable services that evolve with product needs. Apply clean boundaries, dependency inversion, and modular monolith or microservice patterns as appropriate with clear contracts.",
        "points": [
            {"name": "Service Design", "desc": "Hexagonal/clean architecture, DDD-lite, modules and boundaries"},
            {"name": "Async Messaging", "desc": "Event-driven design, queues/brokers, back-pressure and retries"},
            {"name": "Consistency", "desc": "Sagas/outbox, eventual consistency, idempotent consumers"},
            {"name": "Resilience", "desc": "Circuit breakers, timeouts, bulkheads, exponential backoff"},
            {"name": "Observability", "desc": "Structured logs, metrics, traces, correlation IDs, SLOs"}
        ],
        "links": [
            {"name": "12-Factor Apps", "url": "https://12factor.net/"},
            {"name": "Microservices Patterns (Book)", "url": "https://microservices.io/book"}
        ],
        "other_resources": [
            {"name": "OpenTelemetry", "url": "https://opentelemetry.io/"},
            {"name": "Istio (service mesh)", "url": "https://istio.io/latest/docs/"}
        ]
    },
    {
        "title": "Security & Compliance",
        "description": "Bake in security from the start. Handle secrets safely, validate inputs, sanitize outputs, and adopt secure defaults for authentication, authorization, crypto, and data protection.",
        "points": [
            {"name": "AuthN/Z", "desc": "OAuth/OIDC, session vs token, RBAC/ABAC, password storage"},
            {"name": "Input & Output", "desc": "Validation, escaping, CSRF, SSRF, deserialization risks"},
            {"name": "Secrets", "desc": "Secret managers, rotation, envelope encryption, KMS integration"},
            {"name": "Supply Chain", "desc": "SBOMs, dependency pinning, signing, container image scanning"},
            {"name": "Compliance", "desc": "PII handling, audit trails, logging policies, data retention"}
        ],
        "links": [
            {"name": "OWASP ASVS", "url": "https://owasp.org/www-project-application-security-verification-standard/"},
            {"name": "NIST Crypto Guidelines", "url": "https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines"}
        ],
        "other_resources": [
            {"name": "Sigstore (cosign)", "url": "https://www.sigstore.dev/"},
            {"name": "Trivy (scanner)", "url": "https://aquasecurity.github.io/trivy/"}
        ]
    },
    {
        "title": "Containers & Orchestration",
        "description": "Package services with containers and deploy predictably across environments. Learn basic Kubernetes to manage rollout strategies, configs, secrets, and autoscaling.",
        "points": [
            {"name": "Docker", "desc": "Minimal images, multi-stage builds, healthchecks, resource limits"},
            {"name": "Compose", "desc": "Local multi-service environments, networks, volumes, overrides"},
            {"name": "Kubernetes Basics", "desc": "Pods/Deployments/Services, Ingress, HPA, ConfigMap/Secret"},
            {"name": "Rollouts", "desc": "Readiness/liveness, blue/green, canary, progressive delivery"},
            {"name": "Stateful Needs", "desc": "PVCs, StatefulSets, operators, connection draining"}
        ],
        "links": [
            {"name": "Docker Docs", "url": "https://docs.docker.com/"},
            {"name": "Kubernetes Docs", "url": "https://kubernetes.io/docs/home/"}
        ],
        "other_resources": [
            {"name": "Helm", "url": "https://helm.sh/docs/"},
            {"name": "Argo Rollouts", "url": "https://argo-rollouts.readthedocs.io/en/stable/"}
        ]
    },
    {
        "title": "CI/CD & Testing Strategy",
        "description": "Automate build, test, and deployment with pipelines. Keep fast feedback loops and guard production with quality gates, smoke tests, and safe rollback paths.",
        "points": [
            {"name": "Pipelines", "desc": "GitHub Actions/GitLab CI/Jenkins; caches, matrix builds, artifacts"},
            {"name": "Test Pyramid", "desc": "Unit/integration/contract/e2e; flaky test management, test data"},
            {"name": "Release Flows", "desc": "Tags, changelogs, semantic releases, feature flags, canary tests"},
            {"name": "Infra in CI", "desc": "Ephemeral environments, docker-in-docker, preview URLs"},
            {"name": "Quality Gates", "desc": "Coverage thresholds, lint/format, SAST/DAST, SBOM generation"}
        ],
        "links": [
            {"name": "GitHub Actions", "url": "https://docs.github.com/actions"},
            {"name": "GitLab CI", "url": "https://docs.gitlab.com/ee/ci/"}
        ],
        "other_resources": [
            {"name": "SonarQube", "url": "https://docs.sonarsource.com/sonarqube/"},
            {"name": "OWASP ZAP", "url": "https://www.zaproxy.org/docs/"}
        ]
    },
    {
        "title": "Performance & Reliability",
        "description": "Design for scale and resilience. Profile hot paths, use caches and pools appropriately, and implement timeouts, retries, and fallbacks so services degrade gracefully under stress.",
        "points": [
            {"name": "Profiling", "desc": "CPU/memory/heap/allocs, tracing slow endpoints and queries"},
            {"name": "Caching & Queues", "desc": "Request-level and data caches, async work queues, DLQs"},
            {"name": "Resilience", "desc": "Circuit breakers, hedged requests, retries with jitter, timeouts"},
            {"name": "Rate Limits & Quotas", "desc": "Token bucket/leaky bucket, fairness, abuse prevention"},
            {"name": "DB Performance", "desc": "Connection pools, prepared statements, N+1 elimination"}
        ],
        "links": [
            {"name": "SRE Workbook", "url": "https://sre.google/workbook/"},
            {"name": "Caching Strategies", "url": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching"}
        ],
        "other_resources": [
            {"name": "Envoy", "url": "https://www.envoyproxy.io/docs"},
            {"name": "HAProxy", "url": "https://www.haproxy.org/"}
        ]
    },
    {
        "title": "Cloud Platforms & Services",
        "description": "Leverage managed services to accelerate development while remaining cost-aware. Master IAM, networking, and platform primitives that underpin secure, reliable backends.",
        "points": [
            {"name": "IAM", "desc": "Principle of least privilege, roles/policies, workload identity"},
            {"name": "Networking", "desc": "VPC/VNet, subnets, load balancers, private endpoints, TLS"},
            {"name": "Managed Services", "desc": "Queues, streams, caches, databases, object stores, email/SMS"}
        ],
        "links": [
            {"name": "AWS Well-Architected", "url": "https://aws.amazon.com/architecture/well-architected/"},
            {"name": "GCP Architecture Center", "url": "https://cloud.google.com/architecture"}
        ],
        "other_resources": [
            {"name": "Azure Architecture Center", "url": "https://learn.microsoft.com/azure/architecture/"},
            {"name": "Cloud Design Patterns", "url": "https://learn.microsoft.com/azure/architecture/patterns/"}
        ]
    },
    {
        "title": "Projects & Portfolio",
        "description": "Demonstrate end-to-end backend engineering: design APIs, model data, implement auth and observability, and deploy with pipelines and rollout safety. Document trade-offs and performance results.",
        "points": [
            {"name": "E2E Service", "desc": "REST/gRPC API, DB schema, caching, background jobs, observability"},
            {"name": "Security & Tests", "desc": "AuthN/Z, input validation, test pyramid, load tests and chaos drills"},
            {"name": "Deploy & Operate", "desc": "Containerized, Kubernetes or PaaS, SLOs, alerts, runbooks and dashboards"},
            {"name": "Docs", "desc": "OpenAPI, ADRs, READMEs, architecture diagrams, postmortem templates"}
        ],
        "links": [
            {"name": "OpenAPI Tools", "url": "https://openapi.tools/"},
            {"name": "k6 Load Testing", "url": "https://k6.io/docs/"}
        ],
        "other_resources": [
            {"name": "ADR Templates", "url": "https://github.com/joelparkerhenderson/architecture_decision_record"},
            {"name": "Awesome Production-Ready", "url": "https://github.com/topics/production-ready"}
        ]
    },
    {
        "title": "Continuous Learning",
        "description": "Keep up with evolving frameworks, runtimes, and cloud services. Read release notes, follow benchmarks, and improve architecture by contributing to and learning from community examples.",
        "points": [
            {"name": "Release Notes", "desc": "Language/runtime/framework changes, deprecations and migrations"},
            {"name": "Benchmarking", "desc": "Latency/throughput, cost/performance, cold-start vs warm pool"},
            {"name": "Community", "desc": "Meetups, RFCs, issues/PRs, design docs and postmortems"}
        ],
        "links": [
            {"name": "Awesome Backend", "url": "https://github.com/tiimgreen/github-cheat-sheet"},
            {"name": "InfoQ & HighScalability", "url": "http://highscalability.com/"}
        ],
        "other_resources": [
            {"name": "Awesome Microservices", "url": "https://github.com/mfornos/awesome-microservices"},
            {"name": "Awesome Observability", "url": "https://github.com/cncf/tag-observability"}
        ]
    }
]

@app.route("/")
def home():
    return redirect(url_for('backend_developer'))

def render_page():
    return render_template("roadmaps/backend_eng.html", roadmap=BACKEND_DEVELOPER_ROADMAP)

# ✅ Optional standalone Flask runner for testing
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('Backened_developer'))

    @app.route("/appdev")
    def app_developer():
        return render_page()

    app.run(debug=True)
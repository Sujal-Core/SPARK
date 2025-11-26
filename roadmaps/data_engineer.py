# roadmap/dataeng_road.py
from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory (project_root/templates)
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

# Data Engineer Roadmap (role-accurate variable)
DATA_ENGINEER_ROADMAP = [
    {
        "title": "Programming & Software Foundations",
        "description": "Develop strong fundamentals to build reliable, maintainable data systems. Write clean, testable Python and/or Java/Scala; manage environments; and structure projects for CI/CD and collaboration.",
        "points": [
            {"name": "Python for DE", "desc": "Typing, logging, packaging, virtualenv/poetry, CLI tooling, error handling/retries"},
            {"name": "Java/Scala Basics", "desc": "JVM ecosystem familiarity for Spark/Beam; build tools (Maven/Gradle/sbt)"},
            {"name": "Testing & Quality", "desc": "pytest/JUnit, property-based tests, contracts, code formatting and linting"},
            {"name": "APIs & SDKs", "desc": "REST/gRPC clients, cloud SDKs, pagination, rate limits, auth flows"},
            {"name": "Concurrency & Parallelism", "desc": "Multiprocessing/threading/asyncio, producer–consumer queues, backpressure awareness"},
            {"name": "Configuration & Secrets", "desc": "12-factor configs, env vars, .env/yaml, secret injection via vaults"},
            {"name": "Docs & Reviews", "desc": "Docstrings, READMEs, ADRs, code review checklists, changelogs and release notes"}
        ],
        "links": [
            {"name": "Effective Python", "url": "https://effectivepython.com/"},
            {"name": "Scala at a Glance", "url": "https://docs.scala-lang.org/overviews/scala-book/introduction.html"}
        ],
        "other_resources": [
            {"name": "12-Factor Apps (principles)", "url": "https://12factor.net/"}
        ]
    },
    {
        "title": "Linux, Networking & Shell",
        "description": "Operate data services on Linux. Use shell tools for inspection and quick fixes, and understand basic networking to debug connectivity, DNS, and routing problems.",
        "points": [
            {"name": "Shell Proficiency", "desc": "awk/sed/grep, xargs, tmux/screen, process signals, systemd services/logs"},
            {"name": "Filesystems & IO", "desc": "Permissions/ACLs, inodes, bandwidth vs IOPS, buffering, compression"},
            {"name": "Networking Basics", "desc": "DNS, TLS, proxies, firewalls, CIDR/subnets, tools (curl, dig, ss, tcpdump)"},
            {"name": "Monitoring Tools", "desc": "top/htop, iostat/vmstat, dmesg/journalctl, lsof/strace for troubleshooting"},
            {"name": "SSH & Tunnels", "desc": "Agent forwarding, jump hosts, port forwarding, socks proxies for data access"},
            {"name": "Containers Basics", "desc": "docker build/run, logs/exec, image scanning, minimal base images for jobs"}
        ],
        "links": [
            {"name": "The Linux Command Line", "url": "https://linuxcommand.org/tlcl.php"},
            {"name": "Julia Evans Zines (networking)", "url": "https://jvns.ca/zines/"}
        ]
    },
    {
        "title": "SQL Mastery",
        "description": "Write efficient, readable SQL for batch and interactive analytics. Use window functions, CTEs, and advanced joins; reason about execution plans and indexes.",
        "points": [
            {"name": "Analytical SQL", "desc": "Window functions, CTEs, conditional aggregation, pivot/unpivot"},
            {"name": "Performance", "desc": "Indexing, partition pruning, statistics, avoiding anti-patterns"},
            {"name": "Data Correctness", "desc": "Constraints, keys, null semantics, time zones, idempotent upserts/merges"},
            {"name": "Time-Series SQL", "desc": "Date binning, gaps-and-islands, sessionization, SCD-friendly patterns"},
            {"name": "Procedures & UDFs", "desc": "Safe usage guidelines, portability concerns, versioning and governance"},
            {"name": "Style & Conventions", "desc": "Readable formatting, naming standards, linting and reviewable query diffs"}
        ],
        "links": [
            {"name": "Mode SQL Tutorial", "url": "https://mode.com/sql-tutorial/"},
            {"name": "PostgreSQL Docs", "url": "https://www.postgresql.org/docs/"}
        ],
        "other_resources": [
            {"name": "SQLBolt", "url": "https://sqlbolt.com/"},
            {"name": "Exasol Window Functions Guide", "url": "https://docs.exasol.com/sql_references/functions/alphabeticlistfunctions/window_functions.htm"}
        ]
    },
    {
        "title": "Data Modeling & Warehousing",
        "description": "Design schemas and storage that support reliable analytics and scalable pipelines. Apply dimensional modeling, maintain slowly changing dimensions, and plan partitioning and clustering.",
        "points": [
            {"name": "Dimensional Modeling", "desc": "Star/snowflake, facts/dimensions, SCD types, conformed dimensions"},
            {"name": "Warehouse Patterns", "desc": "Partitioning, clustering/z-ordering, materialized views, snapshotting"},
            {"name": "Semantic Layers", "desc": "Metrics layers (LookML/dbt metrics), governance, documentation and lineage"},
            {"name": "Keys & Surrogates", "desc": "Surrogate vs natural keys, identity management, referential integrity"},
            {"name": "Data Vault (Intro)", "desc": "Hub/link/satellite basics, when to consider vault vs dimensional"},
            {"name": "Multitenancy & Zones", "desc": "Bronze/silver/gold zones, access boundaries and workload isolation"}
        ],
        "links": [
            {"name": "Kimball Toolkit", "url": "https://www.kimballgroup.com/"},
            {"name": "dbt Core Docs", "url": "https://docs.getdbt.com/docs"}
        ],
        "other_resources": [
            {"name": "BigQuery Best Practices", "url": "https://cloud.google.com/bigquery/docs/best-practices-performance-overview"},
            {"name": "Snowflake Docs", "url": "https://docs.snowflake.com/"}
        ]
    },
    {
        "title": "Batch Processing",
        "description": "Build resilient batch pipelines that transform large datasets on a schedule. Use Spark or SQL-first transformations (dbt) with clear dependency graphs and data contracts.",
        "points": [
            {"name": "Spark Core", "desc": "RDD/DataFrame/Dataset APIs, shuffle, partitions, joins, broadcast, caching"},
            {"name": "Resource Tuning", "desc": "Executors, memory, parallelism, skew mitigation, file sizing"},
            {"name": "dbt & SQL ELT", "desc": "Model layers, macros, tests, snapshots, exposures, docs site"},
            {"name": "Checkpointing", "desc": "Idempotent writes, atomic swaps, incremental processing, watermarking"},
            {"name": "Small Files & Layout", "desc": "Compaction strategies, file size targets, partition scheme choices"},
            {"name": "Retry & Backoff", "desc": "Exponential backoff, dead-letter handling, partial failures and reruns"}
        ],
        "links": [
            {"name": "Apache Spark Docs", "url": "https://spark.apache.org/docs/latest/"},
            {"name": "dbt Core", "url": "https://docs.getdbt.com/docs"}
        ],
        "other_resources": [
            {"name": "Delta Lake", "url": "https://docs.delta.io/latest/"},
            {"name": "Apache Iceberg", "url": "https://iceberg.apache.org/"}
        ]
    },
    {
        "title": "Streaming & Real-Time",
        "description": "Process events with low latency and exactly-once semantics where possible. Choose between logs and tables, design partition keys, and manage schema evolution over streams.",
        "points": [
            {"name": "Kafka Fundamentals", "desc": "Producers/consumers, partitions, consumer groups, offset management"},
            {"name": "Stream Processing", "desc": "Flink/Spark Structured Streaming, windows, watermarks, state, timers"},
            {"name": "Delivery Semantics", "desc": "At-most/at-least/exactly-once trade-offs, idempotent sinks and dedupe"},
            {"name": "Transactional Flows", "desc": "Kafka transactional producers/consumers, EOS patterns for sinks"},
            {"name": "CDC Pipelines", "desc": "Debezium connectors, schema evolution, outbox patterns, replays"},
            {"name": "Backpressure & SLAs", "desc": "Rate limiting, buffer sizing, lag dashboards, autoscaling triggers"}
        ],
        "links": [
            {"name": "Apache Kafka Docs", "url": "https://kafka.apache.org/documentation/"},
            {"name": "Apache Flink Docs", "url": "https://nightlies.apache.org/flink/flink-docs-stable/"}
        ],
        "other_resources": [
            {"name": "Kafka Streams", "url": "https://kafka.apache.org/documentation/streams/"},
            {"name": "Spark Streaming", "url": "https://spark.apache.org/streaming/"}
        ]
    },
    {
        "title": "Orchestration & Workflow",
        "description": "Schedule and monitor data workflows with clear dependencies, retries, and alerting. Keep DAGs modular and observable; capture lineage and runtime metadata.",
        "points": [
            {"name": "Airflow/Prefect", "desc": "Task/DAG design, sensors/triggers, retries, SLAs, backfills, pools"},
            {"name": "Idempotency", "desc": "Checkpointing, atomic writes, partition overwrites, late data handling"},
            {"name": "Observability", "desc": "Metrics, logs, traces, run history, data lineage and artifacts"},
            {"name": "Secrets & Conns", "desc": "Connection managers, secret backends, rotations, impersonation"},
            {"name": "Templating & Mapping", "desc": "Jinja/macros, dynamic task mapping, reusable operators/hooks"},
            {"name": "Deploy Patterns", "desc": "DAG versioning, blue/green scheduler updates, plugins and providers"}
        ],
        "links": [
            {"name": "Apache Airflow", "url": "https://airflow.apache.org/docs/"},
            {"name": "Prefect", "url": "https://docs.prefect.io/"}
        ],
        "other_resources": [
            {"name": "OpenLineage", "url": "https://openlineage.io/"},
            {"name": "Marquez", "url": "https://marquezproject.github.io/marquez/"}
        ]
    },
    {
        "title": "Data Storage & Lakehouse",
        "description": "Select storage formats and table technologies that enable ACID, time travel, schema evolution, and scalable reads/writes across batch and streaming.",
        "points": [
            {"name": "Columnar & Files", "desc": "Parquet/ORC/Avro; compression codecs; file sizing for optimal scans"},
            {"name": "Table Formats", "desc": "Delta Lake, Apache Iceberg, Apache Hudi; compaction and clustering"},
            {"name": "Metadata & Catalogs", "desc": "Hive Metastore/Glue/Unity Catalog; governance and permissions"},
            {"name": "Compaction & Vacuum", "desc": "Retention settings, snapshot cleanup, optimize/z-ordering strategies"},
            {"name": "Partition Design", "desc": "Low/high cardinality, time bucketing, multi-column partition trade-offs"},
            {"name": "Caching & Indices", "desc": "Caching layers, data skipping, bloom filters, min/max stats usage"}
        ],
        "links": [
            {"name": "Delta Lake Docs", "url": "https://docs.delta.io/latest/"},
            {"name": "Apache Iceberg Docs", "url": "https://iceberg.apache.org/"}
        ],
        "other_resources": [
            {"name": "Apache Hudi Docs", "url": "https://hudi.apache.org/docs/"},
            {"name": "Parquet Format", "url": "https://parquet.apache.org/docs/"}
        ]
    },
    {
        "title": "Data Contracts & Quality",
        "description": "Define explicit contracts between producers and consumers. Validate schemas, ranges, and distributions; alert on anomalies and drift to prevent broken dashboards and ML pipelines.",
        "points": [
            {"name": "Schema Management", "desc": "Avro/Protobuf, schema registry, compatibility and evolution policies"},
            {"name": "Quality Checks", "desc": "Great Expectations/Soda, unit tests on data, freshness and completeness"},
            {"name": "Contract Enforcement", "desc": "Fail fast vs quarantine, backfills, SLAs/SLOs for data products"},
            {"name": "Contract Testing", "desc": "CI checks on schemas and example payloads; sample-based diffs"},
            {"name": "Data Diffing", "desc": "Row/column-level diffs, reconciliation jobs, tolerance thresholds"},
            {"name": "Anomaly Detection", "desc": "Statistical thresholds, seasonal baselines, alert routing and runbooks"}
        ],
        "links": [
            {"name": "Great Expectations", "url": "https://docs.greatexpectations.io/"},
            {"name": "Soda Core", "url": "https://docs.soda.io/soda-core/"}
        ],
        "other_resources": [
            {"name": "Confluent Schema Registry", "url": "https://docs.confluent.io/platform/current/schema-registry/index.html"}
        ]
    },
    {
        "title": "Cloud Platforms & IAM",
        "description": "Use managed data services on AWS/Azure/GCP. Configure least-privilege access, service identities, network boundaries, and encryption to protect data at rest and in transit.",
        "points": [
            {"name": "Core Services", "desc": "Object storage, managed Postgres, data warehouse, serverless functions"},
            {"name": "IAM & Secrets", "desc": "Roles/policies, workload identity/OIDC, KMS, secret managers"},
            {"name": "Networking & Security", "desc": "VPC peering, private endpoints, TLS, DLP and key rotation policies"},
            {"name": "Cross-Account Access", "desc": "Assume-role patterns, org policies, boundary permissions and audits"},
            {"name": "Private Connectivity", "desc": "VPC peering vs transit, PrivateLink/Private Service Connect comparisons"}
        ],
        "links": [
            {"name": "AWS Data Analytics", "url": "https://aws.amazon.com/big-data/datalakes-and-analytics/"},
            {"name": "GCP Analytics", "url": "https://cloud.google.com/solutions/big-data"}
        ],
        "other_resources": [
            {"name": "Azure Synapse", "url": "https://learn.microsoft.com/azure/synapse-analytics/"}
        ]
    },
    {
        "title": "Infrastructure as Code & DevOps",
        "description": "Provision and manage data infra declaratively with Terraform or cloud-native stacks. Add CI/CD for pipelines and infra, and bake in policy-as-code for safety and compliance.",
        "points": [
            {"name": "Terraform", "desc": "State, modules, workspaces, plans, drift detection, CI validation"},
            {"name": "Policy-as-Code", "desc": "OPA/Conftest; guardrails on resources, networks, encryption, tagging"},
            {"name": "CI/CD", "desc": "GitHub Actions/GitLab CI for jobs, tests, deploys, and environment promotions"},
            {"name": "Module Registries", "desc": "Reusable infra modules, version pinning, changelog and docs"},
            {"name": "Pre-commit Hooks", "desc": "Format/lint/security scan before commit; policy and secret checks"},
            {"name": "Drift Management", "desc": "Scheduled drift detection, reconciliation jobs, break-glass procedures"}
        ],
        "links": [
            {"name": "Terraform Docs", "url": "https://developer.hashicorp.com/terraform/docs"},
            {"name": "OPA", "url": "https://www.openpolicyagent.org/"}
        ]
    },
    {
        "title": "Cost, Reliability & Observability",
        "description": "Design pipelines for predictable costs and high reliability. Track job performance and failures, implement retries and backoffs, and monitor SLIs/SLOs for data freshness and completeness.",
        "points": [
            {"name": "Cost Controls", "desc": "File sizing, partition pruning, caching, warehouse slots/credits, budgets"},
            {"name": "Reliability Patterns", "desc": "Retries with jitter, dead-letter queues, idempotent sinks, circuit breakers"},
            {"name": "Observability", "desc": "Metrics/logs/traces for pipelines, lineage dashboards, on-call playbooks"},
            {"name": "SLO Dashboards", "desc": "Freshness/completeness SLIs with targets, error budgets and burn rates"},
            {"name": "Capacity Planning", "desc": "Throughput limits, concurrency, backfills vs daily windows, quotas"}
        ],
        "links": [
            {"name": "Prometheus", "url": "https://prometheus.io/docs/introduction/overview/"},
            {"name": "Grafana", "url": "https://grafana.com/docs/grafana/latest/"}
        ],
        "other_resources": [
            {"name": "Evidently (Data Monitoring)", "url": "https://docs.evidentlyai.com/"}
        ]
    },
    {
        "title": "Data Products & Interfaces",
        "description": "Expose trustworthy data through well-defined interfaces—tables, views, CDC streams, and APIs. Document SLAs, semantics, and change policies for downstream consumers.",
        "points": [
            {"name": "Publishing", "desc": "Materialized views, curated tables, CDC/Kafka topics with schemas"},
            {"name": "APIs", "desc": "Read services for key aggregates, pagination, authN/Z, rate limits"},
            {"name": "Docs & SLAs", "desc": "Data product pages: owners, freshness SLOs, contact, change log"},
            {"name": "Versioning", "desc": "Schema and dataset versioning, deprecation windows, compatibility guides"},
            {"name": "Client Libraries", "desc": "Thin SDKs for common access patterns with retries/metrics/telemetry"}
        ],
        "links": [
            {"name": "LakeFS/lakeFS", "url": "https://lakefs.io/"},
            {"name": "OpenAPI", "url": "https://swagger.io/specification/"}
        ]
    },
    {
        "title": "Security, Privacy & Compliance",
        "description": "Protect sensitive data with encryption, masking, tokenization, and access controls. Embed privacy by design and log access for audits.",
        "points": [
            {"name": "Data Protection", "desc": "PII classification, field-level encryption/masking, tokenization"},
            {"name": "Access Control", "desc": "Row/column-level security, attribute-based access, approval workflows"},
            {"name": "Compliance", "desc": "Retention policies, audits, incident response runbooks"},
            {"name": "Scanning & DLP", "desc": "Automated PII scanning, quarantine, redaction rules, DLP policies"},
            {"name": "Deterministic Crypto", "desc": "Format-preserving/deterministic encryption for joins and analytics"}
        ],
        "links": [
            {"name": "NIST Privacy Framework", "url": "https://www.nist.gov/privacy-framework"},
            {"name": "GDPR Overview", "url": "https://gdpr-info.eu/"}
        ]
    },
    {
        "title": "Projects & Portfolio",
        "description": "Demonstrate end-to-end pipelines with clear contracts, lineage, and SLAs. Show batch and streaming, warehouse modeling, and observability with cost and reliability considerations.",
        "points": [
            {"name": "Batch + Streaming", "desc": "Ingest API/files, process with Spark/Flink, publish to warehouse and Kafka"},
            {"name": "Modeling & Docs", "desc": "dbt models, tests, docs site; data product pages with SLAs and lineage"},
            {"name": "Ops & Monitoring", "desc": "Airflow DAGs with retries/alerts; Prometheus/Grafana dashboards"},
            {"name": "Architecture Docs", "desc": "High-level diagrams, dataflow, ADRs, runbooks, cost and SLO callouts"},
            {"name": "Resilience & Cost", "desc": "Backfill drills, failure injections, cost reports and dashboards"}
        ],
        "links": [
            {"name": "dbt Examples", "url": "https://github.com/dbt-labs/jaffle_shop"},
            {"name": "Flink Examples", "url": "https://nightlies.apache.org/flink/flink-docs-stable/docs/try-flink/datastream/"}
        ]
    },
    {
        "title": "Continuous Learning",
        "description": "Stay current with table formats, engines, and platform features. Read release notes, benchmark trade-offs, and refine architecture patterns by contributing to community examples.",
        "points": [
            {"name": "Release Notes", "desc": "Delta/Iceberg/Hudi and warehouse updates, engine version changes"},
            {"name": "Benchmarks", "desc": "Storage/compute trade-offs, cost vs latency vs freshness comparisons"},
            {"name": "Community", "desc": "Meetups, RFCs, issues/PRs, sharing design docs and lessons learned"},
            {"name": "Certifications", "desc": "Targeted cloud/data exams to validate breadth and platform fluency"},
            {"name": "Reading Groups", "desc": "Internal guilds/book clubs to digest new features and patterns"}
        ],
        "links": [
            {"name": "Delta Lake Blog", "url": "https://delta.io/blog/"},
            {"name": "Apache Iceberg Blog", "url": "https://iceberg.apache.org/blog/"}
        ],
        "other_resources": [
            {"name": "Data Engineering Weekly", "url": "https://www.dataengineeringweekly.com/"}
        ]
    }
]

def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/data_engineer.html", roadmap=DATA_ENGINEER_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('data_engineer'))

    @app.route("/data_engineer")
    def data_engineer():
        return render_page()

    app.run(debug=True)
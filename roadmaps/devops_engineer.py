# roadmap/devops_road.py
from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory (project_root/templates)
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

# DevOps Engineer Roadmap (aligned to roadmap.sh)
DEVOPS_ENGINEER_ROADMAP = [
    {
        "title": "DevOps Foundations",
        "description": "Build a collaboration-first culture that unifies development and operations using automation, shared ownership, and continuous improvement; plan weekly learning sprints and ship small portfolio projects to compound skills over time.",
        "points": [
            {"name": "Mindset & Culture", "desc": "Shared responsibility, continuous improvement, blameless postmortems, and cross-functional collaboration with developers and SREs"},
            {"name": "Weekly Plan", "desc": "Balance programming, Linux, Git, networking, and a primary cloud to sustain consistent momentum"},
            {"name": "Portfolio Projects", "desc": "Deliver small infra/automation projects with clear READMEs, diagrams, and runbooks"},
            {"name": "Flow & Feedback", "desc": "Value stream mapping, reduce handoffs, shorten lead time, and tighten feedback loops"},
            {"name": "Metrics", "desc": "Track DORA metrics (Lead Time, Deployment Frequency, MTTR, Change Failure Rate) to guide improvement"}
        ],
        "links": [
            {"name": "DevOps Roadmap", "url": "https://roadmap.sh/devops"},
            {"name": "How to Become DevOps Engineer", "url": "https://roadmap.sh/devops/how-to-become-devops-engineer"},
            {"name": "DevOps PDF", "url": "https://roadmap.sh/pdfs/roadmaps/devops.pdf"}
        ],
        "other_resources": [
            {"name": "Accelerate (Book)", "url": "https://itrevolution.com/accelerate/"},
            {"name": "The Phoenix Project (Book)", "url": "https://www.thephoenixproject.org/"}
        ]
    },
    {
        "title": "Programming & Scripting",
        "description": "Use one primary language for automation and platform tooling, supported by shell scripting for operational glue; write clean, tested, and maintainable code to integrate APIs, CLIs, and pipeline tasks.",
        "points": [
            {"name": "Primary Language", "desc": "Python or Go for CLIs, integrations, automation, and platform tooling"},
            {"name": "Shell", "desc": "Bash or PowerShell for quick scripts, provisioning glue, and ops workflows"},
            {"name": "Testing & Packaging", "desc": "pytest or Go test, virtualenv/poetry or Go modules, semantic versioning and releases"},
            {"name": "API & SDKs", "desc": "Interact with cloud/provider SDKs, REST/GraphQL APIs, and Webhooks for integrations"}
        ],
        "links": [
            {"name": "Beginner Path", "url": "https://roadmap.sh/devops/how-to-become-devops-engineer"},
            {"name": "DevOps PDF", "url": "https://roadmap.sh/pdfs/roadmaps/devops.pdf"}
        ],
        "other_resources": [
            {"name": "Python Packaging User Guide", "url": "https://packaging.python.org/en/latest/"},
            {"name": "Go Modules", "url": "https://go.dev/doc/modules"}
        ]
    },
    {
        "title": "Linux, OS, and Terminal",
        "description": "Master Linux primitives, processes, filesystems, permissions, service managers, and performance tooling to troubleshoot servers, containers, and CI runners confidently.",
        "points": [
            {"name": "Distros & Editors", "desc": "Ubuntu/Debian or RHEL-family; Vim/Nano for live editing on servers and containers"},
            {"name": "CLI & Observability", "desc": "htop, iostat, vmstat, lsof, strace; awk, sed, grep; Bash/PowerShell essentials"},
            {"name": "Networking Basics", "desc": "ip/ss/tcpdump, firewall basics (ufw/iptables/nftables), name resolution and routing"},
            {"name": "Filesystems & Permissions", "desc": "Ext4/XFS, inodes, permissions, ACLs, systemd services and journald logs"}
        ],
        "links": [
            {"name": "DevOps PDF", "url": "https://roadmap.sh/pdfs/roadmaps/devops.pdf"}
        ],
        "other_resources": [
            {"name": "Linux Journey", "url": "https://linuxjourney.com/"},
            {"name": "The Linux Command Line", "url": "https://linuxcommand.org/tlcl.php"}
        ]
    },
    {
        "title": "Git & Hosting",
        "description": "Use Git fluently with branches, PR reviews, tags, and release flows on GitHub/GitLab/Bitbucket; design repo strategies that enable automation, code reviews, and traceable delivery.",
        "points": [
            {"name": "Git Essentials", "desc": "Branching models (trunk vs gitflow), code reviews, semantic versioning, release tagging"},
            {"name": "Repo Platforms", "desc": "GitHub, GitLab, Bitbucket; issues, project boards, and CI triggers"},
            {"name": "Quality & Security", "desc": "Commit signing, CODEOWNERS, protected branches, and required checks"}
        ],
        "links": [
            {"name": "DevOps PDF", "url": "https://roadmap.sh/pdfs/roadmaps/devops.pdf"},
            {"name": "Interview Questions", "url": "https://roadmap.sh/questions/devops"}
        ],
        "other_resources": [
            {"name": "Conventional Commits", "url": "https://www.conventionalcommits.org/en/v1.0.0/"},
            {"name": "Semantic Release", "url": "https://semantic-release.gitbook.io/"}
        ]
    },
    {
        "title": "Networking & Web Basics",
        "description": "Operate production web stacks by understanding OSI layers, core protocols, certificates, and edge components like proxies, load balancers, and CDNs.",
        "points": [
            {"name": "Core Protocols", "desc": "DNS, HTTP/HTTPS, TLS certs/PKI, SSH; optionally SMTP/IMAP with DMARC/SPF"},
            {"name": "Edge & Web", "desc": "Nginx/Apache/Caddy, reverse proxies, load balancers, caching servers and CDNs"},
            {"name": "IPv4/IPv6 & Security", "desc": "CIDR, subnets, firewall rules, NAT, security groups/NSGs"}
        ],
        "links": [
            {"name": "DevOps PDF", "url": "https://roadmap.sh/pdfs/roadmaps/devops.pdf"}
        ],
        "other_resources": [
            {"name": "Let’s Encrypt", "url": "https://letsencrypt.org/"},
            {"name": "HTTP RFCs (Overview)", "url": "https://www.rfc-editor.org/rfc/rfc9110"}
        ]
    },
    {
        "title": "Containers",
        "description": "Standardize packaging and runtime with Docker; build minimal, secure, and reproducible images and use Compose for local multi-service development.",
        "points": [
            {"name": "Docker Fundamentals", "desc": "Images, containers, multi-stage builds, tagging, scanning, networking, volumes"},
            {"name": "Compose", "desc": "Local orchestration for multi-service development and testing"},
            {"name": "Image Hygiene", "desc": "Rootless builds, distroless/minimal images, SBOMs, cache optimization with BuildKit"},
            {"name": "Registries", "desc": "Private registries, access control, image retention policies, and immutability"}
        ],
        "links": [
            {"name": "DevOps Roadmap", "url": "https://roadmap.sh/devops"},
            {"name": "DevOps PDF", "url": "https://roadmap.sh/pdfs/roadmaps/devops.pdf"}
        ],
        "other_resources": [
            {"name": "Docker Docs", "url": "https://docs.docker.com/"},
            {"name": "Chainguard Images", "url": "https://www.chainguard.dev/secure-images"}
        ]
    },
    {
        "title": "Cloud & Serverless",
        "description": "Choose AWS, Azure, or GCP as a primary provider; learn core compute, networking, storage, IAM, managed databases, and managed Kubernetes; complement with serverless patterns for event-driven workloads.",
        "points": [
            {"name": "Core Cloud Services", "desc": "VMs/containers, VPC/VNet, subnets, storage, IAM, managed DBs and K8s"},
            {"name": "Serverless & Edge", "desc": "AWS Lambda, Azure Functions, Cloudflare Workers, Vercel, Netlify"},
            {"name": "Accounts & Guardrails", "desc": "Multi-account/subscriptions, least privilege, budgets, tagging, cost visibility"}
        ],
        "links": [
            {"name": "DevOps PDF", "url": "https://roadmap.sh/pdfs/roadmaps/devops.pdf"},
            {"name": "How-To Guide", "url": "https://roadmap.sh/devops/how-to-become-devops-engineer"}
        ],
        "other_resources": [
            {"name": "AWS Well-Architected", "url": "https://aws.amazon.com/architecture/well-architected/"},
            {"name": "Google Cloud Architecture Center", "url": "https://cloud.google.com/architecture"}
        ]
    },
    {
        "title": "Infrastructure as Code",
        "description": "Express infrastructure declaratively with Terraform and cloud-native stacks; enforce reviews, testing, policy-as-code, and versioned, reproducible environments.",
        "points": [
            {"name": "Terraform", "desc": "State, backends, modules, workspaces, plans, drift detection, CI validation"},
            {"name": "Cloud-Native Stacks", "desc": "CloudFormation/CDK, ARM/Bicep, Deployment Manager, Pulumi"},
            {"name": "Policy & Testing", "desc": "OPA/Conftest, tfsec/checkov, Terragrunt patterns, integration tests"}
        ],
        "links": [
            {"name": "DevOps Roadmap", "url": "https://roadmap.sh/devops"},
            {"name": "DevOps PDF", "url": "https://roadmap.sh/pdfs/roadmaps/devops.pdf"}
        ],
        "other_resources": [
            {"name": "Terraform Docs", "url": "https://developer.hashicorp.com/terraform/docs"},
            {"name": "OPA (Open Policy Agent)", "url": "https://www.openpolicyagent.org/"}
        ]
    },
    {
        "title": "Configuration Management",
        "description": "Automate OS and application configuration, reduce drift, and standardize environments across stages with idempotent tooling and reusable roles.",
        "points": [
            {"name": "Ansible First", "desc": "Agentless provisioning with roles, inventories (static/dynamic), and idempotent playbooks"},
            {"name": "At Scale", "desc": "Chef or Puppet for policy-driven configuration and compliance"},
            {"name": "Secrets & Vaults", "desc": "Integrate secret backends and parameter stores into config runs"}
        ],
        "links": [
            {"name": "DevOps PDF", "url": "https://roadmap.sh/pdfs/roadmaps/devops.pdf"}
        ],
        "other_resources": [
            {"name": "Ansible Docs", "url": "https://docs.ansible.com/"},
            {"name": "Puppet Docs", "url": "https://www.puppet.com/docs"}
        ]
    },
    {
        "title": "CI/CD",
        "description": "Design resilient pipelines that build, test, scan, and deploy quickly with clear promotion paths, fast feedback, and safe rollbacks across environments.",
        "points": [
            {"name": "Pipeline Tools", "desc": "GitHub Actions, GitLab CI, Jenkins, CircleCI, Octopus Deploy, TeamCity"},
            {"name": "Standards", "desc": "Artifact promotion, environment gates, reproducible workflows, blue/green and canary"},
            {"name": "Performance & Quality", "desc": "Caching, matrix builds, parallelization, test flakiness control, release automation"}
        ],
        "links": [
            {"name": "DevOps PDF", "url": "https://roadmap.sh/pdfs/roadmaps/devops.pdf"}
        ],
        "other_resources": [
            {"name": "GitHub Actions Docs", "url": "https://docs.github.com/actions"},
            {"name": "GitLab CI/CD Docs", "url": "https://docs.gitlab.com/ee/ci/"}
        ]
    },
    {
        "title": "Secrets & Security",
        "description": "Centralize secret management, adopt least-privilege IAM, and secure the software supply chain by shifting left with scanning, SBOMs, and signed artifacts.",
        "points": [
            {"name": "Secret Stores", "desc": "Vault or SOPS + KMS; sealed-secrets for encrypted delivery to clusters"},
            {"name": "DevSecOps", "desc": "Image and dependency scanning, SAST/DAST, SBOM generation and policies"},
            {"name": "Identity & Signing", "desc": "OIDC federation to clouds, short-lived credentials, cosign/sigstore signing"}
        ],
        "links": [
            {"name": "DevOps Roadmap", "url": "https://roadmap.sh/devops"},
            {"name": "DevOps PDF", "url": "https://roadmap.sh/pdfs/roadmaps/devops.pdf"}
        ],
        "other_resources": [
            {"name": "Sigstore (cosign)", "url": "https://www.sigstore.dev/"},
            {"name": "SLSA Framework", "url": "https://slsa.dev/"}
        ]
    },
    {
        "title": "Observability & Logging",
        "description": "Instrument systems with metrics, logs, and traces; define SLIs/SLOs, alert on symptoms, and build dashboards for fast diagnosis and capacity planning.",
        "points": [
            {"name": "Metrics & Dashboards", "desc": "Prometheus, Grafana, cloud-native monitors; custom exporters and alerting"},
            {"name": "Logs & Traces", "desc": "Elastic/Graylog/Splunk, OpenTelemetry, Jaeger/New Relic for distributed tracing"},
            {"name": "Reliability Signals", "desc": "SLIs/SLOs, error budgets, blackbox probes, log retention and cost control"}
        ],
        "links": [
            {"name": "DevOps PDF", "url": "https://roadmap.sh/pdfs/roadmaps/devops.pdf"}
        ],
        "other_resources": [
            {"name": "OpenTelemetry", "url": "https://opentelemetry.io/"},
            {"name": "Prometheus Docs", "url": "https://prometheus.io/docs/introduction/overview/"}
        ]
    },
    {
        "title": "Kubernetes & GitOps",
        "description": "Operate workloads on managed Kubernetes (EKS/AKS/GKE) and use Git as the source of truth for declarative, pull-based deployments with auditable changes.",
        "points": [
            {"name": "Kubernetes Fundamentals", "desc": "Pods, Deployments, Services, HPA/VPA, Ingress, NetworkPolicy, StorageClasses"},
            {"name": "Packaging & Templating", "desc": "Helm/Helmfile or Kustomize; chart versioning and promotion strategies"},
            {"name": "GitOps", "desc": "Argo CD or Flux for pull-based reconciliation, multi-env and multi-cluster patterns"}
        ],
        "links": [
            {"name": "DevOps Roadmap", "url": "https://roadmap.sh/devops"},
            {"name": "DevOps PDF", "url": "https://roadmap.sh/pdfs/roadmaps/devops.pdf"}
        ],
        "other_resources": [
            {"name": "Kubernetes Docs", "url": "https://kubernetes.io/docs/home/"},
            {"name": "Argo CD Docs", "url": "https://argo-cd.readthedocs.io/en/stable/"}
        ]
    },
    {
        "title": "Service Mesh & Artifacts",
        "description": "Introduce a service mesh when microservice traffic policy, mTLS, observability, and reliability patterns are needed; manage artifacts centrally for traceable promotion.",
        "points": [
            {"name": "Service Mesh", "desc": "Istio, Linkerd, Consul, Envoy for mTLS, retries, timeouts, circuit-breaking, and telemetry"},
            {"name": "Artifact Repos", "desc": "Artifactory, Nexus, Cloudsmith; retention, provenance, and access policies"}
        ],
        "links": [
            {"name": "DevOps PDF", "url": "https://roadmap.sh/pdfs/roadmaps/devops.pdf"}
        ],
        "other_resources": [
            {"name": "Istio Docs", "url": "https://istio.io/latest/docs/"},
            {"name": "Sonatype Nexus", "url": "https://help.sonatype.com/repomanager3"}
        ]
    },
    {
        "title": "Cloud Patterns & Reliability",
        "description": "Apply cloud design patterns for availability, data, deployment, and monitoring to architect robust, scalable systems; integrate SRE practices to operate them reliably.",
        "points": [
            {"name": "Reliability Patterns", "desc": "Blue/green, canary, circuit breakers, retries with exponential backoff, bulkheads"},
            {"name": "SRE Practices", "desc": "SLIs/SLOs, incident response, on-call, postmortems, capacity planning, chaos experiments"},
            {"name": "Resilience & DR", "desc": "Backups, RPO/RTO targets, multi-AZ/region designs, failover and runbooks"}
        ],
        "links": [
            {"name": "DevOps Roadmap", "url": "https://roadmap.sh/devops"},
            {"name": "DevOps PDF", "url": "https://roadmap.sh/pdfs/roadmaps/devops.pdf"}
        ],
        "other_resources": [
            {"name": "Google SRE Book", "url": "https://sre.google/sre-book/table-of-contents/"},
            {"name": "AWS Architecture Patterns", "url": "https://aws.amazon.com/architecture/patterns/"}
        ]
    },
    {
        "title": "Projects & Portfolio",
        "description": "Demonstrate end-to-end delivery: containerize services, provision infra with code, deploy via GitOps to managed Kubernetes, instrument observability, and document decisions, SLIs/SLOs, and runbooks.",
        "points": [
            {"name": "E2E Delivery", "desc": "Containerized app with GitHub Actions/GitLab CI, Terraform infra, Helm on managed K8s, monitored with Prometheus/Grafana"},
            {"name": "Operational Docs", "desc": "Architecture decision records (ADRs), rollout strategies, incident playbooks, SLIs/SLOs dashboards"},
            {"name": "Security & Supply Chain", "desc": "Signed images, SBOMs, policy gates in CI/CD, environment promotions"}
        ],
        "links": [
            {"name": "How to Become DevOps Engineer", "url": "https://roadmap.sh/devops/how-to-become-devops-engineer"},
            {"name": "DevOps Skills", "url": "https://roadmap.sh/devops/skills"}
        ],
        "other_resources": [
            {"name": "Awesome DevOps Projects", "url": "https://roadmap.sh/devops/projects"},
            {"name": "ADR GitHub Template", "url": "https://github.com/joelparkerhenderson/architecture_decision_record"}
        ]
    },
    {
        "title": "Next Steps & Specializations",
        "description": "Go deeper on Docker, Kubernetes, cloud providers, platform engineering, security, and FinOps; practice interviews and scenario-based troubleshooting to match target roles.",
        "points": [
            {"name": "Focused Tracks", "desc": "Kubernetes, Docker, AWS/Azure/GCP, Security, Platform Engineering, FinOps"},
            {"name": "Interview Prep", "desc": "Hands-on labs, design scenarios, outage drills, cost/perf optimization challenges"}
        ],
        "links": [
            {"name": "Roadmaps Index", "url": "https://roadmap.sh/roadmaps"},
            {"name": "DevOps Interview Q&A", "url": "https://roadmap.sh/questions/devops"}
        ],
        "other_resources": [
            {"name": "Platform Engineering Community", "url": "https://platformengineering.org/"},
            {"name": "FinOps Foundation", "url": "https://www.finops.org/"}
        ]
    }
]

def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/devops_engineer.html", roadmap=DEVOPS_ENGINEER_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('devops_engineer'))

    @app.route("/devops_engineer")
    def devops_engineer():
        return render_page()

    app.run(debug=True)

from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory
BASE_DIR = Path(__file__).resolve().parent.parent  # Correct __file__
TEMPLATES_DIR = BASE_DIR / "templates"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))  # Correct __name__
CLOUD_ENGINEER_ROADMAP = [
    {
        "title": "Foundations of Cloud Computing",
        "description": "Build a strong foundation by thoroughly understanding the fundamentals of cloud computing. Learn why cloud computing is transforming IT infrastructure, how it compares to traditional on-premises systems, and the practical benefits it brings to organizations. Gain insights into deployment models, service models, and core technologies that form the backbone of modern cloud solutions, setting the stage for advanced cloud learning.",
        "points": [
            {"name": "Cloud Basics", "desc": "Learn the benefits, deployment models (public, private, hybrid), and differences from traditional computing."},
            {"name": "Service Models", "desc": "Understand IaaS, PaaS, SaaS with practical examples."},
            {"name": "Virtualization & Containers", "desc": "Learn VMs, Docker, and Kubernetes for scalable cloud applications."}
        ],
        "links": [
            {"name": "Intro to Cloud Computing (Coursera)", "url": "https://www.coursera.org/learn/introduction-to-cloud"},
            {"name": "Cloud Computing Basics (Udemy)", "url": "https://www.udemy.com/course/introduction-to-cloud-computing/"}
        ],
        "other_resources": [
            {"name": "AWS Cloud Overview", "url": "https://aws.amazon.com/what-is-cloud-computing/"},
            {"name": "Microsoft Learn Cloud Fundamentals", "url": "https://learn.microsoft.com/en-us/training/modules/cloud-computing-fundamentals/"}
        ]
    },
    {
        "title": "Major Cloud Platforms",
        "description": "Understand the leading cloud platforms—AWS, Azure, and Google Cloud—by exploring their core services, deployment capabilities, and pricing models. Gain a clear understanding of compute, storage, networking, and database services that power enterprise-scale applications. Learn how to navigate these platforms efficiently to build, deploy, and manage cloud-native applications.",
        "points": [
            {"name": "AWS", "desc": "EC2, S3, VPC, RDS/DynamoDB, pricing, global regions."},
            {"name": "Azure", "desc": "VMs, Azure Functions, Blob Storage, Cosmos DB, networking."},
            {"name": "Google Cloud", "desc": "Compute Engine, Cloud Functions, BigQuery, GKE."}
        ],
        "links": [
            {"name": "AWS Training and Certification", "url": "https://aws.amazon.com/training/"},
            {"name": "Microsoft Azure Learning Paths", "url": "https://learn.microsoft.com/en-us/training/azure/"},
            {"name": "Google Cloud Training", "url": "https://cloud.google.com/training"}
        ],
        "other_resources": [
            {"name": "A Cloud Guru", "url": "https://acloudguru.com/"},
            {"name": "Cloud Academy", "url": "https://cloudacademy.com/"}
        ]
    },
    {
        "title": "Cloud Networking & Security",
        "description": "Learn to design secure and robust cloud architectures by mastering networking concepts, access management, and security best practices. Gain knowledge about virtual networks, routing, security controls, and compliance requirements to protect cloud workloads and data. Understand how networking and security integrate into cloud solutions to maintain high availability and protect against potential threats.",
        "points": [
            {"name": "Cloud Networking", "desc": "VPCs, subnets, load balancers, DNS, CDNs."},
            {"name": "IAM & Access Control", "desc": "Roles, policies, and multi-factor authentication."},
            {"name": "Cloud Security Best Practices", "desc": "Encryption, firewalls, key management, compliance, monitoring."}
        ],
        "links": [
            {"name": "Cloud Security Basics (Coursera)", "url": "https://www.coursera.org/learn/cloud-security-basics"}
        ],
        "other_resources": [
            {"name": "OWASP Cloud Security", "url": "https://owasp.org/www-project-cloud-security/"},
            {"name": "AWS Security Best Practices", "url": "https://aws.amazon.com/architecture/security-best-practices/"}
        ]
    },
    {
        "title": "Infrastructure as Code & Automation",
        "description": "Learn how to provision, manage, and scale cloud infrastructure programmatically. Embrace automation through Infrastructure as Code (IaC) to deploy resources consistently and reliably. Understand CI/CD pipelines, monitoring, logging, and automated workflows to maintain high-performing cloud environments while reducing manual errors.",
        "points": [
            {"name": "Infrastructure as Code", "desc": "Terraform, CloudFormation, Azure ARM templates."},
            {"name": "CI/CD Pipelines", "desc": "Jenkins, GitHub Actions, GitLab CI for automated deployment."},
            {"name": "Monitoring & Logging", "desc": "CloudWatch, Azure Monitor, Stackdriver for performance and issue detection."}
        ],
        "links": [
            {"name": "Terraform Getting Started", "url": "https://learn.hashicorp.com/terraform"},
            {"name": "CI/CD with GitHub Actions", "url": "https://docs.github.com/en/actions"}
        ],
        "other_resources": [
            {"name": "Jenkins Documentation", "url": "https://www.jenkins.io/doc/"},
            {"name": "Azure DevOps Pipelines", "url": "https://learn.microsoft.com/en-us/azure/devops/pipelines/?view=azure-devops"}
        ]
    },
    {
        "title": "Cloud Databases & Data Services",
        "description": "Gain expertise in cloud-native data storage and processing solutions, enabling efficient handling of structured, semi-structured, and unstructured data. Understand the differences between relational and NoSQL databases, and explore data analytics tools and big data processing frameworks to derive meaningful insights from massive datasets in the cloud.",
        "points": [
            {"name": "Relational Databases", "desc": "AWS RDS, Azure SQL, Cloud SQL for structured data."},
            {"name": "NoSQL Databases", "desc": "DynamoDB, Cosmos DB, Firestore for scalable, flexible storage."},
            {"name": "Big Data & Analytics", "desc": "EMR, BigQuery, and data lakes for analytics and insights."}
        ],
        "links": [
            {"name": "AWS Database Services Overview", "url": "https://aws.amazon.com/products/databases/"},
            {"name": "Azure Data Services", "url": "https://azure.microsoft.com/en-us/overview/data-platform/"}
        ],
        "other_resources": [
            {"name": "Google Cloud Big Data", "url": "https://cloud.google.com/products/big-data"},
            {"name": "Data Engineering on Cloud", "url": "https://www.coursera.org/specializations/data-engineering-gcp"}
        ]
    },
    {
        "title": "Serverless & Event-Driven Architectures",
        "description": "Learn to design applications that scale automatically without managing underlying servers. Understand event-driven design patterns, messaging services, and orchestration of serverless functions to build highly responsive and cost-efficient cloud applications suitable for modern enterprise and startup needs.",
        "points": [
            {"name": "Serverless Computing", "desc": "AWS Lambda, Azure Functions, GCP Cloud Functions."},
            {"name": "Event-Driven Design", "desc": "Use messaging queues, event sources, and triggers for decoupled applications."},
            {"name": "Function Orchestration", "desc": "Coordinate serverless functions for workflows using Step Functions or Durable Functions."}
        ],
        "links": [
            {"name": "AWS Lambda Guide", "url": "https://docs.aws.amazon.com/lambda/"},
            {"name": "Azure Functions Docs", "url": "https://learn.microsoft.com/en-us/azure/azure-functions/"}
        ],
        "other_resources": [
            {"name": "Serverless Framework", "url": "https://www.serverless.com/"},
            {"name": "Event-Driven Architectures", "url": "https://martinfowler.com/articles/201701-event-driven.html"}
        ]
    },
    {
        "title": "Cloud DevOps & Automation",
        "description": "Integrate DevOps practices into cloud operations for faster, reliable, and repeatable deployments. Learn how to automate build, test, deployment, and monitoring processes to improve productivity, reduce downtime, and ensure continuous delivery of high-quality cloud applications.",
        "points": [
            {"name": "CI/CD Pipelines", "desc": "Automate build, test, and deployment processes."},
            {"name": "Infrastructure Automation", "desc": "Automate provisioning, configuration, and updates."},
            {"name": "Monitoring & Alerting", "desc": "Proactively detect issues and optimize cloud performance."}
        ],
        "links": [
            {"name": "DevOps on AWS", "url": "https://aws.amazon.com/devops/"},
            {"name": "Azure DevOps Overview", "url": "https://azure.microsoft.com/en-us/services/devops/"}
        ],
        "other_resources": [
            {"name": "Google Cloud DevOps Tools", "url": "https://cloud.google.com/products/devops"}
        ]
    },
    {
        "title": "Cloud Architecture & Design Patterns",
        "description": "Learn to design scalable, resilient, and cost-efficient cloud systems. Explore architectural best practices, microservices, high availability, and disaster recovery strategies. Understand how to optimize resources for cost and performance while ensuring maintainability and security across cloud deployments.",
        "points": [
            {"name": "Microservices", "desc": "Break applications into independent, loosely coupled services."},
            {"name": "High Availability & Resilience", "desc": "Multi-region deployments, failover, disaster recovery."},
            {"name": "Cost Optimization", "desc": "Right-sizing resources, reserved instances, monitoring usage."}
        ],
        "links": [
            {"name": "AWS Well-Architected Framework", "url": "https://aws.amazon.com/architecture/well-architected/"},
            {"name": "Azure Architecture Guide", "url": "https://learn.microsoft.com/en-us/azure/architecture/"}
        ],
        "other_resources": [
            {"name": "Google Cloud Architecture Framework", "url": "https://cloud.google.com/architecture/framework"}
        ]
    },
    {
        "title": "Containerization & Orchestration",
        "description": "Master container-based application deployment to enable consistency, scalability, and simplified maintenance. Learn orchestration using Kubernetes and related technologies to manage containerized applications in production, ensuring observability, reliability, and automation across environments.",
        "points": [
            {"name": "Docker", "desc": "Package applications into portable containers."},
            {"name": "Kubernetes", "desc": "Orchestrate container deployments, scaling, and management."},
            {"name": "Service Mesh & Observability", "desc": "Monitor containerized apps using Istio, Prometheus, and Grafana."}
        ],
        "links": [
            {"name": "Docker Docs", "url": "https://docs.docker.com/"},
            {"name": "Kubernetes Documentation", "url": "https://kubernetes.io/docs/"}
        ],
        "other_resources": [
            {"name": "Prometheus Monitoring", "url": "https://prometheus.io/docs/introduction/overview/"},
            {"name": "Istio Service Mesh", "url": "https://istio.io/latest/docs/"}
        ]
    },
    {
        "title": "Cloud Security & Compliance",
        "description": "Protect cloud workloads, ensure data security, and comply with industry regulations. Understand security best practices, cloud-native security tools, compliance standards, and threat detection mechanisms to maintain a secure and compliant cloud environment.",
        "points": [
            {"name": "Security Best Practices", "desc": "IAM policies, encryption, VPC security, network segmentation."},
            {"name": "Compliance Standards", "desc": "ISO 27001, SOC 2, GDPR, HIPAA adherence."},
            {"name": "Monitoring & Threat Detection", "desc": "Cloud-native security tools and logging for anomaly detection."}
        ],
        "links": [
            {"name": "AWS Security Best Practices", "url": "https://aws.amazon.com/architecture/security-best-practices/"},
            {"name": "Azure Security Documentation", "url": "https://learn.microsoft.com/en-us/azure/security/"}
        ],
        "other_resources": [
            {"name": "Cloud Security Alliance", "url": "https://cloudsecurityalliance.org/"}
        ]
    },
    {
        "title": "Hybrid & Multi-Cloud Strategies",
        "description": "Learn to design cloud solutions that integrate multiple cloud providers and on-premises infrastructure. Understand hybrid cloud networking, multi-cloud management, security, and orchestration to optimize flexibility, reliability, and cost across complex IT landscapes.",
        "points": [
            {"name": "Hybrid Cloud", "desc": "Integrate on-premises infrastructure with cloud resources."},
            {"name": "Multi-Cloud Management", "desc": "Use tools and strategies to manage workloads across providers."},
            {"name": "Networking & Security", "desc": "Ensure secure and performant communication between clouds."}
        ],
        "links": [
            {"name": "Hybrid Cloud Solutions", "url": "https://azure.microsoft.com/en-us/overview/hybrid-cloud/"},
            {"name": "Multi-Cloud Strategies", "url": "https://cloud.google.com/multi-cloud"}
        ],
        "other_resources": [
            {"name": "VMware Multi-Cloud", "url": "https://www.vmware.com/solutions/multi-cloud.html"}
        ]
    },
    {
        "title": "Emerging Cloud Technologies",
        "description": "Stay updated with evolving cloud-native technologies such as AI/ML services, edge computing, IoT integrations, and serverless advancements. Understand new tools and patterns that enhance cloud application performance, scalability, and automation.",
        "points": [
            {"name": "AI/ML in Cloud", "desc": "Use managed AI/ML services for analytics, predictions, and automation."},
            {"name": "Edge & IoT Cloud", "desc": "Integrate cloud with edge devices and IoT networks."},
            {"name": "Serverless & Event-Driven Advances", "desc": "Adopt new patterns for scalable, event-driven workloads."}
        ],
        "links": [
            {"name": "AI/ML Cloud Services", "url": "https://aws.amazon.com/machine-learning/"},
            {"name": "IoT Cloud Integration", "url": "https://azure.microsoft.com/en-us/overview/iot/"}
        ],
        "other_resources": [
            {"name": "Google Cloud AI", "url": "https://cloud.google.com/products/ai"}
        ]
    },
    {
        "title": "Certifications & Continuous Learning",
        "description": "Validate cloud skills and stay up-to-date with industry best practices.",
        "points": [
            {"name": "AWS Certifications", "desc": "Cloud Practitioner, Solutions Architect, SysOps Administrator."},
            {"name": "Azure Certifications", "desc": "AZ-900, AZ-104, AZ-305 for cloud proficiency."},
            {"name": "Google Cloud Certifications", "desc": "Associate Cloud Engineer, Professional Cloud Architect."},
            {"name": "Continuous Learning", "desc": "Follow cloud blogs, community updates, labs, and hands-on projects."}
        ],
        "links": [
            {"name": "AWS Training & Certification", "url": "https://aws.amazon.com/training/"},
            {"name": "Microsoft Learn", "url": "https://learn.microsoft.com/en-us/training/"},
            {"name": "Google Cloud Training", "url": "https://cloud.google.com/training"}
        ],
        "other_resources": [
            {"name": "Cloud Academy", "url": "https://cloudacademy.com/"},
            {"name": "A Cloud Guru", "url": "https://acloudguru.com/"},
            {"name": "Medium Cloud Blogs", "url": "https://medium.com/tag/cloud-computing"}
        ]
    }
]
def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/cloud_engineer.html", roadmap= CLOUD_ENGINEER_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('cloud_engineer'))

    @app.route("/cloud_engineer")
    def cloud_engineer():
        return render_page()

    app.run(debug=True)
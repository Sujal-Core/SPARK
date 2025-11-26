from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory
BASE_DIR = Path(__file__).resolve().parent.parent  # Correct __file__
TEMPLATES_DIR = BASE_DIR / "templates"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))  # Correct __name__
MLOps_Roadmap= [
    {
        "title": "Programming Foundations",
        "description": "Establish a strong foundation in programming, which is essential for implementing and automating machine learning pipelines. This stage focuses on mastering Python, the dominant language in ML and MLOps, for tasks ranging from data manipulation and model development to automation scripts. Additionally, shell scripting with Bash is introduced to handle task automation and system-level operations efficiently. Version control with Git and GitHub ensures collaborative workflows, reproducibility, and proper tracking of code changes, which are crucial in professional MLOps environments.",
        "points": [
            {"name": "Python", "desc": "Learn Python for data manipulation, ML model development, and automation."},
            {"name": "Bash", "desc": "Understand shell scripting for task automation and system management."},
            {"name": "Version Control", "desc": "Use Git and GitHub for code collaboration and version tracking."}
        ],
        "links": [
            {"name": "Python Official Documentation", "url": "https://docs.python.org/3/"},
            {"name": "Git Handbook", "url": "https://guides.github.com/introduction/git-handbook/"}
        ],
        "other_resources": [
            {"name": "Automate the Boring Stuff with Python", "url": "https://automatetheboringstuff.com/"},
            {"name": "Bash Scripting Tutorial", "url": "https://www.tutorialspoint.com/unix/shell_scripting.htm"}
        ]
    },
    {
        "title": "DevOps & Cloud Platforms",
        "description": "Gain comprehensive knowledge of cloud computing and DevOps practices, which are critical for deploying, managing, and scaling ML solutions. This stage emphasizes understanding cloud providers such as AWS, Azure, and GCP, setting up infrastructure for machine learning workflows, and automating deployment pipelines. Continuous Integration and Continuous Deployment (CI/CD) principles are covered to ensure rapid, reliable, and repeatable delivery of ML models. Infrastructure as Code (IaC) tools like Terraform and CloudFormation help automate cloud provisioning, enabling scalable and maintainable MLOps systems.",
        "points": [
            {"name": "Cloud Providers", "desc": "Familiarize with AWS, Azure, or GCP for cloud infrastructure."},
            {"name": "CI/CD Pipelines", "desc": "Implement continuous integration and deployment using tools like Jenkins or GitHub Actions."},
            {"name": "Infrastructure as Code", "desc": "Use Terraform or CloudFormation for automating infrastructure provisioning."}
        ],
        "links": [
            {"name": "AWS Training and Certification", "url": "https://aws.amazon.com/training/"},
            {"name": "Terraform Documentation", "url": "https://www.terraform.io/docs"}
        ],
        "other_resources": [
            {"name": "Azure DevOps Documentation", "url": "https://learn.microsoft.com/en-us/azure/devops/?view=azure-devops"},
            {"name": "Google Cloud Training", "url": "https://cloud.google.com/training"}
        ]
    },
    {
        "title": "Containerization & Orchestration",
        "description": "Learn to package, deploy, and manage machine learning applications using containerization and orchestration technologies. Containers, such as Docker, allow you to bundle applications with all dependencies, ensuring consistency across development, testing, and production environments. Kubernetes is introduced to orchestrate these containers at scale, managing deployment, scaling, and maintenance. Helm charts simplify application management on Kubernetes, enabling reproducible deployments and better lifecycle management. This stage ensures MLOps engineers can efficiently deploy scalable and reliable ML services.",
        "points": [
            {"name": "Docker", "desc": "Package applications and dependencies into containers for consistency."},
            {"name": "Kubernetes", "desc": "Orchestrate containerized applications for scalability and management."},
            {"name": "Helm", "desc": "Manage Kubernetes applications using Helm charts."}
        ],
        "links": [
            {"name": "Docker Documentation", "url": "https://docs.docker.com/"},
            {"name": "Kubernetes Documentation", "url": "https://kubernetes.io/docs/"}
        ],
        "other_resources": [
            {"name": "Docker Mastery Course", "url": "https://www.udemy.com/course/docker-mastery/"},
            {"name": "Kubernetes for Developers", "url": "https://www.udemy.com/course/kubernetes-for-developers/"}
        ]
    },
    {
        "title": "Machine Learning Fundamentals",
        "description": "Acquire a solid understanding of core machine learning concepts and algorithms, which are fundamental to any MLOps workflow. This stage covers supervised and unsupervised learning techniques, providing the knowledge needed to build, evaluate, and optimize ML models. Understanding model evaluation metrics and validation techniques is crucial for monitoring model performance in production. This foundation ensures MLOps engineers can collaborate effectively with data scientists and support deployment of robust ML models.",
        "points": [
            {"name": "Supervised Learning", "desc": "Understand algorithms like linear regression and decision trees."},
            {"name": "Unsupervised Learning", "desc": "Explore clustering and dimensionality reduction techniques."},
            {"name": "Model Evaluation", "desc": "Learn metrics such as accuracy, precision, recall, and F1-score."}
        ],
        "links": [
            {"name": "Scikit-learn Documentation", "url": "https://scikit-learn.org/stable/documentation.html"},
            {"name": "Machine Learning Crash Course", "url": "https://developers.google.com/machine-learning/crash-course"}
        ],
        "other_resources": [
            {"name": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", "url": "https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/"},
            {"name": "Deep Learning Specialization", "url": "https://www.coursera.org/specializations/deep-learning"}
        ]
    },
    {
        "title": "MLOps Principles",
        "description": "Understand the core principles and best practices of MLOps, bridging the gap between model development and production deployment. This stage focuses on collaboration between data science and operations teams, automating workflows for model training, testing, and deployment, and establishing monitoring systems to track model performance and detect data drift. Adhering to these principles ensures that ML models are scalable, reliable, and maintainable in real-world applications.",
        "points": [
            {"name": "Collaboration", "desc": "Foster collaboration between data scientists and operations teams."},
            {"name": "Automation", "desc": "Automate workflows for model training, testing, and deployment."},
            {"name": "Monitoring", "desc": "Implement monitoring for model performance and data drift."}
        ],
        "links": [
            {"name": "MLOps: Continuous Delivery and Automation Pipelines in Machine Learning", "url": "https://www.oreilly.com/library/view/mlops-continuous-delivery/9781098116748/"},
            {"name": "MLOps Community", "url": "https://mlops.community/"}
        ],
        "other_resources": [
            {"name": "MLflow Documentation", "url": "https://mlflow.org/docs/latest/index.html"},
            {"name": "Kubeflow Documentation", "url": "https://www.kubeflow.org/docs/"}
        ]
    },
    {
        "title": "Model Deployment & Serving",
        "description": "Learn to deploy and serve machine learning models efficiently in production environments. This stage includes saving models in standardized formats such as Pickle or ONNX, using model serving platforms like TensorFlow Serving or TorchServe, and creating REST APIs with Flask or FastAPI to allow external applications to access predictions. Proper deployment strategies ensure model reliability, scalability, and maintainability.",
        "points": [
            {"name": "Model Serialization", "desc": "Save models using formats like Pickle or ONNX."},
            {"name": "Model Serving", "desc": "Use tools like TensorFlow Serving or TorchServe for serving models."},
            {"name": "API Development", "desc": "Develop REST APIs for model inference using Flask or FastAPI."}
        ],
        "links": [
            {"name": "TensorFlow Serving", "url": "https://www.tensorflow.org/tfx/guide/serving"},
            {"name": "FastAPI Documentation", "url": "https://fastapi.tiangolo.com/"}
        ],
        "other_resources": [
            {"name": "Model Deployment with Flask", "url": "https://www.udemy.com/course/model-deployment-with-flask/"},
            {"name": "Deploying Machine Learning Models", "url": "https://www.coursera.org/learn/deploying-machine-learning-models"}
        ]
    },
    {
        "title": "Monitoring & Maintenance",
        "description": "Ensure ML models remain reliable and accurate in production by implementing monitoring and maintenance strategies. This stage covers tracking system metrics such as latency and error rates, detecting data drift to identify when input distributions change, and automating retraining pipelines to update models as needed. Effective monitoring and maintenance are critical for sustaining high-performance MLOps systems and preventing model degradation over time.",
        "points": [
            {"name": "Model Monitoring", "desc": "Track metrics like latency, throughput, and error rates."},
            {"name": "Data Drift Detection", "desc": "Identify changes in data distribution over time."},
            {"name": "Model Retraining", "desc": "Automate retraining pipelines to update models as needed."}
        ],
        "links": [
            {"name": "Evidently AI", "url": "https://evidentlyai.com/"},
            {"name": "Model Monitoring with Prometheus", "url": "https://www.prometheus.io/docs/introduction/overview/"}
        ],
        "other_resources": [
            {"name": "Continuous Machine Learning", "url": "https://www.oreilly.com/library/view/continuous-machine-learning/9781098116748/"},
            {"name": "Kubeflow Pipelines", "url": "https://www.kubeflow.org/docs/pipelines/"}
        ]
    },
    {
        "title": "Security & Compliance",
        "description": "Ensure MLOps practices adhere to security and regulatory standards. This stage focuses on implementing encryption for data at rest and in transit, managing access control using IAM roles and policies, and complying with regulatory frameworks such as GDPR and HIPAA. Security and compliance are vital to protect sensitive data, maintain trust, and ensure that ML systems are legally and ethically responsible.",
        "points": [
            {"name": "Data Encryption", "desc": "Implement encryption for data at rest and in transit."},
            {"name": "Access Control", "desc": "Use IAM roles and policies to control access."},
            {"name": "Compliance Standards", "desc": "Adhere to standards like GDPR and HIPAA."}
        ],
        "links": [
            {"name": "OWASP Machine Learning Security", "url": "https://owasp.org/www-project-machine-learning-security/"},
            {"name": "GDPR Compliance Guide", "url": "https://gdpr.eu/what-is-gdpr/"}
        ],
        "other_resources": [
            {"name": "Data Privacy and Security in Machine Learning", "url": "https://www.coursera.org/learn/data-privacy-machine-learning"},
            {"name": "HIPAA Compliance for Cloud Services", "url": "https://aws.amazon.com/compliance/hipaa-compliance/"}
        ]
    },
    {
        "title": "Collaboration & Communication",
        "description": "Develop effective collaboration and communication skills to work successfully in MLOps teams. This stage emphasizes maintaining clear documentation, communicating project progress and results to both technical and non-technical stakeholders, and implementing agile practices in workflows. Strong collaboration ensures smooth integration of ML solutions into production and fosters a productive team environment.",
        "points": [
            {"name": "Documentation", "desc": "Maintain clear and comprehensive documentation."},
            {"name": "Stakeholder Communication", "desc": "Communicate effectively with non-technical stakeholders."},
            {"name": "Agile Practices", "desc": "Implement agile methodologies in MLOps workflows."}
        ],
        "links": [
            {"name": "Agile Methodology Guide", "url": "https://www.agilealliance.org/agile101/"},
            {"name": "Effective Communication Skills", "url": "https://www.coursera.org/learn/wharton-communication-skills"}
        ],
        "other_resources": [
            {"name": "Documentation Best Practices", "url": "https://www.oreilly.com/library/view/documentation-standards/9781491945077/"},
            {"name": "Team Collaboration Tools", "url": "https://slack.com/features/collaboration"}
        ]
    },
    {
        "title": "Real-World Projects",
        "description": "Apply the skills and knowledge gained in MLOps to hands-on projects. This stage focuses on selecting industry-relevant projects, managing code versions with Git, and maintaining thorough documentation throughout the project lifecycle. Practical experience solidifies theoretical knowledge, enhances problem-solving abilities, and builds a strong portfolio that showcases expertise in end-to-end MLOps pipelines.",
        "points": [
            {"name": "Project Selection", "desc": "Choose projects that align with industry needs."},
            {"name": "Version Control", "desc": "Use Git for code management."},
            {"name": "Documentation", "desc": "Document the project lifecycle and outcomes."}
        ],
        "links": [
            {"name": "Kaggle Competitions", "url": "https://www.kaggle.com/competitions"},
            {"name": "GitHub Projects", "url": "https://github.com/topics/mlops"}
        ]
    },
    {
        "title": "Continuous Learning & Industry Trends",
        "description": "Stay updated with the rapidly evolving MLOps landscape by exploring new tools, frameworks, and best practices. Regularly reviewing research papers, industry blogs, and attending conferences ensures that you remain proficient and competitive. Continuous learning enables MLOps engineers to adapt to emerging challenges, adopt innovative techniques, and maintain high standards in building, deploying, and monitoring machine learning systems.",
        "points": [
            {"name": "Latest MLOps Tools", "desc": "Explore new tools for automation, monitoring, deployment, and orchestration."},
            {"name": "Research Papers & Blogs", "desc": "Follow publications, ArXiv papers, and blogs from industry leaders."},
            {"name": "Community Engagement", "desc": "Join MLOps forums, conferences, and online communities to learn and share knowledge."}
        ],
        "links": [
            {"name": "MLOps Community", "url": "https://mlops.community/"},
            {"name": "ArXiv MLOps Papers", "url": "https://arxiv.org/list/cs.LG/recent"}
        ],
        "other_resources": [
            {"name": "Towards Data Science - MLOps Articles", "url": "https://towardsdatascience.com/tagged/mlops"},
            {"name": "O'Reilly Continuous Machine Learning", "url": "https://www.oreilly.com/library/view/continuous-machine-learning/9781098116748/"}
        ]
    }
]
     


def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/mlops.html", roadmap=MLOps_Roadmap)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('mlops_engineer'))

    @app.route("/mlops_engineer")
    def mlops_engineer():
        return render_page()

    app.run(debug=True)
from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory
BASE_DIR = Path(__file__).resolve().parent.parent  # Correct __file__
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))  # Correct __name__
ETHICAL_AI_ENGINEER_ROADMAP = [
   {
        "title": "Foundations of AI & Ethics",
        "description": "Begin your journey by understanding the fundamental concepts of artificial intelligence alongside the ethical principles that guide responsible AI development. This stage ensures that you not only grasp the technical mechanisms of AI, including machine learning types such as supervised, unsupervised, and reinforcement learning, but also appreciate the importance of designing AI systems that are fair, transparent, accountable, and socially responsible. Learning these foundations will help you make informed decisions and set a strong ethical framework for all future AI projects, minimizing risks and maximizing positive societal impact.",
        "points": [
            {"name": "AI Basics", "desc": "Covers machine learning types (supervised, unsupervised, reinforcement learning) and how AI systems learn patterns and make predictions."},
            {"name": "Ethical AI Principles", "desc": "Core concepts of fairness, accountability, transparency, and responsibility (FATR) for safe and inclusive AI."},
            {"name": "Responsible AI Frameworks", "desc": "Overview of global frameworks like EU AI Act, OECD principles, and UNESCO ethics guidelines."}
        ],
        "links": [
            {"name": "AI For Everyone (Coursera)", "url": "https://www.coursera.org/learn/ai-for-everyone"},
            {"name": "Ethics of AI (edX)", "url": "https://online-learning.harvard.edu/course/ethics-artificial-intelligence"}
        ],
        "other_resources": [
            {"name": "OECD AI Principles", "url": "https://oecd.ai/en/ai-principles"},
            {"name": "UNESCO AI Ethics Framework", "url": "https://unesdoc.unesco.org/ark:/48223/pf0000381137"}
        ]
    },
    {
        "title": "Fairness & Bias Mitigation",
        "description": "Learn to identify, measure, and mitigate bias in AI systems to ensure equitable outcomes for all users. Bias can arise from historical data, sampling methods, or the way models are trained, and if left unchecked, can perpetuate inequalities. This stage focuses on understanding the sources of bias, selecting appropriate fairness metrics such as demographic parity, equalized odds, or predictive parity, and applying mitigation techniques across pre-processing, in-processing, and post-processing stages. Developing these skills will enable you to create AI systems that are more inclusive, reliable, and socially responsible.",
        "points": [
            {"name": "Sources of Bias", "desc": "Data bias, sampling bias, and measurement bias that impact AI fairness."},
            {"name": "Fairness Metrics", "desc": "Metrics like demographic parity, equalized odds, and predictive parity to evaluate fairness."},
            {"name": "Bias Mitigation Techniques", "desc": "Pre-processing (balancing datasets), in-processing (fairness constraints), and post-processing (adjusting predictions)."}
        ],
        "links": [
            {"name": "Fairness in AI (Coursera)", "url": "https://www.coursera.org/learn/fairness-in-ai"},
            {"name": "Responsible AI with Fairlearn", "url": "https://learn.microsoft.com/en-us/ai/responsible-ai/"}
        ],
        "other_resources": [
            {"name": "IBM AI Fairness 360 Toolkit", "url": "https://aif360.mybluemix.net/"},
            {"name": "Microsoft Fairlearn", "url": "https://fairlearn.org/"}
        ]
    },
    {
        "title": "Explainable AI (XAI)",
        "description": "Transparency is a cornerstone of ethical AI. This stage teaches how to make AI models interpretable for both technical and non-technical stakeholders. You will learn about global model explanations, which provide insight into overall model behavior, and local explanations that clarify individual predictions. Using tools like SHAP, LIME, and Captum, you can visualize feature importance, detect unexpected model behavior, and communicate results effectively. Emphasizing human-centered AI ensures that users trust the system, regulators can audit it, and organizations can deploy AI responsibly in sensitive domains.",
        "points": [
            {"name": "Model Explainability", "desc": "Global explanations for models vs. local explanations for individual predictions."},
            {"name": "XAI Tools", "desc": "Use SHAP, LIME, Captum, and other interpretability tools."},
            {"name": "Human-Centered AI", "desc": "Design AI that users can understand and trust."}
        ],
        "links": [
            {"name": "Explainable AI with Python (Udemy)", "url": "https://www.udemy.com/course/explainable-ai-with-python/"},
            {"name": "Interpretable Machine Learning (Coursera)", "url": "https://www.coursera.org/learn/interpretable-machine-learning"}
        ],
        "other_resources": [
            {"name": "SHAP Documentation", "url": "https://shap.readthedocs.io/en/latest/"},
            {"name": "LIME GitHub", "url": "https://github.com/marcotcr/lime"}
        ]
    },
    {
        "title": "Data Privacy & Security",
        "description": "Protecting sensitive data is essential for ethical AI practices. This stage covers legal, technical, and procedural safeguards to maintain user privacy and comply with regulations like GDPR, HIPAA, and CCPA. You will explore privacy-preserving machine learning techniques, including differential privacy, federated learning, and homomorphic encryption, which allow AI models to learn without exposing individual data. Additionally, you will learn to secure data pipelines through encryption, anonymization, and secure storage strategies, ensuring that user trust and compliance standards are maintained throughout the AI lifecycle.",
        "points": [
            {"name": "Privacy Laws", "desc": "Understand GDPR, HIPAA, and CCPA."},
            {"name": "Privacy-Preserving ML", "desc": "Differential privacy, federated learning, and homomorphic encryption."},
            {"name": "Data Security", "desc": "Techniques for encryption, anonymization, and secure data pipelines."}
        ],
        "links": [
            {"name": "Data Privacy Fundamentals (Coursera)", "url": "https://www.coursera.org/learn/data-privacy"},
            {"name": "Privacy in AI (FutureLearn)", "url": "https://www.futurelearn.com/courses/privacy-in-ai"}
        ],
        "other_resources": [
            {"name": "NIST Privacy Framework", "url": "https://www.nist.gov/privacy-framework"},
            {"name": "OpenMined Resources", "url": "https://www.openmined.org/"}
        ]
    },
    {
        "title": "Adversarial Robustness & Security",
        "description": "AI systems can be vulnerable to intentional manipulations or adversarial attacks, which may compromise reliability, fairness, and safety. In this stage, you will learn to identify and defend against evasion attacks like FGSM and PGD, data poisoning, and model inversion. You will also develop skills in designing robust architectures, applying adversarial training, and implementing input sanitization. Understanding secure deployment practices, monitoring systems for anomalies, and promptly patching vulnerabilities are essential to maintain trustworthy AI in production and prevent exploitation by malicious actors.",
        "points": [
            {"name": "Adversarial Attacks", "desc": "Evasion attacks (FGSM, PGD), data poisoning, and model inversion."},
            {"name": "Defense Mechanisms", "desc": "Adversarial training, input sanitization, robust architectures."},
            {"name": "Secure Deployment", "desc": "Monitoring, anomaly detection, patching vulnerabilities."}
        ],
        "links": [
            {"name": "Adversarial ML (Udemy)", "url": "https://www.udemy.com/course/adversarial-machine-learning/"},
            {"name": "Robust AI (Coursera)", "url": "https://www.coursera.org/learn/robust-ai"}
        ],
        "other_resources": [
            {"name": "CleverHans Library", "url": "https://github.com/cleverhans-lab/cleverhans"},
            {"name": "IBM ART Toolbox", "url": "https://github.com/Trusted-AI/adversarial-robustness-toolbox"}
        ]
    },
    {
        "title": "Governance, Risk & Compliance",
        "description": "Ethical AI requires structured governance, rigorous risk management, and adherence to compliance standards. You will learn how to establish accountability frameworks, oversee AI operations, and implement decision-making protocols. Risk management skills involve identifying potential harms, assessing their impact, and mitigating them proactively. Compliance includes documenting AI processes, conducting audits, and ensuring adherence to global regulations such as the EU AI Act and OECD guidelines. Mastering these practices will ensure that AI deployments are legally sound, ethically responsible, and socially beneficial.",
        "points": [
            {"name": "AI Governance", "desc": "Frameworks for accountability, oversight, and decision-making."},
            {"name": "Risk Management", "desc": "Identify, measure, and mitigate risks of AI deployments."},
            {"name": "Compliance", "desc": "Documentation, audits, and adherence to AI regulations."}
        ],
        "links": [
            {"name": "AI Governance Guide (World Economic Forum)", "url": "https://www.weforum.org/reports/global-ai-action-alliance"},
            {"name": "OECD Responsible AI", "url": "https://oecd.ai/en/ai-principles"}
        ],
        "other_resources": [
            {"name": "NIST AI Risk Management Framework", "url": "https://www.nist.gov/itl/ai-risk-management-framework"},
            {"name": "EU AI Act Resources", "url": "https://artificialintelligenceact.eu/"}
        ]
    },
    {
        "title": "Soft Skills & Advocacy",
        "description": "Being an ethical AI engineer also involves strong communication, collaboration, and advocacy skills. Learn how to effectively articulate ethical considerations, balance innovation with responsibility, and communicate technical insights to non-technical stakeholders and policymakers. Participate in cross-disciplinary discussions, promote awareness of responsible AI practices, and advocate for inclusive, fair, and transparent AI within organizations. These soft skills are crucial for shaping organizational culture, influencing decision-making, and ensuring AI projects align with ethical standards.",
        "points": [
            {"name": "Ethical Reasoning", "desc": "Balance innovation and responsibility."},
            {"name": "Stakeholder Communication", "desc": "Bridge the gap between technical experts and policymakers."},
            {"name": "Advocacy", "desc": "Promote responsible AI adoption across organizations."}
        ],
        "links": [
            {"name": "AI Ethics: Global Perspectives (edX)", "url": "https://www.edx.org/course/ethics-of-ai-global-perspectives"},
            {"name": "Communication in AI (Coursera)", "url": "https://www.coursera.org/learn/communication-in-ai"}
        ],
        "other_resources": [
            {"name": "Partnership on AI", "url": "https://partnershiponai.org/"},
            {"name": "AI Now Institute Reports", "url": "https://ainowinstitute.org/reports.html"}
        ]
    },
    {
        "title": "Continuous Learning & Certifications",
        "description": "The field of ethical AI is constantly evolving with new research, technologies, and regulations. Stay current by pursuing certifications such as Microsoft Responsible AI and IAPP Privacy Tech, specializing in domains like healthcare, finance, or public sector ethics, and actively engaging in communities that promote ethical AI practices. Contributing to open-source ethics tools, participating in forums, and reading the latest guidelines will enhance your expertise, credibility, and ability to implement AI responsibly throughout your career.",
        "points": [
            {"name": "Certifications", "desc": "Microsoft Responsible AI, IAPP Privacy Tech, and other credentials."},
            {"name": "Domain Specialization", "desc": "Focus on healthcare, finance, or public sector AI ethics."},
            {"name": "Community Engagement", "desc": "Contribute to open-source ethics tools and join forums."}
        ],
        "links": [
            {"name": "Microsoft Responsible AI Certification", "url": "https://learn.microsoft.com/en-us/ai/responsible-ai/responsible-ai-certification"},
            {"name": "IAPP Privacy Tech Certification", "url": "https://iapp.org/certify/cipt/"}
        ],
        "other_resources": [
            {"name": "AI Ethics Guidelines Global Inventory", "url": "https://algorithmwatch.org/en/project/ai-ethics-guidelines-global-inventory/"},
            {"name": "Google Responsible AI Practices", "url": "https://ai.google/responsibilities/responsible-ai-practices/"}
        ]
    }
]

def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/ethical_ai_engineer.html", roadmap=ETHICAL_AI_ENGINEER_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('ethical_ai_engineer'))

    @app.route("/ethical_ai_engineer")
    def ethical_ai_engineer():
        return render_page()

    app.run(debug=True)
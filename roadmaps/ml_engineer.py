from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory
BASE_DIR = Path(__file__).resolve().parent.parent  # Correct __file__
TEMPLATES_DIR = BASE_DIR / "templates"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))  # Correct __name__
ML_ENGINEER_ROADMAP = [
        {
        "title": "Programming Foundations",
        "description": "Master the essential programming skills required for machine learning development. This stage focuses on Python as the primary language, ensuring you can write clean, modular, and efficient code. You will also learn version control using Git and GitHub to manage projects, collaborate with others, and track changes in a professional environment. Solid programming foundations are critical for implementing ML models, data pipelines, and experimentation frameworks effectively.",
        "points": [
            {"name": "Python Basics", "desc": "Learn syntax, data types, loops, functions, and modules for foundational scripting."},
            {"name": "Advanced Python", "desc": "Understand OOP, decorators, context managers, and package management for complex applications."},
            {"name": "Version Control", "desc": "Use Git and GitHub to track code changes, manage branches, and collaborate efficiently."}
        ],
        "links": [
            {"name": "Python for Everybody (Coursera)", "url": "https://www.coursera.org/specializations/python"},
            {"name": "Git Tutorial", "url": "https://git-scm.com/docs/gittutorial"}
        ]
    },
    {
        "title": "Mathematics & Statistics",
        "description": "Develop a strong mathematical foundation to understand and optimize machine learning algorithms. This stage covers linear algebra, probability, statistics, and calculus, which are essential for understanding model behavior, implementing algorithms, and analyzing performance. Knowledge of these concepts enables you to reason about data, transform features, compute gradients, and evaluate models effectively.",
        "points": [
            {"name": "Linear Algebra", "desc": "Understand vectors, matrices, tensors, eigenvalues, and eigenvectors used in ML computations."},
            {"name": "Probability & Statistics", "desc": "Learn distributions, Bayes theorem, hypothesis testing, and sampling techniques to interpret data and model predictions."},
            {"name": "Calculus & Optimization", "desc": "Master derivatives, gradients, and optimization methods like gradient descent for training models."}
        ],
        "links": [
            {"name": "Khan Academy Linear Algebra", "url": "https://www.khanacademy.org/math/linear-algebra"},
            {"name": "Probability & Statistics (MIT OCW)", "url": "https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/"}
        ]
    },
    {
        "title": "Data Handling & Preprocessing",
        "description": "Learn to acquire, clean, and transform raw datasets into structured forms suitable for machine learning. Data preprocessing ensures that models receive high-quality input, leading to more accurate predictions. You will also practice feature engineering and data visualization to extract insights and detect patterns from datasets.",
        "points": [
            {"name": "Data Manipulation", "desc": "Use Pandas and NumPy to clean, filter, and organize data for analysis."},
            {"name": "Feature Engineering", "desc": "Transform raw data into meaningful features that improve model performance."},
            {"name": "Data Visualization", "desc": "Visualize distributions, correlations, and patterns using Matplotlib and Seaborn."}
        ],
        "links": [
            {"name": "Data Science Handbook", "url": "https://jakevdp.github.io/PythonDataScienceHandbook/"},
            {"name": "Kaggle Data Cleaning Tutorials", "url": "https://www.kaggle.com/learn/data-cleaning"}
        ]
    },
    {
        "title": "Machine Learning Fundamentals",
        "description": "Understand the core principles and algorithms of machine learning, including supervised, unsupervised, and reinforcement learning. Learn how to build models, evaluate their performance, and apply them to real-world problems. This stage emphasizes both theoretical understanding and practical implementation of ML workflows.",
        "points": [
            {"name": "Supervised Learning", "desc": "Implement linear regression, logistic regression, decision trees, and random forests for labeled data."},
            {"name": "Unsupervised Learning", "desc": "Apply clustering algorithms, PCA, and dimensionality reduction for pattern discovery in unlabeled data."},
            {"name": "Model Evaluation", "desc": "Use metrics such as accuracy, precision, recall, F1-score, and cross-validation to assess model performance."}
        ],
        "links": [
            {"name": "Machine Learning by Andrew Ng (Coursera)", "url": "https://www.coursera.org/learn/machine-learning"}
        ]
    },
    {
        "title": "Deep Learning",
        "description": "Dive into deep learning techniques to handle complex data types such as images, sequences, and text. Learn to build, train, and optimize neural networks using modern frameworks. This stage equips you to tackle tasks requiring high-dimensional representations and advanced architectures like CNNs and RNNs.",
        "points": [
            {"name": "Neural Networks Basics", "desc": "Study perceptrons, activation functions, forward/backpropagation, and loss computation."},
            {"name": "CNNs & RNNs", "desc": "Understand convolutional layers for image processing and recurrent architectures for sequential data."},
            {"name": "Deep Learning Frameworks", "desc": "Use TensorFlow and PyTorch to implement, train, and deploy deep learning models."}
        ],
        "links": [
            {"name": "Deep Learning Specialization (Coursera)", "url": "https://www.coursera.org/specializations/deep-learning"}
        ]
    },
    {
        "title": "Model Deployment & MLOps",
        "description": "Learn to operationalize machine learning models for production environments. This stage focuses on deploying models via APIs, using containerization, implementing monitoring, and adopting CI/CD pipelines to maintain robust and scalable ML services. Understanding MLOps is critical to bridging the gap between development and production systems.",
        "points": [
            {"name": "API Development", "desc": "Expose ML models as services using Flask or FastAPI for real-world applications."},
            {"name": "Containers & Orchestration", "desc": "Use Docker and Kubernetes to deploy scalable, maintainable, and reproducible ML solutions."},
            {"name": "MLOps & Monitoring", "desc": "Track experiments, model performance, and implement logging for production-ready ML systems using MLFlow and Kubeflow."}
        ],
        "links": [
            {"name": "MLFlow Docs", "url": "https://mlflow.org/docs/latest/index.html"},
            {"name": "Kubeflow Docs", "url": "https://www.kubeflow.org/docs/"}
        ]
    },
    {
        "title": "Cloud Platforms & Scalability",
        "description": "Gain expertise in scaling ML solutions using cloud services and distributed computing platforms. Learn how to leverage cloud infrastructure for model training, data processing, and automated scaling. This stage ensures you can deploy ML pipelines efficiently for large datasets and high-demand applications.",
        "points": [
            {"name": "AWS/GCP/Azure", "desc": "Deploy and manage ML workflows using major cloud platforms."},
            {"name": "Distributed Computing", "desc": "Handle large-scale datasets and computations using Spark or Dask."},
            {"name": "Serverless & Auto-scaling", "desc": "Implement infrastructure that automatically scales based on workload demand."}
        ],
        "links": [
            {"name": "AWS ML Services", "url": "https://aws.amazon.com/machine-learning/"},
            {"name": "Google Cloud AI Platform", "url": "https://cloud.google.com/ai-platform"}
        ]
    },
    {
        "title": "Advanced Topics & Specialization",
        "description": "Explore specialized areas in machine learning such as natural language processing, computer vision, reinforcement learning, and time series forecasting. This stage allows you to develop deep expertise and tackle domain-specific challenges using state-of-the-art methods and architectures.",
        "points": [
            {"name": "Natural Language Processing", "desc": "Work on text classification, sentiment analysis, and sequence modeling using NLP techniques."},
            {"name": "Computer Vision", "desc": "Implement image classification, object detection, and segmentation pipelines."},
            {"name": "Reinforcement Learning & Time Series", "desc": "Design and train agents using Q-learning, policy gradients, and forecast trends using time series models."}
        ],
        "links": [
            {"name": "Stanford CS231n", "url": "http://cs231n.stanford.edu/"},
            {"name": "CS224n NLP Course", "url": "http://web.stanford.edu/class/cs224n/"}
        ]
    },
    {
        "title": "Competitions & Community",
        "description": "Apply your ML knowledge in real-world challenges, open-source contributions, and community engagement. Participate in competitions and collaborate with peers to enhance practical skills, build a strong portfolio, and gain recognition in the ML ecosystem.",
        "points": [
            {"name": "Kaggle Competitions", "desc": "Compete on real-world datasets to apply ML skills and benchmark performance."},
            {"name": "Open Source Contributions", "desc": "Contribute to ML libraries, tools, and frameworks to gain hands-on experience."},
            {"name": "Community Engagement", "desc": "Engage with forums, Discord groups, and meetups to network, learn, and share knowledge."}
        ],
        "links": [
            {"name": "Kaggle", "url": "https://www.kaggle.com/"},
            {"name": "ML Community Forums", "url": "https://www.reddit.com/r/MachineLearning/"}
        ]
    },
    {
        "title": "Continuous Learning & Industry Trends",
        "description": "Stay up-to-date with the rapidly evolving field of machine learning by following new research, learning emerging tools, and exploring cutting-edge techniques. Continuous learning ensures that you can adapt to new algorithms, frameworks, and industry best practices, maintaining your competitive edge and expertise over time.",
        "points": [
            {"name": "Research Papers & Journals", "desc": "Regularly read ArXiv papers, journals, and technical blogs to stay informed on the latest ML developments."},
            {"name": "New Tools & Frameworks", "desc": "Experiment with emerging ML libraries, cloud services, and automation tools."},
            {"name": "Conferences & Workshops", "desc": "Attend workshops, webinars, and conferences to network and learn from industry experts."}
        ],
        "links": [
            {"name": "NeurIPS Conference", "url": "https://nips.cc/"},
            {"name": "ICML Conference", "url": "https://icml.cc/"}
        ]
    }
]

def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/ml_engineer.html", roadmap=ML_ENGINEER_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('ml_engineer'))

    @app.route("/ml_engineer")
    def ml_engineer():
        return render_page()

    app.run(debug=True)
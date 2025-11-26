from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))
AI_ENGINEER_ROADMAP = [
    {
        "title": "Core Programming & Mathematics",
        "description": "Master Python, data structures, and algorithms while building a strong foundation in linear algebra, calculus, and statistics — essential tools for AI problem-solving and model development.",
        "points": [
            {"name": "Python Mastery", "desc": "Advanced Python syntax, OOP concepts, NumPy for numerical computing, Pandas for data manipulation, Matplotlib for visualization"},
            {"name": "C++ Basics", "desc": "Fundamental C++ programming for performance-critical AI applications and system-level optimization"},
            {"name": "Linear Algebra", "desc": "Vectors, matrices, eigenvalues, SVD decomposition - essential for understanding neural network operations"},
            {"name": "Calculus", "desc": "Derivatives, gradients, optimization techniques - core mathematics behind machine learning algorithms"},
            {"name": "Probability & Statistics", "desc": "Probability distributions, Bayesian inference, statistical testing - foundation for probabilistic AI models"},
            {"name": "Git Version Control", "desc": "Collaborative coding, branch management, code review workflows essential for team-based AI development"}
        ],
        "links": [
            {"name": "Python for Data Science Handbook", "url": "https://jakevdp.github.io/PythonDataScienceHandbook/"},
            {"name": "Mathematics for Machine Learning", "url": "https://www.coursera.org/specializations/mathematics-machine-learning"}
        ],
        "other_resources": [
            {"name": "NumPy Documentation", "url": "https://numpy.org/doc/"},
            {"name": "Pandas User Guide", "url": "https://pandas.pydata.org/docs/user_guide/index.html"},
            {"name": "Git Official Documentation", "url": "https://git-scm.com/doc"}
        ]
    },
    {
        "title": "Machine Learning Fundamentals",
        "description": "Understand core machine learning concepts, algorithms, and evaluation techniques. Learn how models like regression, classification, and clustering are applied in real-world AI systems.",
        "points": [
            {"name": "Supervised Learning", "desc": "Linear regression, logistic regression, Support Vector Machines (SVMs), decision trees, random forests for predictive modeling"},
            {"name": "Unsupervised Learning", "desc": "K-means clustering, hierarchical clustering, PCA for dimensionality reduction, anomaly detection techniques"},
            {"name": "Model Evaluation", "desc": "Cross-validation strategies, hyperparameter tuning with grid/random search, performance metrics (accuracy, precision, recall, F1-score)"},
            {"name": "Neural Networks", "desc": "Perceptrons, activation functions (ReLU, sigmoid, tanh), backpropagation algorithm, gradient descent optimization"}
        ],
        "links": [
            {"name": "Scikit-learn Documentation", "url": "https://scikit-learn.org/stable/"},
            {"name": "Machine Learning Course by Andrew Ng", "url": "https://www.coursera.org/learn/machine-learning"}
        ],
        "other_resources": [
            {"name": "ML Cheatsheets", "url": "https://ml-cheatsheet.readthedocs.io/"},
            {"name": "Towards Data Science", "url": "https://towardsdatascience.com/"}
        ]
    },
    {
        "title": "Deep Learning Frameworks",
        "description": "Gain hands-on experience with deep learning libraries such as TensorFlow and PyTorch. Learn to design, train, and fine-tune neural networks for advanced AI tasks.",
        "points": [
            {"name": "PyTorch", "desc": "Dynamic computation graphs, extensive research applications, strong community support, intuitive Pythonic interface"},
            {"name": "TensorFlow", "desc": "Production-ready deployment, TensorFlow Serving for model serving, TensorFlow Lite for mobile devices, comprehensive ecosystem"},
            {"name": "JAX", "desc": "Functional programming approach, high-performance computing, automatic differentiation, growing research adoption"},
            {"name": "Keras", "desc": "High-level API for rapid prototyping, user-friendly interface, runs on top of TensorFlow, excellent for beginners"}
        ],
        "links": [
            {"name": "PyTorch Tutorials", "url": "https://pytorch.org/tutorials/"},
            {"name": "TensorFlow Guide", "url": "https://www.tensorflow.org/guide"},
            {"name": "JAX Documentation", "url": "https://jax.readthedocs.io/"}
        ],
        "other_resources": [
            {"name": "Keras Examples", "url": "https://keras.io/examples/"},
            {"name": "Fast.ai Practical Deep Learning", "url": "https://www.fast.ai/"}
        ]
    },
    {
        "title": "Advanced AI Architectures",
        "description": "Explore cutting-edge architectures such as CNNs, RNNs, Transformers, and GANs. Understand how they drive breakthroughs in vision, language, and generative AI applications.",
        "points": [
            {"name": "CNNs", "desc": "Convolutional Neural Networks for image recognition, computer vision applications, feature extraction from spatial data"},
            {"name": "RNNs/LSTMs", "desc": "Recurrent Neural Networks and Long Short-Term Memory networks for sequence data, time series analysis, and temporal patterns"},
            {"name": "Transformers", "desc": "BERT, GPT models, attention mechanism for handling long-range dependencies in sequential data"},
            {"name": "Generative Models", "desc": "GANs (Generative Adversarial Networks), VAEs (Variational Autoencoders), Diffusion Models for content generation and synthesis"}
        ],
        "links": [
            {"name": "Transformer Paper", "url": "https://arxiv.org/abs/1706.03762"},
            {"name": "CNN Guide", "url": "https://cs231n.github.io/"}
        ]
    },
    {
        "title": "Natural Language Processing",
        "description": "Study NLP fundamentals including tokenization, embeddings, and attention mechanisms. Build models for text classification, translation, and conversational AI systems.",
        "points": [
            {"name": "Text Processing", "desc": "Tokenization, stemming, lemmatization, word embeddings (Word2Vec, GloVe) for text representation"},
            {"name": "Hugging Face Transformers", "desc": "Pre-trained models, fine-tuning techniques, model hub for state-of-the-art NLP models"},
            {"name": "LLM Applications", "desc": "Prompt engineering, RAG (Retrieval-Augmented Generation) systems, few-shot learning applications"},
            {"name": "NLP Deployment", "desc": "Chatbots, text classification systems, sentiment analysis, named entity recognition in production"}
        ],
        "links": [
            {"name": "Hugging Face Docs", "url": "https://huggingface.co/docs"},
            {"name": "NLP Course", "url": "https://www.coursera.org/specializations/natural-language-processing"}
        ]
    },
    {
        "title": "Computer Vision",
        "description": "Learn algorithms and deep learning methods for image recognition, object detection, and scene understanding. Apply vision techniques to AI systems in real-world contexts.",
        "points": [
            {"name": "Object Detection", "desc": "YOLO (You Only Look Once), Faster R-CNN implementations for real-time object identification"},
            {"name": "Image Segmentation", "desc": "U-Net, Mask R-CNN architectures for pixel-level image analysis and segmentation"},
            {"name": "Video Analysis", "desc": "Real-time processing, action recognition, temporal analysis in video sequences"},
            {"name": "CV Deployment", "desc": "Mobile applications, edge devices, optimized models for resource-constrained environments"}
        ],
        "links": [
            {"name": "OpenCV Tutorials", "url": "https://docs.opencv.org/master/d9/df8/tutorial_root.html"},
            {"name": "YOLO Official", "url": "https://pjreddie.com/darknet/yolo/"}
        ]
    },
    {
        "title": "Model Deployment & Serving",
        "description": "Understand how to deploy AI models efficiently using APIs, containers, and inference frameworks. Learn about scaling, monitoring, and optimizing performance in production.",
        "points": [
            {"name": "API Development", "desc": "Flask, FastAPI, Django REST Framework for creating model inference APIs"},
            {"name": "Model Serving", "desc": "TensorFlow Serving, TorchServe, Triton Inference Server for high-performance model serving"},
            {"name": "Containerization", "desc": "Docker for AI applications, creating reproducible environments for model deployment"},
            {"name": "Web Integration", "desc": "REST APIs, WebSocket streaming for real-time inference in web applications"}
        ],
        "links": [
            {"name": "FastAPI Docs", "url": "https://fastapi.tiangolo.com/"},
            {"name": "Docker for ML", "url": "https://docs.docker.com/ai/"}
        ]
    },
    {
        "title": "MLOps & Production Engineering",
        "description": "Dive into MLOps principles for automating data pipelines, CI/CD, and model lifecycle management. Build robust systems that ensure reliability and reproducibility in AI projects.",
        "points": [
            {"name": "Experiment Tracking", "desc": "MLflow, Weights & Biases for experiment management, parameter tracking, and result comparison"},
            {"name": "CI/CD Pipelines", "desc": "Automated testing, continuous integration/deployment for ML models, automated retraining pipelines"},
            {"name": "Model Registry", "desc": "Version control, lifecycle management, model lineage tracking, and staging environments"},
            {"name": "Feature Stores", "desc": "Data pipeline management, feature engineering, feature versioning, and serving"}
        ],
        "links": [
            {"name": "MLflow Documentation", "url": "https://mlflow.org/docs/latest/index.html"},
            {"name": "Weights & Biases", "url": "https://docs.wandb.ai/"}
        ]
    },
    {
        "title": "Cloud AI Platforms",
        "description": "Explore cloud-based AI platforms like AWS, Azure, and Google Cloud AI. Learn to use managed services for scalable model training, deployment, and real-time inference.",
        "points": [
            {"name": "AWS AI Services", "desc": "SageMaker for end-to-end ML, Rekognition for computer vision, Bedrock for foundation models"},
            {"name": "Google Cloud AI", "desc": "Vertex AI unified platform, AutoML for automated model building, AI Platform for MLOps"},
            {"name": "Azure AI", "desc": "Machine Learning Studio for drag-and-drop ML, Cognitive Services for pre-built AI capabilities"},
            {"name": "Multi-cloud Strategies", "desc": "Hybrid deployment approaches, vendor-agnostic architectures, cost optimization"}
        ],
        "links": [
            {"name": "AWS ML Services", "url": "https://aws.amazon.com/machine-learning/"},
            {"name": "Google Vertex AI", "url": "https://cloud.google.com/vertex-ai"}
        ]
    },
    {
    "title": "Scalable Infrastructure",
    "description": "Infrastructure technologies for scaling AI systems",
    "points": [
        {"name": "Kubernetes", "desc": "Container orchestration for AI workloads, auto-scaling, and resource management"},
        {"name": "Distributed Training", "desc": "Data parallelism, model parallelism, multi-GPU training, distributed computing frameworks"},
        {"name": "Model Optimization", "desc": "Quantization for reduced precision, pruning for model size reduction, knowledge distillation"},
        {"name": "Monitoring Systems", "desc": "Performance tracking, model drift detection, alerting systems, and health checks"}
    ],
    "links": [
        {"name": "Kubernetes for ML", "url": "https://kubernetes.io/blog/tags/machine-learning/"},
        {"name": "PyTorch Distributed", "url": "https://pytorch.org/tutorials/intermediate/ddp_tutorial.html"}
    ]
    },
    {
        "title": "Large Language Models Engineering",
        "description": "Learn how to fine-tune, optimize, and integrate large language models like GPT and LLaMA. Explore prompt engineering and efficient deployment for advanced AI applications.",
        "points": [
        {"name": "Prompt Engineering", "desc": "Effective LLM interaction patterns, few-shot learning, chain-of-thought prompting"},
        {"name": "Fine-tuning Techniques", "desc": "LoRA (Low-Rank Adaptation), QLoRA (Quantized LoRA), adapter methods for efficient tuning"},
        {"name": "LLM Deployment", "desc": "Optimization for production inference, latency reduction, cost optimization, scaling strategies"},
        {"name": "RAG Systems", "desc": "Retrieval-Augmented Generation pipelines, vector databases, semantic search integration"}
        ],
        "links": [
        {"name": "Hugging Face PEFT", "url": "https://huggingface.co/docs/peft/index"},
        {"name": "LangChain Documentation", "url": "https://python.langchain.com/docs/get_started/introduction"}
        ]
    },{
    "title": "Edge AI & Mobile Deployment",
    "description": "Master techniques for deploying lightweight AI models on edge devices and mobile platforms. Learn about optimization, latency reduction, and on-device intelligence.",
    "points": [
        {"name": "TensorFlow Lite", "desc": "Mobile-optimized models, quantization, on-device inference for Android and iOS"},
        {"name": "PyTorch Mobile", "desc": "On-device inference, model optimization for mobile deployment, performance tuning"},
        {"name": "Model Compression", "desc": "Techniques for edge deployment including pruning, quantization, and architecture search"},
        {"name": "IoT Integration", "desc": "Real-time sensor data processing, embedded systems, low-power AI applications"}
    ],
    "links": [
        {"name": "TensorFlow Lite Guide", "url": "https://www.tensorflow.org/lite/guide"},
        {"name": "PyTorch Mobile", "url": "https://pytorch.org/mobile/"}
    ]},{
    "title": "Ethical AI & Governance",
    "description": "Understand ethical principles, fairness, transparency, and accountability in AI. Learn governance frameworks that ensure responsible and trustworthy AI development.",
    "points": [
        {"name": "Model Explainability", "desc": "SHAP (SHapley Additive exPlanations), LIME (Local Interpretable Model-agnostic Explanations) interpretations"},
        {"name": "Bias Detection", "desc": "Fairness metrics, bias mitigation techniques, demographic parity, equalized odds"},
        {"name": "AI Ethics", "desc": "Responsible AI development practices, transparency, accountability, and fairness principles"},
        {"name": "Model Governance", "desc": "Compliance frameworks, auditing procedures, regulatory requirements, and risk management"}
    ],
    "links": [
        {"name": "AI Ethics Guidelines", "url": "https://www.partnershiponai.org/"},
        {"name": "Responsible AI Toolkit", "url": "https://responsibleaitoolkit.ai/"}
    ]
    },{
    "title": "Continuous Learning",
    "description": "Strategies for staying updated and advancing in the rapidly evolving AI field",
    "points": [
        {"name": "Research Paper Reading", "desc": "Regularly follow ArXiv, conference proceedings (NeurIPS, ICML, CVPR), and implement recent papers"},
        {"name": "Open Source Contributions", "desc": "Contribute to AI frameworks, libraries, and tools on GitHub to build expertise and reputation"},
        {"name": "Competitions & Challenges", "desc": "Participate in Kaggle competitions, Hackathons, and research challenges to practice skills"},
        {"name": "Community Engagement", "desc": "Join AI communities, attend meetups, conferences, and participate in online forums"},
        {"name": "Specialization Tracks", "desc": "Choose emerging specializations like Multimodal AI, AI Safety, Quantum ML, or Neuro-symbolic AI"},

    ],
    "links": [
        {"name": "ArXiv Sanity Preserver", "url": "http://www.arxiv-sanity.com/"},
        {"name": "Papers with Code", "url": "https://paperswithcode.com/"},
        {"name": "AI Conference Deadlines", "url": "https://aideadlin.es/"}
    ],
    "other_resources": [
        {"name": "AI Newsletters", "url": "The Batch by deeplearning.ai, Import AI"},
        {"name": "Podcasts", "url": "Lex Fridman Podcast, TWIML AI, Practical AI"},
        {"name": "Learning Platforms", "url": "DeepLearning.AI, Fast.ai, Coursera Specializations"},
        {"name": "Research Institutions", "url": "OpenAI Research, Google AI Blog, Meta AI Publications"}
    ],
    }

]
@app.route("/")
def home():
    return redirect(url_for('ai_engineer'))

def render_page():
    return render_template("roadmaps/ai_engineer.html", roadmap=AI_ENGINEER_ROADMAP)

# ✅ Optional: allows running this file independently too
if __name__ == "__main__":
    app = Flask(__name__, template_folder="../templates")
    @app.route("/")
    def standalone():
        return render_page()
    app.run(debug=True)
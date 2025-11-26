from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory
BASE_DIR = Path(__file__).resolve().parent.parent  # Correct __file__
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))  # Correct __name__
GEN_AI_ENGINEER_ROADMAP=[
  {
    "title": "Foundations of AI & Machine Learning",
    "description": "This stage lays the groundwork for a career in AI by introducing the fundamental concepts that underpin machine intelligence. You will explore how machines learn from data, uncover patterns, and make predictions. Beyond theory, you will practice implementing algorithms, understanding model evaluation, and gain intuition about real-world AI applications. This foundation is essential for tackling more advanced topics like deep learning, natural language processing, and generative AI.",
    "points": [
      {"name": "Machine Learning Basics", "desc": "Learn supervised, unsupervised, and reinforcement learning approaches, including regression, classification, clustering, and policy-based learning."},
      {"name": "Deep Learning Fundamentals", "desc": "Understand neural networks, CNNs, RNNs, activation functions, and backpropagation that allow machines to learn complex patterns."},
      {"name": "Python for AI", "desc": "Practice libraries such as NumPy for numerical computing, Pandas for data manipulation, and PyTorch/TensorFlow for building and training deep learning models."}
    ],
    "links": [
      {"name": "Machine Learning by Andrew Ng", "url": "https://www.coursera.org/learn/machine-learning"}
    ],
    "other_resources": [
      {"name": "PyTorch Tutorials", "url": "https://pytorch.org/tutorials/"}
    ]
  },
  {
    "title": "Mathematics & Statistics for AI",
    "description": "Mathematical foundations are essential for understanding AI at a deeper level. This stage focuses on the core mathematical concepts required for modeling, analyzing, and optimizing AI algorithms. Mastery of linear algebra, probability, statistics, and calculus will empower you to design better models and understand their inner workings.",
    "points": [
      {"name": "Linear Algebra", "desc": "Study vectors, matrices, eigenvalues, eigenvectors, and their applications in data transformations and neural networks."},
      {"name": "Probability & Statistics", "desc": "Understand Bayes theorem, probability distributions, descriptive statistics, and hypothesis testing to make informed predictions."},
      {"name": "Calculus & Optimization", "desc": "Learn derivatives, gradients, partial derivatives, chain rule, and optimization techniques for training machine learning models effectively."}
    ],
    "links": [
      {"name": "Mathematics for Machine Learning", "url": "https://mml-book.github.io/"}
    ],
    "other_resources": [
      {"name": "3Blue1Brown YouTube", "url": "https://www.3blue1brown.com/"}
    ]
  },
  {
    "title": "Data Engineering & Preprocessing",
    "description": "Clean, preprocess, and prepare data for AI models. This stage teaches how to handle messy real-world datasets, transform raw data into meaningful features, and automate data pipelines for large-scale machine learning projects.",
    "points": [
      {"name": "Data Cleaning", "desc": "Handle missing values, remove duplicates, detect and treat outliers, and ensure data quality."},
      {"name": "Feature Engineering", "desc": "Transform raw data into useful features using normalization, encoding, and dimensionality reduction techniques."},
      {"name": "Data Pipelines", "desc": "Automate ETL processes using tools like Apache Airflow, Spark, or Python-based Pandas pipelines to streamline data flow."}
    ],
    "links": [
      {"name": "Data Engineering Zoomcamp", "url": "https://github.com/DataTalksClub/data-engineering-zoomcamp"}
    ],
    "other_resources": [
      {"name": "Kaggle Datasets", "url": "https://www.kaggle.com/datasets"}
    ]
  },
  {
    "title": "Natural Language Processing Basics",
    "description": "Before diving into large language models, understand classical NLP techniques. Learn to preprocess text, build representations, and apply models to real-world language tasks like sentiment analysis and topic modeling.",
    "points": [
      {"name": "Text Preprocessing", "desc": "Learn tokenization, stemming, lemmatization, stopword removal, and text normalization techniques."},
      {"name": "Classical NLP", "desc": "Understand TF-IDF, Word2Vec, and GloVe embeddings for representing textual data."},
      {"name": "Applications", "desc": "Build practical NLP applications like sentiment analysis, text classification, and topic modeling."}
    ],
    "links": [
      {"name": "CS224N: NLP with Deep Learning", "url": "http://web.stanford.edu/class/cs224n/"}
    ],
    "other_resources": [
      {"name": "NLTK Documentation", "url": "https://www.nltk.org/"}
    ]
  },
  {
    "title": "Large Language Models (LLMs)",
    "description": "Dive into the world of transformers and generative models such as GPT, BERT, and LLaMA. Learn how attention mechanisms work, how to fine-tune models, and how embeddings capture semantic meaning in language.",
    "points": [
      {"name": "Transformers", "desc": "Understand self-attention, multi-head attention, encoder-decoder architectures, and their advantages over traditional RNNs."},
      {"name": "Pretrained Models", "desc": "Learn the difference between fine-tuning, zero-shot, and few-shot model usage for various tasks."},
      {"name": "Embeddings", "desc": "Explore word embeddings, contextual embeddings, and how they encode semantic relationships between words."}
    ],
    "links": [
      {"name": "HuggingFace Transformers Course", "url": "https://huggingface.co/course/chapter1"}
    ],
    "other_resources": [
      {"name": "The Illustrated Transformer", "url": "http://jalammar.github.io/illustrated-transformer/"}
    ]
  },
  {
    "title": "Prompt Engineering",
    "description": "Learn how to craft effective prompts to maximize the performance of LLMs. This includes designing instructions, using reasoning strategies, and applying few-shot or zero-shot methods to guide AI behavior without retraining.",
    "points": [
      {"name": "Prompt Design", "desc": "Understand how to phrase instructions, provide context, and structure inputs for optimal results."},
      {"name": "Chain-of-Thought", "desc": "Implement reasoning strategies within prompts to help models solve complex problems step by step."},
      {"name": "Few-Shot & Zero-Shot", "desc": "Leverage examples or descriptive instructions to guide model behavior without additional training."}
    ],
    "links": [
      {"name": "Learn Prompting", "url": "https://learnprompting.org/"}
    ],
    "other_resources": [
      {"name": "FlowGPT", "url": "https://flowgpt.com/"}
    ]
  },
  {
    "title": "Fine-Tuning & Custom Models",
    "description": "Adapt large language models to specific domains, tasks, or datasets. This stage covers full fine-tuning, parameter-efficient methods like LoRA, and evaluating model performance using standard metrics.",
    "points": [
      {"name": "Full Fine-Tuning", "desc": "Retrain large models on domain-specific datasets to improve task-specific performance."},
      {"name": "LoRA & PEFT", "desc": "Apply parameter-efficient fine-tuning to reduce computational costs while achieving comparable results."},
      {"name": "Evaluation", "desc": "Measure model quality using metrics such as ROUGE, BLEU, and perplexity to ensure effective adaptation."}
    ],
    "links": [
      {"name": "Fine-Tuning HuggingFace", "url": "https://huggingface.co/docs/transformers/training"}
    ],
    "other_resources": [
      {"name": "OpenAI Fine-Tuning", "url": "https://platform.openai.com/docs/guides/fine-tuning"}
    ]
  },{
    "title": "Retrieval-Augmented Generation (RAG)",
    "description": "RAG combines large language models with external knowledge sources to provide more accurate, up-to-date, and context-aware responses. By integrating document retrieval and vector search, you can enhance the model's ability to answer specific questions, generate relevant content, and connect with domain-specific data.",
    "points": [
      {"name": "Vector Databases", "desc": "Learn FAISS, Pinecone, and Weaviate for storing and searching high-dimensional embeddings efficiently."},
      {"name": "Document Retrieval", "desc": "Implement semantic search, ranking, and retrieval pipelines to extract relevant information from large datasets."},
      {"name": "RAG Pipelines", "desc": "Combine LLMs with retrieval systems using frameworks like LangChain and LlamaIndex to generate contextually enriched outputs."}
    ],
    "links": [
      {"name": "LangChain RAG", "url": "https://docs.langchain.com/docs/use_cases/question_answering"}
    ],
    "other_resources": [
      {"name": "FAISS Quickstart", "url": "https://github.com/facebookresearch/faiss/wiki/Quickstart"}
    ]
  },
  {
    "title": "Multi-Modal AI",
    "description": "Multi-modal AI models can process and integrate information from multiple data types such as text, images, audio, and video. Understanding this allows you to build AI systems that can generate captions, summarize videos, or combine sensory data to make more intelligent decisions.",
    "points": [
      {"name": "Vision-Language Models", "desc": "Explore models like CLIP, BLIP, and Flamingo to connect visual content with natural language understanding."},
      {"name": "Speech Models", "desc": "Work with audio-to-text and speech recognition models like Whisper and Wav2Vec for processing speech data."},
      {"name": "Applications", "desc": "Build projects like image captioning, video summarization, or multi-modal search engines."}
    ],
    "links": [
      {"name": "CLIP Paper", "url": "https://arxiv.org/abs/2103.00020"}
    ],
    "other_resources": [
      {"name": "OpenAI Whisper", "url": "https://github.com/openai/whisper"}
    ]
  },
  {
    "title": "Evaluation & Safety",
    "description": "Ensuring AI reliability, fairness, and safety is critical. This stage covers techniques to identify biases, implement safety guardrails, and leverage human feedback. Proper evaluation ensures AI systems are trustworthy, ethical, and aligned with societal standards.",
    "points": [
      {"name": "Bias Detection", "desc": "Identify and mitigate biases in datasets and model predictions to ensure fairness across demographics."},
      {"name": "Safety Guardrails", "desc": "Implement rules, filters, and monitoring to prevent harmful outputs and unsafe behavior."},
      {"name": "Human Feedback", "desc": "Use Reinforcement Learning from Human Feedback (RLHF) and continuous monitoring to align models with human values."}
    ],
    "links": [
      {"name": "Microsoft Responsible AI", "url": "https://learn.microsoft.com/en-us/azure/ai/responsible-ai/"}
    ],
    "other_resources": [
      {"name": "HuggingFace Evaluate", "url": "https://huggingface.co/docs/evaluate"}
    ]
  },
  {
    "title": "MLOps for Generative AI",
    "description": "MLOps focuses on operationalizing AI models in production. Learn CI/CD pipelines, deployment strategies, monitoring, and scaling to ensure models remain reliable, reproducible, and maintainable in real-world applications.",
    "points": [
      {"name": "Model Deployment", "desc": "Serve models via REST APIs, gRPC, or other endpoints for integration with applications."},
      {"name": "CI/CD", "desc": "Implement automated testing, retraining pipelines, and continuous deployment for AI models."},
      {"name": "Monitoring", "desc": "Track model drift, latency, accuracy, and resource usage to ensure system performance and reliability."}
    ],
    "links": [
      {"name": "MLOps Specialization", "url": "https://www.coursera.org/specializations/mlops-machine-learning-production"}
    ],
    "other_resources": [
      {"name": "Kubeflow Docs", "url": "https://www.kubeflow.org/"}
    ]
  },
  {
    "title": "Deployment & Scaling",
    "description": "Take AI models from development to production at scale. Learn to build APIs, host models on cloud platforms, and implement serverless inference to ensure cost-efficient, high-performance AI services.",
    "points": [
      {"name": "API Development", "desc": "Use frameworks like FastAPI or Flask to expose AI models as services."},
      {"name": "Cloud Hosting", "desc": "Deploy models on cloud platforms like AWS Sagemaker, GCP Vertex AI, or Azure ML for scalable inference."},
      {"name": "Serverless AI", "desc": "Run AI inference using serverless solutions to reduce cost and handle variable traffic efficiently."}
    ],
    "links": [
      {"name": "FastAPI Docs", "url": "https://fastapi.tiangolo.com/"}
    ],
    "other_resources": [
      {"name": "HuggingFace Inference API", "url": "https://huggingface.co/inference-api"}
    ]
  },
  {
    "title": "AI Agents & Automation",
    "description": "Build autonomous AI agents capable of planning, decision-making, and tool usage. Learn to develop systems that can break down complex goals into actionable tasks and execute them independently.",
    "points": [
      {"name": "LangChain Agents", "desc": "Develop AI agents that can use external tools, APIs, and reasoning to complete tasks."},
      {"name": "AutoGPT", "desc": "Implement autonomous agents capable of goal-directed task execution with minimal human intervention."},
      {"name": "Task Planning", "desc": "Break complex goals into subtasks, prioritize actions, and monitor agent performance."}
    ],
    "links": [
      {"name": "LangChain Agents Docs", "url": "https://docs.langchain.com/docs/modules/agents"}
    ],
    "other_resources": [
      {"name": "AutoGPT GitHub", "url": "https://github.com/Torantulino/Auto-GPT"}
    ]
  },
  {
    "title": "Ethics, Policy & Governance",
    "description": "Understanding legal, ethical, and societal implications is critical for responsible AI. Learn about fairness, transparency, accountability, and global AI regulations. Evaluate the impact of AI on society, including employment, misinformation, and accessibility.",
    "points": [
      {"name": "AI Ethics", "desc": "Understand principles of fairness, transparency, and accountability in AI systems."},
      {"name": "Regulations", "desc": "Study EU AI Act, GDPR, and other AI policies to ensure legal compliance."},
      {"name": "Societal Impact", "desc": "Analyze AI effects on employment, misinformation, digital accessibility, and equitable technology deployment."}
    ],
    "links": [
      {"name": "AI Ethics Stanford", "url": "https://ethicsinaction.ieee.org/ai-ethics/"}
    ],
    "other_resources": [
      {"name": "OECD AI Policy Observatory", "url": "https://oecd.ai/"}
    ]
  },
  {
    "title": "Continue Learning",
    "description": "Generative AI is rapidly evolving. Staying up-to-date with research papers, participating in communities, and building hands-on projects ensures continuous growth. Embrace lifelong learning to remain at the forefront of AI advancements.",
    "points": [
      {"name": "Research Papers", "desc": "Stay updated on AI advancements via arXiv, NeurIPS, ICLR, and other top conferences."},
      {"name": "Communities", "desc": "Join HuggingFace forums, Reddit ML communities, and Discord groups to share knowledge and learn from peers."},
      {"name": "Projects & Hackathons", "desc": "Develop real-world projects, contribute to open-source, and participate in hackathons to sharpen your skills."}
    ],
    "links": [
      {"name": "Arxiv.org AI Section", "url": "https://arxiv.org/list/cs.AI/recent"}
    ],
    "other_resources": [
      {"name": "Papers with Code", "url": "https://paperswithcode.com/"}
    ]
  }
]


def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/gen_ai_engineer.html", roadmap=GEN_AI_ENGINEER_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('gen_ai_engineer'))

    @app.route("/gen_ai_engineer")
    def gen_ai_engineer():
        return render_page()

    app.run(debug=True)
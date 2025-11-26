from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory
BASE_DIR = Path(__file__).resolve().parent.parent  # Correct __file__
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))  # Correct __name__
LLM_ENGINEER_ROADMAP =[
   {
        "title": "Programming Foundations",
        "description": "This stage focuses on building a strong programming foundation necessary for working with large language models (LLMs). You will master Python, which is the primary language for AI and ML development, including scripting, modular code design, and best practices for clean, maintainable code. In addition, you will gain expertise in version control using Git and GitHub, which is critical for collaborative software development, tracking experiments, and managing multiple model versions. These skills will enable you to implement pipelines, handle datasets, and collaborate effectively in AI projects while preparing you for the more advanced stages of model development and deployment.",
        "points": [
            {"name": "Python Basics", "desc": "Learn Python syntax, data types, control flow, functions, and modules for basic scripting and automation."},
            {"name": "Advanced Python", "desc": "Deepen your knowledge with object-oriented programming, decorators, context managers, generators, and package management for large-scale projects."},
            {"name": "Version Control", "desc": "Use Git and GitHub to manage code, track changes, create branches, merge pull requests, and collaborate on team projects efficiently."}
        ],
        "links": [
            {"name": "Python for Everybody (Coursera)", "url": "https://www.coursera.org/specializations/python"},
            {"name": "Git Tutorial", "url": "https://git-scm.com/docs/gittutorial"}
        ]
    },
    {
        "title": "Mathematics for LLMs",
        "description": "A deep understanding of mathematics is essential for grasping how LLMs operate under the hood. This stage covers linear algebra, probability, statistics, and calculus, providing the theoretical foundation for neural networks, optimization, and evaluation. Linear algebra concepts such as vectors, matrices, and tensor operations form the backbone of model computations, while probability and statistics help in modeling uncertainty, understanding distributions, and evaluating model outputs. Calculus and optimization teach you how gradients, derivatives, and optimization techniques like gradient descent drive model training. Mastery of these topics ensures you can understand, debug, and improve LLM architectures effectively.",
        "points": [
            {"name": "Linear Algebra", "desc": "Understand vectors, matrices, tensor operations, eigenvalues, and eigenvectors to manipulate and analyze model inputs and weights."},
            {"name": "Probability & Statistics", "desc": "Learn probability distributions, Bayes theorem, hypothesis testing, and statistical inference for modeling and evaluation."},
            {"name": "Calculus & Optimization", "desc": "Study derivatives, gradients, chain rule, and optimization algorithms like gradient descent and Adam to train neural networks effectively."}
        ],
        "links": [
            {"name": "Khan Academy Linear Algebra", "url": "https://www.khanacademy.org/math/linear-algebra"},
            {"name": "Probability & Statistics (MIT OCW)", "url": "https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/"}
        ]
    },
    {
        "title": "Deep Learning Fundamentals",
        "description": "This stage introduces neural networks and deep learning, which are essential to building LLMs. You will learn how perceptrons, activation functions, and backpropagation work to train models. Additionally, convolutional neural networks (CNNs) and recurrent neural networks (RNNs) are covered to understand feature extraction and sequence modeling. A foundational understanding of transformer architectures, attention mechanisms, and self-attention is provided, as these form the core of modern LLMs. Mastery of these concepts ensures you can understand and innovate on complex model architectures while bridging the gap between theory and practical implementation.",
        "points": [
            {"name": "Neural Networks", "desc": "Learn the architecture of neurons, forward and backward propagation, loss functions, and optimization for building neural networks."},
            {"name": "CNNs & RNNs", "desc": "Understand convolutional layers for spatial data, recurrent layers for sequential data, and their applications in feature extraction and modeling."},
            {"name": "Transformer Basics", "desc": "Explore attention mechanisms, encoder-decoder architectures, positional encoding, and self-attention, which are central to modern LLMs."}
        ],
        "links": [
            {"name": "Deep Learning Specialization (Coursera)", "url": "https://www.coursera.org/specializations/deep-learning"}
        ]
    },
    {
        "title": "Natural Language Processing (NLP)",
        "description": "This stage focuses on understanding, processing, and representing text data, which is the foundation for training and applying LLMs. You will learn essential NLP techniques like tokenization, stemming, lemmatization, and stop-word removal for preprocessing raw text. Embeddings such as Word2Vec, GloVe, and contextual embeddings help in representing text meaningfully in vector space. You will also explore common NLP tasks like text classification, summarization, translation, and named entity recognition. A strong grasp of NLP ensures you can handle data, extract meaning, and build models that understand language effectively.",
        "points": [
            {"name": "Text Preprocessing", "desc": "Prepare text for modeling using tokenization, stemming, lemmatization, and stop-word removal techniques."},
            {"name": "Embeddings & Representations", "desc": "Represent words and sentences using vector embeddings such as Word2Vec, GloVe, and contextual embeddings for semantic understanding."},
            {"name": "NLP Tasks", "desc": "Apply NLP techniques to tasks like sentiment analysis, text summarization, machine translation, and named entity recognition."}
        ],
        "links": [
            {"name": "NLP Specialization (Coursera)", "url": "https://www.coursera.org/specializations/natural-language-processing"}
        ]
    },
    {
        "title": "LLM Architecture Deep Dive",
        "description": "In this stage, you explore the internal workings of LLMs and transformer-based architectures like GPT, BERT, and T5. You will gain a detailed understanding of attention mechanisms, including scaled dot-product and multi-head attention, and positional encodings that allow models to understand sequence order. Layer designs, residual connections, and normalization techniques are also covered to help you comprehend model stability and learning dynamics. By mastering this stage, you will be able to read, interpret, and innovate on LLM architectures and design new models effectively.",
        "points": [
            {"name": "GPT, BERT, T5", "desc": "Learn differences between encoder-only, decoder-only, and encoder-decoder architectures, and how they are applied in tasks like text generation and understanding."},
            {"name": "Attention & Self-Attention", "desc": "Understand how attention calculates relationships between tokens and enables models to focus on relevant information across sequences."},
            {"name": "Position Encoding & Layers", "desc": "Learn about positional encodings, layer normalization, and residual connections that improve model learning and stability."}
        ],
        "links": [
            {"name": "The Illustrated Transformer", "url": "http://jalammar.github.io/illustrated-transformer/"},
            {"name": "HuggingFace Docs", "url": "https://huggingface.co/docs/transformers/"}
        ]
    },
    {
        "title": "Pre-training LLMs",
        "description": "This stage focuses on the process of training large language models from scratch or leveraging existing large datasets. You will learn how to collect and clean massive text corpora, tokenize text, and implement distributed training strategies using GPUs or TPUs. Training objectives such as masked language modeling and causal language modeling are explored in depth. Understanding hardware requirements, memory optimization, and mixed-precision training ensures efficient training of large-scale models. Mastery of this stage equips you with the ability to develop and scale your own LLMs effectively.",
        "points": [
            {"name": "Data Collection & Cleaning", "desc": "Acquire large datasets, clean noisy text, tokenize efficiently, and prepare corpora for training."},
            {"name": "Training Strategies", "desc": "Implement different objectives like masked LM, causal LM, and autoregressive learning for various tasks."},
            {"name": "Hardware & Resources", "desc": "Use GPUs/TPUs, distributed training frameworks, and mixed-precision training to handle large-scale model computation efficiently."}
        ],
        "links": [
            {"name": "vLLM Docs", "url": "https://vllm.ai/"},
            {"name": "DeepSpeed Docs", "url": "https://www.deepspeed.ai/"}
        ]
    },
    {
        "title": "Fine-Tuning & Adaptation",
        "description": "In this stage, you learn how to adapt pre-trained LLMs to specific tasks, domains, or datasets. Full model fine-tuning allows you to update all parameters for optimal performance on your target task, while parameter-efficient fine-tuning techniques like LoRA, adapters, or prefix-tuning help reduce computational requirements. Prompt engineering is also a key skill, where you design zero-shot, few-shot, or chain-of-thought prompts to guide the model towards desired outputs. Mastery of this stage ensures you can leverage pre-trained LLMs effectively, achieving high accuracy on specialized tasks without unnecessary retraining from scratch.",
        "points": [
            {"name": "Full Model Fine-Tuning", "desc": "Update all model parameters on your domain-specific data for maximum task performance."},
            {"name": "Parameter-Efficient Fine-Tuning", "desc": "Use LoRA, adapters, or prefix-tuning to fine-tune models efficiently with lower computational cost."},
            {"name": "Prompt Engineering", "desc": "Craft prompts for zero-shot, few-shot, or chain-of-thought reasoning to control and improve model outputs."}
        ],
        "links": [
            {"name": "HuggingFace Fine-Tuning", "url": "https://huggingface.co/docs/transformers/training"},
            {"name": "LangChain Docs", "url": "https://www.langchain.com/docs/"}
        ]
    },
    {
        "title": "Retrieval-Augmented Generation (RAG)",
        "description": "This stage introduces Retrieval-Augmented Generation, combining retrieval systems with generative LLMs. You will learn to generate embeddings for documents and queries, use vector databases such as FAISS, Pinecone, or Weaviate for efficient similarity searches, and integrate retrieved knowledge into the generative process. RAG enables LLMs to access external knowledge bases, enhancing their ability to answer knowledge-intensive questions accurately. Mastery of this stage equips you to build robust applications where the model can reason over vast, dynamically updated datasets rather than relying solely on pre-trained knowledge.",
        "points": [
            {"name": "Vector Embeddings", "desc": "Generate high-dimensional vector representations of documents and queries for semantic similarity."},
            {"name": "Vector Databases", "desc": "Store and query embeddings efficiently using tools like FAISS, Pinecone, or Weaviate."},
            {"name": "RAG Pipelines", "desc": "Integrate retrieval outputs into LLM generation pipelines for more accurate and context-aware responses."}
        ],
        "links": [
            {"name": "Pinecone Docs", "url": "https://www.pinecone.io/docs/"},
            {"name": "LangChain RAG Tutorial", "url": "https://www.langchain.com/docs/use_cases/retrieval_augmentation"}
        ]
    },
    {
        "title": "Distributed Training & Optimization",
        "description": "Scaling LLMs efficiently requires expertise in distributed training and memory optimization techniques. In this stage, you will learn how to split computations across multiple GPUs or nodes using data and model parallelism, implement gradient accumulation and mixed-precision training to optimize memory usage, and leverage sharding and checkpointing to safely resume large-scale training. Mastering these concepts ensures that you can train state-of-the-art models efficiently, reducing computational costs while maintaining high performance and stability across clusters of hardware.",
        "points": [
            {"name": "Data & Model Parallelism", "desc": "Distribute computation across GPUs or nodes to handle models larger than a single device's memory."},
            {"name": "Gradient Accumulation & Mixed Precision", "desc": "Optimize memory usage and speed by accumulating gradients and using FP16/FP32 mixed precision training."},
            {"name": "Sharding & Checkpointing", "desc": "Safely resume large-scale training by partitioning models and saving intermediate checkpoints."}
        ],
        "links": [
            {"name": "PyTorch DDP Tutorial", "url": "https://pytorch.org/tutorials/intermediate/ddp_tutorial.html"},
            {"name": "TensorRT-LLM", "url": "https://developer.nvidia.com/tensorrt"}
        ]
    },
    {
        "title": "Deployment & MLOps",
        "description": "Deploying LLMs in production requires a solid understanding of MLOps practices. This stage covers serving LLMs through APIs using FastAPI, Triton, or containerized services, setting up monitoring and logging to track latency, throughput, and resource usage, and implementing CI/CD pipelines to automate testing, retraining, and versioning. You will also learn strategies for scaling models for high-demand scenarios and ensuring reliability, robustness, and maintainability in real-world applications. Mastery ensures that your models can move seamlessly from research to production environments.",
        "points": [
            {"name": "Serving LLMs", "desc": "Deploy APIs for your models using FastAPI, Triton, or Docker/Kubernetes containerized services."},
            {"name": "Monitoring & Logging", "desc": "Track key performance metrics like latency, throughput, errors, and resource utilization for model health."},
            {"name": "CI/CD for LLMs", "desc": "Automate testing, retraining, deployment, and version control to ensure smooth model updates in production."}
        ],
        "links": [
            {"name": "FastAPI Deployment", "url": "https://fastapi.tiangolo.com/tutorial/first-steps/"},
            {"name": "Weights & Biases", "url": "https://wandb.ai/site"}
        ]
    },
    {
        "title": "Evaluation & Metrics",
        "description": "Evaluating LLMs is critical for ensuring reliability, performance, and alignment with task requirements. You will learn quantitative metrics such as perplexity, loss functions, BLEU, ROUGE, and F1-score for assessing model quality. Additionally, human evaluation and qualitative assessment methods provide insights into output coherence, relevance, and ethical alignment. Understanding these evaluation techniques allows you to systematically improve LLM performance, fine-tune models effectively, and measure real-world effectiveness in NLP and multimodal tasks.",
        "points": [
            {"name": "Perplexity & Loss Metrics", "desc": "Measure how well the model predicts the next token and overall language modeling performance."},
            {"name": "Task-Specific Metrics", "desc": "Use metrics like BLEU, ROUGE, and F1-score to evaluate specific NLP tasks such as summarization or classification."},
            {"name": "Human Evaluation", "desc": "Perform subjective assessment to evaluate output quality, relevance, and ethical considerations."}
        ],
        "links": [
            {"name": "Evaluation Metrics Overview", "url": "https://huggingface.co/docs/evaluate"}
        ]
    },
    {
        "title": "Multimodal LLMs",
        "description": "This stage introduces multimodal models that handle multiple input types such as text, images, and audio. You will learn vision-language models like CLIP and BLIP, audio-language models for speech-to-text and text-to-speech, and integration techniques to combine embeddings from different modalities. Mastering multimodal LLMs allows you to build richer AI applications that can understand and generate across various types of data, enhancing creativity, accessibility, and practical utility in real-world scenarios.",
        "points": [
            {"name": "Vision-Language Models", "desc": "Learn CLIP, BLIP, or GPT-4 multimodal approaches to handle text and image inputs."},
            {"name": "Audio-Language Models", "desc": "Implement speech-to-text, text-to-speech, and audio embeddings for multimodal tasks."},
            {"name": "Integration Techniques", "desc": "Combine embeddings from different modalities effectively to create unified representations for downstream tasks."}
        ],
        "links": [
            {"name": "Multimodal Models on HuggingFace", "url": "https://huggingface.co/models?pipeline_tag=multimodal"}
        ]
    },
    {
        "title": "Advanced Research & Community Engagement",
        "description": "Stay at the cutting edge of LLM research and actively engage with the AI community. You will explore emerging architectures like LLaMA, Falcon, and Mistral, and learn efficiency techniques such as sparse models, pruning, and quantization. Regularly reading research papers, blogs, and participating in AI communities, competitions, and open-source projects will enhance your practical skills and network. This stage ensures that you remain informed about breakthroughs, contribute to collaborative projects, and continuously improve your understanding and implementation of state-of-the-art LLMs.",
        "points": [
            {"name": "Emerging LLM Architectures", "desc": "Stay updated with new models like LLaMA, Falcon, and Mistral, and analyze their architecture and performance."},
            {"name": "Sparse & Efficient Models", "desc": "Learn techniques such as mixture-of-experts, pruning, and quantization for resource-efficient LLMs."},
            {"name": "Research Papers & Blogs", "desc": "Read ArXiv papers, OpenAI and HuggingFace blogs, and follow leading researchers to stay current with innovations."},
            {"name": "Community & Competitions", "desc": "Engage in forums, hackathons, and open-source projects to gain practical experience and collaborate with peers."}
        ],
        "links": [
            {"name": "ArXiv NLP Papers", "url": "https://arxiv.org/list/cs.CL/recent"},
            {"name": "OpenAI Research Blog", "url": "https://openai.com/research"},
            {"name": "HuggingFace Forums", "url": "https://discuss.huggingface.co/"},
            {"name": "Kaggle Competitions", "url": "https://www.kaggle.com/competitions"}
        ]
    },
    {
        "title": "Continuous Learning & Industry Trends",
        "description": "The field of LLMs evolves rapidly, making continuous learning crucial for long-term success. Stay up-to-date with new techniques, frameworks, model releases, and evaluation metrics. Follow AI conferences, webinars, newsletters, blogs, and social media channels of leading organizations. Engage in online courses, certifications, and community projects to refine your skills. This stage ensures you maintain a deep understanding of current trends, adopt best practices, and remain competitive as an LLM engineer throughout your career.",
        "points": [
            {"name": "Emerging Techniques", "desc": "Keep track of new model architectures, optimization methods, and multimodal integrations."},
            {"name": "Conferences & Webinars", "desc": "Attend AI and NLP conferences like NeurIPS, ACL, ICML, and workshops to learn from experts."},
            {"name": "Certifications & Courses", "desc": "Complete online certifications to validate skills in deep learning, LLMs, and NLP."},
            {"name": "Community Participation", "desc": "Stay active in forums, GitHub projects, and discussion groups to exchange knowledge and learn collaboratively."}
        ],
        "links": [
            {"name": "AI Conferences Overview", "url": "https://www.topbots.com/ai-conferences/"},
            {"name": "HuggingFace Courses", "url": "https://huggingface.co/course/chapter1"},
            {"name": "DeepLearning.AI Specializations", "url": "https://www.deeplearning.ai/"}
        ]
    }
]

def render_page():
    return render_template("roadmaps/llm_engineer.html", roadmap=LLM_ENGINEER_ROADMAP)


# ---------------- Standalone Runner (for testing only) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for("llm_engineer"))

    @app.route("/llm_engineer")
    def llm_engineer():
        return render_page()

    app.run(debug=True)
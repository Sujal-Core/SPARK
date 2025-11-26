# roadmap/edge_road.py
from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory (project_root/templates)
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

AI_RESEARCH_SCIENTIST_ROADMAP = [
    {
        "title": "1. Strong Programming & Math Foundations",
        "description": "AI Research requires deep mathematical and computational knowledge. Build mastery in programming, calculus, linear algebra, and probability.",
        "points": [
            {"name": "Python for Research", "desc": "NumPy internals, vectorization, decorators, generators, memory model"},
            {"name": "Advanced Linear Algebra", "desc": "Matrix calculus, eigendecomposition, SVD, norms, orthogonality"},
            {"name": "Probability & Statistics", "desc": "Bayesian rules, distributions, entropy, KL divergence"},
            {"name": "Optimization Basics", "desc": "Gradient descent variations, convexity, Lagrange multipliers"}
        ],
        "links": [
            {"name": "MIT Linear Algebra (Gilbert Strang)", "url": "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"},
            {"name": "Mathematics for Machine Learning", "url": "https://www.coursera.org/specializations/mathematics-machine-learning"}
        ],
        "other_resources": [
            {"name": "Python Scientific Docs", "url": "https://docs.scipy.org/doc/"},
            {"name": "Probability Cheatsheet", "url": "https://stanford.edu/~shervine/teaching/cs-229/cheatsheet-probability"}
        ]
    },

    {
        "title": "2. Deep Learning Fundamentals",
        "description": "Learn the fundamentals of neural networks that power modern AI research—MLPs, CNNs, RNNs, optimization, and regularization.",
        "points": [
            {"name": "Neural Networks", "desc": "Forward/backpropagation, loss functions, activation functions"},
            {"name": "CNNs", "desc": "Convolutions, pooling, feature hierarchy, classical architectures"},
            {"name": "RNNs/LSTMs", "desc": "Sequential modeling, vanishing gradients, gating mechanisms"},
            {"name": "Training Dynamics", "desc": "BatchNorm, Dropout, weight initialization, LR schedulers"}
        ],
        "links": [
            {"name": "DeepLearning.ai Specialization", "url": "https://www.coursera.org/specializations/deep-learning"},
            {"name": "fast.ai DL Course", "url": "https://course.fast.ai/"}
        ],
        "other_resources": [
            {"name": "D2L Book", "url": "https://d2l.ai/"},
            {"name": "PyTorch Docs", "url": "https://pytorch.org/docs/stable/"}
        ]
    },

    {
        "title": "3. Transformers & LLM Foundations",
        "description": "Master the architecture powering GPT, BERT, LLaMA, Gemini, and modern AI.",
        "points": [
            {"name": "Self-Attention", "desc": "Scaled dot-product attention, multi-head attention"},
            {"name": "Positional Encodings", "desc": "Absolute, relative, rotary embeddings"},
            {"name": "Transformer Models", "desc": "BERT, GPT, T5, ViT, LLaMA tokenization & training"},
            {"name": "LLM Scaling Laws", "desc": "Chinchilla scaling, compute-optimal training"}
        ],
        "links": [
            {"name": "Stanford CS25 Transformers Course", "url": "https://web.stanford.edu/class/cs25/"},
            {"name": "HuggingFace NLP Course", "url": "https://huggingface.co/learn/nlp-course"}
        ],
        "other_resources": [
            {"name": "Attention is All You Need", "url": "https://arxiv.org/abs/1706.03762"},
            {"name": "OpenAI Scaling Laws Paper", "url": "https://arxiv.org/abs/2001.08361"}
        ]
    },

    {
        "title": "4. Machine Learning Research Techniques",
        "description": "Develop research skills for experimentation, reproducibility, benchmarking, and literature review.",
        "points": [
            {"name": "Experiment Design", "desc": "Ablation studies, hyperparameter sweeps, scientific reporting"},
            {"name": "Reproducibility", "desc": "Seed fixing, deterministic training, experiment logging"},
            {"name": "Benchmarking", "desc": "Fair comparison, baselines, metrics"},
            {"name": "Paper Reading", "desc": "Understanding methods, assumptions, contributions"}
        ],
        "links": [
            {"name": "Weights & Biases Course", "url": "https://www.wandb.courses/"},
        ],
        "other_resources": [
            {"name": "ML Reproducibility Checklist", "url": "https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf"}
        ]
    },

    {
        "title": "5. Advanced Optimization for Deep Learning",
        "description": "Research-grade training requires advanced optimization and stability techniques.",
        "points": [
            {"name": "Optimizers", "desc": "AdamW, Adafactor, SGD-M, Lion, Shampoo"},
            {"name": "Regularization", "desc": "Dropout, label smoothing, stochastic depth"},
            {"name": "Stability", "desc": "Gradient clipping, FP16/FP8, loss scaling"},
            {"name": "Initialization", "desc": "Xavier, Kaiming, μP scaling"}
        ],
        "links": [],
        "other_resources": [
            {"name": "μP Initialization Paper", "url": "https://arxiv.org/abs/2203.03466"}
        ]
    },

    {
        "title": "6. Vision Research (CV)",
        "description": "Deep dive into modern vision architectures beyond CNNs, including ViT, Diffusion Models, and multimodal systems.",
        "points": [
            {"name": "ViT & MLP-Mixer", "desc": "Patch embeddings, self-attention for images"},
            {"name": "Diffusion Models", "desc": "DDPMs, score-based models, latent diffusion"},
            {"name": "Self-Supervised CV", "desc": "SimCLR, MoCo, DINO, MAE"},
            {"name": "Detection/Segmentation", "desc": "YOLO, Mask R-CNN, SAM"}
        ],
        "links": [],
        "other_resources": [
            {"name": "Vision Transformers (Google)", "url": "https://arxiv.org/abs/2010.11929"},
            {"name": "Stable Diffusion Paper", "url": "https://arxiv.org/abs/2112.10752"}
        ]
    },

    {
        "title": "7. Reinforcement Learning",
        "description": "Critical for robotics, game AI, autonomous agents, RLHF, and decision-making systems.",
        "points": [
            {"name": "Classical RL", "desc": "Q-learning, SARSA, value/policy iteration"},
            {"name": "Deep RL", "desc": "DQN, PPO, A3C, SAC"},
            {"name": "RLHF", "desc": "Preference modeling, reward models, PPO training"},
            {"name": "Simulation", "desc": "Gymnasium, Isaac Gym, Mujoco"}
        ],
        "links": [
            {"name": "DeepMind RL Course", "url": "https://www.deepmind.com/learning-resources"},
        ],
        "other_resources": [
            {"name": "Spinning Up by OpenAI", "url": "https://spinningup.openai.com/"}
        ]
    },

    {
        "title": "8. AI Safety & Alignment",
        "description": "Learn safety techniques needed for training reliable, ethical, and controllable AI systems.",
        "points": [
            {"name": "Red-Teaming", "desc": "Adversarial prompts, jailbreak vulnerabilities"},
            {"name": "Eval Suites", "desc": "Safety benchmarks, bias evaluation"},
            {"name": "Alignment", "desc": "RLHF, constitutional AI, reward hacking"},
            {"name": "Interpretability", "desc": "Feature attribution, activation patching"}
        ],
        "links": [
            {"name": "Anthropic Safety Papers", "url": "https://www.anthropic.com/research"}
        ],
        "other_resources": [
            {"name": "OpenAI Safety", "url": "https://openai.com/safety"}
        ]
    },

    {
        "title": "9. Generative AI",
        "description": "Learn cutting-edge generative models powering modern AI applications.",
        "points": [
            {"name": "GANs", "desc": "StyleGAN, CycleGAN, Progressive GANs"},
            {"name": "VAEs", "desc": "Latent space modeling"},
            {"name": "Diffusion Models", "desc": "Stable Diffusion, Imagen, DALLE architectures"},
            {"name": "LLM Fine-Tuning", "desc": "SFT, LoRA, QLoRA, PEFT methods"}
        ],
        "links": [
            {"name": "Generative AI Google Course", "url": "https://www.cloudskillsboost.google/paths/118"}
        ],
        "other_resources": [
            {"name": "LoRA Paper", "url": "https://arxiv.org/abs/2106.09685"}
        ]
    },

    {
        "title": "10. Scientific Computing & Large-Scale Training",
        "description": "AI research requires distributed computing and cluster-level training.",
        "points": [
            {"name": "Distributed Training", "desc": "DDP, ZeRO, FSDP, DeepSpeed"},
            {"name": "Parallelism", "desc": "Tensor, pipeline, data parallel training"},
            {"name": "Cluster Scheduling", "desc": "SLURM, Ray, Kubernetes"},
            {"name": "Mixed-Precision", "desc": "FP16/FP8 performance optimization"}
        ],
        "links": [],
        "other_resources": [
            {"name": "DeepSpeed Docs", "url": "https://www.deepspeed.ai/"}
        ]
    },

    {
        "title": "11. Research Tools, Libraries & Frameworks",
        "description": "Mastering the right tools boosts research productivity and reproducibility.",
        "points": [
            {"name": "PyTorch", "desc": "Custom layers, autograd internals"},
            {"name": "JAX", "desc": "XLA compilation, functional transformations"},
            {"name": "HuggingFace", "desc": "Transformers, Diffusers, Datasets"},
            {"name": "Lightning", "desc": "Trainer loops, checkpointing"}
        ],
        "links": [],
        "other_resources": [
            {"name": "JAX Docs", "url": "https://jax.readthedocs.io/"},
            {"name": "HuggingFace Docs", "url": "https://huggingface.co/docs"}
        ]
    },

    {
        "title": "12. Scientific Paper Writing & Research Methods",
        "description": "Learn how to communicate scientific findings clearly and publish research.",
        "points": [
            {"name": "Paper Structure", "desc": "Abstract, motivation, experiments, conclusion"},
            {"name": "LaTeX", "desc": "Scientific writing, figures, tables"},
            {"name": "Peer Review", "desc": "Evaluating research quality"},
            {"name": "Open-Source Release", "desc": "Releasing code/models with documentation"}
        ],
        "links": [],
        "other_resources": [
            {"name": "NeurIPS Paper Guidelines", "url": "https://neurips.cc/Conferences/2024/PaperInformation/StyleFiles"}
        ]
    },

    {
        "title": "13. AI Ethics, Law & Responsible AI",
        "description": "Learn the societal, legal, and ethical implications of AI research.",
        "points": [
            {"name": "Bias & Fairness", "desc": "Fairness metrics, debiasing methods"},
            {"name": "Privacy", "desc": "Differential privacy, private ML"},
            {"name": "Governance", "desc": "AI policies, global regulations"},
            {"name": "Security", "desc": "Adversarial attacks, robustness"}
        ],
        "links": [],
        "other_resources": [
            {"name": "Responsible AI Microsoft", "url": "https://www.microsoft.com/ai/responsible-ai"},
        ]
    },

    {
        "title": "14. Build & Publish Real Research Projects",
        "description": "Apply all knowledge through impactful research projects.",
        "points": [
            {"name": "LLM Research", "desc": "Train small LLMs, fine-tune models on custom data"},
            {"name": "CV Research", "desc": "Self-supervised vision models"},
            {"name": "RL Projects", "desc": "Build agents in simulated environments"},
            {"name": "Scientific Paper", "desc": "Publish on arXiv, submit to conferences"}
        ],
        "links": [],
        "other_resources": [
            {"name": "Papers with Code", "url": "https://paperswithcode.com/"},
        ]
    },

    {
        "title": "15. Build Your Research Profile & Career",
        "description": "Prepare for labs such as OpenAI, DeepMind, Meta FAIR, Google Brain, MILA, and academic PhDs.",
        "points": [
            {"name": "Research Portfolio", "desc": "GitHub, documented experiments, reproducibility"},
            {"name": "Profile", "desc": "Google Scholar, LinkedIn, website"},
            {"name": "Collaboration", "desc": "Join open-source AI research communities"},
            {"name": "Internships", "desc": "Apply to DeepMind, FAIR, OpenAI, Google"}
        ],
        "links": [],
        "other_resources": [
            {"name": "AI Research Internships List", "url": "https://github.com/louisfb01/AI-Internships"}
        ]
    }
]

def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/ai_research_scientist.html", roadmap= AI_RESEARCH_SCIENTIST_ROADMAP, title="AI Research Scientist Roadmap")

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('ai_research_scientist'))

    @app.route("/ai_research_scientist")
    def ai_research_scientist():
        return render_page()

    app.run(debug=True)


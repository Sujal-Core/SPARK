# roadmap/deeplearn_road.py
from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory (project_root/templates)
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

# Deep Learning Engineer Roadmap (role-accurate variable)
DEEPLEARN_ENGINEER_ROADMAP = [
    {
        "title": "Foundations & Math",
        "description": "Establish strong mathematical and programming foundations that underpin neural network design and optimization; focus on linear algebra for tensors, calculus for gradients, probability for uncertainty, and coding fluency for experiments.",
        "points": [
            {"name": "Python Mastery", "desc": "Clean coding, OOP, NumPy broadcasting, Pandas data pipelines, and Matplotlib/Seaborn for diagnostics"},
            {"name": "Linear Algebra", "desc": "Vectors, matrices, tensor ops, eigenvalues/eigenvectors, SVD and low-rank approximations"},
            {"name": "Calculus & Optimization", "desc": "Gradients/Jacobians/Hessians, chain rule, gradient descent, momentum, adaptive optimizers"},
            {"name": "Probability & Statistics", "desc": "Distributions, MLE/MAP, Bayesian intuition, hypothesis tests, confidence intervals"},
            {"name": "Software Engineering", "desc": "Virtualenv/poetry, logging, config management, testing and experiment reproducibility"}
        ],
        "links": [
            {"name": "Mathematics for ML (Coursera)", "url": "https://www.coursera.org/specializations/mathematics-machine-learning"},
            {"name": "Python Data Science Handbook", "url": "https://jakevdp.github.io/PythonDataScienceHandbook/"}
        ],
        "other_resources": [
            {"name": "The Matrix Cookbook", "url": "https://www2.imm.dtu.dk/pubdb/edoc/imm3274.pdf"},
            {"name": "Probabilistic ML Book", "url": "https://probml.github.io/pml-book/"}
        ]
    },
    {
        "title": "Deep Learning Frameworks",
        "description": "Become productive with a major framework and understand its computation model, autograd, module APIs, and deployment pathways; complement with tools that accelerate research and prototyping.",
        "points": [
            {"name": "PyTorch", "desc": "Dynamic graphs, autograd, nn.Module patterns, DataLoader, mixed precision, TorchScript"},
            {"name": "TensorFlow/Keras", "desc": "tf.data, Keras Functional API, tf.function, SavedModel, TFLite for edge"},
            {"name": "JAX/Flax", "desc": "jit/vmap/pmap, XLA, Flax modules for high-performance research"},
            {"name": "Lightning/Fastai", "desc": "Training loops, callbacks, boilerplate reduction for faster experimentation"}
        ],
        "links": [
            {"name": "PyTorch Tutorials", "url": "https://pytorch.org/tutorials/"},
            {"name": "TensorFlow Guide", "url": "https://www.tensorflow.org/guide"},
            {"name": "JAX Documentation", "url": "https://jax.readthedocs.io/"}
        ],
        "other_resources": [
            {"name": "Lightning Docs", "url": "https://lightning.ai/docs/pytorch/stable/"},
            {"name": "fastai Course", "url": "https://course.fast.ai/"}
        ]
    },
    {
        "title": "Core Neural Networks",
        "description": "Master building blocks and training dynamics—from initialization and normalization to regularization and schedules—and learn to debug instabilities.",
        "points": [
            {"name": "MLP & Activations", "desc": "ReLU/GELU/SiLU, initialization schemes (Xavier/He), gradient pathologies"},
            {"name": "Normalization", "desc": "BatchNorm/LayerNorm/GroupNorm, residual connections and stable training"},
            {"name": "Regularization", "desc": "Dropout, weight decay, augmentation, early stopping, label smoothing"},
            {"name": "Optimizers & Schedules", "desc": "SGD+momentum, Adam/AdamW, warmup, cosine decay, one-cycle policy"},
            {"name": "Training Recipes", "desc": "AMP, gradient clipping/accumulation, distributed training setup"}
        ],
        "links": [
            {"name": "CS231n Notes", "url": "https://cs231n.github.io/"},
            {"name": "Dive into Deep Learning", "url": "https://d2l.ai/"}
        ]
    },
    {
        "title": "Computer Vision",
        "description": "Design and train modern vision architectures, build strong data/augmentation pipelines, and optimize for production and edge use-cases.",
        "points": [
            {"name": "CNNs & Variants", "desc": "ResNet/DenseNet, EfficientNet, depthwise separable convs"},
            {"name": "Detection & Segmentation", "desc": "YOLO, Faster R-CNN, RetinaNet, Mask R-CNN, U-Net/DeepLab"},
            {"name": "Vision Transformers", "desc": "ViT, Swin, DeiT, hybrid CNN-Transformer designs"},
            {"name": "Augmentations", "desc": "Albumentations, RandAugment, CutMix/MixUp"}
        ],
        "links": [
            {"name": "OpenCV Tutorials", "url": "https://docs.opencv.org/master/d9/df8/tutorial_root.html"},
            {"name": "Papers with Code (CV)", "url": "https://paperswithcode.com/area/computer-vision"}
        ],
        "other_resources": [
            {"name": "Albumentations", "url": "https://albumentations.ai/"},
            {"name": "Ultralytics YOLO Docs", "url": "https://docs.ultralytics.com/"}
        ]
    },
    {
        "title": "NLP & Sequence Modeling",
        "description": "Apply transformers and sequence models; fine-tune LLMs efficiently and ship fast inference with quantization and caching.",
        "points": [
            {"name": "Tokenization & Embeddings", "desc": "BPE/WordPiece, subwords, positional encodings, contextual embeddings"},
            {"name": "Transformers", "desc": "Encoder/decoder stacks, attention, pretraining, fine-tuning"},
            {"name": "LLM Fine-tuning", "desc": "PEFT/LoRA/QLoRA, instruction tuning, safety alignment basics"},
            {"name": "Efficient Inference", "desc": "Quantization, batching, KV cache, distillation, RAG"}
        ],
        "links": [
            {"name": "Hugging Face Docs", "url": "https://huggingface.co/docs"},
            {"name": "Illustrated Transformer", "url": "http://jalammar.github.io/illustrated-transformer/"}
        ],
        "other_resources": [
            {"name": "PEFT Library", "url": "https://huggingface.co/docs/peft/index"},
            {"name": "LangChain Docs", "url": "https://python.langchain.com/docs/get_started/introduction"}
        ]
    },
    {
        "title": "Generative Modeling",
        "description": "Use VAEs, GANs, and diffusion models; understand training stability and evaluate generation quality rigorously.",
        "points": [
            {"name": "VAEs & Flows", "desc": "ELBO training, variational inference, normalizing flows"},
            {"name": "GANs", "desc": "Adversarial training, WGAN-GP, StyleGAN, stabilization tricks"},
            {"name": "Diffusion Models", "desc": "DDPM/DDIM, classifier-free guidance, latent diffusion"},
            {"name": "Evaluation", "desc": "FID, IS, precision/recall, human eval protocols"}
        ],
        "links": [
            {"name": "Diffusion Blog (Lilian Weng)", "url": "https://lilianweng.github.io/posts/2021-07-11-diffusion/"},
            {"name": "GAN Hacks", "url": "https://github.com/soumith/ganhacks"}
        ]
    },
    {
        "title": "Optimization & Training at Scale",
        "description": "Train large models/datasets with distributed strategies, memory-efficient techniques, and robust experiment tracking.",
        "points": [
            {"name": "Distributed Training", "desc": "Data/model/pipeline parallelism, PyTorch DDP/DeepSpeed, checkpointing"},
            {"name": "Memory & Throughput", "desc": "AMP, gradient accumulation, activation checkpointing, fused kernels"},
            {"name": "Experiment Tracking", "desc": "MLflow or Weights & Biases for metrics, artifacts, reproducibility"},
            {"name": "Hyperparameter Search", "desc": "Grid/random search, Bayesian optimization, population-based training"}
        ],
        "links": [
            {"name": "PyTorch Distributed", "url": "https://pytorch.org/tutorials/intermediate/ddp_tutorial.html"},
            {"name": "DeepSpeed", "url": "https://www.deepspeed.ai/"}
        ],
        "other_resources": [
            {"name": "Weights & Biases", "url": "https://docs.wandb.ai/"},
            {"name": "Ray Tune", "url": "https://docs.ray.io/en/latest/tune/index.html"}
        ]
    },
    {
        "title": "Data Engineering for DL",
        "description": "Build reliable, high-throughput data pipelines and enforce dataset quality for robust training and evaluation.",
        "points": [
            {"name": "Datasets & Versioning", "desc": "Parquet/TFRecords/WebDataset, DVC/lakeFS for versioned data"},
            {"name": "Loaders & Caching", "desc": "tf.data/DataLoader, prefetching, sharding, mmap, HDF5/Zarr"},
            {"name": "Augmentation & Balancing", "desc": "Class imbalance remedies, curriculum learning, synthetic data"},
            {"name": "Label Quality", "desc": "Weak supervision, noise handling, consensus labels, audits"}
        ],
        "links": [
            {"name": "TFRecords Guide", "url": "https://www.tensorflow.org/tutorials/load_data/tfrecord"},
            {"name": "PyTorch Data Loading", "url": "https://pytorch.org/docs/stable/data.html"}
        ],
        "other_resources": [
            {"name": "DVC", "url": "https://dvc.org/"},
            {"name": "lakeFS", "url": "https://lakefs.io/"}
        ]
    },
    {
        "title": "Evaluation & Responsible AI",
        "description": "Design robust evaluation protocols, integrate explainability, fairness, and governance into the DL lifecycle.",
        "points": [
            {"name": "Validation & Testing", "desc": "Cross-validation, calibration, uncertainty estimates, ablations"},
            {"name": "Explainability", "desc": "Saliency maps, SHAP/LIME for tabular/text/vision where appropriate"},
            {"name": "Fairness & Bias", "desc": "Group/individual fairness metrics, mitigation strategies"},
            {"name": "Safety & Governance", "desc": "Model cards/datasheets, risk assessments, documentation"}
        ],
        "links": [
            {"name": "Model Cards", "url": "https://modelcards.withgoogle.com/about"},
            {"name": "Responsible AI Toolbox", "url": "https://responsibleaitoolbox.ai/"}
        ]
    },
    {
        "title": "Serving & MLOps",
        "description": "Ship performant inference services with CI/CD, monitor accuracy and drift, and automate the lifecycle with registries and rollouts.",
        "points": [
            {"name": "Inference Servers", "desc": "Triton, TorchServe, TF Serving; batching, CUDA graphs, dynamic shapes"},
            {"name": "APIs & Gateways", "desc": "FastAPI/Flask, gRPC/HTTP, async I/O, streaming, rate limiting"},
            {"name": "CI/CD & Rollouts", "desc": "Canary/blue-green, shadow traffic, feature flags, rollback plans"},
            {"name": "Monitoring & Drift", "desc": "Latency/throughput, accuracy, data drift, model registry/versioning"}
        ],
        "links": [
            {"name": "NVIDIA Triton", "url": "https://github.com/triton-inference-server/server"},
            {"name": "TorchServe", "url": "https://pytorch.org/serve/"}
        ],
        "other_resources": [
            {"name": "MLflow", "url": "https://mlflow.org/"},
            {"name": "Seldon Core", "url": "https://docs.seldon.io/projects/seldon-core/en/latest/"}
        ]
    },
    {
        "title": "Performance & Compression",
        "description": "Optimize models for latency and cost with quantization, pruning, distillation, and accelerator-specific runtimes.",
        "points": [
            {"name": "Quantization", "desc": "PTQ/QAT, int8/fp8/4-bit strategies, hardware-aware tuning"},
            {"name": "Pruning & Sparsity", "desc": "Unstructured/structured pruning, N:M sparsity, speed trade-offs"},
            {"name": "Distillation", "desc": "Teacher–student transfers, logit/feature matching"},
            {"name": "Accelerators", "desc": "ONNX, TensorRT, XLA, OpenVINO; graph/kernel optimizations"}
        ],
        "links": [
            {"name": "TensorRT", "url": "https://developer.nvidia.com/tensorrt"},
            {"name": "ONNX Runtime", "url": "https://onnxruntime.ai/"}
        ]
    },
    {
        "title": "Projects & Portfolio",
        "description": "Deliver end-to-end DL projects with reproducible training, rigorous evaluation, and production-ready serving; document decisions and lessons learned.",
        "points": [
            {"name": "End-to-End Project", "desc": "Dataset curation, scalable training, evaluation, serving via Triton/FastAPI"},
            {"name": "Reproducibility", "desc": "Seeds, configs, experiment tracking, deterministic ops where possible"},
            {"name": "Documentation", "desc": "Model cards, datasheets, diagrams, concise READMEs and ADRs"}
        ],
        "links": [
            {"name": "Papers with Code", "url": "https://paperswithcode.com/"},
            {"name": "Awesome Deep Learning", "url": "https://github.com/ChristosChristofidis/awesome-deep-learning"}
        ],
        "other_resources": [
            {"name": "Kaggle", "url": "https://www.kaggle.com/"},
            {"name": "W&B Reports", "url": "https://wandb.ai/site/reports"}
        ]
    },
    {
        "title": "Continuous Learning",
        "description": "Stay current with research and practice by reading papers, replicating results, participating in communities, and pursuing focused specializations.",
        "points": [
            {"name": "Paper Routine", "desc": "Track arXiv, conferences (NeurIPS/ICML/ICLR/CVPR), and implement recent methods"},
            {"name": "Open Source", "desc": "Contribute to frameworks, model hubs, and reproducible baselines"},
            {"name": "Competitions", "desc": "Kaggle and academic challenges to stress-test skills and ideas"},
            {"name": "Community & Talks", "desc": "Meetups, seminars, reading groups, and conference workshops"},
            {"name": "Specializations", "desc": "Multimodal, audio/speech, RL, VLMs, efficient LLM/ViT training"}
        ],
        "links": [
            {"name": "arXiv Sanity", "url": "http://www.arxiv-sanity.com/"},
            {"name": "AI Deadlines", "url": "https://aideadlin.es/"}
        ],
        "other_resources": [
            {"name": "The Batch Newsletter", "url": "https://www.deeplearning.ai/the-batch/"},
            {"name": "TWIML & Practical AI", "url": "https://twimlai.com/"}
        ]
    }
]

def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/deep_learning_engineer.html", roadmap= DEEPLEARN_ENGINEER_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('deep_learning_engineer'))

    @app.route("/deep_learning_engineer")
    def deep_learning_engineer():
        return render_page()

    app.run(debug=True)
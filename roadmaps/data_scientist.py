from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

# Data Scientist Roadmap (role-accurate variable)
DATA_SCIENTIST_ROADMAP = [
    {
        "title": "Programming & Software Fundamentals",
        "description": "Develop solid programming habits that make analysis reproducible and scalable. Focus on Python fluency, packaging, environments, and testing so notebooks can graduate into maintainable modules and services. Learn to design small utilities, write clear docstrings, and structure projects for collaboration and CI.",
        "points": [
            {"name": "Python Core", "desc": "Data types, control flow, functions, OOP, iterators/generators, list/dict comprehensions"},
            {"name": "Data Stack", "desc": "NumPy broadcasting, Pandas indexing/groupby/window ops, vectorization for speed"},
            {"name": "Engineering Basics", "desc": "venv/conda/poetry, logging, typing, unit tests (pytest), CLI packaging"},
            {"name": "Notebooks → Modules", "desc": "Refactor exploratory notebooks into reusable modules and pipelines"}
        ],
        "links": [
            {"name": "Python Docs", "url": "https://docs.python.org/3/"},
            {"name": "Pandas User Guide", "url": "https://pandas.pydata.org/docs/user_guide/index.html"}
        ],
        "other_resources": [
            {"name": "Effective Python", "url": "https://effectivepython.com/"},
            {"name": "Cookiecutter Data Science", "url": "https://drivendata.github.io/cookiecutter-data-science/"}
        ]
    },
    {
        "title": "Math & Statistics for DS",
        "description": "Strengthen intuition for variability, uncertainty, and inference. Translate business questions into statistical hypotheses, choose valid tests, and quantify uncertainty. Build the calculus and linear algebra needed to understand optimization and regularization in ML.",
        "points": [
            {"name": "Probability", "desc": "Random variables, common distributions, Bayes’ rule, expectation/variance"},
            {"name": "Statistical Inference", "desc": "Confidence intervals, hypothesis tests, p-values, power, A/B testing"},
            {"name": "Linear Algebra", "desc": "Vectors, matrices, eigen/SVD, projections, least squares and geometry of regression"},
            {"name": "Calculus & Optimization", "desc": "Gradients, convexity, L1/L2 regularization, constrained optimization basics"}
        ],
        "links": [
            {"name": "Mathematics for ML (Coursera)", "url": "https://www.coursera.org/specializations/mathematics-machine-learning"},
            {"name": "Khan Academy Stats", "url": "https://www.khanacademy.org/math/statistics-probability"}
        ],
        "other_resources": [
            {"name": "The Elements of Statistical Learning", "url": "https://hastie.su.domains/ElemStatLearn/"},
            {"name": "Statistical Rethinking", "url": "https://xcelab.net/rm/statistical-rethinking/"}
        ]
    },
    {
        "title": "Data Acquisition & Cleaning",
        "description": "Collect, parse, and normalize data from files, APIs, and the web. Build resilient ingestion that handles encoding, missingness, outliers, units, and schema drift. Document assumptions and data provenance for downstream trust and reproducibility.",
        "points": [
            {"name": "Files & Formats", "desc": "CSV/Parquet/JSON; date/time parsing, categorical handling, schema validation"},
            {"name": "APIs & Web", "desc": "Requests/HTTP, pagination and rate limits, auth, scraping with BeautifulSoup/Scrapy"},
            {"name": "Cleaning Toolkit", "desc": "Missing data strategies, outlier rules, deduplication, text/locale normalization"},
            {"name": "Quality & Provenance", "desc": "Data dictionaries, expectations, lineage, and versioned raw vs curated layers"}
        ],
        "links": [
            {"name": "Requests", "url": "https://requests.readthedocs.io/en/latest/"},
            {"name": "BeautifulSoup", "url": "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"}
        ],
        "other_resources": [
            {"name": "Scrapy", "url": "https://docs.scrapy.org/en/latest/"},
            {"name": "Great Expectations", "url": "https://docs.greatexpectations.io/"}
        ]
    },
    {
        "title": "SQL & Data Management",
        "description": "Query relational data efficiently and correctly. Learn indexing, joins, window functions, CTEs, and analytical SQL patterns. Understand data warehousing concepts and when to use NoSQL or lakehouse patterns in analytics workflows.",
        "points": [
            {"name": "Analytical SQL", "desc": "JOINs, GROUP BY, window functions, CTEs, pivot/unpivot, subqueries"},
            {"name": "Modeling & Warehousing", "desc": "Star/snowflake schemas, dimensional modeling, partitioning and clustering"},
            {"name": "Practical Tuning", "desc": "Indexes, explain plans, avoiding anti-patterns for large scans"}
        ],
        "links": [
            {"name": "PostgreSQL Docs", "url": "https://www.postgresql.org/docs/"},
            {"name": "Mode SQL Tutorial", "url": "https://mode.com/sql-tutorial/"}
        ],
        "other_resources": [
            {"name": "SQLBolt", "url": "https://sqlbolt.com/"},
            {"name": "Data Warehouse Toolkit", "url": "https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/"}
        ]
    },
    {
        "title": "Exploratory Data Analysis (EDA)",
        "description": "Profile datasets to uncover distributions, relationships, leakage, and data quality issues before modeling. Use visual and statistical summaries to guide feature engineering and model selection, capturing insights in narrative form.",
        "points": [
            {"name": "Profiling & Summaries", "desc": "Univariate summaries, pairwise plots, correlations, missingness maps"},
            {"name": "Leakage & Bias Checks", "desc": "Time leakage, target leakage, sampling bias, spurious correlations"},
            {"name": "Reproducible EDA", "desc": "Notebook hygiene, checkpoints, scripts and reports with clear artifacts"}
        ],
        "links": [
            {"name": "Pandas Profiling (YData)", "url": "https://docs.ydata.ai/docs/pandas-profiling/"},
            {"name": "Seaborn", "url": "https://seaborn.pydata.org/"}
        ],
        "other_resources": [
            {"name": "Sweetviz", "url": "https://github.com/fbdesignpro/sweetviz"},
            {"name": "skimpy", "url": "https://github.com/aeturrell/skimpy"}
        ]
    },
    {
        "title": "Visualization & Storytelling",
        "description": "Communicate insights clearly to technical and non-technical audiences. Design charts for cognition, use interactivity where it adds value, and build dashboards that tie metrics to decisions and actions.",
        "points": [
            {"name": "Core Plotting", "desc": "Matplotlib, Seaborn, Plotly; small multiples, annotations, uncertainty visualizations"},
            {"name": "Dashboards", "desc": "Streamlit/Plotly Dash/Power BI/Tableau for interactive storytelling"},
            {"name": "Design Principles", "desc": "Choosing encodings, color and accessibility, avoiding misleading graphics"}
        ],
        "links": [
            {"name": "Plotly", "url": "https://plotly.com/python/"},
            {"name": "Streamlit", "url": "https://docs.streamlit.io/"}
        ],
        "other_resources": [
            {"name": "Storytelling with Data", "url": "https://www.storytellingwithdata.com/"},
            {"name": "Data Viz Catalogue", "url": "https://datavizcatalogue.com/"}
        ]
    },
    {
        "title": "Machine Learning Fundamentals",
        "description": "Build a principled modeling workflow from baseline to tuned model. Understand bias–variance tradeoffs, regularization, feature scaling, and algorithmic assumptions to choose models that fit data and objectives.",
        "points": [
            {"name": "Supervised Learning", "desc": "Linear/logistic regression, trees, random forests, gradient boosting (XGBoost/LightGBM/CatBoost)"},
            {"name": "Unsupervised Learning", "desc": "k-means, hierarchical clustering, DBSCAN, PCA/t-SNE/UMAP"},
            {"name": "Pipelines", "desc": "scikit-learn pipelines, transformers, ColumnTransformer, custom steps"}
        ],
        "links": [
            {"name": "scikit-learn", "url": "https://scikit-learn.org/stable/"},
            {"name": "XGBoost", "url": "https://xgboost.readthedocs.io/"}
        ],
        "other_resources": [
            {"name": "LightGBM", "url": "https://lightgbm.readthedocs.io/"},
            {"name": "CatBoost", "url": "https://catboost.ai/"}
        ]
    },
    {
        "title": "Model Evaluation & Experimentation",
        "description": "Choose metrics that match business goals and data properties. Build robust validation schemes, track experiments, and compare models fairly to avoid overfitting to the leaderboard.",
        "points": [
            {"name": "Metrics", "desc": "Classification (ROC-AUC, F1, PR-AUC), regression (RMSE/MAE), ranking and calibration"},
            {"name": "Validation", "desc": "Stratified k-fold, time-series split, nested CV, leakage prevention"},
            {"name": "Experiment Tracking", "desc": "MLflow/W&B for metrics, parameters, artifacts, and comparisons"}
        ],
        "links": [
            {"name": "MLflow", "url": "https://mlflow.org/"},
            {"name": "Weights & Biases", "url": "https://docs.wandb.ai/"}
        ],
        "other_resources": [
            {"name": "scikit-learn Model Evaluation", "url": "https://scikit-learn.org/stable/modules/model_evaluation.html"},
            {"name": "Calibrated Probabilities", "url": "https://scikit-learn.org/stable/modules/calibration.html"}
        ]
    },
    {
        "title": "Feature Engineering & Selection",
        "description": "Extract predictive signal and reduce noise. Engineer domain features, handle categorical variables thoughtfully, and select features that improve generalization and maintainability.",
        "points": [
            {"name": "Encodings", "desc": "One-hot, target encoding, hashing; leakage-safe encoders in CV"},
            {"name": "Transforms", "desc": "Scaling/normalization, binning, interactions, spline/lag features"},
            {"name": "Selection", "desc": "Filter/wrapper/embedded methods, SHAP-based selection, stability checks"}
        ],
        "links": [
            {"name": "Category Encoders", "url": "https://contrib.scikit-learn.org/category_encoders/"},
            {"name": "SHAP", "url": "https://shap.readthedocs.io/en/latest/"}
        ],
        "other_resources": [
            {"name": "Featuretools", "url": "https://www.featuretools.com/"},
            {"name": "skrebate", "url": "https://epistasislab.github.io/scikit-rebate/"}
        ]
    },
    {
        "title": "Advanced Topics",
        "description": "Dive into ensembles, time series, causal inference, and recommendation systems. Understand assumptions and failure modes so models remain trustworthy when deployed.",
        "points": [
            {"name": "Ensembles", "desc": "Stacking/blending/bagging/boosting, diversity and error decomposition"},
            {"name": "Time Series", "desc": "ARIMA/ETS, Prophet, features (lags/rolling), backtesting and leakage control"},
            {"name": "Causal Inference", "desc": "RCTs vs observational, propensity scores, diff-in-diff, uplift modeling"}
        ],
        "links": [
            {"name": "statsmodels", "url": "https://www.statsmodels.org/"},
            {"name": "Facebook Prophet", "url": "https://facebook.github.io/prophet/"}
        ],
        "other_resources": [
            {"name": "DoWhy (Causal)", "url": "https://microsoft.github.io/dowhy/"},
            {"name": "EconML", "url": "https://econml.azurewebsites.net/"}
        ]
    },
    {
        "title": "NLP & Text Analytics",
        "description": "Turn unstructured text into structured signal. Preprocess robustly, represent text with classical and modern embeddings, and build classification, topic, and similarity systems.",
        "points": [
            {"name": "Preprocessing", "desc": "Tokenization, normalization, stopwords, phrase detection, lemmatization"},
            {"name": "Representations", "desc": "TF–IDF, word2vec/GloVe/fastText, sentence embeddings"},
            {"name": "Tasks", "desc": "Classification, NER, topic modeling, semantic search with vector DBs"}
        ],
        "links": [
            {"name": "spaCy", "url": "https://spacy.io/"},
            {"name": "Hugging Face", "url": "https://huggingface.co/docs"}
        ],
        "other_resources": [
            {"name": "Gensim", "url": "https://radimrehurek.com/gensim/"},
            {"name": "Sentence-Transformers", "url": "https://www.sbert.net/"}
        ]
    },
    {
        "title": "Deep Learning Basics",
        "description": "Adopt neural approaches for vision, text, and tabular data where they drive value. Start with small, well-regularized models and scale thoughtfully as data and requirements justify complexity.",
        "points": [
            {"name": "Frameworks", "desc": "PyTorch or TensorFlow/Keras for prototyping and training"},
            {"name": "Architectures", "desc": "CNNs for images, RNN/Transformers for sequences, MLPs for tabular"},
            {"name": "Practices", "desc": "Early stopping, checkpoints, mixed precision, transfer learning"}
        ],
        "links": [
            {"name": "PyTorch Tutorials", "url": "https://pytorch.org/tutorials/"},
            {"name": "Keras Guides", "url": "https://keras.io/"}
        ],
        "other_resources": [
            {"name": "fastai", "url": "https://www.fast.ai/"},
            {"name": "D2L.ai", "url": "https://d2l.ai/"}
        ]
    },
    {
        "title": "Production & MLOps for DS",
        "description": "Bridge the gap from notebook to production. Build pipelines, automate retraining, and expose models behind reliable APIs with CI/CD, monitoring, and governance for data and models.",
        "points": [
            {"name": "Pipelines", "desc": "Airflow/Prefect/Kedro for data and training orchestration"},
            {"name": "Experiment & Registry", "desc": "MLflow/W&B tracking, model registry, lineage and approvals"},
            {"name": "Serving & Monitoring", "desc": "FastAPI/Flask, batch vs real-time, drift/quality monitors and alerts"}
        ],
        "links": [
            {"name": "Prefect", "url": "https://docs.prefect.io/"},
            {"name": "Kedro", "url": "https://docs.kedro.org/"}
        ],
        "other_resources": [
            {"name": "Seldon Core", "url": "https://docs.seldon.io/projects/seldon-core/en/latest/"},
            {"name": "Evidently AI", "url": "https://docs.evidentlyai.com/"}
        ]
    },
    {
        "title": "Big Data & Distributed Computing",
        "description": "Scale processing and modeling with distributed frameworks. Choose Spark for large-scale ETL and MLlib when data exceeds single-node memory and latency isn’t real-time critical.",
        "points": [
            {"name": "Spark", "desc": "Spark SQL, DataFrames, MLlib pipelines and model selection"},
            {"name": "Dask/Ray", "desc": "Scale Python workloads with minimal code changes and cluster execution"},
            {"name": "Storage & Lakes", "desc": "Object storage, partitioning, file formats, and compute–storage separation"}
        ],
        "links": [
            {"name": "Apache Spark", "url": "https://spark.apache.org/docs/latest/"},
            {"name": "Dask", "url": "https://docs.dask.org/en/stable/"}
        ],
        "other_resources": [
            {"name": "Ray", "url": "https://docs.ray.io/en/latest/"},
            {"name": "Delta Lake", "url": "https://docs.delta.io/latest/index.html"}
        ]
    },
    {
        "title": "Cloud & Tooling",
        "description": "Leverage cloud platforms for storage, compute, and managed ML services. Standardize environments and credentials, and adopt cost-aware patterns for experimentation and production.",
        "points": [
            {"name": "Cloud Platforms", "desc": "AWS/GCP/Azure fundamentals, IAM, storage, notebooks, and managed ML"},
            {"name": "Environments", "desc": "Docker for reproducible dev, Makefiles or tox for repeatable tasks"},
            {"name": "Data Apps", "desc": "Streamlit/Gradio for quick internal tools and experiment sharing"}
        ],
        "links": [
            {"name": "AWS ML Services", "url": "https://aws.amazon.com/machine-learning/"},
            {"name": "Google Vertex AI", "url": "https://cloud.google.com/vertex-ai"}
        ],
        "other_resources": [
            {"name": "Azure ML", "url": "https://learn.microsoft.com/azure/machine-learning/"},
            {"name": "Gradio", "url": "https://www.gradio.app/docs"}
        ]
    },
    {
        "title": "Business & Communication",
        "description": "Translate analysis into impact. Tie metrics to objectives, set baselines and targets, and communicate trade-offs and risks clearly to stakeholders through concise narratives and visuals.",
        "points": [
            {"name": "Problem Framing", "desc": "KPIs, constraints, success criteria, counterfactuals, and sensitivities"},
            {"name": "Stakeholder Comms", "desc": "Narrative memos, dashboards with context, and scenario analysis"},
            {"name": "Decision Support", "desc": "AB tests, lift analyses, confidence intervals, and what-if tools"}
        ],
        "links": [
            {"name": "Google Analytics Academy (foundational thinking)", "url": "https://analytics.google.com/analytics/academy/"},
            {"name": "Storytelling with Data", "url": "https://www.storytellingwithdata.com/"}
        ]
    },
    {
        "title": "Ethics & Responsible AI",
        "description": "Build trustworthy systems by addressing bias, privacy, and transparency. Document data sources and model behavior, and implement guardrails for safe deployment in sensitive contexts.",
        "points": [
            {"name": "Bias & Fairness", "desc": "Group/individual fairness metrics, mitigation strategies across pipeline"},
            {"name": "Transparency", "desc": "Explainability (SHAP/LIME), model/data cards, audit trails"},
            {"name": "Privacy & Policy", "desc": "PII handling, differential privacy basics, governance and approvals"}
        ],
        "links": [
            {"name": "Model Cards", "url": "https://modelcards.withgoogle.com/about"},
            {"name": "Responsible AI Toolbox", "url": "https://responsibleaitoolbox.ai/"}
        ],
        "other_resources": [
            {"name": "Partnership on AI", "url": "https://partnershiponai.org/"},
            {"name": "Aequitas (Fairness Audit)", "url": "http://aequitas.dssg.io/"}
        ]
    },
    {
        "title": "Projects & Portfolio",
        "description": "Build end-to-end projects that demonstrate data acquisition, EDA, modeling, evaluation, and deployment. Prioritize clarity and replicability so reviewers can run and extend your work.",
        "points": [
            {"name": "E2E Projects", "desc": "Public datasets or realistic business problems with measurable outcomes"},
            {"name": "Reproducibility", "desc": "Clear README, data access notes, environment files, and scripts"},
            {"name": "Impact Framing", "desc": "Explain assumptions, limitations, trade-offs, and next steps"}
        ],
        "links": [
            {"name": "Papers with Code", "url": "https://paperswithcode.com/"},
            {"name": "UC Irvine ML Repo", "url": "https://archive.ics.uci.edu/"}
        ],
        "other_resources": [
            {"name": "Kaggle", "url": "https://www.kaggle.com/"},
            {"name": "DrivenData", "url": "https://www.drivendata.org/competitions/"}
        ]
    },
    {
        "title": "Continuous Learning",
        "description": "Stay current by reading papers, following trustworthy blogs and newsletters, replicating benchmarks, contributing to open source, and engaging with the community through talks and competitions.",
        "points": [
            {"name": "Paper Routine", "desc": "Track arXiv and key conferences (NeurIPS/ICML/ICLR/KDD/CVPR/NLP venues)"},
            {"name": "Open Source", "desc": "Contribute bug fixes, docs, and examples to DS/ML libraries"},
            {"name": "Competitions", "desc": "Kaggle/DrivenData for focused practice and leaderboard discipline"},
            {"name": "Community", "desc": "Meetups, reading groups, conference workshops, and mentoring"}
        ],
        "links": [
            {"name": "arXiv Sanity", "url": "http://www.arxiv-sanity.com/"},
            {"name": "AI Conference Deadlines", "url": "https://aideadlin.es/"}
        ],
        "other_resources": [
            {"name": "The Batch", "url": "https://www.deeplearning.ai/the-batch/"},
            {"name": "KDnuggets", "url": "https://www.kdnuggets.com/"}
        ]
    }
]

@app.route("/")
def home():
    return redirect(url_for('data_scientist'))

def render_page():
    return render_template("roadmaps/data_scientist.html", roadmap=DATA_SCIENTIST_ROADMAP)

# ✅ Optional standalone Flask runner for testing
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('data_scientist'))

    @app.route("/appdev")
    def app_developer():
        return render_page()

    app.run(debug=True)
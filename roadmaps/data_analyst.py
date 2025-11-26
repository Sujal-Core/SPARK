# roadmap/dataanalyst_road.py
from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory (project_root/templates)
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

# Data Analyst Roadmap (role-accurate variable)
DATA_ANALYST_ROADMAP = [
    {
        "title": "Analyst Foundations",
        "description": "Build a strong base in spreadsheets, data types, and analytical thinking. Learn to organize workbooks, use references and named ranges effectively, and structure your analysis so that inputs, transformations, and outputs are easy to audit and hand off.",
        "points": [
            {"name": "Spreadsheets", "desc": "Formulas, pivot tables, lookup/index-match, conditional logic, data validation"},
            {"name": "Data Types & Cleaning", "desc": "Dates/times, text parsing, number formats, missing values, deduplication"},
            {"name": "Analytical Mindset", "desc": "Define questions, identify assumptions, separate signal from noise, document steps"}
        ],
        "links": [
            {"name": "Google Sheets Guides", "url": "https://support.google.com/a/users/answer/9282959"},
            {"name": "Excel Training", "url": "https://support.microsoft.com/excel"}
        ],
        "other_resources": [
            {"name": "Spreadsheet Best Practices", "url": "https://www.eusprig.org/"}
        ]
    },
    {
        "title": "SQL Essentials",
        "description": "Query and transform data using SQL with confidence. Master joins, aggregations, subqueries, and window functions to answer common business questions efficiently and reproducibly.",
        "points": [
            {"name": "Core Queries", "desc": "SELECT/FROM/WHERE, GROUP BY/HAVING, ORDER/LIMIT, joins (inner/outer)"},
            {"name": "Window Functions", "desc": "ROW_NUMBER/RANK, LAG/LEAD, partitions for rolling and cumulative metrics"},
            {"name": "CTEs & Views", "desc": "Readable transformations, modularization, and shared logic for teams"}
        ],
        "links": [
            {"name": "Mode SQL Tutorial", "url": "https://mode.com/sql-tutorial/"},
            {"name": "PostgreSQL Docs", "url": "https://www.postgresql.org/docs/"}
        ],
        "other_resources": [
            {"name": "SQLBolt", "url": "https://sqlbolt.com/"},
            {"name": "LeetCode Database", "url": "https://leetcode.com/problemset/database/"}
        ]
    },
    {
        "title": "Data Modeling & Warehousing",
        "description": "Understand how data is structured for analytics. Learn dimensional modeling, star and snowflake schemas, and how partitioning and clustering affect cost and performance in warehouses.",
        "points": [
            {"name": "Dimensional Models", "desc": "Facts and dimensions, slowly changing dimensions, conformed dimensions"},
            {"name": "Warehouse Concepts", "desc": "Partitioning, clustering, materialized views, query optimization"},
            {"name": "Data Lifecycle", "desc": "Bronze/silver/gold layers, governance, and documentation for discoverability"}
        ],
        "links": [
            {"name": "BigQuery Best Practices", "url": "https://cloud.google.com/bigquery/docs/best-practices-performance-overview"},
            {"name": "Snowflake Guides", "url": "https://docs.snowflake.com/en/user-guide"}
        ],
        "other_resources": [
            {"name": "Kimball Toolkit", "url": "https://www.kimballgroup.com/"},
            {"name": "dbt Learn", "url": "https://docs.getdbt.com/docs"}
        ]
    },
    {
        "title": "Python for Analysis",
        "description": "Use Python to extend analysis beyond spreadsheets and SQL. Clean data, compute complex features, and automate repeated reporting with scripts and notebooks that are shareable and versioned.",
        "points": [
            {"name": "Pandas & NumPy", "desc": "Indexing, groupby, merges, window ops, time series, vectorization for speed"},
            {"name": "Visualization", "desc": "Matplotlib/Seaborn/Plotly for clear and trustworthy charts with annotations"},
            {"name": "Automation", "desc": "Scheduled scripts/notebooks, parameterization, environment management"}
        ],
        "links": [
            {"name": "Pandas User Guide", "url": "https://pandas.pydata.org/docs/user_guide/index.html"},
            {"name": "Seaborn Docs", "url": "https://seaborn.pydata.org/"}
        ],
        "other_resources": [
            {"name": "Plotly", "url": "https://plotly.com/python/"},
            {"name": "Papermill (parameterized notebooks)", "url": "https://papermill.readthedocs.io/"}
        ]
    },
    {
        "title": "BI Tools & Dashboards",
        "description": "Build interactive dashboards that connect insights to actions. Use filters, parameters, and drill-downs to let stakeholders explore data safely, with curated metrics and definitions.",
        "points": [
            {"name": "Tools", "desc": "Power BI/Tableau/Looker/Metabase; connectors, modeling layer, permissions"},
            {"name": "Design Patterns", "desc": "Layout, hierarchy, KPIs vs diagnostics, annotations and tooltips"},
            {"name": "Performance", "desc": "Extracts vs live, caching strategies, incremental refresh, row-level security"}
        ],
        "links": [
            {"name": "Tableau Learning", "url": "https://www.tableau.com/learn/training"},
            {"name": "Power BI Docs", "url": "https://learn.microsoft.com/power-bi/"}
        ],
        "other_resources": [
            {"name": "Looker Modeling (LookML)", "url": "https://cloud.google.com/looker/docs"},
            {"name": "Metabase Docs", "url": "https://www.metabase.com/docs/latest/"}
        ]
    },
    {
        "title": "Statistics & Experiments",
        "description": "Ground analyses in sound statistical practice. Estimate uncertainty, build confidence intervals, and design trustworthy A/B tests that account for peeking, power, and business risk.",
        "points": [
            {"name": "Descriptive Stats", "desc": "Distributions, variance, skew, correlations, robust summaries"},
            {"name": "Inference", "desc": "Confidence intervals, hypothesis testing, p-values and power"},
            {"name": "Experimentation", "desc": "A/B test design, sample size, stratification, CUPED, sequential testing"}
        ],
        "links": [
            {"name": "Khan Academy Stats", "url": "https://www.khanacademy.org/math/statistics-probability"},
            {"name": "AB Testing Guide", "url": "https://www.optimizely.com/optimization-glossary/ab-testing/"}
        ],
        "other_resources": [
            {"name": "Causal Inference Booklet", "url": "https://miguelhernan.github.io/causal-inference-book/"}
        ]
    },
    {
        "title": "Data Cleaning & Quality",
        "description": "Make analyses dependable by enforcing quality checks and documenting assumptions. Detect schema changes early, validate ranges and categories, and handle missingness transparently.",
        "points": [
            {"name": "Validation Rules", "desc": "Type checks, ranges, categorical domains, uniqueness, referential integrity"},
            {"name": "Observability", "desc": "Freshness, volume, distribution drift; alerts for upstream changes"},
            {"name": "Documentation", "desc": "Data dictionaries, lineage, and change logs for stakeholders"}
        ],
        "links": [
            {"name": "Great Expectations", "url": "https://docs.greatexpectations.io/"},
            {"name": "Soda Core", "url": "https://docs.soda.io/soda-core/"}
        ],
        "other_resources": [
            {"name": "OpenLineage", "url": "https://openlineage.io/"},
            {"name": "DataHub", "url": "https://datahubproject.io/"}
        ]
    },
    {
        "title": "Visualization & Storytelling",
        "description": "Craft narratives that lead to decisions. Use the right chart types, show uncertainty where relevant, and annotate context so that stakeholders can trust and act on results.",
        "points": [
            {"name": "Chart Literacy", "desc": "Comparisons, trends, distributions, part-to-whole, relationships"},
            {"name": "Narrative Tools", "desc": "Callouts, small multiples, color semantics, accessibility"},
            {"name": "Dashboards vs Reports", "desc": "Real-time monitoring vs point-in-time deep dives; choose accordingly"}
        ],
        "links": [
            {"name": "Data Viz Catalogue", "url": "https://datavizcatalogue.com/"},
            {"name": "Storytelling with Data", "url": "https://www.storytellingwithdata.com/"}
        ]
    },
    {
        "title": "Scripting & Automation",
        "description": "Automate recurring tasks, scheduled reports, and data refreshes. Parameterize notebooks, build small ETL scripts, and integrate with version control and CI where applicable.",
        "points": [
            {"name": "Scheduling", "desc": "Cron/Airflow/Prefect for report refreshes and batch data pulls"},
            {"name": "Parameterization", "desc": "Papermill/metaflow/notebook params for reproducible reporting"},
            {"name": "Versioning", "desc": "Git for change tracking, reviews, and safe releases"}
        ],
        "links": [
            {"name": "Prefect", "url": "https://docs.prefect.io/"},
            {"name": "Airflow", "url": "https://airflow.apache.org/docs/"}
        ],
        "other_resources": [
            {"name": "Git Basics", "url": "https://git-scm.com/doc"}
        ]
    },
    {
        "title": "Domain Knowledge & KPIs",
        "description": "Connect metrics to business levers. Learn common KPI frameworks for product, marketing, sales, and operations, and align analysis to how decisions are actually made.",
        "points": [
            {"name": "Product Metrics", "desc": "Activation, retention, engagement, funnels, cohorts, north-star metrics"},
            {"name": "Growth & Marketing", "desc": "Acquisition, CAC/LTV, attribution pitfalls, incrementality"},
            {"name": "Sales & Ops", "desc": "Pipeline, conversion, capacity, SLA/OTIF, cost and quality metrics"}
        ],
        "links": [
            {"name": "Lean Analytics", "url": "https://leananalyticsbook.com/"},
            {"name": "Google Analytics Academy", "url": "https://analytics.google.com/analytics/academy/"}
        ]
    },
    {
        "title": "Intro to ML for Analysts",
        "description": "Apply lightweight ML when justified to enhance analytics. Focus on interpretable models, careful validation, and clear explanation of impact and limitations to stakeholders.",
        "points": [
            {"name": "Classical Models", "desc": "Linear/logistic regression, decision trees, regularization, cross-validation"},
            {"name": "Practical Care", "desc": "Leakage checks, feature scaling/encoding, imbalanced data remedies"},
            {"name": "Explainability", "desc": "Coefficients, feature importance, partial dependence and SHAP basics"}
        ],
        "links": [
            {"name": "scikit-learn", "url": "https://scikit-learn.org/stable/"},
            {"name": "Imbalanced-learn", "url": "https://imbalanced-learn.org/stable/"}
        ]
    },
    {
        "title": "Portfolio & Communication",
        "description": "Package your work as case studies that show the question, approach, artifacts, and impact. Present trade-offs and alternatives, and make it easy for others to reproduce and extend.",
        "points": [
            {"name": "Case Studies", "desc": "Business framing, methodology, results, limitations, next steps"},
            {"name": "Artifacts", "desc": "Dashboards, notebooks, SQL, and data prep scripts linked together"},
            {"name": "Clarity", "desc": "Concise writing, clear visuals, and action-oriented recommendations"}
        ],
        "links": [
            {"name": "Metabase (free BI)", "url": "https://www.metabase.com/"},
            {"name": "Streamlit", "url": "https://docs.streamlit.io/"}
        ],
        "other_resources": [
            {"name": "Kaggle (datasets & notebooks)", "url": "https://www.kaggle.com/"},
            {"name": "GitHub Pages (host docs)", "url": "https://pages.github.com/"}
        ]
    },
    {
        "title": "Continuous Learning",
        "description": "Keep skills fresh by following trusted blogs and newsletters, joining communities, and practicing on real datasets. Periodically revisit fundamentals in SQL, statistics, and visualization.",
        "points": [
            {"name": "Practice", "desc": "Weekly SQL/EDA exercises and rebuild favorite dashboards from scratch"},
            {"name": "Community", "desc": "Local meetups, online forums, book clubs, and conference workshops"},
            {"name": "Reading List", "desc": "Vendor blogs (warehouse/BI), case studies, and public analytics write-ups"}
        ],
        "links": [
            {"name": "KDnuggets", "url": "https://www.kdnuggets.com/"},
            {"name": "Mode Blog", "url": "https://mode.com/blog/"}
        ],
        "other_resources": [
            {"name": "r/datascience", "url": "https://www.reddit.com/r/datascience/"},
            {"name": "Awesome Public Datasets", "url": "https://github.com/awesomedata/awesome-public-datasets"}
        ]
    }
]

def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/data_analyst.html", roadmap=DATA_ANALYST_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('data_analyst'))

    @app.route("/data_analyst")
    def data_analyst():
        return render_page()

    app.run(debug=True)
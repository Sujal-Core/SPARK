from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory
BASE_DIR = Path(__file__).resolve().parent.parent  # Correct __file__
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))  # Correct __name__
BI_ENGINEER_ROADMAP = [
    {
        "title": "Foundations of BI & Data",
        "description": "Learn the fundamental concepts of business intelligence and data, including the types of data (structured, unstructured, semi-structured) and how they are collected, processed, and analyzed. Understand the data lifecycle and the importance of data quality, accuracy, and consistency. Gain insights into how organizations use data to drive strategic decisions and optimize operations.",
        "points": [
            {"name": "Data Fundamentals", "desc": "Understand different data types (structured, unstructured, semi-structured), the data lifecycle, and the importance of clean, accurate data for analytics."},
            {"name": "Excel & Spreadsheets", "desc": "Master Excel for basic analysis including formulas, pivot tables, charts, and data manipulation techniques essential for reporting."},
            {"name": "Business Fundamentals", "desc": "Learn key business metrics, KPIs, and processes to effectively interpret data in a business context."}
        ],
        "links": [
            {"name": "Data Analysis with Excel (Coursera)", "url": "https://www.coursera.org/learn/excel-data-analysis"}
        ],
        "other_resources": [
            {"name": "Excel Documentation", "url": "https://support.microsoft.com/en-us/excel"}
        ]
    },
    {
        "title": "SQL & Databases",
        "description": "Dive deep into relational databases and SQL to extract, filter, and manipulate data effectively. Learn to combine multiple tables using joins, write subqueries for complex analytics, and understand how databases are structured. Gain knowledge of normalization, indexing, transactions, and ACID properties to ensure data integrity and optimize query performance.",
        "points": [
            {"name": "SQL Basics", "desc": "Use SELECT, WHERE, GROUP BY, HAVING, and ORDER BY statements to retrieve and filter data."},
            {"name": "Joins & Subqueries", "desc": "Understand INNER, LEFT, RIGHT, FULL joins, and nested queries to combine data from multiple tables."},
            {"name": "Database Concepts", "desc": "Learn database design concepts like normalization, indexing, transactions, and ACID properties to ensure data integrity."}
        ],
        "links": [
            {"name": "SQL for Data Science (Coursera)", "url": "https://www.coursera.org/learn/sql-for-data-science"}
        ],
        "other_resources": [
            {"name": "PostgreSQL Docs", "url": "https://www.postgresql.org/docs/"},
            {"name": "SQL W3Schools", "url": "https://www.w3schools.com/sql/"}
        ]
    },
    {
        "title": "ETL & Data Warehousing",
        "description": "Learn to build ETL (Extract, Transform, Load) pipelines to move data from source systems into centralized warehouses. Understand data cleaning, transformation, and schema design for analytics. Gain hands-on experience with ETL tools and warehouse designs (star/snowflake), and learn how OLAP and OLTP systems differ in purpose and structure.",
        "points": [
            {"name": "ETL Basics", "desc": "Understand the ETL process to move data from source systems to data warehouses, including data cleaning and transformation."},
            {"name": "Data Warehousing", "desc": "Learn warehouse schemas like star and snowflake, and differentiate OLAP and OLTP systems for analytics vs transactional workloads."},
            {"name": "ETL Tools", "desc": "Gain hands-on knowledge of tools like Apache Airflow, Talend, SSIS, and dbt for building automated data pipelines."}
        ],
        "links": [
            {"name": "Data Warehousing for Business Intelligence (Coursera)", "url": "https://www.coursera.org/learn/dwdesign"}
        ],
        "other_resources": [
            {"name": "Airflow Documentation", "url": "https://airflow.apache.org/docs/"}
        ]
    },
    {
        "title": "BI Tools & Visualization",
        "description": "Learn to convert raw data into actionable insights through dashboards and interactive visualizations. Explore different BI tools to create compelling stories that help stakeholders understand trends and patterns. Gain expertise in designing reports, tracking KPIs, and communicating data insights effectively for business decisions.",
        "points": [
            {"name": "Tableau", "desc": "Build interactive dashboards, create visual stories, and use calculated fields for data-driven presentations."},
            {"name": "Power BI", "desc": "Use Power Query, DAX, and visualization best practices to transform raw data into business insights."},
            {"name": "Looker & Others", "desc": "Understand LookML basics, KPI tracking, and other BI platforms for diverse organizational needs."}
        ],
        "links": [
            {"name": "Data Visualization with Tableau (Coursera)", "url": "https://www.coursera.org/learn/data-visualization-tableau"},
            {"name": "Getting Started with Power BI (Coursera)", "url": "https://www.coursera.org/learn/power-bi"}
        ],
        "other_resources": [
            {"name": "Tableau Public Resources", "url": "https://public.tableau.com/en-us/s/resources"},
            {"name": "Power BI Docs", "url": "https://learn.microsoft.com/en-us/power-bi/"}
        ]
    },
    {
        "title": "Data Analysis & Statistics",
        "description": "Apply statistical techniques to interpret business data, identify patterns, and make evidence-based decisions. Learn descriptive and inferential statistics, hypothesis testing, and time series analysis to forecast trends. Develop analytical thinking to draw insights that can guide strategic business actions and optimize operations.",
        "points": [
            {"name": "Descriptive Statistics", "desc": "Calculate mean, median, variance, and standard deviation to summarize and understand data."},
            {"name": "Hypothesis Testing", "desc": "Perform t-tests, chi-square tests, and analyze p-values to make informed data-driven decisions."},
            {"name": "Time Series Analysis", "desc": "Identify trends, seasonality, and forecast future values to support business planning."}
        ],
        "links": [
            {"name": "Business Statistics and Analysis (Coursera)", "url": "https://www.coursera.org/specializations/business-statistics-analysis"}
        ],
        "other_resources": [
            {"name": "Khan Academy Statistics", "url": "https://www.khanacademy.org/math/statistics-probability"}
        ]
    },
    {
        "title": "Scripting for BI",
        "description": "Enhance your BI capabilities by using programming for data automation, cleaning, transformation, and advanced analytics. Learn to fetch external data using APIs and integrate it with analytics tools. Acquire Python and R skills to perform complex data manipulations, visualizations, and predictive modeling within BI workflows.",
        "points": [
            {"name": "Python for Data Analysis", "desc": "Leverage Pandas, NumPy, Matplotlib, and Seaborn for cleaning, transforming, and visualizing data."},
            {"name": "R Programming", "desc": "Use R libraries like ggplot2, dplyr, and tidyr for statistical computing and data visualization."},
            {"name": "APIs", "desc": "Consume REST APIs to fetch external data for BI pipelines and integrate with analytics tools."}
        ],
        "links": [
            {"name": "Python for Everybody (Coursera)", "url": "https://www.coursera.org/specializations/python"}
        ],
        "other_resources": [
            {"name": "Pandas Documentation", "url": "https://pandas.pydata.org/docs/"},
            {"name": "R Documentation", "url": "https://www.r-project.org/other-docs.html"}
        ]
    },
    {
        "title": "Business & Domain Knowledge",
        "description": "Develop domain-specific understanding to contextualize BI insights for stakeholders. Learn to define key performance indicators, measure metrics, and communicate findings effectively. Gain expertise in industries such as finance, healthcare, or e-commerce to interpret data meaningfully and provide actionable insights for strategic business decisions.",
        "points": [
            {"name": "KPIs & Metrics", "desc": "Define and monitor key performance indicators to track business objectives."},
            {"name": "Domain Expertise", "desc": "Focus on industry-specific knowledge like finance, healthcare, or e-commerce to contextualize BI insights."},
            {"name": "Data Storytelling", "desc": "Translate data analysis into compelling narratives and visualizations for decision-makers."}
        ],
        "links": [
            {"name": "Business Analytics Specialization (Coursera)", "url": "https://www.coursera.org/specializations/business-analytics"}
        ],
        "other_resources": [
            {"name": "Harvard Business Review – Analytics", "url": "https://hbr.org/topic/data-analytics"}
        ]
    },
    {
        "title": "Advanced BI Topics",
        "description": "Learn advanced techniques in BI, including handling big data, implementing real-time analytics, and integrating machine learning models. Explore distributed processing frameworks and streaming solutions for large-scale, fast-paced business environments. Gain the ability to deliver predictive insights and actionable recommendations that drive business strategy.",
        "points": [
            {"name": "Big Data Tools", "desc": "Use Apache Spark and Hadoop for processing and analyzing massive datasets efficiently."},
            {"name": "Real-time Analytics", "desc": "Implement streaming pipelines using Kafka or other tools for up-to-the-minute insights."},
            {"name": "ML for BI", "desc": "Apply machine learning techniques for forecasting, churn prediction, anomaly detection, and other business use cases."}
        ],
        "links": [
            {"name": "Big Data Specialization (Coursera)", "url": "https://www.coursera.org/specializations/big-data"}
        ],
        "other_resources": [
            {"name": "Apache Spark Docs", "url": "https://spark.apache.org/docs/latest/"}
        ]
    },
    {
        "title": "Data Governance & Security",
        "description": "Ensure BI processes comply with data security, privacy, and governance standards. Learn techniques for cataloging, lineage tracking, and quality control to maintain trustworthy data. Implement encryption, access control, and privacy regulations such as GDPR and HIPAA to protect sensitive information and maintain organizational compliance.",
        "points": [
            {"name": "Data Governance", "desc": "Manage data quality, cataloging, and lineage tracking to ensure reliability and trustworthiness of data."},
            {"name": "Security & Privacy", "desc": "Implement GDPR, HIPAA compliance, encryption, and access control to protect sensitive data."},
            {"name": "Collaboration", "desc": "Use version control (Git) and collaborative platforms to maintain data and dashboard integrity across teams."}
        ],
        "links": [
            {"name": "Data Management and Visualization (Coursera)", "url": "https://www.coursera.org/learn/data-visualization-management"}
        ],
        "other_resources": [
            {"name": "Data Governance Institute", "url": "http://www.datagovernance.com/"},
            {"name": "Microsoft Security Docs", "url": "https://learn.microsoft.com/en-us/security/"}
        ]
    },
    {
        "title": "Cloud & Data Integration for BI",
        "description": "Understand cloud platforms and integrate multiple data sources for centralized BI workflows. Learn to leverage AWS, Azure, or GCP for storage, processing, and deployment. Gain skills in building data lakes and connecting APIs or SaaS platforms for scalable and efficient data analytics environments.",
        "points": [
            {"name": "Cloud Platforms", "desc": "Learn AWS, Azure, or GCP basics for BI deployments and storage."},
            {"name": "APIs & Connectors", "desc": "Integrate SaaS platforms and external data sources into BI pipelines."},
            {"name": "Data Lakes", "desc": "Store and manage unstructured and structured data for analytics and reporting."}
        ],
        "links": [
            {"name": "Cloud Data Engineering (Coursera)", "url": "https://www.coursera.org/specializations/cloud-data-engineering"}
        ],
        "other_resources": [
            {"name": "AWS Data Lakes Docs", "url": "https://docs.aws.amazon.com/datalake/index.html"}
        ]
    },
    {
        "title": "Performance Optimization & BI Scalability",
        "description": "Learn best practices for building scalable BI solutions and optimizing dashboard performance. Understand how to tune queries, design responsive dashboards, and architect data pipelines that handle increasing volumes efficiently. Ensure fast, actionable insights even as data and user load grow within the organization.",
        "points": [
            {"name": "Query Optimization", "desc": "Improve database query performance for faster BI dashboards."},
            {"name": "Dashboard Best Practices", "desc": "Design dashboards for usability, speed, and insight."},
            {"name": "Scaling BI Solutions", "desc": "Architect pipelines to handle increasing data volumes efficiently."}
        ],
        "links": [
            {"name": "Optimizing BI Dashboards (Udemy)", "url": "https://www.udemy.com/course/optimizing-bi-dashboards/"}
        ],
        "other_resources": [
            {"name": "Tableau Performance Tips", "url": "https://help.tableau.com/current/pro/desktop/en-us/performance.htm"}
        ]
    },
    {
        "title": "Automation & Scripting Advanced",
        "description": "Automate BI processes and reporting workflows to save time, reduce errors, and ensure consistency. Learn to use Python and R for ETL automation, scheduled reporting, and batch data processing. Implement task scheduling using cron jobs or Airflow DAGs to maintain recurring BI tasks seamlessly.",
        "points": [
            {"name": "Python Automation", "desc": "Automate ETL pipelines, data cleaning, and report generation."},
            {"name": "R Automation", "desc": "Use R scripts for statistical processing and batch report creation."},
            {"name": "Task Scheduling", "desc": "Implement cron jobs, Airflow DAGs, or other schedulers for recurring BI tasks."}
        ],
        "links": [
            {"name": "Python for Automation (Udemy)", "url": "https://www.udemy.com/course/python-automation/"}
        ],
        "other_resources": [
            {"name": "Airflow Docs", "url": "https://airflow.apache.org/docs/"}
        ]
    },
    {
        "title": "Continuous Learning & Professional Development",
        "description": "Stay updated with BI trends, best practices, tools, and engage with the community to grow professionally.",
        "points": [
            {"name": "Industry Trends", "desc": "Follow BI blogs, newsletters, and updates to stay informed about the latest tools and methodologies."},
            {"name": "Communities", "desc": "Participate in Tableau, Power BI, and data analytics communities to learn and network."},
            {"name": "Competitions", "desc": "Engage in Kaggle competitions, Makeover Monday challenges, and hackathons to practice skills and gain experience."}
        ],
        "links": [
            {"name": "Kaggle Courses", "url": "https://www.kaggle.com/learn"}
        ],
        "other_resources": [
            {"name": "Makeover Monday", "url": "https://www.makeovermonday.co.uk/"},
            {"name": "Towards Data Science", "url": "https://towardsdatascience.com/"}
        ]
    }
]


@app.route("/")
def home():
    return redirect(url_for('business_intelligence_engineer'))

def render_page():
    return render_template("roadmaps/business_intelligence_engineer.html", roadmap=BI_ENGINEER_ROADMAP)

# ---------------- Run Server ----------------
if __name__ == "__main__":
    app.run(debug=True)
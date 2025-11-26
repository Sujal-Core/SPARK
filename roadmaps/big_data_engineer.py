# roadmap/edge_road.py
from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory (project_root/templates)
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

BIG_DATA_ENGINEER_ROADMAP = [
    {
        "title": "1. Programming Foundations",
        "description": "Start with strong programming skills because Big Data systems require efficient, scalable coding.",
        "points": [
            {"name": "Python Basics", "desc": "Loops, lists, dicts, functions, modules"},
            {"name": "Java/Scala", "desc": "Preferred for Hadoop & Spark"},
            {"name": "OOP Concepts", "desc": "Classes, objects, inheritance, abstraction, polymorphism"}
        ],
        "links": [
            {"name": "Python for Everybody", "url": "https://www.coursera.org/specializations/python"},
            {"name": "Java Programming", "url": "https://www.coursera.org/learn/java-programming"}
        ],
        "other_resources": [
            {"name": "Python Docs", "url": "https://docs.python.org/3/"},
            {"name": "Scala Docs", "url": "https://docs.scala-lang.org/"}
        ]
    },
    {
        "title": "2. Linux, Shell & System Basics",
        "description": "Big Data platforms run on Linux. Learn terminal, file systems, and permissions.",
        "points": [
            {"name": "Shell Commands", "desc": "grep, awk, sed, ssh, scp, cronjobs"},
            {"name": "Linux Permissions", "desc": "chmod, chown, user groups"},
            {"name": "Networking Basics", "desc": "DNS, IP, ports"}
        ],
        "links": [
            {"name": "Linux for Developers", "url": "https://www.udacity.com/course/linux-command-line-basics--ud065"}
        ],
        "other_resources": [
            {"name": "GNU Bash Manual", "url": "https://www.gnu.org/software/bash/manual/"}
        ]
    },
    {
        "title": "3. Databases for Big Data",
        "description": "Learn SQL, NoSQL, distributed systems, and modern data storage.",
        "points": [
            {"name": "SQL Databases", "desc": "PostgreSQL, MySQL queries, joins, indexing"},
            {"name": "NoSQL Databases", "desc": "MongoDB, Cassandra, DynamoDB"},
            {"name": "Data Modeling", "desc": "Star schema, denormalization, sharding"}
        ],
        "links": [
            {"name": "SQL for Data Engineering (Coursera)", "url": "https://www.coursera.org/learn/sql-data-engineering"}
        ],
        "other_resources": [
            {"name": "MongoDB Docs", "url": "https://www.mongodb.com/docs/"},
            {"name": "PostgreSQL Docs", "url": "https://www.postgresql.org/docs/"}
        ]
    },
    {
        "title": "4. Hadoop Ecosystem",
        "description": "Learn how distributed storage & processing happens in Big Data systems.",
        "points": [
            {"name": "HDFS", "desc": "Replication, blocks, NameNode/DataNode"},
            {"name": "MapReduce", "desc": "Distributed computation model"},
            {"name": "YARN", "desc": "Cluster resource management"}
        ],
        "links": [
            {"name": "Hadoop Starter Course", "url": "https://www.udemy.com/course/hadoop-tutorial/"},
        ],
        "other_resources": [
            {"name": "Hadoop Docs", "url": "https://hadoop.apache.org/docs/stable/"}
        ]
    },
    {
        "title": "5. Apache Spark",
        "description": "Most important skill for Big Data Engineers. Learn batch and real-time processing.",
        "points": [
            {"name": "Spark Core", "desc": "RDDs, transformations, actions"},
            {"name": "Spark SQL", "desc": "DataFrames, Catalyst optimizer"},
            {"name": "Spark Streaming", "desc": "Real-time processing"}
        ],
        "links": [
            {"name": "Spark Developer Course", "url": "https://www.coursera.org/learn/apache-spark"},
            {"name": "DataBricks Spark Course", "url": "https://academy.databricks.com/"}
        ],
        "other_resources": [
            {"name": "Spark Docs", "url": "https://spark.apache.org/docs/latest/"}
        ]
    },
    {
        "title": "6. Distributed Computing Fundamentals",
        "description": "Understand how large-scale computation works across clusters.",
        "points": [
            {"name": "Distributed File Systems", "desc": "HDFS, S3, GCS"},
            {"name": "Parallel Processing", "desc": "Partitioning, replication"},
            {"name": "Consistency Models", "desc": "CAP theorem, eventual consistency"}
        ],
        "links": [],
        "other_resources": [
            {"name": "Google File System Paper", "url": "https://research.google/pubs/pub51/"}
        ]
    },
    {
        "title": "7. Streaming Systems",
        "description": "Learn real-time big data pipelines for live analytics.",
        "points": [
            {"name": "Kafka", "desc": "Producers, consumers, brokers, topics"},
            {"name": "Flink", "desc": "Stream processing"},
            {"name": "Spark Streaming", "desc": "Structured streaming"}
        ],
        "links": [
            {"name": "Kafka Course (Udemy)", "url": "https://www.udemy.com/course/kafka/"}
        ],
        "other_resources": [
            {"name": "Kafka Docs", "url": "https://kafka.apache.org/documentation/"}
        ]
    },
    {
        "title": "8. Data Warehousing",
        "description": "Modern analytics needs warehouses and data lakes.",
        "points": [
            {"name": "Snowflake", "desc": "Virtual warehouses, cloud scaling"},
            {"name": "BigQuery", "desc": "Google cloud analytics engine"},
            {"name": "Redshift", "desc": "Amazon data warehouse"}
        ],
        "links": [
            {"name": "Snowflake Hands-on", "url": "https://learn.snowflake.com/"}
        ],
        "other_resources": [
            {"name": "BigQuery Docs", "url": "https://cloud.google.com/bigquery/docs"}
        ]
    },
    {
        "title": "9. Data Lake & Lakehouse",
        "description": "Learn modern big data architecture used by large companies.",
        "points": [
            {"name": "Data Lake", "desc": "S3, Azure Blob, GCS storage"},
            {"name": "Delta Lake", "desc": "ACID for data lakes"},
            {"name": "Apache Iceberg", "desc": "Table format for petabyte scale"}
        ],
        "links": [
            {"name": "Lakehouse Fundamentals", "url": "https://academy.databricks.com/lakehouse-fundamentals"}
        ],
        "other_resources": [
            {"name": "Delta Lake Docs", "url": "https://docs.delta.io/latest/"}
        ]
    },
    {
        "title": "10. ETL & ELT Pipelines",
        "description": "Learn how data flows through systems and is transformed.",
        "points": [
            {"name": "ETL Tools", "desc": "Airflow, NiFi, Talend"},
            {"name": "Orchestration", "desc": "Airflow DAGs, scheduling"},
            {"name": "Data Quality", "desc": "Great Expectations, validation"}
        ],
        "links": [
            {"name": "Airflow Course", "url": "https://www.udemy.com/course/apache-airflow/"},
        ],
        "other_resources": [
            {"name": "Airflow Docs", "url": "https://airflow.apache.org/docs/"}
        ]
    },
    {
        "title": "11. Cloud for Big Data",
        "description": "Cloud platforms run the majority of modern big data workloads.",
        "points": [
            {"name": "AWS EMR", "desc": "Managed Hadoop/Spark"},
            {"name": "GCP Dataproc", "desc": "Google's managed cluster"},
            {"name": "Azure HDInsight", "desc": "Microsoft big data service"}
        ],
        "links": [
            {"name": "AWS Data Engineering", "url": "https://www.coursera.org/specializations/aws-data-engineering"}
        ],
        "other_resources": [
            {"name": "AWS EMR Docs", "url": "https://docs.aws.amazon.com/emr/"}
        ]
    },
    {
        "title": "12. Data Engineering Best Practices",
        "description": "Write scalable, maintainable, production-grade pipelines.",
        "points": [
            {"name": "Data Modeling", "desc": "Kimball, Data Vault"},
            {"name": "Pipeline Optimization", "desc": "Partitioning, skipping, caching"},
            {"name": "Monitoring", "desc": "Data drift, data quality alerts"}
        ],
        "links": [],
        "other_resources": []
    },
    {
        "title": "13. Security & Governance",
        "description": "Learn how to secure data and maintain compliance.",
        "points": [
            {"name": "Encryption", "desc": "At rest & in transit"},
            {"name": "IAM Roles", "desc": "Least privilege, key rotation"},
            {"name": "Compliance", "desc": "GDPR, HIPAA, audit logs"}
        ],
        "links": [],
        "other_resources": [
            {"name": "AWS Security Docs", "url": "https://docs.aws.amazon.com/security/"}
        ]
    },
    {
        "title": "14. Real-World Big Data Projects",
        "description": "Build real projects to prove your skills.",
        "points": [
            {"name": "Batch Pipeline", "desc": "Spark + Airflow + S3"},
            {"name": "Streaming Pipeline", "desc": "Kafka → Spark → MongoDB"},
            {"name": "Data Warehouse", "desc": "Snowflake or BigQuery analytics"}
        ],
        "links": [],
        "other_resources": []
    },
    {
        "title": "15. Portfolio, Resume & Interview Prep",
        "description": "Finalize your profile for companies hiring data engineers.",
        "points": [
            {"name": "Portfolio", "desc": "GitHub with real pipelines"},
            {"name": "Resume", "desc": "Highlight Spark, Kafka, Cloud"},
            {"name": "Interview", "desc": "SQL, Python, system design"}
        ],
        "links": [],
        "other_resources": []
    }
]


def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/big_data_engineer.html", roadmap= BIG_DATA_ENGINEER_ROADMAP, title="Big Data Engineer Roadmap")

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('big_data_engineer'))

    @app.route("/big_data_engineer")
    def big_data_engineer():
        return render_page()

    app.run(debug=True)


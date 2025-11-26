from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory
BASE_DIR = Path(__file__).resolve().parent.parent  # Correct __file__
TEMPLATES_DIR = BASE_DIR / "templates"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))  # Correct __name__
BUSINESS_ANALYST_ROADMAP = [
    {
        "title": "Foundations of Business Analysis",
        "description": "Develop a strong foundation in business analysis by understanding the core responsibilities, key competencies, and the overall role of a Business Analyst (BA) in bridging the gap between business needs and IT solutions. Gain insight into how BAs contribute to project success, influence stakeholders, and ensure alignment between business objectives and technical implementations.",
        "points": [
            {"name": "BA Role & Responsibilities", "desc": "Understand what business analysts do and how they bridge business & IT."},
            {"name": "SDLC & Agile Basics", "desc": "Software development lifecycle, Agile, Scrum, Kanban."},
            {"name": "Requirement Types", "desc": "Functional, non-functional, and technical requirements."}
        ],
        "links": [
            {"name": "Business Analysis Fundamentals (Udemy)", "url": "https://www.udemy.com/course/business-analysis-fundamentals/"},
            {"name": "Agile with Atlassian Jira (Coursera)", "url": "https://www.coursera.org/learn/agile-atlassian-jira"}
        ],
        "other_resources": [
            {"name": "IIBA Business Analysis Core Standard", "url": "https://www.iiba.org/standards-and-resources/"},
            {"name": "Scrum Guides", "url": "https://scrumguides.org/"}
        ]
    },
    {
        "title": "Requirement Gathering & Process Modeling",
        "description": "Learn how to capture and analyze business requirements effectively. Understand different techniques for elicitation, documentation, and visualization of requirements to ensure clarity and alignment among stakeholders. Master process modeling to identify workflows, dependencies, and improvement areas in business operations.",
        "points": [
            {"name": "Requirement Elicitation", "desc": "Interviews, workshops, surveys, observation."},
            {"name": "User Stories & Use Cases", "desc": "How to write clear user stories and acceptance criteria."},
            {"name": "Process Modeling", "desc": "Flowcharts, BPMN, UML diagrams."}
        ],
        "links": [
            {"name": "Business Process Modeling (Udemy)", "url": "https://www.udemy.com/course/business-process-modeling-for-business-analysts/"},
            {"name": "Requirements Engineering (Coursera)", "url": "https://www.coursera.org/learn/requirements-gathering"}
        ],
        "other_resources": [
            {"name": "Lucidchart BPMN Guide", "url": "https://www.lucidchart.com/pages/bpmn"},
            {"name": "Visual Paradigm UML", "url": "https://www.visual-paradigm.com/guide/uml-unified-modeling-language/"}
        ]
    },
    {
        "title": "Stakeholder Analysis & Management",
        "description": "Learn to identify all stakeholders involved in a project and analyze their influence, interests, and expectations. Develop engagement strategies to maintain communication, resolve conflicts, and align stakeholders toward shared project goals. Understanding stakeholder dynamics is crucial for successful project delivery.",
        "points": [
            {"name": "Stakeholder Identification", "desc": "Recognize all stakeholders and their influence."},
            {"name": "Engagement Strategies", "desc": "Techniques to engage stakeholders effectively."},
            {"name": "Conflict Resolution", "desc": "Manage disagreements and align priorities."}
        ],
        "links": [
            {"name": "Stakeholder Management (Coursera)", "url": "https://www.coursera.org/learn/stakeholder-management"},
            {"name": "Effective Communication for BAs (Udemy)", "url": "https://www.udemy.com/course/communication-for-business-analysts/"}
        ],
        "other_resources": [
            {"name": "PMI Stakeholder Management Guide", "url": "https://www.pmi.org/learning/library/stakeholder-management-9937"}
        ]
    },
    {
        "title": "Data Skills for Business Analysts",
        "description": "Develop the ability to work with business data, perform analysis, and create insightful visualizations. Gain practical skills in Excel, SQL, and business intelligence tools like Tableau and Power BI to analyze, interpret, and communicate data-driven insights effectively to stakeholders.",
        "points": [
            {"name": "Excel", "desc": "Formulas, Pivot tables, macros."},
            {"name": "SQL", "desc": "Queries, joins, aggregations for business data."},
            {"name": "Visualization Tools", "desc": "Tableau / Power BI dashboards."}
        ],
        "links": [
            {"name": "Excel Skills for Business (Coursera)", "url": "https://www.coursera.org/specializations/excel"},
            {"name": "SQL for Business Analysts (Udemy)", "url": "https://www.udemy.com/course/sql-for-newbs/"},
            {"name": "Data Visualization with Tableau (Coursera)", "url": "https://www.coursera.org/learn/data-visualization-tableau"}
        ],
        "other_resources": [
            {"name": "Power BI Learning Path (Microsoft)", "url": "https://learn.microsoft.com/en-us/power-bi/learning-catalog/"},
            {"name": "Tableau Public Resources", "url": "https://public.tableau.com/en-us/s/resources"}
        ]
    },
    {
        "title": "Business Process Improvement",
        "description": "Learn techniques to analyze, evaluate, and optimize business processes for efficiency and effectiveness. Apply Lean and Six Sigma methodologies to identify bottlenecks, reduce waste, and implement measurable improvements. Define KPIs and success metrics to track process performance and demonstrate value to the organization.",
        "points": [
            {"name": "Process Analysis Techniques", "desc": "Identify bottlenecks and inefficiencies."},
            {"name": "Lean & Six Sigma Basics", "desc": "Apply Lean and Six Sigma principles to improve processes."},
            {"name": "KPI & Metrics Definition", "desc": "Define measurable indicators for process success."}
        ],
        "links": [
            {"name": "Lean Six Sigma for Business Analysts (Udemy)", "url": "https://www.udemy.com/course/lean-six-sigma-for-business-analysts/"},
            {"name": "Process Improvement Fundamentals (Coursera)", "url": "https://www.coursera.org/learn/process-improvement"}
        ],
        "other_resources": [
            {"name": "Six Sigma Resources", "url": "https://www.sixsigmacouncil.org/"}
        ]
    },
    {
        "title": "Tools for Business Analysis",
        "description": "Become proficient in essential BA tools for collaboration, documentation, and modeling. Use JIRA and Confluence for project management, BPMN tools for process mapping, and collaboration platforms like Miro or Notion to improve teamwork and communication.",
        "points": [
            {"name": "JIRA & Confluence", "desc": "Agile project management and documentation."},
            {"name": "BPMN Tools", "desc": "Bizagi, Lucidchart, Signavio."},
            {"name": "Collaboration Tools", "desc": "Slack, Miro, Notion."}
        ],
        "links": [
            {"name": "Mastering JIRA and Confluence (Udemy)", "url": "https://www.udemy.com/course/jira-agile-project-management-confluence/"},
            {"name": "BPMN for Business Analysts (Udemy)", "url": "https://www.udemy.com/course/bpmn-business-process-modeling/"}
        ],
        "other_resources": [
            {"name": "Atlassian University (Jira/Confluence)", "url": "https://university.atlassian.com/"},
            {"name": "Miro Academy", "url": "https://miro.com/academy/"}
        ]
    },
    {
        "title": "Advanced Analytics & Reporting",
        "description": "Enhance your analytical capabilities with advanced techniques to derive actionable insights from data. Learn predictive analytics, statistical models, and forecasting methods. Build interactive dashboards and automate repetitive reporting tasks to deliver timely, accurate, and meaningful business insights to decision-makers.",
        "points": [
            {"name": "Predictive Analytics", "desc": "Regression, classification, and forecasting models."},
            {"name": "Dashboards & Reporting", "desc": "Interactive dashboards using Power BI or Tableau."},
            {"name": "Automation", "desc": "Automate repetitive reporting tasks with scripts or tools."}
        ],
        "links": [
            {"name": "Predictive Business Analytics (Udemy)", "url": "https://www.udemy.com/course/predictive-business-analytics/"},
            {"name": "Data Visualization with Tableau (Coursera)", "url": "https://www.coursera.org/learn/data-visualization-tableau"}
        ],
        "other_resources": [
            {"name": "IBM Analytics Community", "url": "https://community.ibm.com/community/user/businessanalytics"}
        ]
    },
    {
        "title": "Domain Knowledge & Industry Expertise",
        "description": "Understand key business domains and industry-specific processes to provide context-aware solutions. Learn domain terminologies, regulations, KPIs, and workflows to deliver more impactful analysis and recommendations tailored to the specific industry.",
        "points": [
            {"name": "Finance & Banking", "desc": "Learn core processes, compliance, and KPIs."},
            {"name": "Healthcare", "desc": "Understand regulations, patient data, and workflows."},
            {"name": "Retail & E-commerce", "desc": "Inventory, sales, customer behavior analytics."}
        ],
        "links": [
            {"name": "Finance for Business Analysts (Udemy)", "url": "https://www.udemy.com/course/finance-for-business-analysts/"},
            {"name": "Healthcare Analytics (Coursera)", "url": "https://www.coursera.org/learn/healthcare-analytics"}
        ],
        "other_resources": [
            {"name": "Industry Reports (McKinsey)", "url": "https://www.mckinsey.com/industries"}
        ]
    },
    {
        "title": "Agile & Scrum Deep Dive",
        "description": "Master Agile methodologies and Scrum practices for successful project delivery. Understand the roles, responsibilities, and ceremonies in Scrum, and learn how to estimate, plan, and manage sprints effectively. Gain skills to optimize workflows using Kanban, prioritize tasks, and ensure continuous delivery of business value.",
        "points": [
            {"name": "Scrum Roles & Events", "desc": "Product Owner, Scrum Master, ceremonies."},
            {"name": "Agile Estimation & Planning", "desc": "Story points, sprints, velocity tracking."},
            {"name": "Kanban & Continuous Delivery", "desc": "Visualize workflow and improve throughput."}
        ],
        "links": [
            {"name": "Agile Scrum Masterclass (Udemy)", "url": "https://www.udemy.com/course/agile-scrum-masterclass/"},
            {"name": "Agile Project Management (Coursera)", "url": "https://www.coursera.org/learn/agile-project-management"}
        ],
        "other_resources": [
            {"name": "Scrum Alliance Resources", "url": "https://www.scrumalliance.org/resources"}
        ]
    },
    {
        "title": "Business Intelligence & Data Warehousing",
        "description": "Gain expertise in business intelligence concepts and data warehousing techniques to support data-driven decision-making. Learn ETL processes, design and understand data warehouse structures, and use BI tools to generate insights and actionable reports for stakeholders.",
        "points": [
            {"name": "ETL Processes", "desc": "Extract, Transform, Load pipelines."},
            {"name": "Data Warehouses", "desc": "Understand OLAP, OLTP, star & snowflake schemas."},
            {"name": "BI Tools", "desc": "Power BI, Tableau, Qlik for insights and dashboards."}
        ],
        "links": [
            {"name": "Data Warehousing and BI (Udemy)", "url": "https://www.udemy.com/course/data-warehousing-business-intelligence/"},
            {"name": "Business Intelligence with Power BI (Coursera)", "url": "https://www.coursera.org/learn/business-intelligence-power-bi"}
        ],
        "other_resources": [
            {"name": "Microsoft Power BI Docs", "url": "https://learn.microsoft.com/en-us/power-bi/"},
            {"name": "Tableau Resources", "url": "https://www.tableau.com/learn/training"}
        ]
    },
    {
        "title": "Process Improvement & Lean Six Sigma",
        "description": "Develop advanced process improvement skills using Lean and Six Sigma methodologies. Learn to analyze workflows, identify inefficiencies, and implement strategies for operational excellence. Embed a culture of continuous improvement within organizations to achieve higher quality, efficiency, and customer satisfaction.",
        "points": [
            {"name": "Lean Methodology", "desc": "Eliminate waste and improve flow."},
            {"name": "Six Sigma Tools", "desc": "DMAIC, process mapping, statistical analysis."},
            {"name": "Continuous Improvement", "desc": "Embed culture of ongoing process refinement."}
        ],
        "links": [
            {"name": "Lean Six Sigma White Belt (Coursera)", "url": "https://www.coursera.org/learn/lean-six-sigma-white-belt"},
            {"name": "Advanced Lean Six Sigma (Udemy)", "url": "https://www.udemy.com/course/advanced-lean-six-sigma/"}
        ],
        "other_resources": [
            {"name": "iSixSigma Resources", "url": "https://www.isixsigma.com/"}
        ]
    },
    {
        "title": "Business Analysis for Digital Transformation",
        "description": "Equip yourself with skills to analyze and drive digital initiatives in modern organizations. Learn to leverage automation, AI, and digital tools to optimize processes, improve decision-making, and enhance customer experiences. Understand change management strategies to facilitate smooth adoption of technology-driven transformation.",
        "points": [
            {"name": "Digital Tools & Automation", "desc": "RPA, workflow automation, AI integration."},
            {"name": "Change Management", "desc": "Guide teams through technology adoption."},
            {"name": "Innovation Analysis", "desc": "Assess impact of new digital initiatives."}
        ],
        "links": [
            {"name": "Digital Transformation Fundamentals (Coursera)", "url": "https://www.coursera.org/learn/digital-transformation"},
            {"name": "RPA for Business Analysts (Udemy)", "url": "https://www.udemy.com/course/rpa-for-business-analysts/"}
        ],
        "other_resources": [
            {"name": "Digital Transformation Resources", "url": "https://www.gartner.com/en/information-technology/insights/digital-transformation"}
        ]
    },
    {
        "title": "Soft Skills & Communication Mastery",
        "description": "Enhance interpersonal and communication skills to improve collaboration and stakeholder management. Develop strong presentation, negotiation, and critical thinking abilities that allow you to influence decisions, solve complex problems, and effectively convey insights to technical and non-technical audiences.",
        "points": [
            {"name": "Presentation Skills", "desc": "Deliver clear, persuasive presentations."},
            {"name": "Negotiation & Influence", "desc": "Build consensus among stakeholders."},
            {"name": "Critical Thinking & Problem Solving", "desc": "Analyze situations and make data-driven decisions."}
        ],
        "links": [
            {"name": "Effective Communication Skills (Coursera)", "url": "https://www.coursera.org/learn/wharton-communication-skills"},
            {"name": "Critical Thinking for Business (Udemy)", "url": "https://www.udemy.com/course/critical-thinking-for-business/"}
        ],
        "other_resources": [
            {"name": "MindTools Communication & Leadership", "url": "https://www.mindtools.com/"}
        ]
    },
    {
        "title": "Business Analytics & AI Integration",
        "description": "Learn to leverage analytics and AI technologies to enhance business decision-making. Understand descriptive, predictive, and prescriptive analytics, and apply AI/ML techniques to generate insights, optimize processes, and support strategic initiatives. Build decision support systems that transform raw data into actionable intelligence.",
        "points": [
            {"name": "Descriptive & Predictive Analytics", "desc": "Analyze historical data and forecast trends."},
            {"name": "AI & ML Applications", "desc": "Use AI models for customer insights, recommendation engines."},
            {"name": "Decision Support Systems", "desc": "Build dashboards and systems that guide business choices."}
        ],
        "links": [
            {"name": "AI for Business Leaders (Coursera)", "url": "https://www.coursera.org/learn/ai-for-everyone"},
            {"name": "Business Analytics with R (Udemy)", "url": "https://www.udemy.com/course/business-analytics-with-r/"}
        ],
        "other_resources": [
            {"name": "Towards Data Science", "url": "https://towardsdatascience.com/"}
        ]
    },
    {
        "title": "Continuous Learning & Professional Development",
        "description": "Stay updated with industry trends, certifications, and professional communities to maintain a competitive edge as a Business Analyst. Engage in lifelong learning, participate in forums, attend webinars, and pursue certifications to advance your skills and career growth.",
        "points": [
            {"name": "IIBA Certifications", "desc": "ECBA, CCBA, CBAP for Business Analysts."},
            {"name": "Agile & Scrum Certifications", "desc": "CSPO, CSM for Agile BA roles."},
            {"name": "Community & Blogs", "desc": "Join BA forums, webinars, and follow industry updates."}
        ],
        "links": [
            {"name": "ECBA Certification Preparation (Udemy)", "url": "https://www.udemy.com/course/ecba-certification-preparation/"},
            {"name": "Certified ScrumMaster (Scrum Alliance)", "url": "https://www.scrumalliance.org/get-certified/scrum-master-track/certified-scrummaster"}
        ],
        "other_resources": [
            {"name": "IIBA Certifications Guide", "url": "https://www.iiba.org/certification/"},
            {"name": "Agile Alliance Resources", "url": "https://www.agilealliance.org/resources/"}
        ]
    }
]
@app.route("/")
def home():
    return redirect(url_for('Business_analyst'))


def render_page():
    return render_template("roadmaps/business_analyst.html", roadmap=BUSINESS_ANALYST_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('business_analyst'))

    @app.route("/")
    def blockchain_engineer():
        return render_page()

    app.run(debug=True)
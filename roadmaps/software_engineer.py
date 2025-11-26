from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))


# =====================================================================
# 📌 SOFTWARE ENGINEER ROADMAP (15 steps)
# =====================================================================

SOFTWARE_ENGINEER_ROADMAP = [
    {
        "title": "1. Programming & Logic Foundations",
        "description": "Start with the basics of how programming works. Build strong logical thinking and understand how computers execute instructions.",
        "points": [
            {"name": "Programming Basics", "desc": "Variables, data types, loops, conditionals, functions"},
            {"name": "Logic Building", "desc": "Flowcharts, pseudocode, problem breakdown"},
            {"name": "Beginner Language", "desc": "Start with Python or JavaScript"}
        ],
        "links": [
            {"name": "Python Docs", "url": "https://docs.python.org/3/"},
            {"name": "W3Schools Python", "url": "https://www.w3schools.com/python/"}
        ],
        "other_resources": [
            {"name": "CS50 Intro Course", "url": "https://cs50.harvard.edu/"}
        ]
    },
    {
        "title": "2. Master a Primary Programming Language",
        "description": "Choose one solid backend-friendly language and master its syntax, OOP, and environment setup.",
        "points": [
            {"name": "Languages", "desc": "Java / Python / JavaScript / C++"},
            {"name": "OOP", "desc": "Classes, objects, inheritance, polymorphism"},
            {"name": "Environment", "desc": "IDEs, packages, file handling"}
        ],
        "links": [
            {"name": "Java Tutorial", "url": "https://docs.oracle.com/javase/tutorial/"},
            {"name": "Python OOP", "url": "https://realpython.com/python3-object-oriented-programming/"}
        ]
    },
    {
        "title": "3. Git, GitHub & Version Control",
        "description": "Learn to manage versions, collaborate, and push code like a real engineer.",
        "points": [
            {"name": "Git Basics", "desc": "Commit, branch, merge"},
            {"name": "GitHub", "desc": "Pull requests, issues, project boards"},
            {"name": "Collaboration", "desc": "Working with teams and maintaining repos"}
        ],
        "links": [
            {"name": "Git Docs", "url": "https://git-scm.com/doc"},
            {"name": "GitHub Guides", "url": "https://guides.github.com/"}
        ]
    },
    {
        "title": "4. Data Structures & Algorithms (DSA)",
        "description": "Build problem-solving skills and prepare for internships and coding interviews.",
        "points": [
            {"name": "Core DSA", "desc": "Arrays, Strings, Linked Lists, Stacks, Queues"},
            {"name": "Advanced", "desc": "Trees, Graphs, HashMaps, Heaps"},
            {"name": "Algorithms", "desc": "Searching, sorting, recursion, greedy, DP (basics)"}
        ],
        "links": [
            {"name": "LeetCode", "url": "https://leetcode.com/"},
            {"name": "InterviewBit", "url": "https://www.interviewbit.com/"}
        ]
    },
    {
        "title": "5. Web Fundamentals",
        "description": "Understand how the internet works and build simple web pages.",
        "points": [
            {"name": "Frontend Basics", "desc": "HTML, CSS, JavaScript"},
            {"name": "Web Concepts", "desc": "HTTP, REST, APIs, browsers, servers"},
            {"name": "Responsive Design", "desc": "Flexbox, Grid, media queries"}
        ],
        "links": [
            {"name": "MDN Web Docs", "url": "https://developer.mozilla.org/"}
        ]
    },
    {
        "title": "6. Backend Development",
        "description": "Build server-side applications and APIs.",
        "points": [
            {"name": "Frameworks", "desc": "Flask/Django (Python), Node.js/Express (JS), Spring Boot (Java)"},
            {"name": "APIs", "desc": "REST API design, routing, controllers"},
            {"name": "Auth", "desc": "JWT, sessions, cookies"}
        ],
        "links": [
            {"name": "Flask Docs", "url": "https://flask.palletsprojects.com/"},
            {"name": "Node.js Docs", "url": "https://nodejs.org/"}
        ]
    },
    {
        "title": "7. Databases & SQL",
        "description": "Learn to store, query, and manage application data.",
        "points": [
            {"name": "SQL", "desc": "Joins, indexing, stored procedures"},
            {"name": "NoSQL", "desc": "MongoDB, Firestore"},
            {"name": "ORMs", "desc": "SQLAlchemy, Django ORM"}
        ],
        "links": [
            {"name": "SQLBolt", "url": "https://sqlbolt.com/"},
            {"name": "MongoDB University", "url": "https://www.mongodb.com/university"}
        ]
    },
    {
        "title": "8. Software Engineering Principles",
        "description": "Learn best practices that make code maintainable.",
        "points": [
            {"name": "Clean Code", "desc": "Naming, readability, modularity"},
            {"name": "Design Patterns", "desc": "Singleton, Observer, Factory"},
            {"name": "Architectures", "desc": "MVC, layered architecture"}
        ],
        "links": [
            {"name": "Clean Code Book", "url": "https://www.oreilly.com/library/view/clean-code/9780136083238/"}
        ]
    },
    {
        "title": "9. Build Real Projects",
        "description": "Create practical applications to showcase skills.",
        "points": [
            {"name": "Beginner Projects", "desc": "Portfolio, to-do app, calculator"},
            {"name": "Intermediate", "desc": "E-commerce, blog system, weather app"},
            {"name": "Advanced", "desc": "Chat app, job portal, learning system"}
        ]
    },
    {
        "title": "10. Testing",
        "description": "Ensure software quality with automated tests.",
        "points": [
            {"name": "Unit Testing", "desc": "pytest, unittest"},
            {"name": "Integration", "desc": "API tests, DB tests"},
            {"name": "Tools", "desc": "Postman, Selenium (UI testing)"}
        ]
    },
    {
        "title": "11. DevOps Basics",
        "description": "Learn deployment workflows for real-world software.",
        "points": [
            {"name": "CI/CD", "desc": "GitHub Actions, pipelines"},
            {"name": "Containers", "desc": "Docker basics"},
            {"name": "Hosting", "desc": "Render, AWS EC2, Vercel, Railway"}
        ]
    },
    {
        "title": "12. System Design Basics",
        "description": "Understand real-world scalable systems.",
        "points": [
            {"name": "Core Concepts", "desc": "Load balancing, caching, replication"},
            {"name": "Databases", "desc": "Sharding, indexing, read-write split"},
            {"name": "Designing", "desc": "URL shortener, chat system, e-commerce backend"}
        ]
    },
    {
        "title": "13. Operating Systems & Networking",
        "description": "Develop a deeper understanding of how systems work under the hood.",
        "points": [
            {"name": "OS", "desc": "Processes, threads, memory, file systems"},
            {"name": "Networking", "desc": "TCP/IP, DNS, firewalls"}
        ]
    },
    {
        "title": "14. Cloud Basics",
        "description": "Understand cloud platforms and hosting environments.",
        "points": [
            {"name": "Platforms", "desc": "AWS, Azure, GCP fundamentals"},
            {"name": "Storage", "desc": "S3, Cloud Storage"},
            {"name": "Compute", "desc": "EC2, App Engine"}
        ]
    },
    {
        "title": "15. Portfolio & Interview Prep",
        "description": "Prepare for job applications and build a strong presence.",
        "points": [
            {"name": "Portfolio", "desc": "GitHub, deployed projects, resume"},
            {"name": "DSA", "desc": "LeetCode interview practice"},
            {"name": "HR Prep", "desc": "Behavioral questions, resume review"}
        ]
    }
]


def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/software_engineer.html", roadmap=SOFTWARE_ENGINEER_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('software_engineer'))

    @app.route("/software-engineer")
    def software_engineer():
        return render_page()

    app.run(debug=True)
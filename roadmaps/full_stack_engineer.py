from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory
BASE_DIR = Path(__file__).resolve().parent.parent  # Correct __file__
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))  # Correct __name__

# full_stack_engineer_roadmap.py
FULL_STACK_ENGINEER_ROADMAP =[
    {
        "title": "Internet & Web Fundamentals",
        "description": "Build a deep understanding of how the internet and web technologies function, which is the foundation of all full-stack development. Learn about clients, servers, HTTP/HTTPS protocols, DNS, and domain name systems, which govern how requests and responses travel across the network. Grasping these concepts enables you to understand how front-end and back-end communicate, how web pages are delivered, and how web applications scale, providing the necessary background for both development and troubleshooting in real-world scenarios.",
        "points": [
            {"name": "How the Internet Works", "desc": "Learn about IP addresses, DNS, hosting, and domains."},
            {"name": "HTTP/HTTPS Protocols", "desc": "Understand requests, responses, headers, cookies, and status codes."},
            {"name": "Client-Server Model", "desc": "How browsers send requests and servers respond with data."}
        ],
        "links": [
            {"name": "How the Internet Works (MDN)", "url": "https://developer.mozilla.org/en-US/docs/Learn/Common_questions/How_does_the_Internet_work"}
        ],
        "other_resources": [
            {"name": "Computer Networking Crash Course", "url": "https://roadmap.sh/guides/computer-networking"}
        ]
    },
    {
        "title": "HTML Fundamentals",
        "description": "Master the backbone of every web page by learning HTML, the language used to structure content on the web. This stage covers semantic elements, forms, multimedia, and accessibility best practices. Understanding HTML enables you to create meaningful, well-structured web pages that are easy to style with CSS and interact with using JavaScript. This foundation is critical for building user-friendly, SEO-optimized, and accessible web applications.",
        "points": [
            {"name": "HTML Elements", "desc": "Headings, paragraphs, links, lists, tables, forms."},
            {"name": "Semantic HTML", "desc": "Use tags like <header>, <footer>, <article> for accessibility."},
            {"name": "Forms & Validation", "desc": "Create interactive input fields and validate data."}
        ],
        "links": [
            {"name": "HTML Basics (MDN)", "url": "https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics"}
        ],
        "other_resources": [
            {"name": "W3Schools HTML", "url": "https://www.w3schools.com/html/"}
        ]
    },
    {
        "title": "CSS Fundamentals",
        "description": "Learn how to bring your web pages to life with CSS by applying styles, layouts, colors, and animations. This stage covers the box model, selectors, responsive design techniques, Flexbox, and Grid, enabling you to create visually appealing and consistent user interfaces. CSS knowledge allows you to translate design mockups into interactive and responsive web pages, forming a crucial bridge between aesthetics and functionality in full-stack development.",
        "points": [
            {"name": "Selectors & Properties", "desc": "Learn CSS syntax, classes, and IDs."},
            {"name": "Box Model", "desc": "Understand margin, border, padding, and content."},
            {"name": "Flexbox & Grid", "desc": "Build responsive layouts easily."}
        ],
        "links": [
            {"name": "Learn CSS (MDN)", "url": "https://developer.mozilla.org/en-US/docs/Learn/CSS"}
        ],
        "other_resources": [
            {"name": "CSS Tricks", "url": "https://css-tricks.com/"}
        ]
    },
    {
        "title": "JavaScript Basics",
        "description": "Develop interactive and dynamic web pages using JavaScript, the programming language of the web. Gain proficiency in variables, data types, control flow, functions, and objects. Learn DOM manipulation to access and modify HTML elements dynamically. Understanding JavaScript fundamentals enables you to implement client-side logic, enhance user experiences, and prepare for advanced topics such as asynchronous programming, frameworks, and full-stack application development.",
        "points": [
            {"name": "Variables & Data Types", "desc": "Strings, numbers, booleans, arrays, objects."},
            {"name": "Control Flow", "desc": "Conditionals, loops, functions."},
            {"name": "DOM Manipulation", "desc": "Access and modify HTML elements dynamically."}
        ],
        "links": [
            {"name": "JavaScript Guide (MDN)", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"}
        ],
        "other_resources": [
            {"name": "Eloquent JavaScript", "url": "https://eloquentjavascript.net/"}
        ]
    },
    {
        "title": "Version Control (Git & GitHub)",
        "description": "Learn to manage your code efficiently and collaborate seamlessly with others using Git and GitHub. Understand how to track code history, manage multiple development branches, handle merges, and participate in pull requests. Version control is crucial for team projects, ensuring reproducibility, preventing conflicts, and maintaining a robust development workflow. Mastery of these tools allows you to contribute to open-source projects and work professionally in collaborative environments.",
        "points": [
            {"name": "Git Basics", "desc": "Init, clone, add, commit, push, pull."},
            {"name": "Branching & Merging", "desc": "Work on multiple features in parallel."},
            {"name": "Collaboration", "desc": "Pull requests, code reviews, GitHub projects."}
        ],
        "links": [
            {"name": "Pro Git Book", "url": "https://git-scm.com/book/en/v2"}
        ],
        "other_resources": [
            {"name": "GitHub Learning Lab", "url": "https://lab.github.com/"}
        ]
    },
    {
        "title": "Front-End Frameworks",
        "description": "Master modern front-end frameworks such as React, Vue, or Angular to build scalable, reusable, and high-performance user interfaces. Learn component-based architecture, state management, hooks, context API, and client-side routing. This stage equips you to create sophisticated single-page applications (SPAs) and enhances your ability to maintain complex front-end projects efficiently while ensuring a responsive and interactive user experience.",
        "points": [
            {"name": "React.js", "desc": "Components, state, hooks, context API."},
            {"name": "Vue.js or Angular", "desc": "Alternatives for building dynamic apps."},
            {"name": "Routing", "desc": "Navigation between pages using React Router or Vue Router."}
        ],
        "links": [
            {"name": "React Official Docs", "url": "https://react.dev/"}
        ],
        "other_resources": [
            {"name": "Vue.js Docs", "url": "https://vuejs.org/guide/introduction.html"}
        ]
    },
    {
        "title": "Responsive & Modern UI",
        "description": "Learn techniques for designing mobile-first, responsive, and accessible web applications. Understand media queries, fluid layouts, relative units, and modern UI libraries like Bootstrap, TailwindCSS, and Material UI. Incorporating accessibility (a11y) ensures that applications are usable by all users, including those with disabilities. This stage allows you to build interfaces that are visually appealing, user-friendly, and adaptive across multiple devices and screen sizes.",
        "points": [
            {"name": "Responsive Design", "desc": "Media queries, fluid layouts, relative units."},
            {"name": "UI Libraries", "desc": "Bootstrap, TailwindCSS, Material UI."},
            {"name": "Accessibility (a11y)", "desc": "Build inclusive applications for all users."}
        ],
        "links": [
            {"name": "TailwindCSS Docs", "url": "https://tailwindcss.com/docs"}
        ],
        "other_resources": [
            {"name": "A11y Project", "url": "https://www.a11yproject.com/"}
        ]
    },
    {
        "title": "Back-End Fundamentals",
        "description": "Gain proficiency in server-side programming to manage databases, business logic, and APIs. Learn Node.js and Express for building RESTful APIs, handle authentication using JWT, sessions, and OAuth2, and work with both SQL and NoSQL databases. This stage forms the backbone of full-stack development, enabling you to build secure, scalable, and maintainable server-side applications that communicate effectively with front-end clients.",
        "points": [
            {"name": "Node.js & Express", "desc": "Build REST APIs with middleware and routing."},
            {"name": "Databases", "desc": "Learn SQL (PostgreSQL/MySQL) and NoSQL (MongoDB)."},
            {"name": "Authentication", "desc": "Sessions, JWT, OAuth2."}
        ],
        "links": [
            {"name": "Node.js Docs", "url": "https://nodejs.org/docs/latest/api/"}
        ],
        "other_resources": [
            {"name": "Express.js Docs", "url": "https://expressjs.com/"}
        ]
    },
    {
        "title": "API Design & Integration",
        "description": "Learn to design scalable and secure APIs for communication between front-end and back-end systems. Understand REST API principles including CRUD operations, versioning, error handling, and security. Explore GraphQL for more flexible queries and efficient data fetching. Strong API design skills are essential for integrating services, enabling third-party consumption, and building modular and maintainable applications.",
        "points": [
            {"name": "REST APIs", "desc": "CRUD operations, versioning, error handling."},
            {"name": "GraphQL", "desc": "Flexible queries with Apollo or Relay."},
            {"name": "API Security", "desc": "Rate limiting, CORS, validation."}
        ],
        "links": [
            {"name": "REST API Tutorial", "url": "https://restfulapi.net/"}
        ],
        "other_resources": [
            {"name": "GraphQL Docs", "url": "https://graphql.org/learn/"}
        ]
    },{
    "title": "Testing & Debugging",
    "description": "Ensure the reliability, maintainability, and quality of your applications by mastering testing and debugging practices. Learn how to write unit tests to verify individual components, integration tests to ensure system-wide functionality, and end-to-end tests for full workflows. Gain proficiency in tools like Jest, Mocha, Jasmine, Supertest, and Cypress. Understanding debugging techniques with Chrome DevTools, VS Code debugger, and error tracing allows you to quickly identify and resolve issues, resulting in robust and production-ready applications.",
    "points": [
        {"name": "Unit Testing", "desc": "Jest, Mocha, Jasmine."},
        {"name": "Integration Testing", "desc": "Supertest, Cypress."},
        {"name": "Debugging Tools", "desc": "Chrome DevTools, VS Code debugger."}
    ],
    "links": [
        {"name": "Jest Docs", "url": "https://jestjs.io/docs/getting-started"}
    ],
    "other_resources": [
        {"name": "Cypress Docs", "url": "https://docs.cypress.io/"}
    ]
},
{
    "title": "DevOps & Deployment",
    "description": "Learn how to deploy, monitor, and scale full-stack applications in production environments. Understand containerization using Docker to package applications with all dependencies, continuous integration/continuous deployment (CI/CD) pipelines using GitHub Actions, Jenkins, or GitLab CI, and cloud provider fundamentals on AWS, GCP, or Azure. These skills allow you to release software faster, maintain stability, and ensure scalability for applications that serve real-world users, bridging the gap between development and operations.",
    "points": [
        {"name": "Containerization", "desc": "Docker basics for packaging apps."},
        {"name": "CI/CD", "desc": "Automate deployment with GitHub Actions, Jenkins, GitLab CI."},
        {"name": "Cloud Providers", "desc": "AWS, GCP, Azure basics."}
    ],
    "links": [
        {"name": "Docker Docs", "url": "https://docs.docker.com/"}
    ],
    "other_resources": [
        {"name": "Kubernetes Docs", "url": "https://kubernetes.io/docs/"}
    ]
},
{
    "title": "System Design & Scalability",
    "description": "Acquire the ability to design large-scale, reliable, and high-performance systems. Learn design principles such as load balancing, caching strategies, microservices architecture, and database optimization including replication, sharding, and indexing. Explore messaging systems like RabbitMQ and Kafka to handle asynchronous communication. Mastering system design ensures your applications can handle growing user bases, maintain high availability, and perform efficiently under various workloads.",
    "points": [
        {"name": "Design Principles", "desc": "Load balancing, caching, microservices."},
        {"name": "Databases at Scale", "desc": "Replication, sharding, indexing."},
        {"name": "Message Queues", "desc": "RabbitMQ, Kafka for async communication."}
    ],
    "links": [
        {"name": "System Design Primer", "url": "https://github.com/donnemartin/system-design-primer"}
    ],
    "other_resources": [
        {"name": "Scalable System Design Patterns", "url": "https://github.com/checkcheckzz/system-design-interview"}
    ]
},
{
    "title": "Web Security",
    "description": "Protect applications from threats and vulnerabilities by learning web security principles. Understand common attacks such as Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), SQL Injection, and learn best practices for prevention. Implement secure authentication and authorization methods, including role-based access control and OAuth2. Knowledge of web security ensures that applications are safe for users, comply with regulatory standards, and maintain trust in production environments.",
    "points": [
        {"name": "Common Attacks", "desc": "XSS, CSRF, SQL Injection."},
        {"name": "Best Practices", "desc": "Use HTTPS, CORS, security headers."},
        {"name": "Authentication & Authorization", "desc": "Role-based access control, OAuth2."}
    ],
    "links": [
        {"name": "OWASP Top 10", "url": "https://owasp.org/www-project-top-ten/"}
    ],
    "other_resources": [
        {"name": "Web Security Academy", "url": "https://portswigger.net/web-security"}
    ]
},
{
    "title": "Soft Skills & Collaboration",
    "description": "Enhance your effectiveness as a full-stack engineer by mastering collaboration and communication skills. Learn agile methodologies and Scrum workflows to manage projects efficiently, communicate clearly with team members and stakeholders, and document processes comprehensively. Participate in code reviews and provide constructive feedback to foster a culture of learning and quality assurance. Strong soft skills are critical for career growth, team productivity, and successful delivery of complex projects.",
    "points": [
        {"name": "Agile & Scrum", "desc": "Learn agile workflows, standups, sprints."},
        {"name": "Communication Skills", "desc": "Effective teamwork, documentation, and reporting."},
        {"name": "Code Reviews", "desc": "Best practices for giving and receiving feedback."}
    ],
    "links": [
        {"name": "Agile Guide", "url": "https://www.atlassian.com/agile"}
    ],
    "other_resources": [
        {"name": "Scrum Guide", "url": "https://scrumguides.org/"}
    ]
},
{
    "title": "Continue Learning",
    "description": "Full-stack development is an ever-evolving field with new frameworks, libraries, tools, and best practices emerging constantly. Stay ahead by consistently exploring new technologies, building personal and open-source projects, reading blogs, and engaging with developer communities. Learn about cutting-edge trends such as WebAssembly, serverless computing, edge computing, and modern JavaScript frameworks. Continuous learning ensures that your skills remain relevant, allowing you to adapt to industry changes and tackle complex problems with confidence.",
    "points": [
        {"name": "Stay Updated", "desc": "Follow blogs, GitHub repos, and YouTube channels."},
        {"name": "Build Projects", "desc": "Create personal and open-source projects."},
        {"name": "Explore Trends", "desc": "Learn about WebAssembly, serverless, and edge computing."}
    ],
    "links": [
        {"name": "Roadmap.sh Full-Stack", "url": "https://roadmap.sh/full-stack"}
    ],
    "other_resources": [
        {"name": "FreeCodeCamp News", "url": "https://www.freecodecamp.org/news/"}
    ]
}

    
]


def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/full_stack_engineer.html", roadmap=FULL_STACK_ENGINEER_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('full_stack_engineer'))

    @app.route("/full_stack_engineer")
    def full_stack_engineer():
        return render_page()

    app.run(debug=True)
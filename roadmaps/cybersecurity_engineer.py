from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory
BASE_DIR = Path(__file__).resolve().parent.parent  # Correct __file__
TEMPLATES_DIR = BASE_DIR / "templates"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))  # Correct __name__
CYBERSECURITY_ROADMAP = [
    {
        "title": "Foundations of IT & Networking",
        "description": "Begin your cybersecurity journey by building a strong foundation in IT fundamentals, operating systems, networking, and scripting. Understand how computers communicate, how operating systems manage resources, and how scripts can automate tasks, which is essential for any cybersecurity role.",
        "points": [
            {"name": "Operating Systems", "desc": "Linux and Windows basics, file systems, processes, services, permissions, system logs."},
            {"name": "Networking Basics", "desc": "TCP/IP, DNS, HTTP, routing, switching, and network communication fundamentals."},
            {"name": "Scripting Basics", "desc": "Python and Bash for automation, log parsing, and basic security tasks."}
        ],
        "links": [
            {"name": "Computer Networking (Coursera)", "url": "https://www.coursera.org/learn/computer-networking"},
            {"name": "Python for Everybody", "url": "https://www.coursera.org/specializations/python"}
        ],
        "other_resources": [
            {"name": "Cisco Networking Basics", "url": "https://www.cisco.com/c/en/us/training-events/training-certifications.html"},
            {"name": "Linux Journey", "url": "https://linuxjourney.com/"}
        ]
    },
    {
        "title": "System Administration & Security",
        "description": "Learn how to manage and secure computer systems effectively. This includes creating and managing users, configuring essential services securely, and maintaining systems with updates and patches to reduce vulnerabilities. These skills are critical for defending IT infrastructures.",
        "points": [
            {"name": "User & Group Management", "desc": "Add, remove, and configure users and groups securely."},
            {"name": "Service Configuration", "desc": "Configure critical services with security in mind."},
            {"name": "Patch Management", "desc": "Keep systems updated to prevent vulnerabilities."}
        ],
        "links": [
            {"name": "Linux System Administration", "url": "https://www.edx.org/course/introduction-to-linux"},
            {"name": "Windows Server Administration", "url": "https://docs.microsoft.com/en-us/learn/windows-server/"}
        ],
        "other_resources": [
            {"name": "Cybersecurity Labs", "url": "https://tryhackme.com/"},
            {"name": "OverTheWire Wargames", "url": "https://overthewire.org/wargames/"}
        ]
    },
    {
        "title": "Core Security Concepts",
        "description": "Gain a strong understanding of the core principles of information security, including confidentiality, integrity, and availability (CIA Triad). Learn about common threats, vulnerabilities, and encryption methods, as well as identity and access management, which form the backbone of cybersecurity practices.",
        "points": [
            {"name": "CIA Triad", "desc": "Confidentiality, Integrity, and Availability principles."},
            {"name": "Threats & Vulnerabilities", "desc": "Malware, phishing, ransomware, and common exploits."},
            {"name": "Cryptography Basics", "desc": "Symmetric/asymmetric encryption, hashing, digital signatures."},
            {"name": "Identity & Access Management", "desc": "Authentication, authorization, and RBAC."}
        ],
        "links": [
            {"name": "Introduction to Cybersecurity (Coursera)", "url": "https://www.coursera.org/specializations/intro-cyber-security"},
            {"name": "Cryptography Basics", "url": "https://www.khanacademy.org/computing/computer-science/cryptography"}
        ],
        "other_resources": [
            {"name": "OWASP Top 10", "url": "https://owasp.org/www-project-top-ten/"},
            {"name": "NIST Cybersecurity Framework", "url": "https://www.nist.gov/cyberframework"}
        ]
    },
    {
        "title": "Network Security",
        "description": "Learn to secure networks against attacks and misconfigurations. This includes deploying firewalls, IDS/IPS systems, VPNs, and monitoring traffic to detect anomalies. Network security is critical for protecting sensitive data and ensuring the integrity of IT infrastructures.",
        "points": [
            {"name": "Firewalls & IDS/IPS", "desc": "Configure firewalls and intrusion detection/prevention systems."},
            {"name": "VPN & Secure Communications", "desc": "Implement encrypted tunnels for safe communication."},
            {"name": "Network Monitoring", "desc": "Monitor traffic for anomalies using tools like Wireshark and Zeek."}
        ],
        "links": [
            {"name": "Network Security Fundamentals", "url": "https://www.coursera.org/learn/network-security"}
        ],
        "other_resources": [
            {"name": "Wireshark Labs", "url": "https://www.wireshark.org/"},
            {"name": "Zeek Network Security Monitor", "url": "https://zeek.org/"}
        ]
    },
    {
        "title": "Web Application Security",
        "description": "Develop skills to secure web applications against common vulnerabilities and attacks. Understand OWASP Top 10 risks, apply secure coding practices, and conduct web security testing to protect applications from SQL injection, XSS, CSRF, and other attacks.",
        "points": [
            {"name": "OWASP Top 10", "desc": "Learn about SQL Injection, XSS, CSRF, and other common web risks."},
            {"name": "Secure Coding Practices", "desc": "Follow guidelines to minimize vulnerabilities in code."},
            {"name": "Web Security Testing", "desc": "Use tools like Burp Suite for penetration testing."}
        ],
        "links": [
            {"name": "OWASP Web Security Testing Guide", "url": "https://owasp.org/www-project-web-security-testing-guide/"},
            {"name": "Burp Suite Docs", "url": "https://portswigger.net/burp/documentation"}
        ],
        "other_resources": [
            {"name": "Hack The Box Labs", "url": "https://www.hackthebox.eu/"},
            {"name": "PortSwigger Web Security Academy", "url": "https://portswigger.net/web-security"}
        ]
    },
    {
        "title": "Cloud Security",
        "description": "Understand cloud security principles and how to protect resources in AWS, Azure, and GCP. Learn IAM policies, monitoring, logging, and best practices for secure cloud deployments. Cloud security is increasingly critical as enterprises adopt cloud-first strategies.",
        "points": [
            {"name": "Cloud Provider Security", "desc": "AWS, Azure, GCP security features and best practices."},
            {"name": "IAM & Policies", "desc": "Manage users, roles, and policies in cloud services."},
            {"name": "Monitoring & Logging", "desc": "Set up cloud monitoring and auditing mechanisms."}
        ],
        "links": [
            {"name": "AWS Security Fundamentals", "url": "https://www.aws.training/Details/Curriculum?id=20685"},
            {"name": "Azure Security Docs", "url": "https://docs.microsoft.com/en-us/azure/security/"}
        ],
        "other_resources": [
            {"name": "GCP Security Overview", "url": "https://cloud.google.com/security"},
            {"name": "Cloud Security Alliance", "url": "https://cloudsecurityalliance.org/"}
        ]
    },
    {
        "title": "Vulnerability Assessment & Penetration Testing",
        "description": "Learn to identify system vulnerabilities and perform ethical penetration testing. Gain hands-on experience with tools such as Nessus, OpenVAS, Metasploit, and Burp Suite to simulate attacks, find weaknesses, and recommend remediation.",
        "points": [
            {"name": "Vulnerability Scanning", "desc": "Use Nessus, OpenVAS, or Qualys to detect vulnerabilities."},
            {"name": "Penetration Testing", "desc": "Simulate attacks to find and fix weaknesses using Metasploit, Burp Suite."}
        ],
        "links": [
            {"name": "Metasploit Unleashed", "url": "https://www.offensive-security.com/metasploit-unleashed/"},
            {"name": "Nessus Documentation", "url": "https://docs.tenable.com/nessus/"}
        ],
        "other_resources": [
            {"name": "OWASP Testing Guide", "url": "https://owasp.org/www-project-web-security-testing-guide/"},
            {"name": "TryHackMe Pentesting Labs", "url": "https://tryhackme.com/paths/outline/pentesting"}
        ]
    },
    {
        "title": "Digital Forensics & Incident Response",
        "description": "Learn how to investigate cyber incidents and recover from attacks. Master log analysis, forensic tools, and incident response planning to ensure organizations can quickly detect, respond, and recover from security breaches.",
        "points": [
            {"name": "Log Analysis", "desc": "Analyze system, application, and network logs for suspicious activity."},
            {"name": "Forensics Tools", "desc": "Use tools like Autopsy, FTK, or Volatility to investigate incidents."},
            {"name": "Incident Response Planning", "desc": "Develop playbooks for breach containment and recovery."}
        ],
        "links": [
            {"name": "SANS Digital Forensics Courses", "url": "https://www.sans.org/cyber-security-courses/forensics/"},
            {"name": "Volatility Framework", "url": "https://www.volatilityfoundation.org/"}
        ],
        "other_resources": [
            {"name": "Autopsy Forensics Tool", "url": "https://www.sleuthkit.org/autopsy/"},
            {"name": "Incident Response Guide (NIST)", "url": "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf"}
        ]
    },
    {
        "title": "Advanced Topics & Emerging Threats",
        "description": "Stay ahead of cutting-edge security challenges, including AI-powered attacks, cloud-native security, container security, and zero trust architectures. Understand how to implement modern security frameworks to protect complex enterprise environments.",
        "points": [
            {"name": "AI & Cybersecurity", "desc": "Understand AI-driven attacks and defenses."},
            {"name": "Cloud-Native Security", "desc": "Secure Kubernetes, containers, and microservices."},
            {"name": "Zero Trust Architecture", "desc": "Implement least-privilege and identity-centric security."}
        ],
        "links": [
            {"name": "Zero Trust Security Guide", "url": "https://www.nist.gov/news-events/news/2020/08/zero-trust-architecture"}  
        ],
        "other_resources": [
            {"name": "Kubernetes Security Best Practices", "url": "https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/"},
            {"name": "Cloud Security Blog (CSA)", "url": "https://cloudsecurityalliance.org/blog/"}
        ]
    },
    {
        "title": "Continuous Learning",
        "description": "Validate your cybersecurity skills and advance your career through certifications. Learn the progression from entry-level certifications like CompTIA Security+ to advanced certifications like OSCP and CISSP. Continuously engage with the cybersecurity community and follow trends to remain current in this rapidly evolving field.",
        "points": [
            {"name": "Entry-Level", "desc": "CompTIA Security+, CCNA Security."},
            {"name": "Intermediate", "desc": "CEH, eJPT, CySA+."},
            {"name": "Advanced", "desc": "OSCP, CISSP, CISM."},
        ],
        "links": [
            {"name": "CompTIA Security+", "url": "https://www.comptia.org/certifications/security"},
            {"name": "OSCP Training", "url": "https://www.offensive-security.com/pwk-oscp/"}
        ],
        "other_resources": [
            {"name": "Krebs on Security Blog", "url": "https://krebsonsecurity.com/"},
            {"name": "CVE Database", "url": "https://cve.mitre.org/"}
        ]
    }
]
@app.route("/")
def home():
    return redirect(url_for('cybersecurity_engineer'))


def render_page():
    return render_template("roadmaps/cybersecurity_engineer.html", roadmap=CYBERSECURITY_ROADMAP)

if __name__ == "__main__":
    app.run(debug=True)
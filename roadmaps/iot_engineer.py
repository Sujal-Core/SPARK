from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory
BASE_DIR = Path(__file__).resolve().parent.parent  # Correct __file__
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))  # Correct __name__
IOT_ENGINEER_ROADMAP = [
    {
        "title": "Foundations of IoT & Embedded Systems",
        "description": "This stage introduces the core concepts of the Internet of Things (IoT) and embedded systems, providing a solid foundation for building smart connected devices. You will learn how IoT devices work, their architecture, communication methods, and the role of embedded systems in enabling intelligence at the edge. This stage emphasizes understanding both the hardware and software aspects, allowing you to work effectively with sensors, microcontrollers, and programming languages that drive IoT solutions. By mastering these fundamentals, you will be prepared for more advanced topics such as data analytics, edge computing, and IoT security.",
        "points": [
            {"name": "IoT Basics", "desc": "Understand IoT architecture, use cases, and how devices communicate with each other and the cloud."},
            {"name": "Embedded Systems", "desc": "Study microcontrollers and microprocessors, including memory, I/O, and interfacing with hardware."},
            {"name": "Programming Foundations", "desc": "Strengthen C, C++, and Python skills for embedded programming and data handling."}
        ],
        "links": [
            {"name": "Introduction to IoT (Coursera)", "url": "https://www.coursera.org/learn/iot"},
            {"name": "Embedded Systems Essentials (Udemy)", "url": "https://www.udemy.com/course/embedded-systems/"}
        ],
        "other_resources": [
            {"name": "Arduino Documentation", "url": "https://www.arduino.cc/en/Tutorial/HomePage"},
            {"name": "Raspberry Pi Foundation", "url": "https://www.raspberrypi.org/"}
        ]
    },
    {
        "title": "IoT Hardware & Circuit Design",
        "description": "In this stage, you will gain hands-on experience with IoT hardware and circuit design, focusing on sensors, actuators, and microcontrollers. You will learn how to design and prototype circuits using breadboards, modules, and standard electronic components. Emphasis is placed on understanding how devices interact with the physical environment, reading sensor data, and controlling actuators. Practical experience in building and testing circuits is critical for creating reliable IoT devices, preparing you for real-world applications like home automation, industrial monitoring, and wearable devices.",
        "points": [
            {"name": "Microcontrollers", "desc": "Work with Arduino, ESP32, or STM32 to read sensor data and control actuators."},
            {"name": "Circuit Prototyping", "desc": "Use breadboards, resistors, capacitors, and modules to design simple circuits."},
            {"name": "Sensor Integration", "desc": "Learn to connect temperature, motion, and other sensors for real-world data collection."}
        ],
        "links": [
            {"name": "Arduino Programming (Udemy)", "url": "https://www.udemy.com/course/arduino-systems/"},
            {"name": "Electronics for IoT (Coursera)", "url": "https://www.coursera.org/learn/electronics"}
        ],
        "other_resources": [
            {"name": "ESP32 Projects", "url": "https://randomnerdtutorials.com/projects-esp32/"},
            {"name": "Hackster.io IoT Projects", "url": "https://www.hackster.io/"}
        ]
    },
    {
        "title": "Networking & Communication Protocols",
        "description": "This stage covers how IoT devices communicate over networks, which is critical for building connected solutions. You will learn the fundamentals of TCP/IP, UDP, DNS, and HTTP, as well as specialized IoT protocols like MQTT, CoAP, and AMQP that are optimized for low-power, low-bandwidth devices. Understanding wireless communication technologies such as Wi-Fi, Bluetooth Low Energy (BLE), LoRa, and Zigbee is essential for creating efficient, reliable, and scalable IoT systems. This knowledge enables you to design systems that are not only functional but also secure and efficient in real-world deployment.",
        "points": [
            {"name": "Networking Basics", "desc": "Learn TCP/IP, UDP, DNS, and HTTP for device communication."},
            {"name": "IoT Protocols", "desc": "Understand MQTT, CoAP, and AMQP for low-power and efficient messaging."},
            {"name": "Wireless Communication", "desc": "Work with Wi-Fi, Bluetooth Low Energy (BLE), LoRa, and Zigbee for IoT connectivity."}
        ],
        "links": [
            {"name": "IoT Protocols Explained (Udemy)", "url": "https://www.udemy.com/course/iot-protocols/"},
            {"name": "Networking Fundamentals (Cisco)", "url": "https://www.netacad.com/courses/networking"}
        ],
        "other_resources": [
            {"name": "MQTT Official Docs", "url": "http://mqtt.org/documentation"},
            {"name": "LoRaWAN Alliance", "url": "https://lora-alliance.org/"}
        ]
    },
    {
        "title": "IoT Programming & Edge Computing",
        "description": "This stage focuses on programming IoT devices and implementing edge computing solutions. You will learn how to run Python or MicroPython scripts on devices like Raspberry Pi or ESP32 to prototype quickly and process data locally. Edge computing allows real-time decision-making, reduces latency, and lowers bandwidth usage by performing computations closer to the source of data. You will also understand real-time system constraints, interrupts, and optimization techniques for mission-critical IoT applications. By mastering these skills, you can develop highly responsive and intelligent IoT devices.",
        "points": [
            {"name": "Python for IoT", "desc": "Use Python and MicroPython on Raspberry Pi or ESP32 for quick prototyping."},
            {"name": "Edge Computing", "desc": "Perform data processing locally on devices to reduce latency and bandwidth usage."},
            {"name": "Real-Time Systems", "desc": "Understand timing constraints, interrupts, and optimization for IoT applications."}
        ],
        "links": [
            {"name": "MicroPython Documentation", "url": "https://docs.micropython.org/"},
            {"name": "Edge Computing Fundamentals (Coursera)", "url": "https://www.coursera.org/learn/edge-computing"}
        ],
        "other_resources": [
            {"name": "FreeCodeCamp IoT Tutorials", "url": "https://www.freecodecamp.org/news/tag/iot/"},
            {"name": "MIT IoT Lectures", "url": "https://ocw.mit.edu/"}
        ]
    },
    {
        "title": "IoT Cloud & Data Management",
        "description": "Learn to connect IoT devices to cloud platforms for storage, analytics, and remote management. This stage emphasizes cloud-based data ingestion, device management, and visualization. You will explore AWS IoT Core, Azure IoT Hub, and other cloud services to collect and analyze telemetry from multiple devices. You will also learn to visualize data using Grafana, Power BI, or custom dashboards to extract actionable insights. Mastering cloud integration is essential for creating scalable IoT systems capable of handling large-scale deployments.",
        "points": [
            {"name": "AWS IoT Core", "desc": "Use AWS services to connect devices, store telemetry, and analyze data."},
            {"name": "Azure IoT Hub", "desc": "Manage devices and telemetry ingestion at scale on Microsoft Azure."},
            {"name": "Data Visualization", "desc": "Visualize IoT data using Grafana, Power BI, or custom dashboards."}
        ],
        "links": [
            {"name": "AWS IoT Workshop", "url": "https://aws.amazon.com/iot-core/"},
            {"name": "Azure IoT Hub Training", "url": "https://learn.microsoft.com/en-us/training/paths/azure-iot/"}
        ],
        "other_resources": [
            {"name": "Google Cloud IoT", "url": "https://cloud.google.com/solutions/iot"},
            {"name": "ThingSpeak IoT Platform", "url": "https://thingspeak.com/"}
        ]
    },
    {
        "title": "IoT Security & Privacy",
        "description": "IoT devices often handle sensitive data and interact with critical systems, making security and privacy essential. This stage focuses on protecting devices, networks, and data from attacks and breaches. You will learn about device authentication, secure boot, firmware updates, encryption, and secure storage. Network security practices such as TLS, VPNs, and intrusion detection systems are explored to ensure safe communication. Compliance with data privacy laws, such as GDPR, is also emphasized to safeguard user data. By mastering these concepts, you can develop IoT systems that are both reliable and trusted by users.",
        "points": [
            {"name": "Device Security", "desc": "Implement authentication, secure boot, and encrypted storage."},
            {"name": "Network Security", "desc": "Secure IoT traffic using TLS, VPNs, and intrusion detection systems."},
            {"name": "Data Privacy", "desc": "Ensure compliance with data privacy laws like GDPR for IoT data."}
        ],
        "links": [
            {"name": "IoT Security Fundamentals (Coursera)", "url": "https://www.coursera.org/learn/iot-security"},
            {"name": "Cybersecurity for IoT (edX)", "url": "https://www.edx.org/course/cybersecurity-and-the-internet-of-things"}
        ],
        "other_resources": [
            {"name": "OWASP IoT Security Guidelines", "url": "https://owasp.org/www-project-iot-security/"},
            {"name": "NIST IoT Framework", "url": "https://csrc.nist.gov/publications/detail/sp/800-183/final"}
        ]
    },
    {
        "title": "IoT Data Analytics & AI Integration",
        "description": "IoT generates massive volumes of data that can provide actionable insights. In this stage, you will learn how to preprocess, clean, and aggregate data collected from IoT devices. You will also integrate AI and machine learning models to implement predictive maintenance, anomaly detection, automation, and smart decision-making. Techniques for running lightweight AI models directly on edge devices (Edge AI) using frameworks like TensorFlow Lite or PyTorch Mobile are covered. Mastery of these skills allows you to transform raw IoT data into intelligent applications that drive business value and operational efficiency.",
        "points": [
            {"name": "Data Preprocessing", "desc": "Clean, transform, and aggregate IoT data for analysis."},
            {"name": "ML for IoT", "desc": "Deploy machine learning models for predictive maintenance, anomaly detection, and automation."},
            {"name": "Edge AI", "desc": "Run lightweight AI models directly on IoT devices using TensorFlow Lite or PyTorch Mobile."}
        ],
        "links": [
            {"name": "AI for IoT (Coursera)", "url": "https://www.coursera.org/learn/ai-for-iot"},
            {"name": "Edge AI Fundamentals (Udemy)", "url": "https://www.udemy.com/course/edge-ai/"}
        ],
        "other_resources": [
            {"name": "TensorFlow Lite Docs", "url": "https://www.tensorflow.org/lite"},
            {"name": "Edge Impulse Platform", "url": "https://edgeimpulse.com/"}
        ]
    },
    {
        "title": "System Integration & Troubleshooting",
        "description": "This stage emphasizes integrating hardware, software, and cloud components to build complete IoT solutions. You will learn how to connect multiple devices, sensors, and actuators with cloud services, ensuring seamless end-to-end communication. Techniques for monitoring system health, setting up alerts, and analyzing logs are explored to maintain reliability. Additionally, troubleshooting methods are covered to diagnose and fix common issues with hardware, software, and networking. These skills are crucial for deploying robust IoT systems that operate smoothly in real-world environments.",
        "points": [
            {"name": "Integration", "desc": "Connect devices, networks, and services into end-to-end IoT systems."},
            {"name": "Monitoring", "desc": "Set up logs, alerts, and dashboards to monitor system health."},
            {"name": "Troubleshooting", "desc": "Diagnose and fix common issues with hardware, software, and networking."}
        ],
        "links": [
            {"name": "IoT System Design Guide", "url": "https://www.iotforall.com/iot-system-design-guide"},
            {"name": "Troubleshooting IoT Systems (Udemy)", "url": "https://www.udemy.com/course/iot-troubleshooting/"}
        ],
        "other_resources": [
            {"name": "IoT Central Community", "url": "https://www.iotcentral.io/"},
            {"name": "Reddit IoT Forum", "url": "https://www.reddit.com/r/IOT/"}
        ]
    },
    {
        "title": "IoT Project Development",
        "description": "Hands-on projects are the best way to consolidate your IoT knowledge. In this stage, you will work on real-world projects such as smart home automation, industrial IoT monitoring, and healthcare devices. This stage emphasizes practical skills like connecting sensors, programming devices, collecting and visualizing data, and integrating cloud services. By completing projects, you will develop a strong portfolio that demonstrates your ability to design, implement, and deploy IoT solutions. Practical experience is key to understanding the challenges and nuances of IoT system development.",
        "points": [
            {"name": "Smart Home Projects", "desc": "Build IoT-based home automation systems using Arduino or Raspberry Pi."},
            {"name": "Industrial IoT", "desc": "Develop predictive maintenance or sensor monitoring systems for factories."},
            {"name": "Healthcare IoT", "desc": "Create wearable or remote monitoring devices for patient care."}
        ],
        "links": [
            {"name": "IoT Projects (Hackster.io)", "url": "https://www.hackster.io/projects/tags/iot"},
            {"name": "Raspberry Pi Projects", "url": "https://projects.raspberrypi.org/en/"}
        ],
        "other_resources": [
            {"name": "GitHub IoT Projects", "url": "https://github.com/topics/iot-project"},
            {"name": "Awesome IoT GitHub", "url": "https://github.com/HQarroum/awesome-iot"}
        ]
    },
    {
        "title": "Continuous Learning & Industry Trends",
        "description": "The IoT industry evolves rapidly, with new hardware, protocols, AI techniques, and security standards emerging constantly. This stage focuses on staying up-to-date with industry trends, emerging technologies like 5G, edge AI, LoRaWAN, and next-gen sensors. Participation in communities, forums, conferences, and meetups is emphasized to network with professionals and learn best practices. Additionally, certifications such as AWS IoT Specialty, Cisco IoT, and other credentials can help validate your expertise and make you more competitive in the job market. Continuous learning ensures you remain capable of designing and deploying cutting-edge IoT solutions.",
        "points": [
            {"name": "Emerging Tech", "desc": "Follow 5G, edge AI, and new wireless protocols for IoT."},
            {"name": "Communities & Conferences", "desc": "Join IoT meetups, IEEE groups, and international IoT conferences."},
            {"name": "Certifications", "desc": "Earn IoT certifications (Cisco, AWS IoT Specialty) to validate skills."}
        ],
        "links": [
            {"name": "IoT World Conference", "url": "https://tmt.knect365.com/iot-world/"},
            {"name": "Coursera IoT Specializations", "url": "https://www.coursera.org/browse/information-technology/iot"}
        ],
        "other_resources": [
            {"name": "IEEE IoT Journal", "url": "https://ieee-iotj.org/"},
            {"name": "IoT World Today", "url": "https://www.iotworldtoday.com/"}
        ]
    }
]

def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/iot_engineer.html", roadmap=IOT_ENGINEER_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('iot_engineer'))

    @app.route("/iot_engineer")
    def iot_engineer():
        return render_page()

    app.run(debug=True)
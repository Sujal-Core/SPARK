# roadmap/edge_road.py
from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory (project_root/templates)
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))


EMBEDDED_SYSTEM_ENGINEER_ROADMAP = [
    {
        "title": "1. Foundations of Electronics & Circuits",
        "description": "Start with understanding how electronic components work, how circuits behave, and how hardware interacts with software.",
        "points": [
            {"name": "Electronics Basics", "desc": "Resistors, capacitors, diodes, transistors"},
            {"name": "Circuit Theory", "desc": "Ohm’s law, Kirchhoff’s laws, series/parallel circuits"},
            {"name": "Tools", "desc": "Multimeter, breadboard, power supply basics"}
        ],
        "links": [
            {"name": "All About Circuits", "url": "https://www.allaboutcircuits.com/"},
            {"name": "Electronics Khan Academy", "url": "https://www.khanacademy.org/science/electrical-engineering"}
        ]
    },
    {
        "title": "2. C/C++ Programming",
        "description": "Embedded systems rely heavily on low-level, memory-efficient programming languages such as C and C++.",
        "points": [
            {"name": "C Programming", "desc": "Pointers, memory, structs, arrays"},
            {"name": "C++ Basics", "desc": "Classes, objects, OOP principles"},
            {"name": "Memory", "desc": "Heap, stack, manual memory management"}
        ],
        "links": [
            {"name": "Learn C", "url": "https://www.learn-c.org/"},
            {"name": "C++ Reference", "url": "https://cplusplus.com/"}
        ]
    },
    {
        "title": "3. Microcontrollers",
        "description": "Learn how to program microcontrollers such as Arduino, ESP32, STM32, and PIC.",
        "points": [
            {"name": "Arduino", "desc": "Digital I/O, PWM, sensors, timers"},
            {"name": "ESP32", "desc": "WiFi/Bluetooth modules, IoT firmware"},
            {"name": "STM32", "desc": "ARM Cortex-M programming, HAL drivers"}
        ],
        "links": [
            {"name": "Arduino Docs", "url": "https://docs.arduino.cc/"},
            {"name": "STM32Cube", "url": "https://www.st.com/en/ecosystems/stm32cube.html"}
        ]
    },
    {
        "title": "4. Embedded C & Firmware Development",
        "description": "Learn how software interacts with microcontroller hardware, registers, and peripherals.",
        "points": [
            {"name": "Registers", "desc": "Memory-mapped I/O, flags, control registers"},
            {"name": "Interrupts", "desc": "ISR handling, priority configuration"},
            {"name": "Timers", "desc": "Delays, counters, PWM configuration"}
        ],
        "links": []
    },
    {
        "title": "5. Sensors & Actuators",
        "description": "Learn how embedded devices interact with the physical world through input/output components.",
        "points": [
            {"name": "Sensors", "desc": "Temperature, IR, ultrasonic, pressure"},
            {"name": "Actuators", "desc": "Motors, relays, servos, LEDs"},
            {"name": "Signal Conditioning", "desc": "Filters, amplification, ADC/DAC"}
        ],
        "links": []
    },
    {
        "title": "6. Communication Protocols",
        "description": "Protocols allow microcontrollers and external devices to communicate.",
        "points": [
            {"name": "UART", "desc": "Serial communication basics"},
            {"name": "SPI", "desc": "High-speed sensor and memory communication"},
            {"name": "I2C", "desc": "Multi-device communication with minimal pins"}
        ],
        "links": []
    },
    {
        "title": "7. Real-Time Operating Systems (RTOS)",
        "description": "Use RTOS to schedule tasks efficiently for real-time embedded applications.",
        "points": [
            {"name": "FreeRTOS", "desc": "Tasks, queues, semaphores"},
            {"name": "Task Management", "desc": "Context switching, priorities"},
            {"name": "Interrupt Handling", "desc": "Latency optimization"}
        ],
        "links": []
    },
    {
        "title": "8. Embedded Linux Basics",
        "description": "Learn Linux-based boards and how firmware interacts with OS kernels.",
        "points": [
            {"name": "Raspberry Pi", "desc": "GPIO, Linux commands, Python"},
            {"name": "Yocto", "desc": "Building custom Linux images"},
            {"name": "Device Drivers", "desc": "Kernel modules and hardware abstraction"}
        ],
        "links": []
    },
    {
        "title": "9. PCB Design & Hardware Tools",
        "description": "Create your own custom hardware boards for embedded products.",
        "points": [
            {"name": "PCB Tools", "desc": "KiCad, Eagle"},
            {"name": "Schematic Design", "desc": "Component placement, power routing"},
            {"name": "Testing", "desc": "Oscilloscope, logic analyzer"}
        ],
        "links": []
    },
    {
        "title": "10. IoT Systems",
        "description": "Connect embedded systems to cloud platforms and mobile apps.",
        "points": [
            {"name": "IoT Cloud", "desc": "AWS IoT, Firebase, Azure IoT"},
            {"name": "MQTT", "desc": "Lightweight message communication"},
            {"name": "Networking", "desc": "WiFi, Bluetooth, LoRa"}
        ],
        "links": []
    },
    {
        "title": "11. Power Management",
        "description": "Design embedded systems optimized for low power usage.",
        "points": [
            {"name": "Sleep Modes", "desc": "Deep sleep, light sleep"},
            {"name": "Battery Management", "desc": "Charging circuits, Li-ion safety"},
            {"name": "Efficiency", "desc": "Voltage regulators, power gating"}
        ],
        "links": []
    },
    {
        "title": "12. Debugging & Testing",
        "description": "Learn to diagnose hardware and firmware problems.",
        "points": [
            {"name": "JTAG", "desc": "Low-level debugging"},
            {"name": "Debuggers", "desc": "GDB, OpenOCD"},
            {"name": "Simulation", "desc": "Proteus, TinkerCAD"}
        ],
        "links": []
    },
    {
        "title": "13. Safety & Standards",
        "description": "Embedded systems often power critical devices, so safety is essential.",
        "points": [
            {"name": "ISO 26262", "desc": "Functional safety for automotive"},
            {"name": "EMI/EMC", "desc": "Electromagnetic compliance basics"},
            {"name": "Reliability", "desc": "Fail-safe design principles"}
        ],
        "links": []
    },
    {
        "title": "14. Build Real Embedded Projects",
        "description": "Show practical skills through hands-on hardware development.",
        "points": [
            {"name": "Mini Projects", "desc": "Line follower robot, weather station"},
            {"name": "Intermediate", "desc": "IoT home automation, sensor fusion"},
            {"name": "Advanced", "desc": "Drone firmware, real-time robotics"}
        ]
    },
    {
        "title": "15. Portfolio & Internship Prep",
        "description": "Prepare for placements by showcasing hardware + firmware skills.",
        "points": [
            {"name": "GitHub Portfolio", "desc": "Show PCB files, firmware, schematics"},
            {"name": "Resume", "desc": "Highlight tools, boards, protocols"},
            {"name": "Interview Prep", "desc": "C, microcontrollers, debugging questions"}
        ]
    }
]


def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/embedded_system_engineer.html", roadmap= EMBEDDED_SYSTEM_ENGINEER_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('embedded_system_engineer'))

    @app.route("/embedded_system_engineer")
    def embedded_system_engineer():
        return render_page()

    app.run(debug=True)


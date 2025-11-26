# roadmap/edge_road.py
from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory (project_root/templates)
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

# Edge Engineer Roadmap (role-accurate variable)
EDGE_ENGINEER_ROADMAP = [
    {
        "title": "Foundations: Systems & Networking",
        "description": "Develop a solid grasp of OS, filesystems, and resource constraints common on gateways and devices. Learn IP networking, routing, NAT, VLANs, and wireless specifics so you can design reliable data paths across constrained, lossy, or intermittent links.",
        "points": [
            {"name": "Linux & Filesystems", "desc": "Systemd, journald, udev, ext4/xfs, read-only roots, OTA partitions"},
            {"name": "Networking", "desc": "IPv4/IPv6, subnetting, DHCP/DNS, TLS, firewalls, NAT and routing"},
            {"name": "Wireless", "desc": "Wi‑Fi, LTE/5G, LoRaWAN, BLE; coverage, interference, roaming"},
            {"name": "Time & NTP", "desc": "Clock sync, monotonic clocks, GPS time, drift handling"},
            {"name": "Resource Limits", "desc": "CPU/mem/storage caps, temp throttling, power budgets"}
        ],
        "links": [
            {"name": "The Linux Command Line", "url": "https://linuxcommand.org/tlcl.php"},
            {"name": "Julia Evans (Networking)", "url": "https://jvns.ca/zines/"}
        ],
        "other_resources": [
            {"name": "BusyBox", "url": "https://busybox.net/"},
            {"name": "Chrony (NTP)", "url": "https://chrony-project.org/"}
        ]
    },
    {
        "title": "Hardware, Protocols & Buses",
        "description": "Understand device buses and industrial protocols to interface with sensors and actuators. Choose physical layers, connectors, and power designs that survive real environments and meet regulatory requirements.",
        "points": [
            {"name": "MCUs & SBCs", "desc": "ARM SBCs (Pi/Jetson), STM32/ESP32; GPIO, interrupts, DMA"},
            {"name": "Buses", "desc": "I2C/SPI/UART, USB, CAN/CAN‑FD, RS‑485/Modbus, EtherCAT"},
            {"name": "Industrial Protocols", "desc": "OPC UA, MQTT Sparkplug B, PROFINET, Modbus/TCP"},
            {"name": "Sensors & Actuators", "desc": "Signal levels, debouncing, isolation, drivers, calibration"},
            {"name": "Power & Enclosure", "desc": "PSU sizing, UPS, thermal design, ingress protection (IP ratings)"}
        ],
        "links": [
            {"name": "OPC UA", "url": "https://opcfoundation.org/about/opc-technologies/opc-ua/"},
            {"name": "Sparkplug B", "url": "https://www.eclipse.org/tahu/"}
        ],
        "other_resources": [
            {"name": "SocketCAN", "url": "https://www.kernel.org/doc/Documentation/networking/can.txt"},
            {"name": "Modbus Spec", "url": "https://modbus.org/specs.php"}
        ]
    },
    {
        "title": "IoT Messaging & Edge Patterns",
        "description": "Adopt messaging and data models that tolerate unreliable networks. Use topic structures, retained messages, and session state wisely; design local-first patterns with backpressure and store‑and‑forward queues.",
        "points": [
            {"name": "MQTT/AMQP/Kafka", "desc": "QoS levels, retained/last-will, shared subs, edge brokers/gateways"},
            {"name": "Topic Design", "desc": "Hierarchies, wildcards, tenancy, access control per topic"},
            {"name": "Offline Resilience", "desc": "Local queues, disk persistence, retransmit, dedupe and idempotency"},
            {"name": "Compression & Encoding", "desc": "CBOR/Protobuf/Avro trade-offs, schema evolution, binary vs JSON"},
            {"name": "Edge-Cloud Sync", "desc": "Batching, delta updates, conflict handling, replay and compaction"}
        ],
        "links": [
            {"name": "MQTT Essentials", "url": "https://www.hivemq.com/mqtt-essentials/"},
            {"name": "Confluent Kafka", "url": "https://docs.confluent.io/platform/current/overview.html"}
        ],
        "other_resources": [
            {"name": "NATS", "url": "https://docs.nats.io/"},
            {"name": "Eclipse Mosquitto", "url": "https://mosquitto.org/"}
        ]
    },
    {
        "title": "Edge AI & Inference",
        "description": "Run ML inference close to data sources with tight latency and privacy requirements. Optimize models and pipelines for limited compute, memory, and power, while maintaining accuracy and reliability.",
        "points": [
            {"name": "Runtimes", "desc": "TensorRT, ONNX Runtime, OpenVINO, TVM; CPU/GPU/NPU targeting"},
            {"name": "Optimization", "desc": "Quantization, pruning, distillation, op fusion, int8/fp16/fp8"},
            {"name": "Pipelines", "desc": "Zero-copy, batching, async graphs, GStreamer/DeepStream"},
            {"name": "Telemetry", "desc": "Latency/throughput, thermals, frame drops, drift and accuracy"},
            {"name": "Fallbacks", "desc": "Graceful degradation, rule-based backups, remote assist"}
        ],
        "links": [
            {"name": "TensorRT", "url": "https://developer.nvidia.com/tensorrt"},
            {"name": "ONNX Runtime", "url": "https://onnxruntime.ai/"}
        ],
        "other_resources": [
            {"name": "OpenVINO", "url": "https://docs.openvino.ai/"},
            {"name": "NVIDIA DeepStream", "url": "https://developer.nvidia.com/deepstream-sdk"}
        ]
    },
    {
        "title": "Security & Zero Trust",
        "description": "Embed security by design despite physical access and untrusted networks. Use device identity, mutual TLS, secure boot, measured boot, and defense-in-depth across data at rest and in transit.",
        "points": [
            {"name": "Identity & PKI", "desc": "Device certificates, enrollment, rotation, revocation, CRL/OCSP"},
            {"name": "Secure Boot", "desc": "u-boot/UEFI, verified boot, measured boot, TPM/TEE integration"},
            {"name": "Secrets & Storage", "desc": "TPM/SE, disk/file encryption, KMS, sealing to device identity"},
            {"name": "Network Policy", "desc": "mTLS everywhere, least privilege, broker ACLs, firewall rules"},
            {"name": "Hardening & Logs", "desc": "Minimal attack surface, ASLR/relro, audit logs, tamper evidence"}
        ],
        "links": [
            {"name": "NIST Zero Trust", "url": "https://csrc.nist.gov/publications/detail/sp/800-207/final"},
            {"name": "U-Boot Verified Boot", "url": "https://source.denx.de/u-boot/u-boot/-/wikis/Verified-boot"}
        ],
        "other_resources": [
            {"name": "TPM 2.0 TSS", "url": "https://tpm2-software.github.io/"},
            {"name": "Sigstore (cosign)", "url": "https://www.sigstore.dev/"}
        ]
    },
    {
        "title": "Ops: OTA, Fleet & Observability",
        "description": "Operate fleets at scale with safe over‑the‑air updates, staged rollouts, and robust observability. Standardize telemetry, handle constrained uplinks, and maintain remote access for support.",
        "points": [
            {"name": "OTA Updates", "desc": "A/B partitions, atomic swaps, rollbacks, delta updates, signing"},
            {"name": "Fleet Config", "desc": "Remote config/flags, parameter stores, templating and drift checks"},
            {"name": "Observability", "desc": "Metrics/logs/traces, edge-to-cloud gateways, sampling and budgets"},
            {"name": "Remote Access", "desc": "Secure tunnels, just-in-time access, audit trails, break-glass"},
            {"name": "Ticket to Field", "desc": "Runbooks, SLOs for freshness/uplink, incident drills and postmortems"}
        ],
        "links": [
            {"name": "Mender OTA", "url": "https://docs.mender.io/"},
            {"name": "Balena", "url": "https://www.balena.io/docs/"}
        ],
        "other_resources": [
            {"name": "Azure IoT Edge", "url": "https://learn.microsoft.com/azure/iot-edge/"},
            {"name": "AWS IoT Greengrass", "url": "https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-gg.html"}
        ]
    },
    {
        "title": "Containers & Orchestration at Edge",
        "description": "Package workloads for heterogeneous devices. Use lightweight runtimes and orchestrators that tolerate intermittent connectivity and limited resources while providing security boundaries.",
        "points": [
            {"name": "Runtimes", "desc": "containerd/CRI‑O/Docker, Podman, rootless, OCI images, SBOMs"},
            {"name": "Lightweight K8s", "desc": "k3s/microk8s, single-node HA, local storage, edge ingress"},
            {"name": "Scheduling", "desc": "Device capabilities, taints/tolerations, node labels, resource hints"},
            {"name": "Updates & Rollbacks", "desc": "Canary, blue/green, health probes, staged waves with backoffs"},
            {"name": "Security", "desc": "User namespaces, seccomp/AppArmor, read-only FS, image policies"}
        ],
        "links": [
            {"name": "k3s", "url": "https://docs.k3s.io/"},
            {"name": "microk8s", "url": "https://microk8s.io/docs"}
        ],
        "other_resources": [
            {"name": "OCI Spec", "url": "https://opencontainers.org/"},
            {"name": "Kyverno/OPA", "url": "https://kyverno.io/docs/"}
        ]
    },
    {
        "title": "Data Engineering at Edge",
        "description": "Engineer local data pipelines for preprocessing, filtering, and summarization. Use time-series storage and compact file formats with schema evolution and controlled retention.",
        "points": [
            {"name": "Time-Series & Local DBs", "desc": "SQLite/Badger/InfluxDB; write patterns on flash and SD cards"},
            {"name": "Formats", "desc": "Parquet/Avro/Protobuf; schema registry and evolution strategy"},
            {"name": "Preprocessing", "desc": "Filtering, windowing, resampling, feature extraction on device"},
            {"name": "Retention & Privacy", "desc": "Rolling windows, anonymization, tokenization/redaction"},
            {"name": "Sync Policies", "desc": "Edge compaction, prioritized uploads, bandwidth-aware schedules"}
        ],
        "links": [
            {"name": "InfluxDB", "url": "https://docs.influxdata.com/"},
            {"name": "Parquet", "url": "https://parquet.apache.org/docs/"}
        ],
        "other_resources": [
            {"name": "SQLite", "url": "https://sqlite.org/docs.html"},
            {"name": "Apache Avro", "url": "https://avro.apache.org/docs/"}
        ]
    },
    {
        "title": "Real-Time & Determinism",
        "description": "Meet timing guarantees with RTOS or real-time Linux. Isolate critical workloads, pin CPUs, and design lock-free queues while measuring worst-case latency end-to-end.",
        "points": [
            {"name": "PREEMPT_RT", "desc": "Priority inversion, CPU isolation, IRQ affinity, rlimits"},
            {"name": "RTOS", "desc": "FreeRTOS/Zephyr; scheduler tuning, timers, watchdogs"},
            {"name": "I/O Latency", "desc": "SPI/I2C scheduling, DMA, file system latency on flash"},
            {"name": "Lock-Free Patterns", "desc": "Ring buffers, SPSC/MPSC queues, memory barriers"},
            {"name": "Latency Budgets", "desc": "P99/P999 targets, end-to-end measurement, trace and logs"}
        ],
        "links": [
            {"name": "Zephyr RTOS", "url": "https://docs.zephyrproject.org/latest/"},
            {"name": "PREEMPT_RT", "url": "https://wiki.linuxfoundation.org/realtime/start"}
        ],
        "other_resources": [
            {"name": "FreeRTOS", "url": "https://www.freertos.org/"},
            {"name": "LTTng/Perf", "url": "https://lttng.org/"}
        ]
    },
    {
        "title": "Edge Analytics & Control",
        "description": "Close the loop on the edge by aligning analytics with control actions. Build safety interlocks, test degraded modes, and ensure actions are logged with context for forensic analysis.",
        "points": [
            {"name": "Rules & CEP", "desc": "Complex event processing, thresholds, hysteresis, alarm storm control"},
            {"name": "Local Control", "desc": "PID/PLC logic, safety relays, watchdogs, overrides and manual modes"},
            {"name": "Digital Twins", "desc": "Model assets and state, simulate scenarios, validate changes"},
            {"name": "Audit & Forensics", "desc": "Signed logs, time sync, event correlation, tamper evidence"},
            {"name": "Human Factors", "desc": "Operator UIs, alarm classification, safe defaults and failsafe states"}
        ],
        "links": [
            {"name": "Eclipse Kura", "url": "https://www.eclipse.org/kura/"},
            {"name": "Azure Digital Twins", "url": "https://learn.microsoft.com/azure/digital-twins/"}
        ],
        "other_resources": [
            {"name": "Node-RED", "url": "https://nodered.org/"},
            {"name": "Kapacitor/Telegraf", "url": "https://docs.influxdata.com/kapacitor/v1/introduction/overview/"}
        ]
    },
    {
        "title": "Projects & Portfolio",
        "description": "Demonstrate a robust edge solution: device integration, messaging, edge inference, OTA, security, and cloud sync. Document decisions, constraints, and operational procedures clearly.",
        "points": [
            {"name": "End-to-End Demo", "desc": "Sensors → gateway → local inference → cloud sync → dashboards"},
            {"name": "Resilience", "desc": "Offline buffering, retries with jitter, power fail recovery drills"},
            {"name": "Security", "desc": "Device identity, mTLS, verified boot, signed updates, attestation"},
            {"name": "Ops", "desc": "OTA pipeline, staged rollouts, telemetry dashboards, runbooks"},
            {"name": "Docs", "desc": "Architecture diagrams, topic schemas, SLOs, ADRs and test plans"}
        ],
        "links": [
            {"name": "Greengrass Examples", "url": "https://docs.aws.amazon.com/greengrass/latest/developerguide/samples.html"},
            {"name": "Mender Tutorials", "url": "https://docs.mender.io/get-started"}
        ],
        "other_resources": [
            {"name": "Influx + Grafana", "url": "https://grafana.com/docs/grafana/latest/datasources/influxdb/"},
            {"name": "OpenTelemetry", "url": "https://opentelemetry.io/"}
        ]
    },
    {
        "title": "Continuous Learning",
        "description": "Keep up with hardware platforms, kernel and container updates, and edge runtimes. Maintain upgrade playbooks and test matrices for new boards, drivers, and network conditions.",
        "points": [
            {"name": "Release Notes", "desc": "Kernel/LTS, container runtimes, MQTT brokers, IoT SDKs"},
            {"name": "Benchmarks", "desc": "CPU/GPU/NPU perf vs watt, latency under load and poor links"},
            {"name": "Community", "desc": "Meetups, RFCs, issue trackers, public design docs and tutorials"}
        ],
        "links": [
            {"name": "LF Edge", "url": "https://www.lfedge.org/"},
            {"name": "CNCF Edge", "url": "https://tag-runtime.cncf.io/projects/edge/"}
        ],
        "other_resources": [
            {"name": "EdgeX Foundry", "url": "https://www.edgexfoundry.org/"},
            {"name": "K3s Releases", "url": "https://github.com/k3s-io/k3s/releases"}
        ]
    }
]

def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/edge_ai_developer.html", roadmap= EDGE_ENGINEER_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('edge_ai_developer'))

    @app.route("/edge_ai_developer")
    def edge_ai_developer():
        return render_page()

    app.run(debug=True)

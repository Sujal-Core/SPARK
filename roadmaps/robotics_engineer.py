# roadmap/robotics_road.py
from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory (project_root/templates)
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

# Robotics Engineer Roadmap (role-accurate variable)
ROBOTICS_ENGINEER_ROADMAP = [
    {
        "title": "Math, Physics & Programming",
        "description": "Establish a rigorous foundation in linear algebra, calculus, probability, and classical mechanics that underpins kinematics, dynamics, and state estimation. Pair this with strong programming skills in C++ and Python so algorithms translate into performant, real-time code on embedded and desktop platforms.",
        "points": [
            {"name": "Linear Algebra", "desc": "Matrices, transforms, Lie groups (SO(3)/SE(3)), quaternions for rotations"},
            {"name": "Calculus & Optimization", "desc": "Jacobians, gradients, constrained optimization, least squares"},
            {"name": "Probability & Statistics", "desc": "Bayesian inference, Gaussian models, noise, uncertainty propagation"},
            {"name": "Classical Mechanics", "desc": "Newton–Euler, Lagrangian/energy methods, rigid-body dynamics basics"},
            {"name": "C++ for Robotics", "desc": "Templates, RAII, CMake, modern C++ (11/14/17), concurrency and memory"},
            {"name": "Python Tooling", "desc": "NumPy/SciPy, Jupyter, visualization, quick prototyping of algorithms"}
        ],
        "links": [
            {"name": "Modern C++", "url": "https://en.cppreference.com/w/"},
            {"name": "3D Rotations (Quaternions)", "url": "https://www.euclideanspace.com/maths/geometry/rotations/"},
        ],
        "other_resources": [
            {"name": "Matrix Cookbook", "url": "https://www2.imm.dtu.dk/pubdb/edoc/imm3274.pdf"},
            {"name": "Probabilistic Robotics (Book)", "url": "https://mitpress.mit.edu/9780262201629/probabilistic-robotics/"},
            {"name": "Numerical Recipes", "url": "https://numerical.recipes/"}
        ]
    },
    {
        "title": "Linux, Git & Build Systems",
        "description": "Operate confidently on Linux-based systems used in robotics development and deployment. Master version control for multi-repo workspaces and robust build tooling to manage complex C++ and Python dependencies, cross-compilation, and CI.",
        "points": [
            {"name": "Linux Proficiency", "desc": "Shell, processes, systemd, udev rules, permissions, device nodes"},
            {"name": "Git & Mono/Multirepos", "desc": "Submodules/subtrees, branching, CI policies, code reviews"},
            {"name": "Build Tools", "desc": "CMake, colcon/catkin, Bazel; reproducible builds and cache use"},
            {"name": "Cross-compilation", "desc": "ARM toolchains, sysroot creation, linking issues, strip/size tuning"},
            {"name": "Containers", "desc": "Docker dev images, multi-stage builds, ROS images, GPU passthrough"}
        ],
        "links": [
            {"name": "CMake Docs", "url": "https://cmake.org/cmake/help/latest/"},
            {"name": "Git Book", "url": "https://git-scm.com/book/en/v2"}
        ],
        "other_resources": [
            {"name": "colcon", "url": "https://colcon.readthedocs.io/en/released/"},
            {"name": "Bazel", "url": "https://bazel.build/"},
            {"name": "Docker Docs", "url": "https://docs.docker.com/"}
        ]
    },
    {
        "title": "ROS 1/ROS 2 Ecosystem",
        "description": "Use ROS to structure robotics software with nodes, topics, services, and actions. Learn message types, TF transforms, package structure, and the ROS 2 middleware (DDS) for distributed systems, leveraging tooling for logging, debugging, and simulation integration.",
        "points": [
            {"name": "Core Concepts", "desc": "Nodes, topics, services, actions, parameters, message definitions"},
            {"name": "TF & Frames", "desc": "Frame hierarchies, static/dynamic transforms, time synchronization"},
            {"name": "Build & Launch", "desc": "Package structure, CMake/colcon, launch files, remapping, namespaces"},
            {"name": "DDS & QoS", "desc": "Middleware (FastDDS/Cyclone), reliability, deadlines, discovery"},
            {"name": "Tooling", "desc": "ros2 bag, rqt, rviz, diagnostics, logging and roswtf/doctor equivalents"}
        ],
        "links": [
            {"name": "ROS 2 Tutorials", "url": "https://docs.ros.org/en/rolling/Tutorials.html"},
            {"name": "TF2", "url": "https://wiki.ros.org/tf2"}
        ],
        "other_resources": [
            {"name": "Awesome ROS 2", "url": "https://github.com/fkromer/awesome-ros2"},
            {"name": "Fast DDS", "url": "https://fast-dds.docs.eprosima.com/en/latest/"}
        ]
    },
    {
        "title": "Kinematics & Dynamics",
        "description": "Model robots geometrically and dynamically to control their motion. Implement forward and inverse kinematics for serial chains and mobile bases; derive dynamics for torque control, and handle singularities and constraints safely.",
        "points": [
            {"name": "Forward/Inverse Kinematics", "desc": "DH parameters, Jacobians, IK solvers (analytical/numerical)"},
            {"name": "Mobile Robots", "desc": "Differential/omni/ackermann kinematics, nonholonomic constraints"},
            {"name": "Dynamics", "desc": "Rigid-body dynamics, inertia, Coriolis, gravity terms, inverse dynamics"},
            {"name": "Collision & Limits", "desc": "Self-collision, joint/velocity/torque limits, workspace boundaries"},
            {"name": "Libraries", "desc": "KDL, Pinocchio, RBDL; URDF/SRDF for model definitions"}
        ],
        "links": [
            {"name": "Pinocchio", "url": "https://gepettoweb.laas.fr/doc/stack-of-tasks/pinocchio/master/doxygen-html/"},
            {"name": "URDF", "url": "https://wiki.ros.org/urdf"}
        ],
        "other_resources": [
            {"name": "KDL", "url": "https://www.orocos.org/kdl.html"},
            {"name": "RBDL", "url": "https://github.com/rbdl/rbdl"}
        ]
    },
    {
        "title": "Perception & Sensors",
        "description": "Process data from cameras, LiDARs, IMUs, and wheel encoders to estimate state and build environment representations. Calibrate sensors, synchronize time, and fuse measurements while considering noise and failure modes.",
        "points": [
            {"name": "Cameras & Calibration", "desc": "Pinhole models, distortion, stereo calibration, extrinsics with targets"},
            {"name": "LiDAR Processing", "desc": "Scan registration, ground removal, segmentation, obstacle clustering"},
            {"name": "IMU/Encoders", "desc": "Bias/scale estimation, integration, drift, time alignment with vision"},
            {"name": "Depth & RGB-D", "desc": "ToF and structured light, noise profiles, depth filtering, point clouds"},
            {"name": "Tooling", "desc": "OpenCV, PCL, Open3D, sensor_msgs/PointCloud2 and image message bridges"}
        ],
        "links": [
            {"name": "OpenCV", "url": "https://docs.opencv.org/"},
            {"name": "PCL", "url": "https://pointclouds.org/documentation/"}
        ],
        "other_resources": [
            {"name": "Open3D", "url": "http://www.open3d.org/"},
            {"name": "Kalibr (Calibration)", "url": "https://github.com/ethz-asl/kalibr"}
        ]
    },
    {
        "title": "State Estimation & SLAM",
        "description": "Estimate robot pose and map the environment with probabilistic filters and graph optimization. Choose between filtering (EKF/UKF) and smoothing (factor graphs) based on platform dynamics and sensor suite.",
        "points": [
            {"name": "Filtering", "desc": "Kalman/EKF/UKF, error-state filters for IMU, outlier rejection"},
            {"name": "Graph SLAM", "desc": "Pose graphs, factor graphs, loop closure, optimization backends"},
            {"name": "Visual/Visual–Inertial", "desc": "Feature-based vs direct, VIO pipelines, keyframe management"},
            {"name": "LiDAR SLAM", "desc": "Scan-to-map, ICP variants, odometry, map maintenance and relocalization"},
            {"name": "Libraries", "desc": "GTSAM, Ceres, Cartographer, ORB-SLAM/OKVIS/VINS-Mono, LIO-SAM"}
        ],
        "links": [
            {"name": "GTSAM", "url": "https://gtsam.org/"},
            {"name": "Ceres Solver", "url": "http://ceres-solver.org/"}
        ],
        "other_resources": [
            {"name": "Cartographer", "url": "https://google-cartographer.readthedocs.io/"},
            {"name": "ORB-SLAM3", "url": "https://github.com/UZ-SLAMLab/ORB_SLAM3"}
        ]
    },
    {
        "title": "Mapping & Localization",
        "description": "Build maps and localize robustly across GPS-denied or dynamic settings. Manage map formats and coordinate frames, and use semantic information when beneficial.",
        "points": [
            {"name": "Occupancy & TSDF", "desc": "2D occupancy grids, 3D TSDF/ESDF maps, memory and resolution trade-offs"},
            {"name": "Global vs Local", "desc": "Global maps for planning, local submaps for real-time collision checks"},
            {"name": "Semantic Layers", "desc": "Detections/segments fused into maps for planning and interaction"},
            {"name": "Localization", "desc": "AMCL/particle filters, scan matching, global relocalization strategies"},
            {"name":"Map Management", "desc": "Save/load, loop closures, multi-session merging, drift correction"}
        ],
        "links": [
            {"name": "OctoMap", "url": "https://octomap.github.io/"},
            {"name": "Cartographer", "url": "https://google-cartographer.readthedocs.io/"}
        ],
        "other_resources": [
            {"name": "Voxblox/ESDF", "url": "https://github.com/ethz-asl/voxblox"},
            {"name": "RTAB-Map", "url": "https://introlab.github.io/rtabmap/"}
        ]
    },
    {
        "title": "Planning & Control",
        "description": "Plan collision-free, dynamically feasible motions and track them with robust controllers. Combine geometric planning with trajectory optimization and MPC for performance under constraints.",
        "points": [
            {"name": "Geometric Planning", "desc": "Grid/graph search (A*, D*), sampling (RRT/RRT*, PRM), heuristics"},
            {"name": "Trajectory Optimization", "desc": "CHOMP, STOMP, MPPI, iLQR; cost design, smoothing, time parameterization"},
            {"name": "Model Predictive Control", "desc": "Constraints, receding horizon, warm-starts, robustification"},
            {"name": "Classical Control", "desc": "PID, LQR/LQG, feedforward terms, tracking with disturbances"},
            {"name": "Libraries", "desc": "OMPL, MoveIt, Control Toolbox; ROS control and hardware interfaces"}
        ],
        "links": [
            {"name": "OMPL", "url": "https://ompl.kavrakilab.org/"},
            {"name": "MoveIt", "url": "https://moveit.picknik.ai/"}
        ],
        "other_resources": [
            {"name": "Control Toolbox (CT)", "url": "https://adrlab.bitbucket.io/ct/"},
            {"name": "mpc_ros resources", "url": "https://github.com/topics/model-predictive-control"}
        ]
    },
    {
        "title": "Embedded & Real-Time Systems",
        "description": "Deploy algorithms on real hardware with deterministic timing. Use RTOSes or real-time Linux, design safe communication between MCU and SBC, and profile performance with the hardware in the loop.",
        "points": [
            {"name": "MCU Platforms", "desc": "STM32/ESP32, FreeRTOS, timer interrupts, DMA, drivers and HALs"},
            {"name": "Real-Time Linux", "desc": "PREEMPT_RT, priorities, CPU pinning/isolation, lock-free queues"},
            {"name": "Buses & Protocols", "desc": "CAN, UART, I2C/SPI, EtherCAT, synchronization, CRC and watchdogs"},
            {"name": "Profiling", "desc": "Cycle counts, cache effects, memory footprint, power and thermal limits"},
            {"name": "Firmware Tooling", "desc": "CMake + cross toolchains, unit tests on firmware, bootloaders and OTA"}
        ],
        "links": [
            {"name": "FreeRTOS", "url": "https://www.freertos.org/"},
            {"name": "PREEMPT_RT", "url": "https://wiki.linuxfoundation.org/realtime/start"}
        ],
        "other_resources": [
            {"name": "Zephyr RTOS", "url": "https://docs.zephyrproject.org/latest/"},
            {"name": "SocketCAN", "url": "https://www.kernel.org/doc/Documentation/networking/can.txt"}
        ]
    },
    {
        "title": "Simulation, HIL & Digital Twins",
        "description": "Simulate sensors, dynamics, and environments to iterate quickly and de-risk field testing. Progress from software-in-the-loop to hardware-in-the-loop and maintain fidelity as features evolve.",
        "points": [
            {"name": "Simulators", "desc": "Gazebo/Ignition, Webots, Isaac Sim/Unity/Unreal; sensor and physics fidelity"},
            {"name": "Scenario Design", "desc": "Edge cases, randomized worlds, domain randomization for robustness"},
            {"name": "HIL Loops", "desc": "MCU-in-loop, driver stubs, latency measurement, fault injection"},
            {"name": "CI with Sim", "desc": "Headless runs in CI, golden logs, regression baselines and tolerances"},
            {"name": "Data Generation", "desc": "Synthetic datasets for perception and planning with labels/ground truth"}
        ],
        "links": [
            {"name": "Gazebo (Ignition)", "url": "https://gazebosim.org/home"},
            {"name": "NVIDIA Isaac Sim", "url": "https://developer.nvidia.com/isaac-sim"}
        ],
        "other_resources": [
            {"name": "Webots", "url": "https://cyberbotics.com/doc/guide/index"},
            {"name": "AirSim", "url": "https://microsoft.github.io/AirSim/"}
        ]
    },
    {
        "title": "Safety, Testing & Compliance",
        "description": "Engineer for safety from the start: hazard analysis, FMEA, watchdogs, and graceful degradation. Write tests across levels, log everything needed for incident analysis, and understand applicable standards in your domain.",
        "points": [
            {"name": "Safety Analysis", "desc": "Hazard/risk analysis, FMEA/FMECA, safety cases, fault trees"},
            {"name": "Watchdogs & Failsafes", "desc": "Heartbeat checks, safe-stop states, e-stop integration and tests"},
            {"name": "Testing Pyramid", "desc": "Unit, integration, simulation, HIL, soak tests, property-based tests"},
            {"name": "Logging & Telemetry", "desc": "Structured logs, synchronized traces, black boxes, postmortems"},
            {"name": "Standards", "desc": "ISO 26262 (auto), IEC 61508 (functional safety), ISO 10218 (industrial)"}
        ],
        "links": [
            {"name": "ISO 26262 Overview", "url": "https://www.iso.org/standard/68383.html"},
            {"name": "IEC 61508 Overview", "url": "https://webstore.iec.ch/publication/5510"}
        ],
        "other_resources": [
            {"name": "ISO 10218 (Industrial Robots)", "url": "https://www.iso.org/standard/66118.html"},
            {"name": "MISRA Guidelines", "url": "https://www.misra.org.uk/"}
        ]
    },
    {
        "title": "Edge AI for Robotics",
        "description": "Integrate perception and decision models efficiently on embedded platforms. Optimize models, manage thermal and power limits, and design fallback strategies for degraded sensing.",
        "points": [
            {"name": "Model Choices", "desc": "Detectors/segmenters/trackers, depth estimation, keypoint/pose networks"},
            {"name": "Optimization", "desc": "Quantization, pruning, TensorRT/OpenVINO, compile-to-kernel runtimes"},
            {"name": "Pipelines", "desc": "Zero-copy, batching, async graphs, multi-sensor fusion with timestamps"},
            {"name": "Fallbacks", "desc": "Heuristic backups, confidence gating, watchdog-triggered simplifications"},
            {"name": "Telemetry", "desc": "FPS/latency tracking, thermal throttling awareness, power budgets"}
        ],
        "links": [
            {"name": "TensorRT", "url": "https://developer.nvidia.com/tensorrt"},
            {"name": "OpenVINO", "url": "https://docs.openvino.ai/latest/index.html"}
        ],
        "other_resources": [
            {"name": "ONNX Runtime", "url": "https://onnxruntime.ai/"},
            {"name": "TVM", "url": "https://tvm.apache.org/"}
        ]
    },
    {
        "title": "Cloud, DevOps & Fleet Ops",
        "description": "Operate fleets with observability, updates, and data pipelines. Implement secure OTA, configuration management, and backend services to analyze logs and improve autonomy over time.",
        "points": [
            {"name": "OTA & Config", "desc": "A/B updates, staged rollouts, rollback safety, feature flags, parameter servers"},
            {"name": "Observability", "desc": "Metrics/logs/traces from robots, edge-to-cloud gateways, bandwidth budgets"},
            {"name": "Data Ops", "desc": "Upload/curate field logs, labeling queues, dataset versioning for ML"},
            {"name": "Security", "desc": "mTLS, device identity, TPM/secure elements, key rotation, attestation"},
            {"name": "Backends", "desc": "APIs for telemetry and commands, message brokers, time-series stores"}
        ],
        "links": [
            {"name": "ROS 2 Security (SROS2)", "url": "https://design.ros2.org/articles/ros2_dds_security.html"},
            {"name": "Open-RMF (fleet mgmt)", "url": "https://osrf.github.io/ros2multirobotbook/"}
        ],
        "other_resources": [
            {"name": "Eclipse Zenoh", "url": "https://zenoh.io/"},
            {"name": "MQTT (Eclipse Mosquitto)", "url": "https://mosquitto.org/"}
        ]
    },
    {
        "title": "Projects & Portfolio",
        "description": "Show end-to-end capabilities: a simulated or real robot with perception, localization, planning, and control, backed by logging, tests, and safety mechanisms. Document assumptions and performance clearly.",
        "points": [
            {"name": "End-to-End Demo", "desc": "Bring-up, mapping/localization, planning/control, teleop and autonomy modes"},
            {"name": "Simulation + HIL", "desc": "Repeatable scenarios, CI runs, sensor latency budgets, golden baselines"},
            {"name": "Docs & Safety", "desc": "System diagrams, TF trees, logs, failure drills, watchdogs and e-stop"},
            {"name": "Metrics & Videos", "desc": "KPIs (localization drift, success rate, MTBF), videos and dashboards"},
            {"name": "Open Source", "desc": "Reusable nodes, packages, and clear READMEs for the community"}
        ],
        "links": [
            {"name": "ROS 2 Tutorials", "url": "https://docs.ros.org/en/rolling/Tutorials.html"},
            {"name": "OMPL + MoveIt Examples", "url": "https://moveit.picknik.ai/"}
        ],
        "other_resources": [
            {"name": "ROS Index", "url": "https://index.ros.org/"},
            {"name": "Awesome Robotics Libraries", "url": "https://github.com/jslee02/awesome-robotics-libraries"}
        ]
    },
    {
        "title": "Continuous Learning",
        "description": "Stay current with literature, standards, and tooling. Revisit fundamentals and evaluate new stacks through controlled experiments before field adoption.",
        "points": [
            {"name": "Reading Pipeline", "desc": "arXiv robotics (cs.RO), ICRA/IROS/RSS papers, blog digests and forums"},
            {"name": "Standards & Safety", "desc": "Follow updates relevant to your industry and incorporate checklists"},
            {"name": "Communities", "desc": "ROS Discourse, robotics Slack/Discords, conferences, and open-source"},
            {"name": "Skill Deep Dives", "desc": "SLAM variants, MPC, non-linear control, embedded optimizations"},
            {"name": "Benchmarking", "desc": "Maintain scenarios/datasets to compare algorithms and regressions"}
        ],
        "links": [
            {"name": "ROS Discourse", "url": "https://discourse.ros.org/"},
            {"name": "arXiv cs.RO", "url": "https://arxiv.org/list/cs.RO/recent"}
        ],
        "other_resources": [
            {"name": "Open Robotics", "url": "https://www.openrobotics.org/"},
            {"name": "Robotics Stack Exchange", "url": "https://robotics.stackexchange.com/"}
        ]
    }
]

def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/robotics_engineer.html", roadmap=ROBOTICS_ENGINEER_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('robotics_engineer'))

    @app.route("/robotics_engineer")
    def robotics_engineer():
        return render_page()

    app.run(debug=True)
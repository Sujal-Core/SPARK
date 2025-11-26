# roadmap/appdev_road.py
from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory (project_root/templates)
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

# App Developer Roadmap (role-accurate variable)
APP_DEVELOPER_ROADMAP = [
    {
        "title": "Mobile Foundations",
        "description": "Understand mobile platform fundamentals and constraints. Learn app lifecycles, UI threads, background work limits, permissions, power/network constraints, and store distribution basics so features ship reliably across device models and OS versions.",
        "points": [
            {"name": "Platform Basics", "desc": "Activities/ViewControllers, app lifecycle, navigation stacks"},
            {"name": "Threads & Handlers", "desc": "Main/UI vs background, run loops, structured concurrency"},
            {"name": "Permissions", "desc": "Runtime prompts, rationale, denial flows, privacy-sensitive APIs"},
            {"name": "Networking", "desc": "Reachability, metered networks, timeouts, retries and backoff"},
            {"name": "Store Readiness", "desc": "Bundle IDs, signing, provisioning, app icons/screenshots, metadata"}
        ],
        "links": [
            {"name": "Android App Fundamentals", "url": "https://developer.android.com/guide/components/fundamentals"},
            {"name": "Apple Human Interface Guidelines", "url": "https://developer.apple.com/design/human-interface-guidelines/"}
        ],
        "other_resources": [
            {"name": "Material Design", "url": "https://m3.material.io/"},
            {"name": "Apple HIG Components", "url": "https://developer.apple.com/design/human-interface-guidelines/components/overview/"}
        ]
    },
    {
        "title": "Languages & Toolchains",
        "description": "Pick native stacks or cross-platform and gain fluency in the language, build system, and IDE. Configure code style, linting, and test runners to create fast feedback loops.",
        "points": [
            {"name": "Android (Kotlin)", "desc": "Coroutines/Flows, Gradle, Android Studio, Jetpack libraries"},
            {"name": "iOS (Swift)", "desc": "Swift Concurrency (async/await), Xcode, Swift Package Manager"},
            {"name": "Cross-Platform", "desc": "Flutter/Dart or React Native/TypeScript; dev server and hot reload"},
            {"name": "Build Config", "desc": "Build variants, flavors/schemes, feature flags and environment files"},
            {"name": "Static Analysis", "desc": "Detekt/ktlint, SwiftLint, ESLint/TS, pre-commit hooks in CI"}
        ],
        "links": [
            {"name": "Kotlin Docs", "url": "https://kotlinlang.org/docs/home.html"},
            {"name": "Swift Language Guide", "url": "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/"}
        ],
        "other_resources": [
            {"name": "Flutter Docs", "url": "https://docs.flutter.dev/"},
            {"name": "React Native Docs", "url": "https://reactnative.dev/docs/getting-started"}
        ]
    },
    {
        "title": "UI Architecture & Patterns",
        "description": "Design maintainable UI layers with modern patterns and composition. Use reactive paradigms, predictable state, navigation, and theming to build accessible and consistent interfaces.",
        "points": [
            {"name": "Declarative UI", "desc": "Jetpack Compose, SwiftUI, Flutter widgets, RN components"},
            {"name": "State Patterns", "desc": "MVVM/MVI/Redux, unidirectional data flow, events and effects"},
            {"name": "Navigation", "desc": "Deep links, back stack, safe args, state restoration"},
            {"name": "Theming & A11y", "desc": "Dynamic color, dark mode, font scaling, screen reader support"},
            {"name": "Design Systems", "desc": "Tokens, components, docs; Storybook/Showkase/SwiftUI previews"}
        ],
        "links": [
            {"name": "Jetpack Compose", "url": "https://developer.android.com/jetpack/compose"},
            {"name": "SwiftUI", "url": "https://developer.apple.com/xcode/swiftui/"}
        ],
        "other_resources": [
            {"name": "Flutter Material 3", "url": "https://m3.material.io/develop/flutter"},
            {"name": "Storybook", "url": "https://storybook.js.org/"}
        ]
    },
    {
        "title": "Networking & Data",
        "description": "Build resilient data layers with offline support. Manage caching, persistence, and sync conflicts; secure traffic; and integrate with modern backend APIs and push services.",
        "points": [
            {"name": "HTTP Clients", "desc": "Retrofit/OkHttp, URLSession/Alamofire, Fetch APIs in RN/Flutter http"},
            {"name": "Caching & Offline", "desc": "Room/Core Data/Realm/sqlite, normalized stores, background sync"},
            {"name": "API Styles", "desc": "REST/GraphQL/gRPC; pagination, websockets, push notifications"},
            {"name": "Security", "desc": "TLS pinning, cert rotation, auth tokens, Keychain/Keystore storage"},
            {"name": "Image & Media", "desc": "Coil/Glide/Picasso, AVFoundation/ExoPlayer; prefetching and memory"}
        ],
        "links": [
            {"name": "Android Networking (OkHttp/Retrofit)", "url": "https://square.github.io/okhttp/"},
            {"name": "URLSession", "url": "https://developer.apple.com/documentation/foundation/urlsession"}
        ],
        "other_resources": [
            {"name": "Room", "url": "https://developer.android.com/training/data-storage/room"},
            {"name": "Core Data", "url": "https://developer.apple.com/documentation/coredata"}
        ]
    },
    {
        "title": "App Architecture & Modularization",
        "description": "Separate concerns to scale teams and builds. Modularize features and core libraries, define clear boundaries and contracts, and enforce versioning with API surfaces and dependency rules.",
        "points": [
            {"name": "Layers", "desc": "Presentation, domain, data; dependency inversion and DI frameworks"},
            {"name": "Modules", "desc": "Feature modules, dynamic delivery/split APKs, Swift packages"},
            {"name": "Contracts", "desc": "Interfaces for navigation, events, and data; test doubles for seams"},
            {"name": "Performance", "desc": "Build graph optimization, incremental builds, codegen where helpful"},
            {"name": "Configuration", "desc": "Env switching, secrets management, build-time vs runtime flags"}
        ],
        "links": [
            {"name": "Android App Architecture", "url": "https://developer.android.com/topic/architecture"},
            {"name": "Clean Architecture iOS", "url": "https://clean-swift.com/"}
        ],
        "other_resources": [
            {"name": "Hilt/Koin/Dagger", "url": "https://developer.android.com/training/dependency-injection"},
            {"name": "Tuist / Swift Package Manager", "url": "https://www.swift.org/package-manager/"}
        ]
    },
    {
        "title": "Testing & Quality",
        "description": "Create confidence with fast unit tests, UI tests, and snapshot tests. Use contract tests for APIs, mock network layers, and run tests in CI with sharding and flake control.",
        "points": [
            {"name": "Unit & VM Tests", "desc": "JUnit/KotlinTest, XCTest; fake repositories, coroutine/test schedulers"},
            {"name": "UI/E2E", "desc": "Espresso/UIAutomator, XCUITest; deterministic selectors and waits"},
            {"name": "Snapshot & Golden", "desc": "Paparazzi/Shot/SnapshotTesting for UI regressions"},
            {"name": "Contract Tests", "desc": "Pact/Schema validation for REST/GraphQL; offline fixtures"},
            {"name": "CI & Reports", "desc": "Parallel runs, flaky retries, coverage, HTML and JUnit outputs"}
        ],
        "links": [
            {"name": "Espresso", "url": "https://developer.android.com/training/testing/espresso"},
            {"name": "XCUITest", "url": "https://developer.apple.com/documentation/xctest"}
        ],
        "other_resources": [
            {"name": "Paparazzi (Android)", "url": "https://cashapp.github.io/paparazzi/"},
            {"name": "SnapshotTesting (Swift)", "url": "https://github.com/pointfreeco/swift-snapshot-testing"}
        ]
    },
    {
        "title": "Performance & Reliability",
        "description": "Optimize app startup, memory, jank, and battery. Diagnose ANRs and crashes, profile hot paths, and implement backoff, retries, and timeouts for flaky networks and background tasks.",
        "points": [
            {"name": "Startup & Memory", "desc": "Cold/warm start KPIs, lazy init, leak detection, bitmaps and pools"},
            {"name": "Rendering & Jank", "desc": "Frame timelines, overdraw, layout thrash, list perf and diffing"},
            {"name": "Background Work", "desc": "WorkManager/BackgroundTasks; constraints and retries with jitter"},
            {"name": "Crash & ANR", "desc": "Crashlytics/Sentry, ANR traces, breadcrumbs, user impact metrics"},
            {"name": "Power & Data", "desc": "Metered networks, batching, doze/low power modes, offline-first"}
        ],
        "links": [
            {"name": "Android Performance", "url": "https://developer.android.com/topic/performance"},
            {"name": "Instruments (Xcode)", "url": "https://help.apple.com/instruments/mac/current/"}
        ],
        "other_resources": [
            {"name": "LeakCanary", "url": "https://square.github.io/leakcanary/"},
            {"name": "Flipper", "url": "https://fbflipper.com/"}
        ]
    },
    {
        "title": "Security & Privacy",
        "description": "Protect user data and keys. Use platform keystores, encrypt at rest and in transit, and comply with privacy requirements. Build safe logging and redaction to avoid leaking sensitive info.",
        "points": [
            {"name": "Key Storage", "desc": "Android Keystore/iOS Keychain, biometrics, hardware-backed keys"},
            {"name": "Network Security", "desc": "TLS pinning, ATS/Network Security Config, cert rotation"},
            {"name": "Local Data Security", "desc": "SQLCipher/EncryptedSharedPrefs, background snapshot privacy"},
            {"name": "Privacy", "desc": "Permission scopes, data minimization, consent and opt-out flows"},
            {"name": "Supply Chain", "desc": "Dependency scanning, integrity, app attestation/play integrity"}
        ],
        "links": [
            {"name": "Android Keystore", "url": "https://developer.android.com/training/articles/keystore"},
            {"name": "Apple Keychain", "url": "https://developer.apple.com/documentation/security/keychain_services"}
        ],
        "other_resources": [
            {"name": "SQLCipher", "url": "https://www.zetetic.net/sqlcipher/"},
            {"name": "SafetyNet/Play Integrity", "url": "https://developer.android.com/google/play/integrity"}
        ]
    },
    {
        "title": "Release & Store Operations",
        "description": "Automate versioning, signing, and multi-track releases. Integrate feature flags, staged rollouts, and instant feedback channels. Track store metrics and respond quickly to crashes and reviews.",
        "points": [
            {"name": "Signing & Provisioning", "desc": "Keystores/profiles, Apple certs, automatic vs manual signing"},
            {"name": "Pipelines", "desc": "Fastlane/Gradle tasks, notarization, TestFlight/Internal testing"},
            {"name": "Tracks & Rollouts", "desc": "Alpha/beta/production, staged rollout, rollbacks and hotfix lanes"},
            {"name": "Store Listings", "desc": "Localizations, screenshots, privacy nutrition labels, changelogs"},
            {"name": "Telemetry & Reviews", "desc": "ANRs/crashes, vitals, reply to reviews, remote config & flags"}
        ],
        "links": [
            {"name": "Google Play Console", "url": "https://play.google.com/console"},
            {"name": "App Store Connect", "url": "https://appstoreconnect.apple.com/"}
        ],
        "other_resources": [
            {"name": "fastlane", "url": "https://docs.fastlane.tools/"},
            {"name": "Gradle Play Publisher", "url": "https://github.com/Triple-T/gradle-play-publisher"}
        ]
    },
    {
        "title": "Cross-Platform Specialization",
        "description": "Evaluate trade-offs of cross-platform frameworks. Optimize startup and UI performance, integrate native modules where needed, and keep a consistent design system and navigation model.",
        "points": [
            {"name": "Flutter", "desc": "Dart isolates, build modes, widget tree perf, platform channels"},
            {"name": "React Native", "desc": "New architecture (Fabric/TurboModules), bridge costs, Hermes"},
            {"name": "Native Modules", "desc": "Write swift/Kotlin modules for device features or performance"},
            {"name": "Design System", "desc": "Tokens and components shared across platforms, a11y parity"},
            {"name": "Release Strategy", "desc": "Over-the-air updates (CodePush), store policy compliance"}
        ],
        "links": [
            {"name": "Flutter Performance", "url": "https://docs.flutter.dev/perf"},
            {"name": "React Native New Arch", "url": "https://reactnative.dev/architecture/overview"}
        ],
        "other_resources": [
            {"name": "CodePush", "url": "https://learn.microsoft.com/appcenter/distribution/codepush/"},
            {"name": "Hermes Engine", "url": "https://reactnative.dev/docs/hermes"}
        ]
    },
    {
        "title": "Projects & Portfolio",
        "description": "Show production-ready apps: accessible UIs, offline-first data, robust error handling, and clean release pipelines. Include screenshots, videos, performance metrics, and links to stores or test builds.",
        "points": [
            {"name": "E2E App", "desc": "Auth, push notifications, deep links, offline cache, background sync"},
            {"name": "Quality & Perf", "desc": "Crash-free users, cold start, frame time metrics, accessibility checks"},
            {"name": "Release", "desc": "Automated builds, staged rollouts, feature flags, rollback paths"},
            {"name": "Docs", "desc": "README, architecture diagrams, store links, privacy notes, ADRs"}
        ],
        "links": [
            {"name": "Firebase App Distribution", "url": "https://firebase.google.com/products/app-distribution"},
            {"name": "TestFlight", "url": "https://developer.apple.com/testflight/"}
        ],
        "other_resources": [
            {"name": "Firebase Crashlytics", "url": "https://firebase.google.com/products/crashlytics"},
            {"name": "Sentry Mobile", "url": "https://docs.sentry.io/platforms/android/"}
        ]
    },
    {
        "title": "Continuous Learning",
        "description": "Mobile platforms evolve quickly—follow OS releases, SDK updates, and device changes. Maintain upgrade playbooks and refactor periodically to keep tech debt under control.",
        "points": [
            {"name": "Release Notes", "desc": "Android/iOS releases, deprecations, privacy policy changes"},
            {"name": "Refactors", "desc": "Architecture and module health checks, dependency upgrades"},
            {"name": "Community", "desc": "Conferences, meetups, RFCs, example apps and open-source"}
        ],
        "links": [
            {"name": "Android Developers Blog", "url": "https://android-developers.googleblog.com/"},
            {"name": "Apple Developer News", "url": "https://developer.apple.com/news/"}
        ],
        "other_resources": [
            {"name": "iOS Dev Weekly", "url": "https://iosdevweekly.com/"},
            {"name": "Android Weekly", "url": "https://androidweekly.net/"}
        ]
    }
]

@app.route("/")
def home():
    return redirect(url_for('app_developer'))
def render_page():
    return render_template("roadmaps/appdev_eng.html", roadmap=APP_DEVELOPER_ROADMAP)

# ✅ Optional standalone Flask runner for testing
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('app_developer'))

    @app.route("/appdev")
    def app_developer():
        return render_page()

    app.run(debug=True)

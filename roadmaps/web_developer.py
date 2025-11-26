# roadmap/webdev_road.py
from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory (project_root/templates)
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

# Web Developer Roadmap (role-accurate variable)
WEB_DEVELOPER_ROADMAP = [
    {
        "title": "Web Fundamentals",
        "description": "Master the core building blocks of the web: semantic HTML for structure and accessibility, modern CSS for layout and responsive design, and vanilla JavaScript for the DOM, events, and browser APIs. These skills create a durable foundation that transfers across frameworks.",
        "points": [
            {"name": "HTML Semantics", "desc": "Headings/landmarks, forms and inputs, media, ARIA basics"},
            {"name": "CSS Layout", "desc": "Flexbox, Grid, cascade/layers, variables, container queries"},
            {"name": "Responsive & A11y", "desc": "Fluid design, color contrast, keyboard nav, focus management"},
            {"name": "JavaScript Core", "desc": "ES6+, modules, async/await, fetch, DOM APIs, storage"},
            {"name": "Browser Basics", "desc": "Rendering pipeline, paint/composite, devtools for layout and JS"}
        ],
        "links": [
            {"name": "MDN Web Docs", "url": "https://developer.mozilla.org/"},
            {"name": "web.dev Learn", "url": "https://web.dev/learn/"}
        ],
        "other_resources": [
            {"name": "A11y Project", "url": "https://www.a11yproject.com/"},
            {"name": "Can I use", "url": "https://caniuse.com/"}
        ]
    },
    {
        "title": "Version Control & Linux",
        "description": "Use Git effectively to collaborate and ship safely. Work productively on Linux or WSL with shell tools to inspect files, logs, and processes, automating repetitive tasks during development.",
        "points": [
            {"name": "Git", "desc": "Branching strategies, PR reviews, rebasing/merging, tags/releases"},
            {"name": "Shell", "desc": "awk/sed/grep, pipes, environment, npm scripts and Makefiles"},
            {"name": "DevTools", "desc": "Chrome/Firefox tools, Lighthouse, network panel, performance"}
        ],
        "links": [
            {"name": "Git Book", "url": "https://git-scm.com/book/en/v2"},
            {"name": "The Linux Command Line", "url": "https://linuxcommand.org/tlcl.php"}
        ]
    },
    {
        "title": "Frontend Frameworks",
        "description": "Adopt a primary framework to build complex client apps. Learn component composition, routing, data fetching, and state management; add server rendering to improve performance and SEO when needed.",
        "points": [
            {"name": "Framework Choice", "desc": "React/Vue/Svelte/Solid; reactivity model and ecosystem"},
            {"name": "Routing", "desc": "File-based routing, nested routes, data loaders/actions"},
            {"name": "State & Data", "desc": "Context/Redux/Pinia, TanStack Query/SWR for cache + mutations"},
            {"name": "SSR/SSG", "desc": "Next.js/Nuxt/SvelteKit; streaming, caching, edge runtimes"},
            {"name": "Forms", "desc": "Validation, a11y patterns, optimistic UI, error boundaries"}
        ],
        "links": [
            {"name": "React Docs", "url": "https://react.dev/"},
            {"name": "Next.js Docs", "url": "https://nextjs.org/docs"}
        ],
        "other_resources": [
            {"name": "TanStack Query", "url": "https://tanstack.com/query/latest"},
            {"name": "Redux Toolkit", "url": "https://redux-toolkit.js.org/"}
        ]
    },
    {
        "title": "Styling & Design Systems",
        "description": "Scale styles with reusable components and tokens. Use utility CSS or CSS-in-JS thoughtfully, ensure accessibility in components, and document your system for consistent UI across pages.",
        "points": [
            {"name": "Utility CSS", "desc": "Tailwind; responsive utilities, design tokens, theming"},
            {"name": "CSS-in-JS", "desc": "Styled-components/Emotion; runtime vs compile-time trade-offs"},
            {"name": "Component Kits", "desc": "MUI/Chakra/Ant/Headless UI; accessible primitives"},
            {"name": "Design Tokens", "desc": "Colors, spacing, typography scales via CSS variables"},
            {"name": "Dark Mode", "desc": "prefers-color-scheme, high-contrast themes, reduced motion"}
        ],
        "links": [
            {"name": "Tailwind Docs", "url": "https://tailwindcss.com/docs"},
            {"name": "MUI", "url": "https://mui.com/"}
        ],
        "other_resources": [
            {"name": "Headless UI", "url": "https://headlessui.com/"},
            {"name": "Design Tokens W3C", "url": "https://tr.designtokens.org/"}
        ]
    },
    {
        "title": "Backend Basics",
        "description": "Learn the essentials of server-side development to build and integrate APIs. Understand HTTP semantics, REST/gRPC, authentication, and data persistence with relational and NoSQL stores.",
        "points": [
            {"name": "Node/Express or Go/FastAPI", "desc": "Routing, middlewares, validation, controllers/services"},
            {"name": "HTTP & APIs", "desc": "Status codes, headers, caching, pagination, OpenAPI"},
            {"name": "Auth", "desc": "Sessions vs tokens, OAuth/OIDC, CSRF, cookie flags"},
            {"name": "Databases", "desc": "Postgres/MySQL + ORM (Prisma/TypeORM), Redis for caching"},
            {"name": "Security", "desc": "Input validation, rate limits, sanitization, dependency audits"}
        ],
        "links": [
            {"name": "Express Guide", "url": "https://expressjs.com/"},
            {"name": "FastAPI", "url": "https://fastapi.tiangolo.com/"}
        ],
        "other_resources": [
            {"name": "OpenAPI Spec", "url": "https://swagger.io/specification/"},
            {"name": "OWASP ASVS", "url": "https://owasp.org/www-project-application-security-verification-standard/"}
        ]
    },
    {
        "title": "Tooling & TypeScript",
        "description": "Use TypeScript for maintainability and confidence in refactors. Configure linters/formatters and bundlers for fast refresh, modern outputs, and small bundles.",
        "points": [
            {"name": "TypeScript", "desc": "Types, generics, narrowing, utility types, strict configs"},
            {"name": "Linters", "desc": "ESLint + Prettier + stylelint; CI gates and pre-commit hooks"},
            {"name": "Bundlers", "desc": "Vite/Webpack/esbuild/SWC; code-splitting and tree-shaking"},
            {"name": "Testing", "desc": "Vitest/Jest, Testing Library, Playwright/Cypress e2e"}
        ],
        "links": [
            {"name": "TypeScript Handbook", "url": "https://www.typescriptlang.org/docs/handbook/intro.html"},
            {"name": "Vite Guide", "url": "https://vitejs.dev/guide/"}
        ],
        "other_resources": [
            {"name": "Testing Library", "url": "https://testing-library.com/docs/"},
            {"name": "Playwright", "url": "https://playwright.dev/docs/intro"}
        ]
    },
    {
        "title": "Performance & Web Vitals",
        "description": "Optimize interaction and loading performance with Core Web Vitals targets. Control JavaScript size, tune images and fonts, and use caching and CDNs for consistent speed.",
        "points": [
            {"name": "Core Web Vitals", "desc": "LCP, CLS, INP; field vs lab data and RUM dashboards"},
            {"name": "Loading Patterns", "desc": "Code-splitting, lazy/streaming, prefetch/prerender strategies"},
            {"name": "Assets", "desc": "AVIF/WebP, responsive images, font subsetting and display modes"},
            {"name": "Caching", "desc": "Immutable assets, service workers, edge caching and rewrites"}
        ],
        "links": [
            {"name": "web.dev/vitals", "url": "https://web.dev/vitals/"},
            {"name": "Image Optimization", "url": "https://web.dev/fast/#images"}
        ],
        "other_resources": [
            {"name": "Lighthouse", "url": "https://developer.chrome.com/docs/lighthouse/"},
            {"name": "Bundlephobia", "url": "https://bundlephobia.com/"}
        ]
    },
    {
        "title": "CI/CD & Deployment",
        "description": "Automate build, test, and deployment with preview environments and safe rollouts. Choose hosting that matches your app style (static, SSR, or hybrid) and instrument for errors and performance.",
        "points": [
            {"name": "Pipelines", "desc": "GitHub Actions/GitLab CI; caches, artifacts, code owners"},
            {"name": "Hosting", "desc": "Vercel/Netlify/Cloudflare Pages or custom containers on K8s"},
            {"name": "Observability", "desc": "Sentry/LogRocket, logs/metrics/traces for SSR backends"},
            {"name": "Env & Secrets", "desc": "Env vars, secret managers, parameter stores, rotation"},
            {"name": "Rollouts", "desc": "Canary/blue-green, feature flags, instant rollback"}
        ],
        "links": [
            {"name": "Vercel Docs", "url": "https://vercel.com/docs"},
            {"name": "Netlify Docs", "url": "https://docs.netlify.com/"}
        ],
        "other_resources": [
            {"name": "Sentry", "url": "https://docs.sentry.io/platforms/javascript/"},
            {"name": "OpenTelemetry", "url": "https://opentelemetry.io/"}
        ]
    },
    {
        "title": "Security & Privacy",
        "description": "Protect users by adopting secure defaults across frontend and backend. Validate inputs, guard cookies, add CSP and other headers, and document data collection with consent where required.",
        "points": [
            {"name": "CSP & Headers", "desc": "CSP, HSTS, Referrer-Policy, XFO, COOP/COEP for isolation"},
            {"name": "XSS & Injection", "desc": "Sanitization, escaping, SSRF/CSRF protections, safe parsers"},
            {"name": "AuthN/Z", "desc": "Sessions/tokens, OAuth/OIDC, RBAC/ABAC, password storage"},
            {"name": "PII & Consent", "desc": "Minimize collection, consent UIs, retention and deletion"}
        ],
        "links": [
            {"name": "OWASP Cheat Sheets", "url": "https://cheatsheetseries.owasp.org/"},
            {"name": "Helmet (Node headers)", "url": "https://helmetjs.github.io/"}
        ],
        "other_resources": [
            {"name": "DOMPurify", "url": "https://github.com/cure53/DOMPurify"},
            {"name": "Trivy", "url": "https://aquasecurity.github.io/trivy/"}
        ]
    },
    {
        "title": "Projects & Portfolio",
        "description": "Build end-to-end web apps demonstrating UI quality, API integration, performance, and deployment. Publish live demos and document trade-offs, limitations, and next steps.",
        "points": [
            {"name": "Full-Stack App", "desc": "Auth, CRUD, search, pagination, file uploads, email/queues"},
            {"name": "Quality", "desc": "A11y checks, unit/e2e tests, visual regression, perf budgets"},
            {"name": "Ops", "desc": "CI/CD, observability, error budgets/SLOs, rollback procedures"},
            {"name": "Docs", "desc": "README, architecture diagrams, OpenAPI, Lighthouse reports"}
        ],
        "links": [
            {"name": "OpenAPI Tools", "url": "https://openapi.tools/"},
            {"name": "Lighthouse CI", "url": "https://github.com/GoogleChrome/lighthouse-ci"}
        ],
        "other_resources": [
            {"name": "Storybook", "url": "https://storybook.js.org/docs"},
            {"name": "Awesome Web Dev", "url": "https://github.com/markodenic/web-development-resources"}
        ]
    },
    {
        "title": "Continuous Learning",
        "description": "Track platform and framework changes, experiment with modern patterns (server components, islands, streaming), and contribute to community examples and documentation.",
        "points": [
            {"name": "Release Notes", "desc": "Browsers, frameworks, runtimes; deprecations and migrations"},
            {"name": "Patterns", "desc": "RSC, islands/partial hydration, edge rendering, RPC over fetch"},
            {"name": "Community", "desc": "Meetups, RFCs, OSS, conference talks and workshops"}
        ],
        "links": [
            {"name": "Chrome Platform Status", "url": "https://chromestatus.com/"},
            {"name": "TC39 Proposals", "url": "https://github.com/tc39/proposals"}
        ],
        "other_resources": [
            {"name": "Smashing Magazine", "url": "https://www.smashingmagazine.com/"},
            {"name": "Frontend Focus", "url": "https://frontendfoc.us/"}
        ]
    }
]

def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/web_developer.html", roadmap=WEB_DEVELOPER_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('web_developer'))

    @app.route("/web_developer")
    def web_developer():
        return render_page()

    app.run(debug=True)
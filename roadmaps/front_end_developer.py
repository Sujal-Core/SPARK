# roadmap/frontend_road.py
from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory (project_root/templates)
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

# Frontend Developer Roadmap (role-accurate variable)
FRONTEND_DEVELOPER_ROADMAP = [
    {
        "title": "Web Foundations",
        "description": "Master the building blocks of the web so your apps render correctly, load fast, and remain accessible. Learn semantic HTML, modern CSS layout, responsive design, and enough vanilla JavaScript to reason about the DOM, events, and browser APIs before adopting frameworks.",
        "points": [
            {"name": "Semantic HTML", "desc": "Headings, landmarks, forms, inputs, attributes, media elements"},
            {"name": "Modern CSS", "desc": "Flexbox, Grid, cascade/layers, logical props, variables, BEM/utility"},
            {"name": "Responsive Design", "desc": "Fluid layout, container queries, media queries, dark mode, DPR"},
            {"name": "JavaScript Core", "desc": "ES6+, modules, async/await, fetch, events, DOM APIs, Web Storage"},
            {"name": "Accessibility", "desc": "Keyboard nav, color contrast, ARIA patterns, focus management"}
        ],
        "links": [
            {"name": "MDN Web Docs", "url": "https://developer.mozilla.org/"},
            {"name": "Web.dev Learn", "url": "https://web.dev/learn/"}
        ],
        "other_resources": [
            {"name": "A11y Project", "url": "https://www.a11yproject.com/"},
            {"name": "Can I use", "url": "https://caniuse.com/"}
        ]
    },
    {
        "title": "Tooling & Package Management",
        "description": "Use modern tooling to develop efficiently and ship optimized bundles. Learn package managers, linters/formatters, TypeScript, and bundlers with code-splitting and modern output targets.",
        "points": [
            {"name": "Package Managers", "desc": "npm, pnpm, yarn; workspaces/monorepos, lockfiles and audit"},
            {"name": "TypeScript", "desc": "Types, generics, narrowing, utility types, tsconfig, strict mode"},
            {"name": "Linters/Formatters", "desc": "ESLint, Prettier, stylelint; CI checks and pre-commit hooks"},
            {"name": "Bundlers/Builders", "desc": "Vite, Webpack, esbuild, SWC; code-splitting, tree-shaking"},
            {"name": "Transpilation Targets", "desc": "browserslist, polyfills, module/nomodule, differential serving"}
        ],
        "links": [
            {"name": "TypeScript Handbook", "url": "https://www.typescriptlang.org/docs/handbook/intro.html"},
            {"name": "Vite Guide", "url": "https://vitejs.dev/guide/"}
        ],
        "other_resources": [
            {"name": "ESLint", "url": "https://eslint.org/docs/latest/"},
            {"name": "Prettier", "url": "https://prettier.io/docs/en/"}
        ]
    },
    {
        "title": "Frontend Frameworks",
        "description": "Adopt a primary framework to build complex UIs with state management, routing, and data fetching. Learn component patterns, accessibility in components, and server rendering strategies.",
        "points": [
            {"name": "React/Vue/Svelte/Solid", "desc": "Reactivity model, lifecycle, composition, SSR/SSG support"},
            {"name": "Routing & Data", "desc": "File-based routing, loaders/actions, mutations, caching, invalidation"},
            {"name": "State Management", "desc": "Context, Redux/RTK, Zustand/Pinia, signals, query libraries"},
            {"name": "Forms", "desc": "Validation, controlled/uncontrolled, optimistic UI, progressive enhancement"},
            {"name": "SSR/SSG/ISR", "desc": "Next.js/Nuxt/SvelteKit; edge/Node runtimes, streaming and caching"}
        ],
        "links": [
            {"name": "React Docs", "url": "https://react.dev/"},
            {"name": "Next.js", "url": "https://nextjs.org/docs"}
        ],
        "other_resources": [
            {"name": "TanStack Query", "url": "https://tanstack.com/query/latest"},
            {"name": "Redux Toolkit", "url": "https://redux-toolkit.js.org/"}
        ]
    },
    {
        "title": "Styling Systems",
        "description": "Scale styles with predictable systems. Choose between utility-first CSS, CSS-in-JS, or component libraries; enforce design tokens and accessibility throughout.",
        "points": [
            {"name": "Utility CSS", "desc": "Tailwind CSS; tokens, responsive utilities, theming"},
            {"name": "CSS-in-JS", "desc": "Styled-components/Emotion, runtime vs build-time trade-offs"},
            {"name": "Component Libraries", "desc": "MUI/Chakra/Ant/Headless UI; customization and a11y patterns"},
            {"name": "Design Tokens", "desc": "Color/spacing/typography scales, CSS variables, themes"},
            {"name": "Theming & Dark Mode", "desc": "Prefers-color-scheme, system vs app toggles, high-contrast"}
        ],
        "links": [
            {"name": "Tailwind Docs", "url": "https://tailwindcss.com/docs"},
            {"name": "MUI", "url": "https://mui.com/material-ui/getting-started/"}
        ],
        "other_resources": [
            {"name": "Headless UI", "url": "https://headlessui.com/"},
            {"name": "Design Tokens W3C", "url": "https://tr.designtokens.org/"}
        ]
    },
    {
        "title": "Data Fetching & APIs",
        "description": "Connect UIs to backends reliably. Use fetch/axios, manage caching and revalidation, and handle errors and retries. Understand REST vs GraphQL vs tRPC and pick for your team’s stack and requirements.",
        "points": [
            {"name": "HTTP Fundamentals", "desc": "Methods, status codes, headers, caching semantics and ETags"},
            {"name": "REST/GraphQL/gRPC", "desc": "Client tooling, schema-driven dev, pagination, batching"},
            {"name": "Data Libraries", "desc": "TanStack Query/SWR/Apollo; cache keys, invalidation, mutations"},
            {"name": "Auth Flows", "desc": "Cookies vs tokens, CSRF, OAuth/OIDC PKCE, refresh strategies"},
            {"name": "Error Handling", "desc": "Boundaries, retry/backoff, offline queues, optimistic UI"}
        ],
        "links": [
            {"name": "MDN Fetch", "url": "https://developer.mozilla.org/docs/Web/API/Fetch_API"},
            {"name": "GraphQL Docs", "url": "https://graphql.org/learn/"}
        ],
        "other_resources": [
            {"name": "Axios", "url": "https://axios-http.com/docs/intro"},
            {"name": "SWR", "url": "https://swr.vercel.app/"}
        ]
    },
    {
        "title": "Testing & Quality",
        "description": "Create a fast feedback loop with unit, component, and end-to-end tests. Test accessibility, interactions, and critical flows with reliable fixtures and CI integration.",
        "points": [
            {"name": "Unit & Component", "desc": "Vitest/Jest, React Testing Library/Cypress Component Testing"},
            {"name": "E2E", "desc": "Playwright/Cypress; selectors, tracing, flake control and retries"},
            {"name": "Accessibility Tests", "desc": "axe-core checks, keyboard traps, focus order, color contrast"},
            {"name": "Visual Regression", "desc": "Storybook snapshots, Percy/Chromatic, threshold tuning"},
            {"name": "CI Integration", "desc": "Parallelism, artifacts/videos, flaky test quarantine"}
        ],
        "links": [
            {"name": "Testing Library", "url": "https://testing-library.com/docs/"},
            {"name": "Playwright", "url": "https://playwright.dev/docs/intro"}
        ],
        "other_resources": [
            {"name": "Cypress", "url": "https://docs.cypress.io/"},
            {"name": "axe-core", "url": "https://github.com/dequelabs/axe-core"}
        ]
    },
    {
        "title": "Performance & Web Vitals",
        "description": "Ship fast, responsive apps by measuring and optimizing Core Web Vitals. Use modern loading patterns, minimize JavaScript, and optimize images, fonts, and critical CSS.",
        "points": [
            {"name": "Core Web Vitals", "desc": "LCP, CLS, INP; thresholds, field vs lab data, RUM dashboards"},
            {"name": "Loading Strategies", "desc": "Code-splitting, lazy/streaming, prefetch/prerender, HTTP/2 push alt"},
            {"name": "Assets", "desc": "Images (AVIF/WebP), responsive sources, fonts (FOIT/FOUT), subsetting"},
            {"name": "JavaScript Diet", "desc": "Reduce bundle size, islands, partial hydration, remove unused code"},
            {"name": "Caching & CDN", "desc": "Immutable assets, SWR, service workers, edge caching and rewrites"}
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
        "title": "Security & Privacy",
        "description": "Defend users and data in the browser. Apply content security policies, sanitize untrusted content, guard cookies and storage, and ensure compliance with privacy expectations.",
        "points": [
            {"name": "CSP & Headers", "desc": "CSP, HSTS, X-Frame-Options, Referrer-Policy, COOP/COEP"},
            {"name": "XSS & Injection", "desc": "Sanitization, DOM sinks, innerHTML risks, template injection"},
            {"name": "Auth in Browser", "desc": "SameSite/HttpOnly/Secure cookies, token storage risks, CSRF"},
            {"name": "Privacy", "desc": "Consent, data minimization, measuring without PII"},
            {"name": "Supply Chain", "desc": "Subresource integrity (SRI), deps audits, lockfiles"}
        ],
        "links": [
            {"name": "OWASP Cheat Sheet Series", "url": "https://cheatsheetseries.owasp.org/"},
            {"name": "CSP Docs", "url": "https://developer.mozilla.org/docs/Web/HTTP/CSP"}
        ],
        "other_resources": [
            {"name": "DOMPurify", "url": "https://github.com/cure53/DOMPurify"},
            {"name": "Snyk Advisor", "url": "https://snyk.io/advisor/"}
        ]
    },
    {
        "title": "Build, Deploy & Observability",
        "description": "Automate builds and deploys with preview environments and guardrails. Observe errors and performance in production and implement progressive rollouts with quick rollback.",
        "points": [
            {"name": "CI/CD", "desc": "Preview builds, artifact caching, test gates, code owners and checks"},
            {"name": "Hosting", "desc": "Vercel/Netlify/Cloudflare Pages or custom; edge vs origin trade-offs"},
            {"name": "Monitoring", "desc": "RUM, error tracking (Sentry), logs/traces for SSR, uptime checks"},
            {"name": "Feature Flags", "desc": "Progressive delivery, A/B tests, kill switches and config"},
            {"name": "Rollbacks", "desc": "Immutable deploys, version pinning, canary and fast revert"}
        ],
        "links": [
            {"name": "Vercel Docs", "url": "https://vercel.com/docs"},
            {"name": "Sentry Frontend", "url": "https://docs.sentry.io/platforms/javascript/"}
        ],
        "other_resources": [
            {"name": "Netlify Docs", "url": "https://docs.netlify.com/"},
            {"name": "Cloudflare Pages", "url": "https://developers.cloudflare.com/pages/"}
        ]
    },
    {
        "title": "Projects & Portfolio",
        "description": "Demonstrate real-world frontend engineering: accessible, responsive UIs with robust data fetching, performance budgets, and CI-backed quality. Explain trade-offs and link to live demos.",
        "points": [
            {"name": "E2E App", "desc": "Auth, routing, forms, data fetching, optimistic updates, error states"},
            {"name": "Performance", "desc": "Web Vitals within budget, images/fonts optimized, code-splitting"},
            {"name": "Quality", "desc": "A11y tests, unit/e2e coverage, visual regression and Storybook"},
            {"name": "Docs", "desc": "README, architecture notes, perf budgets, lighthouse scores, ADRs"}
        ],
        "links": [
            {"name": "Storybook", "url": "https://storybook.js.org/docs"},
            {"name": "Lighthouse CI", "url": "https://github.com/GoogleChrome/lighthouse-ci"}
        ],
        "other_resources": [
            {"name": "Open Props", "url": "https://open-props.style/"},
            {"name": "Awesome React", "url": "https://github.com/enaqx/awesome-react"}
        ]
    },
    {
        "title": "Continuous Learning",
        "description": "Web platforms evolve rapidly—track standards, browser features, and framework releases. Practice by rebuilding small apps with new patterns and sharing insights with the community.",
        "points": [
            {"name": "Release Notes", "desc": "Browser/platform/framework changes, interop updates, deprecations"},
            {"name": "Patterns", "desc": "Server components, islands, streaming/partial hydration"},
            {"name": "Community", "desc": "Meetups, RFCs, contributing examples and docs, conference talks"}
        ],
        "links": [
            {"name": "TC39 Proposals", "url": "https://github.com/tc39/proposals"},
            {"name": "Chrome Platform Status", "url": "https://chromestatus.com/"}
        ],
        "other_resources": [
            {"name": "Smashing Magazine", "url": "https://www.smashingmagazine.com/"},
            {"name": "Frontend Focus", "url": "https://frontendfoc.us/"}
        ]
    }
]

def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/frontend_eng.html", roadmap=FRONTEND_DEVELOPER_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('frontend_developer'))

    @app.route("/frontend_developer")
    def frontend_developer():
        return render_page()

    app.run(debug=True)
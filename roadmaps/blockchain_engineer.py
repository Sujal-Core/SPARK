from flask import Flask, render_template, url_for, redirect
from pathlib import Path

# Resolve project root and templates directory
BASE_DIR = Path(__file__).resolve().parent.parent  # Correct __file__
TEMPLATES_DIR = BASE_DIR / "roadmaps"

# Point Flask at the top-level templates directory
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))  # Correct __name__

blockchain_engineer_ROADMAP = [
    {
        "title": "Foundations of Blockchain",
        "description": "Learn essential computer science concepts and blockchain fundamentals to understand decentralized systems. This includes understanding how distributed networks function, how data integrity is maintained, and why decentralization is key to trustless systems. You'll also gain insights into the differences between traditional databases and blockchain storage.",
        "points": [
            {"name": "Programming Basics", "desc": "Acquire Python or JavaScript skills to interact with blockchains, write scripts, and automate tasks."},
            {"name": "Networking", "desc": "Understand peer-to-peer networks, TCP/IP, and APIs for node-to-node communication."},
            {"name": "Databases", "desc": "Learn SQL and NoSQL databases, and understand how blockchain storage differs from traditional databases."},
            {"name": "Blockchain Basics", "desc": "Understand blocks, chain structure, transactions, nodes, consensus, and decentralization."}
        ],
        "links": [
            {"name": "Blockchain Basics (Coursera)", "url": "https://www.coursera.org/learn/blockchain-basics"}
        ],
        "other_resources": [
            {"name": "Ethereum Whitepaper", "url": "https://ethereum.org/en/whitepaper/"},
            {"name": "Bitcoin Whitepaper", "url": "https://bitcoin.org/bitcoin.pdf"}
        ]
    },
    {
        "title": "Cryptography & Consensus",
        "description": "Dive deep into cryptography and consensus mechanisms that secure blockchain networks. Learn how cryptographic techniques ensure data integrity and authentication, and understand how decentralized networks reach agreement on the state of the blockchain without a central authority. This knowledge is essential for building secure and robust blockchain applications.",
        "points": [
            {"name": "Hash Functions", "desc": "Learn SHA-256, Keccak, and other hashing algorithms to ensure data integrity and security."},
            {"name": "Digital Signatures", "desc": "Understand ECDSA, key pairs, and wallet security for authenticating transactions."},
            {"name": "Merkle Trees", "desc": "Use Merkle Trees for efficient and secure verification of large sets of transactions."},
            {"name": "Consensus Mechanisms", "desc": "Study Proof of Work, Proof of Stake, Byzantine Fault Tolerance, and other consensus methods."}
        ],
        "links": [
            {"name": "Blockchain Specialization – University at Buffalo (Coursera)", "url": "https://www.coursera.org/specializations/blockchain"}
        ],
        "other_resources": [
            {"name": "SWC Registry", "url": "https://swcregistry.io/"}
        ]
    },
    {
        "title": "Smart Contracts",
        "description": "Master smart contract development by learning programming languages, frameworks, and design patterns. Understand how to write contracts that execute automatically, maintain security, and interact with blockchain networks. Gain practical knowledge on deploying and testing contracts on testnets, ensuring your dApps are reliable and bug-free.",
        "points": [
            {"name": "Solidity", "desc": "Primary language for Ethereum smart contracts."},
            {"name": "Vyper & Rust", "desc": "Alternative languages for Ethereum and non-EVM chains."},
            {"name": "Frameworks", "desc": "Use Truffle, Hardhat, and Foundry for building, testing, and deploying contracts."},
            {"name": "Design Patterns", "desc": "Learn ownership, proxy, factory, and access control patterns for safety."}
        ],
        "links": [
            {"name": "Ethereum Blockchain Developer Bootcamp (Udemy)", "url": "https://www.udemy.com/course/blockchain-developer/"}
        ],
        "other_resources": [
            {"name": "Solidity Official Docs", "url": "https://docs.soliditylang.org/"},
            {"name": "OpenZeppelin Contracts", "url": "https://docs.openzeppelin.com/"}
        ]
    },
    {
        "title": "dApp Development",
        "description": "Learn to build decentralized applications (dApps) by integrating smart contracts with frontend interfaces. Understand how blockchain nodes, wallets, and front-end frameworks interact to create responsive, secure, and user-friendly decentralized applications. Deploy your applications on testnets to simulate real-world conditions safely.",
        "points": [
            {"name": "Web3.js & Ethers.js", "desc": "JavaScript libraries to interact with Ethereum nodes and smart contracts."},
            {"name": "Wallet Integration", "desc": "Connect wallets like MetaMask for user interactions."},
            {"name": "Frontend Frameworks", "desc": "Use React or Next.js for responsive dApp UIs."},
            {"name": "Testnets", "desc": "Deploy smart contracts on test networks like Goerli or Mumbai."}
        ],
        "links": [
            {"name": "Build a Blockchain & Cryptocurrency | Full-Stack Edition (Udemy)", "url": "https://www.udemy.com/course/build-blockchain-full-stack/"}
        ],
        "other_resources": [
            {"name": "Ethers.js Docs", "url": "https://docs.ethers.io/"},
            {"name": "Web3.js Docs", "url": "https://web3js.readthedocs.io/"}
        ]
    },
    {
        "title": "Blockchain Ecosystem & Infrastructure",
        "description": "Explore tools, services, and infrastructure components that support blockchain applications. Learn about node providers, decentralized storage, oracles, and indexing services to efficiently manage and access blockchain data. Understanding the ecosystem helps you choose the right tools and platforms for your projects.",
        "points": [
            {"name": "Node Providers", "desc": "Use Infura, Alchemy, or QuickNode to access blockchain nodes."},
            {"name": "Oracles", "desc": "Use Chainlink to fetch off-chain data securely."},
            {"name": "Decentralized Storage", "desc": "Store off-chain data using IPFS or Arweave."},
            {"name": "Indexing Services", "desc": "Use The Graph to query blockchain data efficiently."}
        ],
        "links": [
            {"name": "Designing Decentralized Apps (Coursera)", "url": "https://www.coursera.org/specializations/blockchain"}
        ],
        "other_resources": [
            {"name": "The Graph Docs", "url": "https://thegraph.com/docs/"},
            {"name": "Chainlink Docs", "url": "https://docs.chain.link/"}
        ]
    },
    {
        "title": "Security & Auditing",
        "description": "Implement best practices to secure smart contracts and blockchain applications. Learn how to prevent common vulnerabilities, perform audits, and follow secure coding patterns. Security knowledge is crucial to protect assets and maintain trust in decentralized networks.",
        "points": [
            {"name": "Common Vulnerabilities", "desc": "Prevent reentrancy, integer overflow, front-running, and access control flaws."},
            {"name": "Auditing Tools", "desc": "Use Slither, MythX, and Echidna for analysis."},
            {"name": "Secure Patterns", "desc": "Checks-effects-interactions, access controls, fail-safe mechanisms."},
            {"name": "Bug Bounties & Audits", "desc": "Participate in real-world audits or bug bounty programs."}
        ],
        "links": [
            {"name": "Smart Contracts Security Course (Coursera)", "url": "https://www.coursera.org/specializations/blockchain"}
        ],
        "other_resources": [
            {"name": "SWC Registry", "url": "https://swcregistry.io/"},
            {"name": "Slither GitHub / Docs", "url": "https://github.com/crytic/slither"}
        ]
    },
    {
        "title": "Scalability & Advanced Topics",
        "description": "Learn scaling solutions and advanced protocols for high-performance blockchain applications. Study layer-2 solutions, sharding, cross-chain bridges, and advanced consensus protocols. These topics allow developers to build fast, scalable, and efficient decentralized systems that can handle large user bases.",
        "points": [
            {"name": "Layer 2 Scaling", "desc": "Optimistic Rollups, ZK-Rollups, Plasma, and sidechains."},
            {"name": "Cross-Chain Bridges", "desc": "Transfer assets/data between different networks."},
            {"name": "Sharding & State Channels", "desc": "Parallel computations and off-chain channels for scalability."},
            {"name": "Advanced Consensus & Protocols", "desc": "Tendermint, HotStuff, DAG-based consensus, hybrid protocols."}
        ],
        "links": [
            {"name": "Platforms & Scaling (Coursera)", "url": "https://www.coursera.org/specializations/blockchain"}
        ],
        "other_resources": [
            {"name": "Ethereum Layer 2 Docs", "url": "https://ethereum.org/en/layer-2/"},
            {"name": "Cosmos / Tendermint Docs", "url": "https://docs.tendermint.com/"}
        ]
    },
    {
        "title": "Deployment & DevOps",
        "description": "Learn production deployment, monitoring, and maintenance practices for blockchain applications. Understand CI/CD pipelines, monitoring node health, performance metrics, governance mechanisms, and gas optimization. This ensures your applications run efficiently and securely in real-world environments.",
        "points": [
            {"name": "CI/CD Pipelines", "desc": "Automate testing, deployment, and versioning of contracts and dApps."},
            {"name": "Monitoring & Analytics", "desc": "Track gas usage, performance metrics, node health, and logs."},
            {"name": "Governance & Upgrades", "desc": "Implement proxy patterns, DAO governance, and on-chain upgrades."},
            {"name": "Gas Optimization", "desc": "Write efficient smart contracts to minimize gas costs."}
        ],
        "links": [
            {"name": "DevOps for Blockchain (Udemy)", "url": "https://www.udemy.com/course/devops-blockchain/"}
        ],
        "other_resources": [
            {"name": "Ethereum Gas Optimization Guide", "url": "https://ethereum.org/en/developers/docs/gas/"}
        ]
    },
    {
        "title": "DeFi & Financial Applications",
        "description": "Explore decentralized finance protocols, lending platforms, and tokenomics. Learn how DeFi enables peer-to-peer lending, trading, and yield generation without intermediaries. Gain practical knowledge of automated market makers, decentralized exchanges, staking, and yield farming strategies.",
        "points": [
            {"name": "Lending & Borrowing", "desc": "Understand protocols like Aave and Compound."},
            {"name": "AMM & DEX", "desc": "Automated market makers and decentralized exchanges like Uniswap."},
            {"name": "Token Standards", "desc": "ERC-20, ERC-721, ERC-1155 standards and usage."},
            {"name": "Yield Farming & Staking", "desc": "Mechanisms for earning returns in DeFi ecosystems."}
        ],
        "links": [
            {"name": "DeFi and Blockchain Specialization (Coursera)", "url": "https://www.coursera.org/specializations/defi-blockchain"}
        ],
        "other_resources": [
            {"name": "DeFi Pulse", "url": "https://defipulse.com/"},
            {"name": "Uniswap Docs", "url": "https://docs.uniswap.org/"}
        ]
    },
    {
        "title": "NFTs, Gaming & Web3",
        "description": "Develop applications in NFTs, GameFi, and Web3 ecosystems. Learn how blockchain can be applied in digital art, gaming economies, and decentralized content platforms. Gain knowledge of NFT standards, metadata storage, and integrating interactive frontends with smart contracts.",
        "points": [
            {"name": "NFT Development", "desc": "Create and deploy ERC-721 and ERC-1155 NFTs."},
            {"name": "GameFi & Play-to-Earn", "desc": "Integrate blockchain in gaming and virtual economies."},
            {"name": "IPFS & Metadata Storage", "desc": "Store NFT assets and metadata securely off-chain."},
            {"name": "Web3 Integration", "desc": "Connect smart contracts with interactive frontends for user experiences."}
        ],
        "links": [
            {"name": "NFT & Web3 Bootcamp (Udemy)", "url": "https://www.udemy.com/course/nft-web3/"}
        ],
        "other_resources": [
            {"name": "IPFS Docs", "url": "https://docs.ipfs.io/"},
            {"name": "OpenSea Developer Docs", "url": "https://docs.opensea.io/"}
        ]
    },
    {
        "title": "Enterprise Blockchain & Use Cases",
        "description": "Understand private and permissioned blockchains, and real-world enterprise applications. Learn how large organizations implement blockchain for supply chain, healthcare, finance, and governance solutions. Gain hands-on knowledge of frameworks like Hyperledger Fabric and Corda.",
        "points": [
            {"name": "Hyperledger Fabric & Corda", "desc": "Learn private blockchain frameworks for enterprise use cases."},
            {"name": "Supply Chain & Logistics", "desc": "Blockchain for provenance, tracking, and transparency."},
            {"name": "Healthcare & Finance Applications", "desc": "Secure data sharing and compliance with blockchain."},
            {"name": "Governance Models", "desc": "Implement permissioned blockchain governance."}
        ],
        "links": [
            {"name": "Enterprise Blockchain Specialization (Coursera)", "url": "https://www.coursera.org/specializations/enterprise-blockchain"}
        ],
        "other_resources": [
            {"name": "Hyperledger Docs", "url": "https://www.hyperledger.org/use/fabric"},
            {"name": "Corda Docs", "url": "https://docs.r3.com/"}
        ]
    },
    {
        "title": "Testing & QA",
        "description": "Ensure smart contracts and dApps function correctly, reliably, and securely. Learn unit and integration testing, security analysis, fuzzing, and automation techniques. Proper testing is critical to prevent vulnerabilities, bugs, and financial losses in live blockchain systems.",
        "points": [
            {"name": "Unit Testing", "desc": "Test smart contracts using frameworks like Hardhat and Truffle."},
            {"name": "Integration Testing", "desc": "Test dApp interactions with contracts and APIs."},
            {"name": "Security Testing", "desc": "Perform fuzz testing, static analysis, and exploit simulation."},
            {"name": "Test Automation", "desc": "Automate repetitive testing to ensure reliability across deployments."}
        ],
        "links": [
            {"name": "Blockchain Testing & QA (Udemy)", "url": "https://www.udemy.com/course/blockchain-testing/"}
        ],
        "other_resources": [
            {"name": "MythX Docs", "url": "https://mythx.io/"},
            {"name": "Echidna Fuzzing", "url": "https://github.com/crytic/echidna"}
        ]
    },
    {
        "title": "Continuous Learning ",
        "description": "Engage actively with global blockchain communities, participate in collaborative projects and hackathons, pursue continuous learning opportunities, and build a professional network to advance your career in the rapidly evolving blockchain industry.",
        "points": [
            {"name": "Blockchain Communities", "desc": "Join developer forums, Discord servers, and GitHub projects."},
            {"name": "Hackathons & Competitions", "desc": "Participate in ETHGlobal, Chainlink hackathons, and competitions."},
            {"name": "Certifications", "desc": "Consider blockchain certifications like Certified Blockchain Developer (CBD)."}
        ],
        "links": [
            {"name": "ETHGlobal Hackathons", "url": "https://ethglobal.co/"},
            {"name": "Blockchain Developer Certification", "url": "https://www.blockchain-council.org/certifications/certified-blockchain-developer/"}
        ],
        "other_resources": [
            {"name": "CoinDesk News", "url": "https://www.coindesk.com/"},
            {"name": "Crypto Twitter & Dev Blogs", "url": "https://twitter.com/"}
        ]
    }
]

def render_page():
    """This function is used by the main Flask app to render this roadmap page."""
    return render_template("roadmaps/blockchain_engineer.html", roadmap=blockchain_engineer_ROADMAP)

# ---------------- Standalone Runner (for testing) ----------------
if __name__ == "__main__":
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

    @app.route("/")
    def home():
        return redirect(url_for('blockchain_engineer'))

    @app.route("/blockchain_engineer")
    def blockchain_engineer():
        return render_page()

    app.run(debug=True)
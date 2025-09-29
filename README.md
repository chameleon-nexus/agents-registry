# Agents Registry

A centralized registry for AI agents, similar to Maven Central or npm registry.

## Overview

This repository serves as a static file server for AI agent metadata and files. It provides:

- **Distributed Index System**: Category-based index files for better performance
- **Multi-language Support**: English, Chinese (Simplified), Japanese
- **Semantic Versioning**: Full version control for agent updates
- **Agent Metadata**: Individual `metadata.json` files for each agent
- **Agent Files**: Versioned agent files with naming convention `{agent-id}_v{version}.md`
- **GitHub Raw API**: Direct file access via HTTPS

## Structure

```
agents-registry/
├── index/                         # Distributed index system
│   ├── main.json                 # Main index with category overview
│   ├── featured.json             # Featured/popular agents
│   └── categories/               # Category-specific indexes
│       ├── ui-mobile.json        # UI/UX & Mobile agents
│       ├── core-architecture.json # Core Architecture agents
│       ├── web-programming.json   # Web & Application Programming
│       └── ... (20 categories)
├── agents/                       # Agent storage
│   ├── {author}/                 # Author namespace
│   │   ├── {agent-name}/         # Agent directory
│   │   │   ├── metadata.json     # Agent metadata (multilingual)
│   │   │   ├── {agent-id}_v{version}.md  # Versioned agent file
│   │   │   └── README.md         # Documentation (optional)
│   │   └── ...
│   └── ...
├── scripts/                      # Maintenance scripts
└── README.md
```

## API Endpoints

All files are accessible via GitHub Raw API:

### Index Files
- **Main Index**: `https://raw.githubusercontent.com/chameleon-nexus/agents-registry/master/index/main.json`
- **Featured Agents**: `https://raw.githubusercontent.com/chameleon-nexus/agents-registry/master/index/featured.json`
- **Category Index**: `https://raw.githubusercontent.com/chameleon-nexus/agents-registry/master/index/categories/{category}.json`

### Agent Files
- **Agent Metadata**: `https://raw.githubusercontent.com/chameleon-nexus/agents-registry/master/agents/{author}/{agent-name}/metadata.json`
- **Agent File**: `https://raw.githubusercontent.com/chameleon-nexus/agents-registry/master/agents/{author}/{agent-name}/{agent-id}_v{version}.md`

## Categories

The registry is organized into 20 main categories:

### Architecture & System Design
- **core-architecture** (7 agents) - Backend APIs, system architecture, cloud infrastructure
- **ui-mobile** (5 agents) - UI/UX design, mobile development, visual validation

### Programming Languages
- **systems-programming** (4 agents) - C/C++, Rust, Go system programming
- **web-programming** (5 agents) - JavaScript, TypeScript, Python, Ruby, PHP
- **enterprise-programming** (3 agents) - Java, Scala, C# enterprise development
- **specialized-platforms** (4 agents) - Elixir, Unity, SQL, specialized frameworks

### Infrastructure & Operations
- **devops-deployment** (4 agents) - CI/CD, containerization, infrastructure automation
- **database-management** (2 agents) - Database optimization and administration
- **incident-network** (2 agents) - Production incident management, network operations

### Quality Assurance & Security
- **code-quality** (5 agents) - Code review, security auditing, best practices
- **testing-debugging** (4 agents) - Test automation, debugging, error analysis
- **performance-observability** (3 agents) - Performance optimization, monitoring

### Data & AI
- **data-analytics** (2 agents) - Data processing, analytics, business intelligence
- **machine-learning** (4 agents) - ML pipelines, AI applications, prompt engineering

### Documentation & Content
- **documentation** (5 agents) - Technical documentation, API specs, content creation
- **seo-content** (10 agents) - SEO optimization, content strategy, digital marketing

### Business & Operations
- **business-finance** (3 agents) - Business analysis, financial modeling, risk analysis
- **marketing-sales** (2 agents) - Content marketing, sales automation
- **support-legal** (3 agents) - Customer support, HR operations, legal compliance

### Specialized Domains
- **specialized-domains** (4 agents) - Blockchain, payments, legacy modernization

## Multi-language Support

All agent metadata supports three languages:
- **English** (`en`) - Primary language
- **Chinese Simplified** (`zh`) - Chinese translations
- **Japanese** (`ja`) - Japanese translations

Example metadata structure:
```json
{
  "name": {
    "en": "Python Pro",
    "zh": "Python 专家",
    "ja": "Python プロ"
  },
  "description": {
    "en": "Advanced Python development with optimization techniques",
    "zh": "具有优化技术的高级Python开发",
    "ja": "最適化技術を用いた高度なPython開発"
  }
}
```

## Usage

### CLI Tool
```bash
# Install CLI (now available as 'agt' command)
npm install -g @chameleon-nexus/agents-cli

# Search agents
agt search "code review"

# Search with language filter
agt search "python" --language zh

# Install agent
agt install wshobson/python-pro

# List agents by category
agt list --category web-programming

# Show agent details
agt show wshobson/python-pro
```

### VS Code Extension
The Chameleon VS Code extension provides a graphical interface to browse, search, and install agents directly from the registry with full category support and multi-language display.

## Statistics

- **Total Agents**: 84
- **Authors**: 2 (chameleon-team, wshobson)
- **Categories**: 20
- **Languages**: 3 (English, Chinese, Japanese)
- **Largest Category**: SEO & Content Optimization (10 agents)

## Version Control

Each agent supports semantic versioning:
- Version files follow naming convention: `{agent-id}_v{version}.md`
- Metadata tracks all versions in `versions` object
- Latest version always available via `latest` field

## Contributing

1. Fork this repository
2. Add your agent to the appropriate author directory
3. Follow the naming convention: `{agent-id}_v{version}.md`
4. Create multilingual metadata with `en`, `zh`, `ja` fields
5. Submit a pull request

For automated publishing (coming in v2), use the CLI:
```bash
agt publish my-agent.md --category web-programming
```

## License

MIT License

---

*Last updated: September 29, 2025*
*Registry version: 2.0.0*
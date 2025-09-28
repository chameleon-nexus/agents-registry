# Agents Registry

A centralized registry for AI agents, similar to Maven Central or npm registry.

## Overview

This repository serves as a static file server for AI agent metadata and files. It provides:

- **Global Registry**: `registry.json` - Central index of all available agents
- **Agent Metadata**: Individual `metadata.json` files for each agent
- **Agent Files**: Actual agent files and resources
- **GitHub Raw API**: Direct file access via HTTPS

## Structure

```
agents-registry/
├── registry.json              # Global agent index
├── agents/
│   ├── {author}/
│   │   ├── {agent-name}/
│   │   │   ├── metadata.json  # Agent metadata
│   │   │   ├── agent.md       # Agent file
│   │   │   └── README.md      # Documentation
│   │   └── ...
│   └── ...
└── README.md
```

## API Endpoints

All files are accessible via GitHub Raw API:

- **Registry Index**: `https://raw.githubusercontent.com/chameleon-nexus/agents-registry/master/registry.json`
- **Agent Metadata**: `https://raw.githubusercontent.com/chameleon-nexus/agents-registry/master/agents/{author}/{agent-name}/metadata.json`
- **Agent File**: `https://raw.githubusercontent.com/chameleon-nexus/agents-registry/master/agents/{author}/{agent-name}/agent.md`

## Usage

### CLI Tool
```bash
# Install CLI
npm install -g @chameleon-nexus/agents-cli

# Search agents
agents search "code review"

# Install agent
agents install author/agent-name

# List all agents
agents list
```

### VS Code Extension
The Chameleon VS Code extension provides a graphical interface to browse, search, and install agents directly from the registry.

## Contributing

1. Fork this repository
2. Add your agent to the appropriate directory structure
3. Update the `registry.json` file
4. Submit a pull request

## License

MIT License

# Custom Agents Assets

This repository contains default scaffolding options and templates for AI agents on the [xpander.ai](https://xpander.ai) platform.

## Overview

xpander.ai is a Backend-as-a-Service for AI Agents that enables you to deploy AI agents that think, act, and scale across any stack with zero lock-in. This repository provides ready-to-use templates that help developers quickly bootstrap AI agents with the xpander.ai platform.

## Available Templates

### `agno-template/`
A comprehensive template for building AI agents using the [Agno framework](https://github.com/xpander-ai/agno) integrated with xpander.ai platform.

**Features:**
- Agno Framework Integration
- Thinking Tools with step-by-step reasoning
- Dual Mode Support (standalone and with Xpander backend)
- State Management and conversation history
- Async Operations for high-performance execution
- Multi-provider AI support (OpenAI, Anthropic)
- Model Context Protocol (MCP) support
- Docker containerization ready

## Getting Started

1. **Choose a Template**: Select the appropriate template for your AI agent framework
2. **Copy Template**: Copy the template directory to your project location
3. **Follow Template Instructions**: Each template includes its own README with specific setup instructions
4. **Deploy with xpander.ai**: Use the xpander CLI to deploy your agent

## xpander.ai Platform Features

- **Connect to Anything**: Library of agent-ready tools and Agentic Interfaces
- **Agent Graph System**: Design cross-agent and tool dependency graphs for correct behavior
- **Flexible Deployment**: Run on xpander serverless infrastructure or your own
- **Backend Services**: Memory, tools, multi-user state, storage, agent-to-agent messaging
- **Framework Agnostic**: Works with any agent framework and SDK

## Usage with xpander CLI

```bash
# Install xpander CLI
npm install -g xpander-cli

# Login to xpander.ai
xpander login

# Create new agent project
xpander agent new

# Initialize with template
xpander agent init

# Deploy your agent
xpander deploy
```

## Contributing

When adding new templates:

1. Create a new directory with a descriptive name (e.g., `framework-template`)
2. Include a comprehensive README.md explaining the template
3. Provide example configuration files
4. Include Dockerfile for containerization
5. Add .env.example with required environment variables
6. Update this root README to list the new template

## Support

- **Documentation**: Visit [xpander.ai documentation](https://xpander.ai)
- **Platform**: [xpander.ai](https://xpander.ai)
- **CLI Help**: `xpander --help`

## License

See [LICENSE](LICENSE) file for details.

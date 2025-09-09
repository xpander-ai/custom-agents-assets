# xpander.ai + Agno + NeMo

This project integrates [xpander.ai](https://xpander.ai) agents with NVIDIA's NeMo Assistant Toolkit (NAT) and Agno framework, enabling sophisticated AI agent workflows with enterprise-grade LLM capabilities.

## Overview

The xpander.ai NeMo Agent bridges three powerful AI frameworks:
- **xpander.ai SDK**: Provides agent orchestration, task management, and execution tracking
- **NVIDIA NeMo**: Enterprise LLM gateway and model management
- **Agno**: Agent framework for structured AI interactions and tool usage

## Architecture

The integration supports two execution modes:

### 1. Direct Invocation
Run agents directly through the NeMo Assistant Toolkit CLI:
```bash
nat run --config_file nemo_config.yml --input "your prompt here"
```

### 2. Event Listener (Recommended for Production)
Run as a persistent service that listens for xpander.ai task events:
```bash
python xpander_handler.py
```

## Quick Start

### Prerequisites
- Python 3.11+
- xpander.ai API key and organization ID
- LLM API key (OpenAI, Anthropic, or compatible)
- NVIDIA NeMo Assistant Toolkit

### Installation

1. **Clone and setup virtual environment**
   ```bash
   git clone <repository-url>
   cd nemo-tests
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Build and install the package**
   ```bash
   pip install build
   python -m build
   pip install -e .
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` with your credentials:
   ```env
   XPANDER_API_KEY="your_xpander_api_key"
   XPANDER_ORGANIZATION_ID="your_org_id"
   XPANDER_AGENT_ID="your_agent_id"
   OPENAI_API_KEY="your_openai_key"  # or ANTHROPIC_API_KEY
   ```

4. **Test the installation**
   ```bash
   nat run --config_file nemo_config.yml --input "Hello, test the agent setup"
   ```

## Usage

### Direct Invocation Mode

Perfect for testing, development, and one-off agent executions:

```bash
# Simple text input
nat run --config_file nemo_config.yml --input "Analyze this data and provide insights"

# Complex structured input
nat run --config_file nemo_config.yml --input '{"task": "code_review", "files": ["app.py"]}'
```

### Event Listener Mode (Production)

For production deployments, run the persistent event listener:

```bash
python xpander_handler.py
```

This mode:
- ✅ Automatically processes xpander.ai tasks as they arrive
- ✅ Handles concurrent task execution
- ✅ Provides task lifecycle management
- ✅ Supports horizontal scaling
- ✅ Includes error handling and retry logic

### Docker Deployment

Build and run with Docker:

```bash
# Build the image
docker build -t xpander-nemo-agent .

# Run in event listener mode
docker run -d --env-file .env xpander-nemo-agent
```

## Configuration

### NeMo Configuration example (`nemo_config.yml`)

```yaml
general:
  use_uvloop: true
  telemetry:
    logging:
      console:
        _type: console
        level: CRITICAL

llms:
  openai:
    _type: openai
    model_name: gpt-4.1
    temperature: 0

workflow:
  _type: xpander_nemo_agent
  llm_name: openai
  verbose: false
  retry_parsing_errors: true
  max_retries: 3
```

## Features

### Agent Capabilities
- 🤖 **Multi-modal AI agents** with text, code, and structured output
- 🔧 **Tool integration** via Agno framework
- 📊 **Execution metrics** tracking (tokens, tools used, timing)
- 🔄 **Task lifecycle management** with persistence
- ⚡ **Async execution** for high performance
- 🛡️ **Error handling** with automatic retries

### Enterprise Features
- 🏢 **Multi-tenant** organization support
- 🔐 **Secure credential management**
- 📈 **Telemetry and monitoring** integration
- 🚀 **Horizontal scaling** via event-driven architecture
- 🐳 **Container-ready** deployment

## Development

### Project Structure

```
nemo-tests/
├── xpander_nemo_agent.py    # Main NAT function implementation
├── xpander_handler.py       # Event listener for production
├── nemo_config.yml          # NeMo Assistant Toolkit configuration
├── pyproject.toml           # Python package configuration
├── Dockerfile               # Container deployment
└── .env.example             # Environment variables template
```

### Key Components

1. **`xpander_nemo_agent.py`**: Core NAT function that:
   - Loads LLM via NeMo gateway
   - Invokes xpander.ai agents with Agno integration
   - Handles structured outputs and tool usage
   - Reports execution metrics

2. **`xpander_handler.py`**: Production event listener that:
   - Listens for xpander.ai task events
   - Spawns NAT processes for task execution
   - Manages task lifecycle and results

### Testing

```bash
# Test direct invocation
nat run --config_file nemo_config.yml --input "Test agent functionality"

# Test event listener (in separate terminal)
python xpander_handler.py
# Then trigger a task via xpander.ai SDK or dashboard
```

### Debugging

Enable verbose logging by modifying `nemo_config.yml`:

```yaml
general:
  telemetry:
    logging:
      console:
        level: DEBUG  # Change from CRITICAL
workflow:
  verbose: true  # Enable verbose mode
```

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure all dependencies are installed with `pip install -e .`
2. **API key issues**: Verify `.env` file contains correct credentials
3. **NAT command not found**: Make sure the package is installed and venv is activated
4. **Task execution timeout**: Adjust `max_retries` in `nemo_config.yml`

### Performance Optimization

- Use `use_uvloop: true` for better async performance
- Adjust `temperature` and `max_retries` based on use case
- Consider using faster models for development/testing

## Contributing

When contributing to this project:

1. Follow the existing code structure and patterns
2. Update tests for new functionality
3. Ensure Docker builds successfully
4. Update documentation for new features

## Support

For issues and questions:
- xpander.ai SDK: [xpander.ai documentation](https://docs.xpander.ai)
- NVIDIA NeMo: [NeMo toolkit documentation](https://docs.nvidia.com/nemo-framework/)
- Agno Framework: [Agno documentation](https://github.com/agno-agi/agno)

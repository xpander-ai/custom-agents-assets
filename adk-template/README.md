# Google ADK Agent Template

This template provides a foundation for building AI agents using the Google Agent Development Kit (ADK) with xpander.

## Features

- Google ADK framework integration
- xpander SDK integration for task management
- LiteLLM for multi-provider support
- Session management with InMemorySessionService
- Environment-based configuration
- Docker support

## Setup

1. Install dependencies:
   ```bash
   make install
   ```

2. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. Run the agent:
   ```bash
   python xpander_handler.py
   ```

## Configuration

Set the following environment variables in your `.env` file:

- `XPANDER_API_KEY`: Your xpander API key
- `XPANDER_ORGANIZATION_ID`: Your xpander organization ID
- `XPANDER_AGENT_ID`: Your xpander agent ID
- `GOOGLE_API_KEY`: Your Google API key (if using Google models)
- `OPENAI_API_KEY`: Your OpenAI API key (if using OpenAI models)
- `ANTHROPIC_API_KEY`: Your Anthropic API key (if using Anthropic models)

## Docker

Build and run with Docker:

```bash
docker build -t my-adk-agent .
docker run --env-file .env my-adk-agent
```

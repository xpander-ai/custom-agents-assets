# OpenAI Agents SDK Template

This template provides a foundation for building AI agents using the OpenAI Agents SDK with xpander.

## Features

- OpenAI Agents SDK integration
- xpander SDK integration for task management
- OpenAI model support
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
- `OPENAI_API_KEY`: Your OpenAI API key

## Docker

Build and run with Docker:

```bash
docker build -t my-openai-agents-agent .
docker run --env-file .env my-openai-agents-agent
```

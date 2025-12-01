# LangChain Agent Template

This template provides a foundation for building AI agents using the LangChain framework with xpander.

## Features

- LangChain framework integration
- xpander SDK integration for task management
- OpenAI and Anthropic model support
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
- `OPENAI_API_KEY`: Your OpenAI API key (if using OpenAI models)
- `ANTHROPIC_API_KEY`: Your Anthropic API key (if using Anthropic models)

## Docker

Build and run with Docker:

```bash
docker build -t my-langchain-agent .
docker run --env-file .env my-langchain-agent
```

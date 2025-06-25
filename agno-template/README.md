# Agno Framework Template

This template provides a foundation for building AI agents using the [Agno framework](https://github.com/xpander-ai/agno) integrated with the xpander.ai platform.

## Features

- **Agno Framework Integration**: Built on the powerful Agno AI agent framework
- **Thinking Tools**: Includes step-by-step reasoning capabilities
- **Dual Mode Support**: Works both standalone and with Xpander backend
- **State Management**: Maintains conversation history and state
- **Async Operations**: Built for high-performance async execution

## Files Structure

- `agno_agent.py` - Standalone Agno agent implementation for testing
- `agno_agent_with_backend.py` - Agno agent integrated with Xpander backend
- `xpander_handler.py` - WebSocket event handler for Xpander platform
- `agent_instructions.json` - Agent behavior and goal configuration
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container deployment configuration

## Getting Started

### Local Development

1. **Install Dependencies**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
### Xpander Platform Integration

1. **Initialize in your project**:
   ```bash
   npm install -g xpander-cli
   xpander login
   xpander agent new
   xpander agent init
   ```

2. **Run the agent**
   ```
   python my_agent.py
   ```

3. **Deploy to Xpander**:
   ```bash
   xpander deploy
   ```

### Modifying Instructions

Update `agent_instructions.json` to customize your agent's behavior:

```json
{
    "role": [
        "Always respond in markdown format",
        "Be friendly and approachable"
    ],
    "goal": [
        "Provide general assistance for any user request",
        "Maintain simplicity in all interactions",
        "Help users with basic tasks and questions"
    ],
    "system_prompt": "You are a simple and friendly AI assistant running with Agno Framework and xpander.ai Backend!."
}
```

### Environment Variables

Create a `.env` file for local development:

```env
OPENAI_API_KEY=your_openai_api_key
# Add other environment variables as needed
```

## Dependencies

- **agno**: Core AI agent framework
- **xpander-utils**: Xpander platform utilities and adapters
- **openai**: OpenAI API integration
- **python-dotenv**: Environment variable management

## Notes

- Ensure you have Python 3.9+ installed
- The agent uses GPT-4o by default, but can be configured for other models
- For production deployment, review and update the Dockerfile as needed
- The template includes thinking tools for enhanced reasoning capabilities
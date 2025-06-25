# Custom Agents Assets

This repository provides **templates and infrastructure** for custom agents built on top of the xpander.ai platform.

It includes essential configuration files, Docker assets, and framework-specific handlers to help you quickly set up and deploy your agents using the `xpander` CLI.

## Available Templates

### Base Template (Root Directory)
- **Location**: Root directory 
- **Description**: Simple foundation template with no LLM or AI framework dependencies
- **Usage**: `xpander agent new` → Select "Base Template"

### Agno Framework Template
- **Location**: `agno-template/`
- **Description**: Agno AI framework template for building sophisticated AI agents
- **Features**:
  - Thinking tools for step-by-step reasoning
  - OpenAI GPT-4o model integration
  - Async execution with state management
  - Dual mode support (standalone + backend integration)
  - WebSocket event streaming
- **Usage**: `xpander agent new` → Select "Agno"

## Using Templates with Xpander CLI

### Create a New Agent with Template Selection
```bash
# Create new agent and choose template interactively
xpander agent new

# Or specify name directly
xpander agent new --name "My Agent"
```

### Initialize Existing Agent with Template
```bash
# Initialize with template selection
xpander agent init --template <agent-id>

# Or use regular initialization (base template)
xpander agent init <agent-id>
```

### View Available Templates
```bash
# List visible templates
xpander agent templates list

# List all templates (including hidden/draft)
xpander agent templates list --all

# View templates by category
xpander agent templates categories
```

## Template Structure

Each template should contain:

| File/Folder        | Purpose                                                    |
| ------------------ | ----------------------------------------------------------- |
| `.dockerignore`     | Files and directories to exclude from the Docker build.     |
| `Dockerfile`        | Docker configuration to containerize the agent.             |
| `agent_instructions.json` | Instruction templates and metadata for agent behavior. |
| `requirements.txt`  | Python dependencies required to run the agent.              |
| `xpander_handler.py` | Main handler file to define the agent's logic.              |

### Framework-Specific Files

**Agno Template** includes additional files:
- `agno_agent_with_backend.py` - Agno agent with Xpander backend integration
- `agno_agent.py` - Standalone Agno agent implementation

## Development Workflow

1. **Create Agent**: Use `xpander agent new` to create and choose template
2. **Develop Locally**: Test your agent with `xpander agent dev`
3. **Deploy**: Deploy to cloud with `xpander deploy`

## Contributing Templates

To add a new template:

1. Create a new folder in this repository: `<framework-name>-template/`
2. Include all necessary files following the template structure
3. Update the CLI template configuration to include your template
4. Test with `xpander agent templates list --all`

## Notes

- Ensure you have Python 3.9+ installed if running locally
- Make sure your changes align with the expected handler structure to remain compatible with xpander.ai deployments
- For production deployment, review and update the `Dockerfile` for optimizations or environment-specific settings
- Templates marked as `visible: false` in the CLI won't appear in production builds

## License

This project is licensed under the terms described in the `LICENSE` file.
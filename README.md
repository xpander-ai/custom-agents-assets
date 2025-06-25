# Custom Agents Assets

This repository provides the **initial infrastructure** for custom agents built on top of the xpander.ai platform.

It includes essential configuration files, Docker assets, and Python handlers to help you quickly set up and deploy your agent.  
Users cloning this repository can easily extend and customize their own agents by building on this foundation.

## Structure

| File/Folder        | Purpose                                                    |
| ------------------ | ----------------------------------------------------------- |
| `.dockerignore`     | Files and directories to exclude from the Docker build.     |
| `Dockerfile`        | Docker configuration to containerize the agent.             |
| `instructions.json` | Instruction templates and metadata for agent behavior.      |
| `LICENSE`           | Licensing information for using and distributing the assets. |
| `README.md`         | This document.                                              |
| `requirements.txt`  | Python dependencies required to run the agent.              |
| `xpander_config.json` | Configuration specific to xpander.ai platform integration. |
| `xpander_handler.py` | Main handler file to define the agent’s logic.              |

## Notes

- Ensure you have Python 3.9+ installed if running locally.
- Make sure your changes align with the expected handler structure to remain compatible with xpander.ai deployments.
- For production deployment, review and update the `Dockerfile` for optimizations or environment-specific settings.

## License

This project is licensed under the terms described in the `LICENSE` file.
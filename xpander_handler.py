import json
from xpander_utils.events import XpanderEventListener, AgentExecutionResult, AgentExecution, ExecutionStatus
from xpander_sdk import XpanderClient

# === Load Configuration ===
# Reads API credentials and organization context from a local JSON file
with open('xpander_config.json', 'r') as config_file:
    xpander_config: dict = json.load(config_file)

# === Initialize Event Listener ===
# Create a listener to subscribe to execution requests from specified agent(s)
listener = XpanderEventListener(**xpander_config)

# initialize xpander_client
xpander = XpanderClient(api_key=xpander_config.get("api_key"))

# === Define Execution Handler ===
def on_execution_request(execution_task: AgentExecution) -> AgentExecutionResult:
    """
    Callback triggered when an execution request is received from a registered agent.
    
    Args:
        execution_task (AgentExecution): Object containing execution metadata and input.

    Returns:
        AgentExecutionResult: Object describing the output of the execution.
    """
    # You can access the execution input via `execution_task.input`
    # Example: Extracting a specific input field
    # user_input = execution_task.input.get("user_prompt", "")
    
    # initialize agent instance
    agent = xpander.agents.get(agent_id=xpander_config.get("agent_id"))
    
    # initialize the agent with task
    agent.init_task(execution=execution_task.model_dump()) 
    
    # TODO: Add your execution logic here
    
    return AgentExecutionResult(result="Your execution result")

# === Register Callback ===
# Attach your custom handler to the listener
listener.register(on_execution_request=on_execution_request)
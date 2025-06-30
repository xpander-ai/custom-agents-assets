import json
from xpander_utils.events import XpanderEventListener, AgentExecutionResult, AgentExecution, ExecutionStatus
from loguru import logger
from myAgent import MyAgent

# === Load Configuration ===
# Reads API credentials and organization context from a local JSON file
with open('xpander_config.json', 'r') as config_file:
    xpander_config: dict = json.load(config_file)

# === Initialize Event Listener ===
# Create a listener to subscribe to execution requests from specified agent(s)
listener = XpanderEventListener(**xpander_config)

my_agent = MyAgent()

# === Define Execution Handler ===


async def on_execution_request(execution_task: AgentExecution) -> AgentExecutionResult:
    """
    Callback triggered when an execution request is received from a registered agent.

    Args:
        execution_task (AgentExecution): Object containing execution metadata and input.

    Returns:
        AgentExecutionResult: Object describing the output of the execution.
    """

    user_info = ""
    user = getattr(execution_task.input, "user", None)

    if user:
        name = f"{user.first_name} {user.last_name}".strip()
        email = getattr(user, "email", "")
        user_info = f"👤 From user: {name}\n📧 Email: {email}"

    IncomingEvent = (
        f"\n📨 Incoming message: {execution_task.input.text}\n"
        f"{user_info}"
    )
    # print the incoming event (Delete this after testing)
    logger.info(IncomingEvent)

    await my_agent.run(execution_task)
    execution_result = my_agent.agent_backend.retrieve_execution_result()

    logger.info(f"Agent result: {execution_result.result}")

    return AgentExecutionResult(
        result=execution_result.result,
        is_success=execution_result.status == ExecutionStatus.COMPLETED,
    )

# === Register Callback ===
# Attach your custom handler to the listener
listener.register(on_execution_request=on_execution_request)

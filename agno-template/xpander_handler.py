from dotenv import load_dotenv
load_dotenv()

from xpander_sdk import Task, on_task, Backend, Tokens
from agno.agent import Agent

@on_task
async def my_agent_handler(task: Task):
    # Get xpander agent details
    backend = Backend(configuration=task.configuration)

    # Create Agno agent instance
    agno_args = await backend.aget_args(task=task)
    agno_agent = Agent(**agno_args)

    # Run the agent
    result = await agno_agent.arun(input=task.to_message(), files=task.get_files(), images=task.get_images())

    task.result = result.content

    # report execution metrics
    task.tokens = Tokens(prompt_tokens=result.metrics.input_tokens, completion_tokens=result.metrics.output_tokens)
    task.used_tools = [tool.tool_name for tool in result.tools]

    return task

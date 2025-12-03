from dotenv import load_dotenv
load_dotenv()


from xpander_sdk import Task, on_task, Agents, Configuration, OutputFormat, Tokens
from pydantic import BaseModel
from agents import Agent, Runner

@on_task
async def my_agent_handler(task: Task):
    # Get xpander agent details
    xpander_agent = await Agents(configuration=task.configuration).aget()

    # Create OpenAI Agents agent instance
    agent = Agent(
        name=xpander_agent.name,
        instructions=xpander_agent.instructions.full,
        model=xpander_agent.model_name,
        tools=xpander_agent.openai_agents_sdk_tools
    )

    result = await Runner.run(starting_agent=agent, input=task.to_message())

    # in case of structured output, return as stringified json
    task_result = result.final_output
    if task.output_format == OutputFormat.Json:
        try:
            import json
            parsed = json.loads(task_result)
            if isinstance(parsed, dict):
                task_result = json.dumps(parsed)
        except:
            pass

    task.result = task_result

    # report execution metrics (if available from OpenAI Agents SDK)
    # Note: OpenAI Agents SDK may provide token usage, adjust as needed

    return task

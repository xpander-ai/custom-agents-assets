from dotenv import load_dotenv
load_dotenv()


from xpander_sdk import Task, on_task, Agents, Configuration, OutputFormat, Tokens
from pydantic import BaseModel
from strands import Agent
from strands.models.openai import OpenAIModel

@on_task
async def my_agent_handler(task: Task):
    # Get xpander agent details
    xpander_agent = await Agents(configuration=task.configuration).aget()

    # Create Strands instance
    strands_agent = Agent(
        model=OpenAIModel(
            client_args={
                'api_key': '{YOUR_LLM_KEY}',
            },
            model_id=xpander_agent.model_name
        ),
        description=xpander_agent.instructions.description,
        system_prompt=xpander_agent.instructions.instructions,
        tools=xpander_agent.strands_tools,
    )

    # Run the agent
    result = strands_agent(
        prompt=task.to_message(),
        invocation_state = {'user_details': task.input.user.model_dump_json()} if task.input.user else None
    )

    # in case of structured output, return as stringified json
    task_result = result.message['content'][0]['text']
    if task.output_format == OutputFormat.Json:
        try:
            import json
            parsed = json.loads(task_result)
            if isinstance(parsed, dict):
                task_result = json.dumps(parsed)
        except:
            pass

    task.result = task_result

    # report execution metrics (if available from Strands)
    # Note: Strands may not provide token usage directly, adjust as needed

    return task

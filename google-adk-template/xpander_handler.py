from dotenv import load_dotenv
load_dotenv()


from xpander_sdk import Task, on_task, Agents, Configuration, OutputFormat, Tokens
from pydantic import BaseModel
from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

@on_task
async def my_agent_handler(task: Task):
    # Get xpander agent details
    xpander_agent = await Agents(configuration=task.configuration).aget()

    # Create ADK instance
    adk_agent = Agent(
        name=xpander_agent.sanitized_name,
        model=LiteLlm(model=f'{xpander_agent.model_provider}/{xpander_agent.model_name}'),
        description=xpander_agent.instructions.description,
        instruction=xpander_agent.instructions.full,
        tools=xpander_agent.tools.functions,
    )

    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=xpander_agent.sanitized_name,
        user_id=task.input.user.id if task.input.user else 'user_id',
        session_id=task.id,
    )

    runner = Runner(
        agent=adk_agent,
        app_name=xpander_agent.sanitized_name,
        session_service=session_service,
    )

    content = types.Content(
        role='user',
        parts=[types.Part(text=task.to_message())],
    )

    final_answer = ''

    # Stream events from the agent
    async for event in runner.run_async(
        user_id=task.input.user.id if task.input.user else 'user_id',
        new_message=content,
        session_id=task.id
    ):
        if event.is_final_response() and event.content and event.content.parts:
            final_answer = event.content.parts[0].text

    # in case of structured output, return as stringified json
    if task.output_format == OutputFormat.Json:
        try:
            import json
            parsed = json.loads(final_answer)
            if isinstance(parsed, dict):
                final_answer = json.dumps(parsed)
        except:
            pass

    task.result = final_answer

    # report execution metrics (if available from ADK)
    # Note: ADK may not provide token usage directly, adjust as needed

    return task

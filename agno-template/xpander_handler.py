from dotenv import load_dotenv
load_dotenv()

from datetime import datetime, timezone
from xpander_sdk import Task, on_task, Backend, Tokens, TaskUpdateEvent, TaskUpdateEventType
from agno.agent import Agent, RunContentEvent
from agno.run.agent import RunEvent, RunOutput, RunErrorEvent

@on_task
async def my_agent_handler(task: Task):
    # Get xpander agent details
    backend = Backend(configuration=task.configuration)

    # Create Agno agent instance
    agno_args = await backend.aget_args(task=task)
    agno_agent = Agent(**agno_args, debug_mode=True)

    # Run the agent in streaming mode
    result = None
    async for event in agno_agent.arun(
        input=task.to_message(),
        files=task.get_files(),
        images=task.get_images(),
        stream=True,
        stream_events=True,
        yield_run_output=True,
    ):
        if isinstance(event, RunErrorEvent) and event.content:
            raise Exception(event.content)
        if isinstance(event, RunOutput):
            result = event
        elif hasattr(event, "event") and event.event == RunEvent.run_content and event.content:
            # Yield chunk event
            yield TaskUpdateEvent(
                type=TaskUpdateEventType.Chunk,
                task_id=task.id,
                organization_id=task.organization_id,
                time=datetime.now(timezone.utc),
                data=event.content,
            )

    # Yield final TaskFinished event
    task.result = result.content if result else "Execution completed"
    yield TaskUpdateEvent(
        type=TaskUpdateEventType.TaskFinished,
        task_id=task.id,
        organization_id=task.organization_id,
        time=datetime.now(timezone.utc),
        data=task.result,
    )

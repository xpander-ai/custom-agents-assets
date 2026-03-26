from dotenv import load_dotenv
load_dotenv()

from datetime import datetime, timezone
from xpander_sdk import Task, on_task, Backend, Tokens, TaskUpdateEvent, TaskUpdateEventType
from agno.team import Team
from agno.run.agent import RunEvent, RunOutput, RunErrorEvent
from agno.run.team import TeamRunOutput

@on_task
async def my_agent_handler(task: Task):
    # Get xpander agent details
    backend = Backend(configuration=task.configuration)

    # Create Agno team instance
    agno_args = await backend.aget_args(task=task)
    agno_team = Team(**agno_args)

    # Run the team in streaming mode
    result = None
    async for event in agno_team.arun(
        input=task.to_message(),
        files=task.get_files(),
        images=task.get_images(),
        stream=True,
        stream_events=True,
        yield_run_output=True,
    ):
        if isinstance(event, RunErrorEvent) and event.content:
            raise Exception(event.content)
        if isinstance(event, (RunOutput, TeamRunOutput)):
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

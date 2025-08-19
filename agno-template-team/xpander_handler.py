from dotenv import load_dotenv
load_dotenv()


from xpander_sdk import Task, Backend, on_task, OutputFormat
from pydantic import BaseModel
from agno.team import Team

@on_task
async def my_agent_handler(task: Task):
    backend = Backend(configuration=task.configuration)
    agno_args = await backend.aget_args(task=task)
    agno_agent = Team(**agno_args)
    result = await agno_agent.arun(message=task.to_message())
    
    # in case of structured output, return as stringified json
    if task.output_format == OutputFormat.Json and isinstance(result.content, BaseModel):
        result.content = result.content.model_dump_json()
    
    task.result = result.content
    return task

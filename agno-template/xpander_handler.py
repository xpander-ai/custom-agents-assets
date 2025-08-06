from dotenv import load_dotenv
load_dotenv()


from xpander_sdk import Task, Backend, on_task
from agno.agent import Agent

@on_task
async def my_agent_handler(task: Task):
    backend = Backend(configuration=task.configuration)
    agno_args = await backend.aget_args(task=task)
    agno_agent = Agent(**agno_args)
    result = await agno_agent.arun(message=task.to_message())
    task.result = result.content
    return task

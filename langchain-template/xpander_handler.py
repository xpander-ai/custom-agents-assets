from dotenv import load_dotenv
load_dotenv()


from xpander_sdk import Task, on_task, Agents
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

@on_task
async def my_agent_handler(task: Task):
    # Get xpander agent details
    xpander_agent = await Agents(configuration=task.configuration).aget()

    agent = create_agent(
        model=ChatOpenAI(model=xpander_agent.model_name, temperature=0, api_key='{YOUR_OPENAI_KEY}'),
        tools=xpander_agent.tools.functions
    )
    result = await agent.ainvoke(
        input={'messages': [('system', xpander_agent.instructions.full), ('system', f'User details: {task.input.user.model_dump_json() if task.input.user else "N/A"}'), ('user', task.to_message())]}
    )

    # in case of structured output, return as stringified json
    task_result = result['messages'].pop().content

    task.result = task_result

    # report execution metrics (if available from LangChain)
    # Note: LangChain may provide token usage through callbacks, adjust as needed

    return task

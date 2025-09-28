from dotenv import load_dotenv
load_dotenv()

from nat.builder.builder import Builder
from nat.builder.framework_enum import LLMFrameworkEnum
from nat.builder.function_info import FunctionInfo
from nat.cli.register_workflow import register_function
from nat.data_models.component_ref import LLMRef
from nat.data_models.function import FunctionBaseConfig

from xpander_sdk import Backend, OutputFormat, Tokens
from pydantic import BaseModel
from agno.team import Team
from loguru import logger

class XpanderAgentConfig(FunctionBaseConfig, name="xpander_nemo_agent"):
    llm_name: LLMRef

@register_function(config_type=XpanderAgentConfig, framework_wrappers=[LLMFrameworkEnum.AGNO])
async def xpander_nemo_agent_function(config: XpanderAgentConfig, builder: Builder):
    # run the agent
    async def load_and_run_xpander_nemo_agent(inputs: str) -> str:
        try:
            
            # Load NeMo LLM Gateway
            llm = await builder.get_llm(config.llm_name, wrapper_type=LLMFrameworkEnum.AGNO)
            
            # Load xpander backend
            backend = Backend()
            task = await backend.ainvoke_agent(prompt=inputs,run_locally=True)
            agno_args = await backend.aget_args(task=task,override={"model": llm})
            
            agno_agent = Team(**agno_args)
            result = await agno_agent.arun(input=task.to_message())
            
            # in case of structured output, return as stringified json
            if task.output_format == OutputFormat.Json and isinstance(result.content, BaseModel):
                result.content = result.content.model_dump_json()
            
            task.result = result.content
            
            # report execution metrics
            task.tokens = Tokens(prompt_tokens=result.metrics.input_tokens,completion_tokens=result.metrics.output_tokens)
            task.used_tools = [tool.tool_name for tool in result.tools]
            
            # save changes
            await task.asave()
            
            return task.result
        except Exception as e:
            logger.critical(e)
            return f"Agent execution failed: {str(e)}"

    yield FunctionInfo.from_fn(load_and_run_xpander_nemo_agent)
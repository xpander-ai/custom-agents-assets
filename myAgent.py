"""
Copyright (c) 2025 Xpander, Inc. All rights reserved.
"""

import asyncio
import json
import os
import sys
import time
from pathlib import Path
from xpander_sdk import XpanderClient, LLMProvider, LLMTokens, Tokens, Agent
from openai import AsyncOpenAI
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

# Simple logger setup
logger.remove()
logger.add(sys.stderr, format="{time:HH:mm:ss} | {message}", level="INFO")


class MyAgent:
    def __init__(self):
        logger.info("🚀 Initializing MyAgent...")

        # Load config
        config = json.loads(Path("xpander_config.json").read_text())

        # Get API keys
        xpander_key = config.get("api_key") or os.getenv("XPANDER_API_KEY")
        agent_id = config.get("agent_id") or os.getenv("XPANDER_AGENT_ID")
        openai_key = os.getenv("OPENAI_API_KEY")

        if not all([xpander_key, agent_id, openai_key]):
            raise ValueError("Missing required API keys")

        # Initialize
        self.openai = AsyncOpenAI(api_key=openai_key)
        xpander_client = XpanderClient(api_key=xpander_key)
        self.agent_backend: Agent = xpander_client.agents.get(
            agent_id=agent_id)
        self.agent_backend.select_llm_provider(LLMProvider.OPEN_AI)

        # Log agent details
        logger.info(f"📋 Agent: {self.agent_backend.name}")
        logger.info(f"🔧 Tools: {len(self.agent_backend.tools)} available")
        logger.info(f"💡 Example prompts: {len(self.agent_backend.prompts)}")
        if self.agent_backend.prompts:
            logger.info(f"   e.g. \"{self.agent_backend.prompts[0]}\"")
        logger.info("✅ Ready!")

    async def run(self, task: str) -> dict:
        logger.info(f"📝 Task: {task}")
        self.agent_backend.add_task(input=task)

        step = 0
        start_time = time.perf_counter()
        tokens = Tokens(worker=LLMTokens(0, 0, 0))

        while not self.agent_backend.is_finished():
            step += 1
            if step > 1:
                logger.info(f"  Step {step}...")

            # Call LLM
            response = await self.openai.chat.completions.create(
                model="gpt-4.1",
                messages=self.agent_backend.messages,
                tools=self.agent_backend.get_tools(),
                tool_choice=self.agent_backend.tool_choice,
                temperature=0
            )

            # Track tokens
            if hasattr(response, 'usage'):
                tokens.worker.prompt_tokens += response.usage.prompt_tokens
                tokens.worker.completion_tokens += response.usage.completion_tokens
                tokens.worker.total_tokens += response.usage.total_tokens
                logger.info(f"  📊 Step tokens: {response.usage.total_tokens}")

            # Process response
            self.agent_backend.add_messages(response.model_dump())
            self.agent_backend.report_execution_metrics(
                llm_tokens=tokens, ai_model="gpt-4.1")

            tool_calls = self.agent_backend.extract_tool_calls(
                response.model_dump())
            if tool_calls:
                tool_results = await asyncio.to_thread(self.agent_backend.run_tools, tool_calls)

                # Log tool call results
                for res in tool_results:
                    emoji = "✅" if res.is_success else "❌"
                    logger.info(f"  {emoji} {res.function_name}")

        # Final metrics
        duration = time.perf_counter() - start_time
        logger.info(
            f"✅ Done! Duration: {duration:.1f}s | Total tokens: {tokens.worker.total_tokens}")

        result = self.agent_backend.retrieve_execution_result()
        return {"result": result.result, "thread_id": result.memory_thread_id}


# Example usage
if __name__ == "__main__":
    async def main():
        agent = MyAgent()
        result = await agent.run("Hi!")
        print(f"\n{result['result']}")

    asyncio.run(main())

"""
https://github.com/run-llama/llama-hub/blob/main/llama_hub/tools/notebooks/arxiv.ipynb
"""

import openai
from llama_index.agent import OpenAIAgent
from llama_hub.tools.arxiv.base import ArxivToolSpec
from dotenv import load_dotenv
load_dotenv()




arxiv_tool = ArxivToolSpec()

agent = OpenAIAgent.from_tools(
    arxiv_tool.to_tool_list(),
    verbose=True,
)

print(agent.chat("what do you know about psoriasis?"))

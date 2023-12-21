""""
https://blog.gopenai.com/openai-assistants-api-a-to-z-practitioners-guide-to-code-interpreter-knowledge-retrieval-and-33c1979c5d7d

client.beta.assistants.list() # to list existing Assistants
client.beta.assistants.delete(assistant.id) # to delete Assistant based on id
client.beta.assistants.files.list(assistant.id)
"""

import os
import time
import logging
from datetime import datetime
import openai
from openai import OpenAI

from dotenv import load_dotenv # The dotenv library's load_dotenv function reads a .env file to load environment variables into the process environment. This is a common method to handle configuration settings securely.

# Load env variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)


client = OpenAI()

file_object = client.files.create(
  file=open("factorial.py", "rb"),
  purpose='assistants'
)

assistant = client.beta.assistants.create(
  name = "Coding Assistant 1.0.0",
  instructions="""You are a personal coding assistant. When asked a coding question, "
               "write and run code to answer the question.""",
  model="gpt-4-1106-preview",
  tools=[{"type": "code_interpreter"}],
  file_ids=[file_object.id]
)

#TODO threads
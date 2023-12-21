"""
https://medium.com/@datadrifters/openai-assistants-api-walk-through-and-coding-a-research-assistant-3ddb3d767e99

side note: The dotenv library's load_dotenv function reads a .env file to load environment variables
into the process environment. This is a common method to handle configuration settings securely.

https://platform.openai.com/docs/api-reference/models/list

https://platform.openai.com/assistants

"""
import os
import time
import logging
from datetime import datetime
import openai
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
load_dotenv(find_dotenv(), override=True)
logging.basicConfig(level=logging.INFO)


client = OpenAI()

filepath = './papers/Harnessing the Power of LLMs in Practice A Survey on ChatGPT and Beyond.pdf'
filepath = 'C:/Users/HC138YY/OneDrive - EY/Documents/workproducts-dev/assets/transcripts/subtitle11.txt'
filepath = "C:/Users/HC138YY/OneDrive - EY/Documents/workproducts-dev/assets/arxiv/A Survey on Large Language Model (LLM) Security and Privacy.pdf"

file_object = client.files.create(
    file = open(filepath, 'rb'),
    purpose = 'assistants',
)
print(file_object.id)

assistant = client.beta.assistants.create(
    name="Research Assistant Arxix",
    instructions="""You are a helpful research assistant. Your role is to assist in navigating and understanding 
                    research papers from ArXiv. Summarize papers, clarify terminology within context, and extract key 
                    figures and data. Cross-reference information for additional insights and answer related questions 
                    comprehensively. Analyze the papers, noting strengths and limitations. Respond to queries 
                    effectively, incorporating feedback to enhance your accuracy. Handle data securely and update your 
                    knowledge base with the latest research. Adhere to ethical standards, respect intellectual property,
                    and provide users with guidance on any limitations. Maintain a feedback loop for continuous 
                    improvement and user support. Your ultimate goal is to facilitate a deeper understanding of complex 
                    scientific material, making it more accessible and comprehensible.""",
    tools=[{"type": "retrieval"}],  # API supports Code Interpreter and Retrieval
    model="gpt-4-1106-preview",
    file_ids=[file_object.id]
)


#TODO Threads


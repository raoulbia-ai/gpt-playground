"""
https://medium.com/@datadrifters/autogen-litellm-and-open-source-llms-c4c6bc8fa9c5

https://ollama.ai/library

note: litellm calls OpenAI , an API KEY is required
z
to start litellm server run `litellm --test`

model_names = ["gpt-3.5-turbo", "huggingface/mistralai/Mistral-7B-Instruct-v0.1", "ollama/llama2"]
model_names = ["gpt-3.5-turbo", "command-nightly", "j2-mid"]  # 2-mid is AI21.ai


other links:
https://www.linkedin.com/posts/abigail-haddad_with-litellm-a-python-package-for-making-activity-7139992232786325505-6d8K/?utm_source=share&utm_medium=member_android
"""
from litellm import completion
import logging, os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)
logging.basicConfig(level=logging.INFO)


# Set API keys
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["COHERE_API_KEY"] = os.getenv("COHERE_API_KEY")

# Your prompt
prompt = "When did Einstein discover gravity?"

# Call different models
openai_response = completion(model="gpt-3.5-turbo", messages=[{"content": prompt, "role": "user"}])
cohere_response = completion(model="command-nightly", messages=[{"content": prompt, "role": "user"}])
mistral_response = completion(model="huggingface/mistralai/Mistral-7B-Instruct-v0.1", messages=[{"content": prompt, "role": "user"}])

# Print responses
print("OpenAI:", openai_response['choices'][0]['message']['content'])
print("Cohere:", cohere_response['choices'][0]['message']['content'])
print("Mistral:", mistral_response['choices'][0]['message']['content'])




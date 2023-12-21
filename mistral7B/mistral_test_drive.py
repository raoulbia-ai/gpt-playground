"""
https://chat.openai.com/share/5b6d94a2-30ec-4d21-999a-91000349daa4
"""
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_dir = "model_files"  # Replace with your model directory path
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForCausalLM.from_pretrained(model_dir)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

prompt = "WHen did Einstein discover gravity?"
response = generator(prompt, max_length=50)  # You can adjust max_length as needed
print(response[0]['generated_text'])

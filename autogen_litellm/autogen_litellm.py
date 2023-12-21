"""
https://medium.com/@datadrifters/autogen-litellm-and-open-source-llms-c4c6bc8fa9c5

as of 13/12/2023 running `litellm --model ollama/llama2` will raise an error on Windows

the Ollama server for Windows was not yet available. see https://github.com/jmorganca/ollama

see here for instructions to run Ollama server on Linux: https://chat.openai.com/share/fb8660a0-75af-4143-8cf6-af01562c0826
"""
import autogen

config_list = [
    {
        "api_base": "http://0.0.0.0:8000",
        "api_key" : "NULL",
    }
]

autogen_config={
    "timeout": 600, # specifies that the agent should have a timeout of 60 seconds.
    "seed": 42, # sets a seed for any random number generation, ensuring reproducibility
    "config_list": config_list, # asses the list of configurations that was just created
    "temperature": 0, # 0 means that model will try to produce deterministic output, picking the most likely next word at each step.
}

assistant = autogen.AssistantAgent(
    "assistant",
    llm_config = autogen_config
)

user_proxy = autogen.UserProxyAgent(
    name = "user_proxy",
    human_input_mode = "TERMINATE",
    max_consecutive_auto_reply = 10,
    is_termination_msg = lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config = {"work_dir": "web"},
    llm_config = autogen_config,
    system_message = """Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

user_proxy.initiate_chat(
    assistant,
    message = """What's the today's date?""",
)
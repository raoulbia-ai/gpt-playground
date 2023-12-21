# https://postgresml.org/blog/introducing-the-openai-switch-kit-move-from-closed-to-open-source-ai-in-minutes
# https://postgresml.org/deployments/02cfff72-4773-4a23-a71b-f81e22e49548

import pgml
import os
import asyncio
from pprint import pprint

os.environ['DATABASE_URL'] = "postgres://u_qi9t5ag9kc8f5ss:sayfjyiqca76dfi@02f7e6f1-1adb-4347-835a-02c74fcccb0e.db.cloud.postgresml.org:6432/pgml_amxjpvutw2kdgeg"



def test1():

    model = "HuggingFaceH4/zephyr-7b-beta"
    # model = "mistralai/Mistral-7B-v0.1" # says Please select one of the provided models
    # model = "PygmalionAI/mythalion-13b" # raises type Half overflow error
    # model = "TheBloke/zephyr-7B-beta-GPTQ"  # says Please select one of the provided models

    client = pgml.OpenSourceAI()
    results = client.chat_completions_create(
        model,
        [
            {
                "role": "system",
                "content": "You are a friendly chatbot who always responds in the style of a pirate",
            },
            {
                "role": "user",
                "content": "How many helicopters can a human eat in one sitting?",
            },
        ],
        temperature=0.85,
    )
    print(results)

    content_text = results['choices'][0]['message']['content']
    pprint(content_text)


async def test2():

    from pgml import TransformerPipeline

    model = "TheBloke/zephyr-7B-beta-GPTQ"
    model_type = "mistral"

    model = "TheBloke/Mistral-7B-OpenOrca-GPTQ"
    model_type = "mistral"

    # model = "TheBloke/Llama-2-7b-Chat-GPTQ"
    # model_type = "llama"

    list_of_fragments = []
    pipe = TransformerPipeline("text-generation",
                               model,
                               {"model_type": model_type,
                                "revision": "main",
                                "device_map": "auto"},
                               "postgres://pg:ml@sql.cloud.postgresml.org:6432/pgml")

    async for t in await pipe.transform_stream("AI is going to",
                                               {"max_new_tokens": 100}):
        # print(t)
        list_of_fragments.append(t[0])

    print(f'nbr tokens returned: {len(list_of_fragments)}')
    sentence = ''.join(list_of_fragments)
    pprint(sentence)


if __name__ == "__main__":
    test1()
    # asyncio.run(test2())

"""
https://cobusgreyling.medium.com/pal-program-aided-large-language-models-30db3e59f796

Security note: This class implements an AI technique that generates and evaluates
Python code, which can be dangerous and requires a specially sandboxed environment to be safely used. While this class
implements some basic guardrails by limiting available locals/globals and by parsing and inspecting the generated
Python AST using PALValidation, those guardrails will not deter sophisticated attackers and are not a replacement for a
proper sandbox. Do not use this class on untrusted inputs, with elevated permissions, or without consulting your
security team about proper sandboxing!
source: https://api.python.langchain.com/en/stable/pal_chain/langchain_experimental.pal_chain.base.PALChain.html?highlight=palchain#langchain_experimental.pal_chain.base.PALChain
"""
import os
import logging
# from langchain.chains import PALChain
from langchain_experimental.pal_chain.base import PALChain
from langchain import OpenAI
from dotenv import load_dotenv


def main():
    # Load env variables
    load_dotenv()

    # Set up logging
    logging.basicConfig(level=logging.INFO)

    try:
        llm = OpenAI(temperature=0, max_tokens=512, model_name='gpt-4-0314')
        pal_chain = PALChain.from_math_prompt(llm, verbose=True)

        question = """Jan has three times the number of pets as Marcia. Marcia has two more pets than Cindy. 
                      If Cindy has four pets, how many total pets do the three have?
                      """

        result = pal_chain.run(question)
        print(result)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()

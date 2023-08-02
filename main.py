import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_prompt(model_engine: str):
    prompt_text = input("Enter a prompt: ")

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_text,
        temperature=0.7,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"],
    )

    response = completion.choices[0].text
    print(response)


try:
    while True:
        get_prompt("text-davinci-003")
except KeyboardInterrupt:
    print("\nGoodbye!")
except Exception as e:
    print(e)

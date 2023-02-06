from fastapi import FastAPI
import openai
from typing import Optional
import os

app = FastAPI()

openai.api_key = os.environ["OPENAI_API_KEY"]


@app.get("/")
async def root():
    return {"message": "healthy"}


@app.get("/gpt")
async def return_message(q: Optional[str] = ''):

    if q == "":
        return {"message": ''}
    os.environ["OPENAI_API_KEY"] = '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'
    openai.api_key = os.environ["OPENAI_API_KEY"]
    user_text = q
    completions = openai.Completion.create(
        engine='text-davinci-003',  # Determines the quality, speed, and cost.
        temperature=0.5,  # Level of creativity in the response
        prompt=user_text,  # What the user typed in
        max_tokens=1000,  # Maximum tokens in the prompt AND response
        n=1,  # The number of completions to generate
    )

    text = completions.choices[0].text
    text = text.replace('\n', '')
    return {"message": text}


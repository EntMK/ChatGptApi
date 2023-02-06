from fastapi import FastAPI
import openai
from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "healthy"}


@app.get("/gpt")
async def return_message(q: Optional[str] = ''):

    if q == "":
        return {"message": ''}

    openai.api_key = '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'

    user_text = q
    completions = openai.Completion.create(
        engine='text-davinci-003',  # Determines the quality, speed, and cost.
        temperature=0.5,  # Level of creativity in the response
        prompt=user_text,  # What the user typed in
        max_tokens=1000,  # Maximum tokens in the prompt AND response
        n=1,  # The number of completions to generate
        stop=None,  # An optional setting to control response generation
    )

    text = completions.choices[0].text
    text = text.replace('\n', '')
    return {"message": text}


from fastapi import FastAPI
import openai
from typing import Optional
import os
from pymongo import MongoClient
import asyncio

_CLIENT = MongoClient(host='ec2-3-36-45-47.ap-northeast-2.compute.amazonaws.com', port=33033)
db = _CLIENT['hobby']
collection = db['gpt']

app = FastAPI()

answer_number = [1]


@app.get("/")
async def root():
    return {"message": "healthy"}


@app.get("/test")
async def test():
    number = answer_number.pop()
    answer_number.append(number + 1)
    return {'answer_number': number}


@app.get("/gpt")
async def gpt_message(q: Optional[str] = ''):

    if q == "":
        yield {"message": ''}

    number = answer_number.pop()
    answer_number.append(number + 1)

    await request_processing(q, str(number))

    yield {'message': q, 'answer_number': str(number)}


async def request_processing(q, number):
    openai.api_key = os.environ["OPENAI_API_KEY"]
    user_text = q
    completions = openai.Completion.create(
        engine='text-davinci-003',  # Determines the quality, speed, and cost.
        temperature=0.5,  # Level of creativity in the response
        prompt=user_text,  # What the user typed in
        max_tokens=1000,  # Maximum tokens in the prompt AND response
        n=1,  # The number of completions to generate
        frequency_penalty=0,
        presence_penalty=0
    )

    text = completions.choices[0].text
    text = text.replace('\n', '')

    info = {'answer_number': number, 'question': q, 'answer': text}

    collection.insert_one(info)


@app.get('/gpt/answer')
async def answer_question(q: Optional[str] = ''):

    info = list(collection.find({'answer_number': q}))

    if len(info) == 0:
        return 0

    else:
        return info


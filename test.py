import openai
import os


openai.api_key = os.environ["OPENAI_API_KEY"]
user_text = '철학이란'
completions = openai.Completion.create(
        engine='text-davinci-003',  # Determines the quality, speed, and cost.
        temperature=0.5,            # Level of creativity in the response
        prompt=user_text,           # What the user typed in
        max_tokens=1000,             # Maximum tokens in the prompt AND response
        frequency_penalty=0,
        presence_penalty=0

)

text = completions.choices[0].text

print(text)


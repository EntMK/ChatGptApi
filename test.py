import openai
import os


openai.api_key = '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'

user_text = '철학이란'
completions = openai.Completion.create(
        engine='text-davinci-003',  # Determines the quality, speed, and cost.
        temperature=0.5,            # Level of creativity in the response
        prompt=user_text,           # What the user typed in
        max_tokens=1000,             # Maximum tokens in the prompt AND response
        n=1,                        # The number of completions to generate

)

text = completions.choices[0].text

print(text)


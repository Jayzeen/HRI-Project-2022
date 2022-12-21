import os
import openai
import text_to_speech as tsp
from decouple import config

API_KEY = config('KEY')

openai.api_key = API_KEY

def talkCasual(prompt):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    tsp.text2speech(response.choices[0].text)
    print(response.choices[0].text)
    
def talkSarcastically(prompt):
    
    response2 = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.5,
    max_tokens=60,
    top_p=0.3,
    frequency_penalty=0.5,
    presence_penalty=0.0
    )

    tsp.text2speech(response2.choices[0].text)
    print(response2.choices[0].text)
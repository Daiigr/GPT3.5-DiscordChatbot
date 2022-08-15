#importing libraries (ensure you have these installed using pip, dontenv pip library name is python-dotenv)
import openai
import json
import discord
import os
from dotenv import load_dotenv

import UserManager
#load in the token keys from the .env file
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_TOKEN = os.getenv("OPENAI_TOKEN")
openai.api_key = OPENAI_TOKEN
#load in AI parameters
DEFAULT_PERSONALITY_TYPE = os.getenv("DEFAULT_PERSONALITY_TYPE")
MODEL_TYPE = os.getenv("MODEL_TYPE")
MAX_TOKENS = int(os.getenv("MAX_TOKENS"))

usermanager = UserManager("UserMappings.csv")

client = discord.Client()

prompt_arr = []

users = {'Daiigr':'Daniel(Male)','Father':'Anna(Female,they/them):','PETTAPLAY':'Cristiano'}

def getName(UserName):
    return users[UserName]
    
def getResponce(prompt, userID):
    response = openai.Completion.create(
    model=MODEL_TYPE,
    prompt=prompt,
    temperature=0.90,
    max_tokens=MAX_TOKENS,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[(getName(userID)) + ': ', "DaiigrAI: "]
    )
    print(response)
    for choices in response['choices']:
        output = str(choices['text'])
        prompt_arr.append(output)
    return output

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #formating the message into the GPT input
    prompt = '\n'  + ': ' + message.content + "\nDaiigrAI: "

    prompt_arr.append(prompt)

    if len(prompt_arr) > 3:
        prompt_arr.pop(0)
    input = ' '.join(prompt_arr)

    #messageOutput = getResponce(DEFAULT_PERSONALITY_TYPE + input,message.author.id
    print(str(message.author.id))
    user = usermanager.GetUser(message.author.id, usermanager.GetUserArray)
    

    await message.channel.send( 'Message sent by: '+ user.Name)

client.run(DISCORD_TOKEN)

 
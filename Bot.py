#importing libraries (ensure you have these installed using pip, dontenv pip library name is python-dotenv)
from getpass import getuser
import openai
import json
import discord
import os

import ConfigParser as configparser
DISCORD_TOKEN = configparser.get_discord_api_key()
print(DISCORD_TOKEN)
OPENAI_TOKEN = configparser.get_openai_api_key()
openai.api_key = OPENAI_TOKEN

#load in AI parameters
DEFAULT_PERSONALITY_TYPE = configparser.get_default_personality_type()
MODEL_TYPE = configparser.get_model_type()
MAX_TOKENS = configparser.get_max_tokens()

client = discord.Client()


from User_Object_Array_Generator import UserObjectArrayGenerator
FormattedStringUsers = configparser.get_user_mappings()
user_array_generator = UserObjectArrayGenerator()
user_array = user_array_generator.convertFormatedArraytoUserArray(FormattedStringUsers)

from User_Searcher import UserSearcher
user_searcher = UserSearcher()


prompt_arr = []
    
def getResponce(prompt, userID):
    response = openai.Completion.create(
    model=MODEL_TYPE,
    prompt=prompt,
    temperature=0.90,
    max_tokens=MAX_TOKENS,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[user_searcher.getUserByIDWithBinarySearch(user_array,userID).get_name() + ': ', "DaiigrAI: "]
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
    print(message.author.id)
    user = user_searcher.getUserByIDWithBinarySearch(user_array,message.author.id)
    userNameInput = user.get_name() + '('+user.Pronouns+')'
    prompt = '\n'+ userNameInput + ': ' + message.content + "\nDaiigrAI: "
    prompt_arr.append(prompt)

    if len(prompt_arr) > 3:
        prompt_arr.pop(0)
    input = ' '.join(prompt_arr)

    messageOutput = getResponce(DEFAULT_PERSONALITY_TYPE + input , message.author.id)
    await message.channel.send(messageOutput)

client.run(DISCORD_TOKEN)

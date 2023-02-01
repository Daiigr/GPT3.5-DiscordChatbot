#importing libraries (ensure you have these installed using pip, dontenv pip library name is python-dotenv)
import openai
import json
import os
from colorama import Fore, Back, Style
import time
import asyncio
import sys
import discord
from discord.ext import commands
from discord import app_commands

import ConfigParser as configparser
DISCORD_TOKEN = configparser.get_discord_api_key()
print(DISCORD_TOKEN)
OPENAI_TOKEN = configparser.get_openai_api_key()
openai.api_key = OPENAI_TOKEN

#load in AI parameters
DEFAULT_PERSONALITY_TYPE = configparser.get_default_personality_type()
MODEL_TYPE = configparser.get_model_type()
MAX_TOKENS = configparser.get_max_tokens()


bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

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

@bot.event
async def on_ready():
    prfx = (Back.BLACK + Fore.GREEN  + time.strftime("%H:%M:%S") + Back.RESET + Fore.WHITE  + Style.BRIGHT)
    print(prfx +' Logged in as: ' +  Fore.YELLOW + bot.user.name)
    print(prfx + ' Bot ID: ' + Fore.YELLOW + str(bot.user.id))
    print(prfx + ' Discord Version: ' + Fore.YELLOW + discord.__version__)
    print(prfx + ' OpenAI Version: ' + Fore.YELLOW + str(openai.api_version))
    print(prfx + ' Python Version: ' + Fore.YELLOW + str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2]))
    synced = await bot.tree.sync()
    print(prfx + ' Slash CMDs Synced: ' + Fore.YELLOW + str(len(synced)))


@bot.event
async def on_message(message):
    if message.author == bot.user:
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

bot.run(DISCORD_TOKEN)

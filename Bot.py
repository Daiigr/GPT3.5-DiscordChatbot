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

import Config_Parser as configparser
from User import User

prfx = (Back.BLACK + Fore.GREEN  + time.strftime("%H:%M:%S") + Back.RESET + Fore.WHITE  + Style.BRIGHT)

print(Fore.WHITE + Style.BRIGHT + '---API Parameters---' + Back.RESET + Style.RESET_ALL)
DISCORD_TOKEN = configparser.get_discord_api_key()
print(prfx + ' Discord Token: ' + Fore.BLUE + DISCORD_TOKEN)

OPENAI_TOKEN = configparser.get_openai_api_key()
print(prfx + ' Discord Token: ' + Fore.BLUE + DISCORD_TOKEN)

openai.api_key = OPENAI_TOKEN

#load in AI parameters
print( Fore.WHITE + Style.BRIGHT + '---AI Parameters---' + Back.RESET + Style.RESET_ALL)

DEFAULT_PERSONALITY_TYPE = configparser.get_default_personality_type()
print(prfx + ' Defualt Personality Type: ' + Fore.YELLOW + DEFAULT_PERSONALITY_TYPE)

MODEL_TYPE = configparser.get_model_type()
print(prfx + ' Model Type: ' + Fore.YELLOW + MODEL_TYPE)

MAX_TOKENS = configparser.get_max_tokens()
print(prfx + ' Max Tokens: ' + Fore.YELLOW + str(MAX_TOKENS))


from UserJSONParser import UserJsonParser
user_json_parser = UserJsonParser()

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())


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
    stop=[user_json_parser.getUserByID(userID).get_name() + ': ', "DaiigrAI: "]
    )
    print(prfx + ' Response: ' + Fore.YELLOW + response['choices'][0]['text'])
    for choices in response['choices']:
        output = str(choices['text'])
        prompt_arr.append(output)
    return output

@bot.event
async def on_ready():
    prfx = (Back.BLACK + Fore.GREEN  + time.strftime("%H:%M:%S") + Back.RESET + Fore.WHITE  + Style.BRIGHT)
    print(Fore.WHITE + Style.BRIGHT +'---Discord Parameters---'+ Back.RESET + Style.NORMAL)
    print(prfx +' Logged in as: ' +  Fore.YELLOW + bot.user.name)
    print(prfx + ' Bot ID: ' + Fore.YELLOW + str(bot.user.id))
    print(prfx + ' Discord Version: ' + Fore.YELLOW + discord.__version__)
    print(prfx + ' Python Version: ' + Fore.YELLOW + str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2]))
    synced = await bot.tree.sync()
    print(prfx + ' Slash CMDs Synced: ' + Fore.YELLOW + str(len(synced)))

#slash commands

from Embeds import UserManagementEmbeds

@bot.tree.command(name="adduser", description='Add a user to the bot whitelist')
async def ping(interaction : discord.Interaction, mentioned_user : discord.User, name : str  , pronouns : str ,  admin_priv : bool):
    user_json_parser.AddUser(User(mentioned_user.id,name,pronouns,admin_priv))
    embed = UserManagementEmbeds.createAddedUserEmbed(mentioned_user,name,pronouns,admin_priv)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="removeuser", description='remove a user to the bot whitelist')
async def ping(interaction : discord.Interaction, mentioned_user : discord.User):
    user_json_parser.RemoveUserByID(mentioned_user.id)
    await interaction.response.send_message( str(mentioned_user.id))

@bot.tree.command(name="listusers", description='list all users in the bot whitelist')
async def ping(interaction : discord.Interaction):
    embed = UserManagementEmbeds.createListUsersEmbed(user_json_parser.GetUserListFromJson())
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="setRespondingChannel", description='set the channel the bot will respond in')
async def ping(interaction : discord.Interaction, mentioned_channel : discord.TextChannel):
    await interaction.response.send_message( str(mentioned_channel.id))

@bot.tree.command(name='setPersonalityType', description='set the personality type of the bot')
async def ping(interaction : discord.Interaction, personality_type : str):
    await interaction.response.send_message( str(personality_type))

@bot.tree.command(name='setModelType', description='set the model type of the bot')
async def ping(interaction : discord.Interaction, model_type : str):
    await interaction.response.send_message( str(model_type))

@bot.tree.command(name='setMaxTokens', description='set the max tokens of the bot')
async def ping(interaction : discord.Interaction, max_tokens : int):
    await interaction.response.send_message( str(max_tokens))

@bot.tree.command(name='Shutdown', description='Shutdown the bot')
async def ping(interaction : discord.Interaction):
    await interaction.response.send_message( 'Shutting Down')
    await bot.close()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    #formating the message into the GPT input
    # if user is not in the whitelist then don't respond
    if  user_json_parser.isUserInUserlist(message.author.id):
        return
    else:
        user = user_json_parser.getUserByID(message.author.id)
        try:
            userNameInput = user.Name + '('+user.Pronouns+')'
            prompt = '\n'+ userNameInput + ': ' + message.content + "\nDaiigrAI: "
            userNameInput = message.author.name
        
            prompt_arr.append(prompt)

            if len(prompt_arr) > 3:
                prompt_arr.pop(0)
            input = ' '.join(prompt_arr)

            messageOutput = getResponce(DEFAULT_PERSONALITY_TYPE + input , message.author.id)
            await message.channel.send(messageOutput)
        except:
            print(prfx + ' Error: ' + Fore.RED + 'User not in whitelist')
        

bot.run(DISCORD_TOKEN)

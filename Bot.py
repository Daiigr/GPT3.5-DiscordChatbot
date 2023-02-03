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
allow_non_whitelisted_users = True

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

@bot.tree.command(name="add-user", description='Add a user to the bot whitelist')
async def addUser(interaction : discord.Interaction, mentioned_user : discord.User, name : str  , pronouns : str ,  admin_priv : bool):
    user_json_parser.AddUser(User(mentioned_user.id,name,pronouns,admin_priv))
    embed = UserManagementEmbeds.createAddedUserEmbed(mentioned_user,name,pronouns,admin_priv)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="remove-user", description='remove a user to the bot whitelist')
async def removeUser(interaction : discord.Interaction, mentioned_user : discord.User):
    user_json_parser.RemoveUserByID(mentioned_user.id)
    await interaction.response.send_message( str(mentioned_user.id))

@bot.tree.command(name="list-users", description='list all users in the bot whitelist')
async def listUsers(interaction : discord.Interaction):
    embed = UserManagementEmbeds.createListUsersEmbed(user_json_parser.GetUserListFromJson())
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="set-responding-channel", description='set the channel the bot will respond in')
async def setRespondingChannel(interaction : discord.Interaction, mentioned_channel : discord.TextChannel):
    await interaction.response.send_message( str(mentioned_channel.id))

@bot.tree.command(name="set-responding-role", description='set the role the bot will respond to')
async def setRespondingRole(interaction : discord.Interaction, mentioned_role : discord.Role):
    await interaction.response.send_message( str(mentioned_role.id))

@bot.tree.command(name="allow-non-whitelisted-users", description='set if the bot will respond to non whitelisted users')
async def allowNonWhitelistedUsers(interaction : discord.Interaction, allow : bool):
    allow_non_whitelisted_users = allow
    await interaction.response.send_message( str(allow))

@bot.tree.command(name="allow-nsfw-content-generation", description='set if the bot will respond to non whitelisted users')
async def allowNonWhitelistedUsers(interaction : discord.Interaction, allow : bool):
    await interaction.response.send_message( str(allow))

@bot.tree.command(name='set-personality-type', description='set the personality type of the bot')
async def setPersonalityType(interaction : discord.Interaction, personality_type : str):
    await interaction.response.send_message( str(personality_type))

@bot.tree.command(name='set-model-type', description='set the model type of the bot')
async def setModelType(interaction : discord.Interaction, model_type : str):
    await interaction.response.send_message( str(model_type))

@bot.tree.command(name='set-max-tokens', description='set the max tokens of the bot')
async def setMaxTokens(interaction : discord.Interaction, max_tokens : int):
    await interaction.response.send_message( str(max_tokens))

@bot.tree.command(name='set-temperature', description='set the temperature of the bot')
async def setTemperature(interaction : discord.Interaction, temperature : float):
    await interaction.response.send_message( str(temperature))

@bot.tree.command(name='set-top-p', description='set the top p of the bot')
async def setTopP(interaction : discord.Interaction, top_p : float):
    await interaction.response.send_message( str(top_p))

@bot.tree.command(name='set-frequency-penalty', description='set the frequency penalty of the bot')
async def setFrequencyPenalty(interaction : discord.Interaction, frequency_penalty : float):
    await interaction.response.send_message( str(frequency_penalty))

@bot.tree.command(name='set-memory-length', description='set the memory length of the bot')
async def setMemoryLength(interaction : discord.Interaction, memory_length : int):
    await interaction.response.send_message( str(memory_length))

@bot.tree.command(name='list-configuration', description='list all settings of the bot')
async def listConfiguration(interaction : discord.Interaction):
    await interaction.response.send_message( str(allow_non_whitelisted_users))

@bot.tree.command(name='shutdown', description='Shutdown the bot')
async def ping(interaction : discord.Interaction):
    await interaction.response.send_message( 'Shutting Down')
    await bot.close()

@bot.event

async def isUserAllowedToBeRespondedTo(user):
        if allow_non_whitelisted_users == True:
            return True
        else:
            if user_json_parser.isUserInUserlist(user.id):
                return True
            else:
                return False

async def on_message(message):
    if message.author == bot.user:
        return
    
    #check if the message is in the responding channel and if not then return
    # if responding_channel == '': allow any channel


    if responding_channel == '':    
        responding_channel = message.channel.id
    elif message.channel.id != responding_channel:
        return
    
    #formating the message into the GPT input
    # if user is not in the whitelist then don't respond
    if isUserAllowedToBeRespondedTo(message.author.id) == False:
        return
    user = user_json_parser.getUserByID(message.author.id)
    if user == None:
        user = User(message.author.id,message.author.name,'They/Them',False)
        userNameInput = user.Name + '('+user.Pronouns+')'
        prompt = '\n'+ userNameInput + ': ' + message.content + "\nDaiigrAI: "
        userNameInput = message.author.name
        
        prompt_arr.append(prompt)

        if len(prompt_arr) > 3:
            prompt_arr.pop(0)
        input = ' '.join(prompt_arr)

        messageOutput = getResponce(DEFAULT_PERSONALITY_TYPE + input , message.author.id)
        await message.channel.send(messageOutput)
            
        

bot.run(DISCORD_TOKEN)

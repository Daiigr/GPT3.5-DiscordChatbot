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

from Config_Parser import botConfigParser
from User import User

# creates a config parser object which is used to parse the config.ini file
#checks if config.ini exists, if not it creates one and opens the config.ini creator
configparser = botConfigParser()

prfx = (Back.BLACK + Fore.GREEN  + time.strftime("%H:%M:%S") + Back.RESET + Fore.WHITE  + Style.BRIGHT)

print(Fore.WHITE + Style.BRIGHT + '---API Parameters---' + Back.RESET + Style.RESET_ALL)
DISCORD_TOKEN = configparser.get_discord_api_key()
print(prfx + ' Discord Token: ' + Fore.BLUE + DISCORD_TOKEN)

OPENAI_TOKEN = configparser.get_openai_api_key()
print(prfx + ' Discord Token: ' + Fore.BLUE + DISCORD_TOKEN)

try:
    openai.api_key = OPENAI_TOKEN
except:
    print(Fore.RED + Style.NORMAL + 'Invalid OpenAI API Key' + Back.RESET + Style.RESET_ALL)

#load in AI parameters
print( Fore.WHITE + Style.BRIGHT + '---AI Parameters---' + Back.RESET + Style.RESET_ALL)

DEFAULT_PERSONALITY_TYPE = configparser.get_default_personality_type()
print(prfx + ' Defualt Personality Type: ' + Fore.YELLOW + DEFAULT_PERSONALITY_TYPE)

MODEL_TYPE = configparser.get_model_type()
print(prfx + ' Model Type: ' + Fore.YELLOW + MODEL_TYPE)

MAX_TOKENS = configparser.get_max_tokens()
print(prfx + ' Max Tokens: ' + Fore.YELLOW + str(MAX_TOKENS))

TEMPERATURE = configparser.get_temperature()
print(prfx + ' Temperature: ' + Fore.YELLOW + str(TEMPERATURE))

TOP_P = configparser.get_top_p()
print(prfx + ' Top P: ' + Fore.YELLOW + str(TOP_P))

FREQUENCY_PENALTY = configparser.get_frequency_penalty()
print(prfx + ' Frequency Penalty: ' + Fore.YELLOW + str(FREQUENCY_PENALTY))

PRESENCE_PENALTY = configparser.get_presence_penalty()
print(prfx + ' Presence Penalty: ' + Fore.YELLOW + str(PRESENCE_PENALTY))

memory_length = 3
responding_role = ''
responding_channel = ''

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())



from UserJSONParser import UserJsonParser
user_json_parser = UserJsonParser()
allow_non_whitelisted_users = True

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

userCommandGroup = app_commands.Group(name="user" , description="manage users in the bot whitelist")

@userCommandGroup.command(name="add" , description="add a user to the bot whitelist")
async def addUser(interaction: discord.Interaction, user : discord.User, name : str  , pronouns : str) -> None:
    user_json_parser.AddUser(User(user.id,name,pronouns,'non' ))
    print(prfx + ' Added User: ' + Fore.PURPLE + name + ' (' + str(user.id) + ')' + ' with pronouns: ' + pronouns + ' to the whitelist' + Back.RESET + Fore.WHITE  + Style.BRIGHT)
    embed = UserManagementEmbeds.createAddedUserEmbed(user,name,'they/them')
    await interaction.response.send_message(embed=embed)

@userCommandGroup.command(name="remove" , description="remove a user from the bot whitelist")
async def removeUser(interaction: discord.Interaction, user : discord.User) -> None:
    user_json_parser.RemoveUserByID(user.id)
    print(prfx + ' Removed User: ' + Fore.PURPLE + user.name + ' (' + str(user.id) + ')' + ' from the whitelist' + Back.RESET + Fore.WHITE  + Style.BRIGHT)
    embed = UserManagementEmbeds.createRemovedUserEmbed(user)
    await interaction.response.send_message(embed=embed)

@userCommandGroup.command(name="edit" , description="edit a user in the bot whitelist")
async def editUser(interaction: discord.Interaction, user : discord.User, name : str  , pronouns : str) -> None:
    user_json_parser.EditUser(user.id ,User(user.id,name,pronouns, 'non' ))
    await interaction.response.send_message( str(user.id))

@userCommandGroup.command(name="list" , description="list all users in the bot whitelist")
async def listUsers(interaction: discord.Interaction) -> None:
    embed = UserManagementEmbeds.createListUsersEmbed(user_json_parser.GetUserListFromJson())
    await interaction.response.send_message(embed=embed)


bot.tree.add_command(userCommandGroup)

setCommandGroup = app_commands.Group(name="set" , description="manage bot settings")

@setCommandGroup.command(name="role", description='set the role the bot will respond to')
async def setRespondingRole(interaction : discord.Interaction, mentioned_role : discord.Role):
    responding_role = mentioned_role
    print(prfx + ' Responding Role: ' + Fore.YELLOW + mentioned_role.name + ' (' + str(mentioned_role.id) + ')' + Back.RESET + Fore.WHITE  + Style.BRIGHT   )
    await interaction.response.send_message( str(mentioned_role.id))

@setCommandGroup.command(name="personality", description='set the personality type of the bot')
async def setPersonalityType(interaction : discord.Interaction, personality_type : str):
    DEFAULT_PERSONALITY_TYPE = personality_type
    print(prfx + ' Personality Type: ' + Fore.YELLOW + personality_type + Back.RESET + Fore.WHITE  + Style.BRIGHT)
    await interaction.response.send_message( str(personality_type))

@setCommandGroup.command(name="model-type", description='set the model type of the bot')
async def setModelType(interaction : discord.Interaction, model_type : str):
    await interaction.response.send_message( str(model_type))

@setCommandGroup.command(name="max-tokens", description='set the max tokens of the bot')
async def setMaxTokens(interaction : discord.Interaction, max_tokens : int):
    await interaction.response.send_message( str(max_tokens))

@setCommandGroup.command(name="temperature", description='set the temperature of the bot')
async def setTemperature(interaction : discord.Interaction, temperature : float):
    await interaction.response.send_message( str(temperature))

@setCommandGroup.command(name="top-p", description='set the top p of the bot')
async def setTopP(interaction : discord.Interaction, top_p : float):
    await interaction.response.send_message( str(top_p))

@setCommandGroup.command(name="frequency-penalty", description='set the frequency penalty of the bot')
async def setFrequencyPenalty(interaction : discord.Interaction, frequency_penalty : float):
    await interaction.response.send_message( str(frequency_penalty))

@setCommandGroup.command(name="presence-penalty", description='set the presence penalty of the bot')
async def setPresencePenalty(interaction : discord.Interaction, presence_penalty : float):
    await interaction.response.send_message( str(presence_penalty))

@setCommandGroup.command(name="memory-length", description='set the memory length of the bot')
async def setMemoryLength(interaction : discord.Interaction, memory_length : int):
    await interaction.response.send_message( str(memory_length))

@bot.tree.command(name="stop", description='stop the bot')
async def stopBot(interaction : discord.Interaction):
    print(prfx + ' Stopping Bot' + Back.RESET + Fore.WHITE  + Style.BRIGHT)
    await interaction.response.send_message( 'Stopping Bot')
    await bot.close()

@bot.tree.command(name="restart", description='restart the bot')
async def restartBot(interaction : discord.Interaction):
    await interaction.response.send_message( 'Restarting Bot')
    print(prfx + ' Restarting Bot' + Back.RESET + Fore.WHITE  + Style.BRIGHT)
    await bot.close()
    os.system('python3 Bot.py')

    bot.tree.add_command(setCommandGroup)

ListCommandGroup = app_commands.Group(name="list" , description="list bot settings")

@ListCommandGroup.command(name="configuration", description='list the configuration of the bot')
async def listConfiguration(interaction : discord.Interaction):
    embed = UserManagementEmbeds.createListConfigurationEmbed(DEFAULT_PERSONALITY_TYPE,MODEL_TYPE,MAX_TOKENS,TEMPERATURE,TOP_P,FREQUENCY_PENALTY,PRESENCE_PENALTY)
    await interaction.response.send_message(embed=embed)
bot.tree.add_command(ListCommandGroup)


prompt_arr = []
    
def getResponce(prompt, user):
    response = openai.Completion.create(
    model=MODEL_TYPE,
    prompt=prompt,
    temperature=0.90,
    max_tokens=MAX_TOKENS,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[user.Name + ': ', "DaiigrAI: "]
    )
    print(prfx + ' Response: ' + Fore.YELLOW + response['choices'][0]['text'])
    for choices in response['choices']:
        output = str(choices['text'])
        prompt_arr.append(output)
    return output

#bot events

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
        
    user = user_json_parser.getUserByID(message.author.id)

    if user == None:
        user = User(message.author.id,message.author.name,'he/him','NOTADMIN')
    

    userNameInput = user.Name + '('+user.Pronouns+')'
    prompt = '\n'+ userNameInput + ': ' + message.content + "\nDaiigrAI: "
    userNameInput = message.author.name
            
    prompt_arr.append(prompt)

    if len(prompt_arr) > memory_length:
        prompt_arr.pop(0)
    input = ' '.join(prompt_arr)

    messageOutput = getResponce(DEFAULT_PERSONALITY_TYPE + input , user)
    await message.channel.send(messageOutput)
            
        
try:
    bot.run(DISCORD_TOKEN)
except:
    print(prfx + Fore.RED + ' please enter a valid Discord token' + Fore.RESET + Style.RESET_ALL) 
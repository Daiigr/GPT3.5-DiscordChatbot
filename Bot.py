#importing libraries (ensure you have these installed using pip, dontenv pip library name is python-dotenv)
from getpass import getuser
import openai
import json
import discord
import os

import ConfigParser as configparser
dDISCORD_TOKEN = configparser.get_discord_api_key()
OPENAI_TOKEN = configparser.get_openai_api_key()
openai.api_key = OPENAI_TOKEN

#load in AI parameters
DEFAULT_PERSONALITY_TYPE = configparser.get_default_personality_type()
MODEL_TYPE = configparser.get_model_type()
MAX_TOKENS = configparser.get_max_tokens()

client = discord.Client()

user_arr = []
class User:
    global Name
    def __init__(self,UserID,Name,Pronouns,ADMIN_PRIV):
        self.UserID = UserID
        self.Name = Name
        self.Pronouns = Pronouns
        if ADMIN_PRIV == 'ADMIN':
            self.ADMIN_PRIV = True
        else:
            self.ADMIN_PRIV = False

    def getName():
        return Name
class UserManager:
    def __init__(self,filename):
       f = open(filename, "a")
       import csv
       with open("UserMappings.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                user_arr.append(User(row[0],row[1],row[2],row[3]))

    def GetUser(self,UserID):
        for user in user_arr:
            if user.UserID == UserID:
                return user
        print("User not found")

usermanager = UserManager("UserMappings.csv")

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
    stop=[(usermanager.GetUser(str(userID)).Name)+ ': ', "DaiigrAI: "]
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
    user = usermanager.GetUser(str(message.author.id))
    userNameInput = user.Name + '('+user.Pronouns+')'
    prompt = '\n'+ userNameInput + ': ' + message.content + "\nDaiigrAI: "
    prompt_arr.append(prompt)

    if len(prompt_arr) > 3:
        prompt_arr.pop(0)
    input = ' '.join(prompt_arr)

    messageOutput = getResponce(DEFAULT_PERSONALITY_TYPE + input,message.author.id)
    await message.channel.send(messageOutput)

client.run(DISCORD_TOKEN)

 
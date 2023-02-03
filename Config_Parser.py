import configparser
import json

config = configparser.ConfigParser()
import os
from colorama import Fore, Back, Style
import time

class botConfigParser:

    def createConfig(self):
        """
        This function creates a config.ini file if one does not exist in the working directory
        """
        prfx = (Back.BLACK + Fore.GREEN  + time.strftime("%H:%M:%S") + Back.RESET + Fore.WHITE  + Style.BRIGHT)
        print(Fore.RED + Style.NORMAL + 'Creating Config.ini' + Back.RESET + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + 'Config Creator > API Parameters' + Back.RESET + Style.RESET_ALL)
        print (prfx +Fore.CYAN  + Style.NORMAL+ ' Please enter your OpenAI API Key: ' + Fore.RESET)
        openai_api_key = input()
        print (prfx + Fore.CYAN+ Style.NORMAL +' Please enter your Discord API Key: ' + Fore.RESET)
        discord_api_key = input()

        config['API-KEYS'] = {'OPENAI_API_KEY': openai_api_key,
                            'DISCORD_API_KEY': discord_api_key}

        print(Fore.WHITE + Style.BRIGHT + 'Config Creator > Bot Parameters' + Back.RESET + Style.RESET_ALL)

        print (prfx + Fore.GREEN + Style.NORMAL+' Please enter your Bot Name: ' + Fore.RESET)
        bot_name = input()
        config['BOTCONFIG'] = {'BOT_NAME': bot_name}

        print (prfx + Fore.GREEN + Style.NORMAL +' Please enter your Bot Default Personality Type: ' + Fore.RESET)
        personality_type = input()
        model_type = 'text-davinci-003'
        max_tokens = 200
        temperature = 0.90
        top_p = 1
        frequency_penalty = 0
        presence_penalty = 0.6


        config['APICONFIG'] = {
        'DEFAULT_PERSONALITY_TYPE': personality_type ,
        'MODEL_TYPE': model_type,
        'MAX_TOKENS': max_tokens,
        'TEMPERATURE': temperature,
        'TOP_P': top_p,
        'FREQUENCY_PENALTY': frequency_penalty,
        'PRESENCE_PENALTY': presence_penalty}

        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def updateConfig(self,section, key, value):
        """
        This function updates the config.ini file with the new value
        """
        config.read('config.ini')
        config.set(section, key, value)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)


    def doesConfigExist(self):
        """
        This function checks if the config.ini file exists
        """
        if not os.path.exists("config.ini"):
            print(Fore.RED + Style.NORMAL + 'Config.ini does not exist ...' + Back.RESET + Style.RESET_ALL)
            return False
        else:
            return True

    def get_openai_api_key(self):
        """
        This function returns the OpenAI API Key
        """
        config.read('config.ini')
        return config['API-KEYS']['OPENAI_API_KEY']

    def get_discord_api_key(self):
        """
        This function returns the Discord API Key
        """
        config.read('config.ini')
        return config['API-KEYS']['DISCORD_API_KEY']

    def get_bot_name(self):
        """
        This function returns the Bot Name
        """
        config.read('config.ini')
        return config['BOTCONFIG']['BOT_NAME']

    def get_default_personality_type(self):
        """
        This function returns the Bot Default Personality Type
        """
        config.read('config.ini')
        return config['APICONFIG']['DEFAULT_PERSONALITY_TYPE']

    def get_model_type(self):
        """
        This function returns the Bot Model Type
        """
        config.read('config.ini')
        return config['APICONFIG']['MODEL_TYPE']
    
    def get_max_tokens(self):
        """
        This function returns the Bot Max Tokens
        """
        config.read('config.ini')
        return int(config['APICONFIG']['MAX_TOKENS'])

    def get_temperature(self):
        """
        This function returns the Bot Temperature
        """
        config.read('config.ini')
        return config['APICONFIG']['TEMPERATURE']
    
    def get_top_p(self):
        """
        This function returns the Bot Top P
        """
        config.read('config.ini')
        return config['APICONFIG']['TOP_P']
    
    def get_frequency_penalty(self):
        """
        This function returns the Bot Frequency Penalty
        """
        config.read('config.ini')
        return config['APICONFIG']['FREQUENCY_PENALTY']
    
    def get_presence_penalty(self):
        """
        This function returns the Bot Presence Penalty
        """
        config.read('config.ini')
        return config['APICONFIG']['PRESENCE_PENALTY']


    def __init__(self):
        """
        This function checks if the config.ini file exists in the working directory
        """
        prfx = (Back.BLACK + Fore.GREEN  + time.strftime("%H:%M:%S") + Back.RESET + Fore.WHITE  + Style.BRIGHT)
        if os.path.isfile('config.ini'):
            print(Fore.GREEN + Style.NORMAL + 'Config.ini Exists' + Back.RESET + Style.RESET_ALL)
        else:
            print(Fore.RED + Style.NORMAL + 'Config.ini does not exist ...' + Back.RESET + Style.RESET_ALL)
            self.createConfig()
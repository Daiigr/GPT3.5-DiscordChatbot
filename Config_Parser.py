import configparser
import json

config = configparser.ConfigParser()
import os

def  create_config():
    """
    This function creates a config.ini file if one does not exist in the working directory
    """

    print('config.ini does not exist, creating file')
    config['API-KEYS'] = {'OPENAI_API_KEY': '<api-key>',
                        'DISCORD_API_KEY': '<api-key>'}

    config['APICONFIG'] = {'DEFAULT_PERSONALITY_TYPE':'<personality description>' ,
    'MODEL_TYPE':'<model type>',
    'MAX_TOKENS': '<max number of tokens>'}
    
    config['USERMANAGER'] = {'USERARRAY': '[enter user mappings]',}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    exit()


def get_openai_api_key():
    """
    This function returns the openai api key from the config.ini file
    """
    if not os.path.exists("config.ini"):
        create_config()
        return 
    else:
        config.read('config.ini')
        config.sections()
        return config['API-KEYS']['openai_api_key']

def get_discord_api_key():
    """
    This function returns the discord api key from the config.ini file
    """
    if not os.path.exists("config.ini"):
        create_config()
        return 
    else:
        config.read('config.ini')
        config.sections()
        return config['API-KEYS']['discord_api_key']

def get_default_personality_type():

    """
    This function returns the default personality type from the config.ini file
    """
    if not os.path.exists("config.ini"):
        create_config()
        return 
    else:
        config.read('config.ini')
        config.sections()
        return config['APICONFIG']['DEFAULT_PERSONALITY_TYPE']

def get_model_type():
    """
    This function returns the model type from the config.ini file
    """
    if not os.path.exists("config.ini"):
        create_config()
        return 
    else:
        config.read('config.ini')
        config.sections()
        return config['APICONFIG']['MODEL_TYPE']

def get_max_tokens():
    """
    This function returns the max tokens from the config.ini file as a int
    """
    if not os.path.exists("config.ini"):
        create_config()
        return 
    else:
        config.read('config.ini')
        config.sections()
        return int(config['APICONFIG']['MAX_TOKENS'])
    


def get_user_mappings():
    """
    This function returns the user mappings from the config.ini file
    """
    if not os.path.exists("config.ini"):
        create_config()
        return 
    else:
        config.read('config.ini')
        config.sections()
        return  config['USERMANAGER']['USERARRAY']
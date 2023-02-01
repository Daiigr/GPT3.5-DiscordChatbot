import configparser
import json

config = configparser.ConfigParser()
import os

def  create_config():
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

# if example.ini does not exist in working directory run create_config() 
if not os.path.exists("config.ini"):
    create_config()
else:
    config.read('config.ini')
    config.sections()
   # print(config['API-KEYS']['openai_api_key'])
# if example.ini exists run 

def get_openai_api_key():
    if not os.path.exists("config.ini"):
        create_config()
        return 
    else:
        config.read('config.ini')
        config.sections()
        return config['API-KEYS']['openai_api_key']

def get_discord_api_key():
    if not os.path.exists("config.ini"):
        create_config()
        return 
    else:
        config.read('config.ini')
        config.sections()
        return config['API-KEYS']['discord_api_key']

def get_default_personality_type():
    if not os.path.exists("config.ini"):
        create_config()
        return 
    else:
        config.read('config.ini')
        config.sections()
        return config['APICONFIG']['DEFAULT_PERSONALITY_TYPE']

def get_model_type():
    if not os.path.exists("config.ini"):
        create_config()
        return 
    else:
        config.read('config.ini')
        config.sections()
        return config['APICONFIG']['MODEL_TYPE']

def get_max_tokens():
    if not os.path.exists("config.ini"):
        create_config()
        return 
    else:
        config.read('config.ini')
        config.sections()
        return int(config['APICONFIG']['MAX_TOKENS'])
    


def get_user_mappings():
    if not os.path.exists("config.ini"):
        create_config()
        return 
    else:
        config.read('config.ini')
        config.sections()

        print(config['USERMANAGER']['USERARRAY'])
        return  config['USERMANAGER']['USERARRAY']
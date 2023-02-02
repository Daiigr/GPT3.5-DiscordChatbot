# OpenAI(GPT-3)-Discord-ChatBot
a communication layer between the OpenAI GPT-3 API and the Discord Bot API. Designed for general chatbot use

## 1. setting up your OpenAI API key
[OpenAI](beta.openai.com)

login or create your OpenAI account to access the GPT API keys and head to “View API keys” if you are on the main menu. from there you want to press create new secret key and copy it to your clip board or in a text document temporarily. it should be a long string of randomized letters symbols and numbers. this key will allow us to make requests to GPT-3

note: GPT is not free to use however as of writing this article they provide a 18 dollar trial amount which is more than enough try out all the fun ideas you might have with a bot like this.

at the current price of 0.02$ per 1k tokens it is reasonably priced for the compute, R&D and energy costs associated with running such a service. for those looking for a open source version of GPT-3 lookout for future articles on GPT-J and BLOOM (however this requires very beefy hardware and more setup so its not for everyone)

## 2. setting up your Discord Bot

head to the discord developer portal and login with your discord account

Discord Developer Portal - API Docs for Bots and Developers
Integrate your service with Discord - whether it's a bot or a game or whatever your wildest imagination can come up…
discord.com

select Applications (generally located in the top left of the website) and select Create Application (located top right) once inside your created application, head to the bot tab and click on create bot. reset the token and copy it into your clipboard or text document


from the application page head to the general information tab of your application and copy the application ID into your clipboard and paste it into the [Discord Permission Cacluator](https://discordapi.com/permissions.html#8) which allows you to add it to your discord server

## 3. setting up a python environment

to use OpenAI’s api and Discords API we need to install the correct packages inside a python environment where all our package data will be stored

we will use a program called [Anaconda](https://www.anaconda.com/products/distribution#Downloads) as our environment

for those using macOS and wish to use homebrew follow this [link](https://medium.com/ayuth/install-anaconda-on-macos-with-homebrew-c94437d63a37)

additionally those using linux can just install it through there package manager of choice. being apt-get, pacman, yum or whatever other package manager that supports anaconda

creating and activating our python environment

on macOS & linux use the command in the terminal

`conda create GPT_BOT`

`conda activate GPT_BOT`

in windows search anaconda in the windows search bar and right click and run as administer the program named Anaconda Prompt (anaconda3) which should open a ‘CMD’ terminal. from there run these commands

`conda create GPT_BOT`

`conda activate GPT_BOT`

once you are in your newly created Python Environment we can now install the necessary python libraries

`pip3 install openai discord.py python-dotenv`

note: python-dotenv is a library that allows us to load in a env file into our python program which is where we will store all our api keys later on

now we are ready to start coding!
## 4. setting up  `config.ini` 

copy this GitHub repository to where you want to store your files

run bot.py and it will create a file called config.ini in that config.ini file you will need to add your OpenAI API key and your Discord API key along with some other configuration settings
here is a semi filled out example of what your config.ini file should look like

```sh
[API-KEYS]
openai_api_key = token here
discord_api_key = token here

[APICONFIG]
default_personality_type = this is a converation between a bot and users:
model_type = text-davinci-003
max_tokens = 400

MAX_TOKENS=’50'
```

## 5. running the bot and adding users 

once you have your config.ini file filled out with your API keys and your configuration settings you can now run the bot.py file and it should start up your bot and connect to your discord server

to add users to the bot's whitelist you can use the slash command `/adduser` and it will add the user to the whitelist, input the desired name for that user and it will add them to the whitelist and you can now talk to the bot


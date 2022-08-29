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
## 4. setting up `Bot.py` , `.env` and 'UserMapping.csv'

copy this GitHub repository to where you want to store your files

in the same folder as the Bot.py file create a new file called .env which is where the python script will pull the API keys and program parameters from in this new .env file copy these lines

```sh
DISCORD_TOKEN=’’

OPENAI_TOKEN=’’

#AI parameters

DEFAULT_PERSONALITY_TYPE=’the following is conversation with a AI. the AI is childish, fun and friendly’

MODEL_TYPE=’text-davinci-002'

MAX_TOKENS=’50'
```

copy your discord token (API key) and your openAI token (API key) into the file and save it

additionally create a file called UserMappings.csv and save it into the same folder. That file is where you write all the authorized users that the bot will respond to

the format goes as follows

`DISCORD_USER_ID, NAME,PRONOUNS,ADMIN/USER`

discord user id is found by activating developer mode in discord settings and right clicking on users and copying their Ids

in your python environment you have open (if not open your terminal and use the conda activate GPT_BOT command) head over to the folder where the Bot.py file and the .env file is located and run the command `python3 Bot.py`

if everything is properly set up then the bot should be online and you can begin to talk to it!


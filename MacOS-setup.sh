/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install --cask anaconda
conda create --name openAIenv
conda activate openAIenv
pip3 install requirements.txt
python3 Bot.py

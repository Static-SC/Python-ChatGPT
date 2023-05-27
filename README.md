# Simple-ChatGPT
## Use Python to connect with API to ChatGPT

# Create virtual environment for a given project
Opening the Command Palette (Ctrl+Shift+P), start typing the Python: Create Environment
Select .venv
If you are creating an environment using Venv, the command presents a list of interpreters that can be used as a base for the new virtual environment.

Open up a NEW Terminal

# Installs
~~~
pip install openai python-dotenv pyqt6
~~~

# Install DotEnv to hide the API_KEY from main code
### Create .env file
Create a new file ".env". This file holds your secrets, like API_Key
put in your secrets eg.
~~~
OPENAI_API_KEY=my_api_key_from_openai
~~~

# Run Program
~~~
python Chat_UI_V3.py
~~~

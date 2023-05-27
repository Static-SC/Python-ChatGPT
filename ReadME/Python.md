# Install Python
~~~
pip install python
~~~

## Verify the Python installation (windows)
~~~
py -3 --version
~~~

## Create virtual environment for a given project
Opening the Command Palette (Ctrl+Shift+P), start typing the Python: Create Environment
Select .venv
If you are creating an environment using Venv, the command presents a list of interpreters that can be used as a base for the new virtual environment.

## Create a virtual environment in the terminal
~~~
python -m venv .venv
~~~
When you create a new virtual environment, a prompt will be displayed in VS Code to allow you to select it for the workspace.

## Activate the environment
~~~
.venv\scripts\activate
~~~

## if error, run powershell as admin.
~~~
Set-ExecutionPolicy RemoteSigned
~~~
This should allow VS code to activate the environment

## Deactivate Environment
~~~
deactivate
~~~
# Test automation script for Mash

This repository contains test suite for 

## Preconditions

1) Installed packages:
- Python 3.7
- robotframework	3.1.1
- robotframework-seleniumlibrary	3.3.1
- selenium	3.141.0

2) Correct path added to PYTHONPATH
- {project_path}/mash_automation/libraries

## First time setup of virtualenv
~~~~
 $ sudo apt-get install python-virtualenv
~~~~

## Setting up the environment

After cloning this repo to a host machine, a new virtual environment can be created by calling

~~~~
 $ virtualenv .venv
 or if you want to specify python3 as your project interpreter
 $ virtualenv .venv -p /usr/bin/python3
 then 
 $ source .venv/bin/activate
~~~~

This will then create the virtual environment and return a prompt that has (.venv) at the start. To ensure the right configuration is applied then run the following steps

~~~~
 (.venv) $ pip install --upgrade pip # many distributions ship criminal old pip
 (.venv) $ pip install -r pip_requirements.txt
~~~~


## Leaving the virtual environment

Leaving the virtual environment can be done from the terminal by the following call

~~~~
 (.venv) $ deactivate
~~~~



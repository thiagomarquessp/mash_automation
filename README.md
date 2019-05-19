# Test automation script for Mash

This repository contains test framework based on Python, Robot Framework and Selenium

## Tools used

- PyCharm 2018.2
- Python 3.7
- robotframework	3.1.1
- robotframework-seleniumlibrary	3.3.1
- selenium	3.141.0


## First time setup of virtualenv
~~~~
 $ sudo apt-get install python-virtualenv
~~~~

## Setting up the environment

After cloning this repo to a host machine, navigate to project directory and create new virtual environment by calling

~~~~
 $ virtualenv .venv
 or if you want to specify python3 as your project interpreter
 $ virtualenv .venv -p /usr/bin/python3
 then 
 $ source .venv/bin/activate
~~~~

Then install required packageds (robot framework and selenium)

~~~~
 (.venv) $ pip install --upgrade pip # many distributions ship criminal old pip
 (.venv) $ pip install -r requirements.txt
~~~~

## Leaving the virtual environment

Leaving the virtual environment can be done from the terminal by the following call

~~~~
 (.venv) $ deactivate
~~~~

## Browser drivers

Path to browser drivers should be added to PATH in environment variables settings

##  Running test

In command line/terminal navigate to project directory and execute below command to run test:
~~~~
 robot -d results tests/web_automation.robot
~~~~

## Browsing test execution results

Test results are stored in `results` folder within project

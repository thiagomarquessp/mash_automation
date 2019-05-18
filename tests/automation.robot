*** Settings ***
Library    ../libraries/WebKeywords.py
#Library  ../libraries/locators.py

Test Setup    Initialize
Test Teardown    Teardown
*** Variables ***


*** Test Cases ***
do stuff
    input text to search field
    execute search
    navigate to second results page

*** Keywords ***
Initialize
    Initialize and open browser with url    https://www.google.fi  chrome

Teardown
    close browser
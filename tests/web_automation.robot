*** Settings ***
Library    ../libraries/PyKeywords.py
Variables  ../libraries/PageObjects/locators.py

Suite Setup    Initialize
Suite Teardown    Teardown
*** Variables ***


*** Test Cases ***
Mash site link should not be displayed on second page of Google search result
    Input text to search field    ${SEARCH_INPUT}
    Execute search    ${SEARCH_RESULT_MASH_LINK}
    Navigate to second results page
    Verify if link to Mash site is not visible

*** Keywords ***
Initialize
    Initialize and open browser with url    ${URL}  chrome

Teardown
    Close browser
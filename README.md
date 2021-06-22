# Selenium Framework

Test Automation Framework using Python and Selenium web driver.


## Requirements

 - Python 3.8 or above.
 - Chrome browser version 91.x.x.x


## Setup

 1. Clone repository to desired folder.
 >git clone https://github.com/ErikP-M/Selenium_Framework.git
 
 2. Create a python virtual environment, it can be located at the same level where the repo was cloned.
 >python -m venv venv
 
 3. Activate virtual environment.
 >**Windows:** venv\Scripts\activate.bat
 
 >**Linux:** source venv/bin/activate
 
 4. From ***Selenium_Framework/Libs*** copy folders **html_testRunner-1.2.1.dist-info** and **HtmlTestRunner**  to ***venv/Lib/site-packages*** in order to add the *HtmlTestRunner* module to the python virtual environment. 
 
 5.  Execute the following commands to install required python modules:
 >pip install selenium==3.141.0
 
 >pip install jinja2

## Execution
Using command line place at: ***Selenium_Framework/wizeline_framework/***
Send run test command: 
>python -m TestCases.test_cases

## Reports
Execution reports will be stored at ***Selenium_Framework/wizeline_framework/Reports*** folder in HTML format.

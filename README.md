## World Best App Test
##


## Technical Test

My results for a technical test that I was given. In that test my task was to implement a series of automation tests in order 
to test a given website. 
    
    My tasks
    --------
    
    Complete Behave tests

    Fix broken tests
        1. Open test/behave/features/steps/login.py
        2. You will find that the methods have not been completed as they raise the NotImplemented error.
           According to the described scenario, fill in the necessary steps to pass the test.
        3. What changes would you make to the features to make them better for testing?
        4. Are there any features that you think should be added to improve the testing?

    Fix broken Postman tests

    1. Install and open Postman on your machine.
    2. Open the collection test/postman/collections/WorldsBestApp.json
    3. Setup the environment test/postman/environments/local.json

    Try to run it and you'll find that some of the tests are broken. Fix them.
    Can the test be improved in any way?


The full details for that tests can be found at 

https://sprinkle-burn.a.me/test

##
   
## Before the running the tests the following steps must be done. Step two is not optional and must be done otherwise the packages will not be imported correctly and the tests will fail

1. Setup your virtualenv optional
1. To run the tests run the following commands
   
   1. cd into the WorldsBestApp directory.
   1. Once inside directory run the following commands on the setup.py file. This commands will enable the packages to be imported anyway into tests.
      1. python setup.py install
      1. python setup.py develop
   1. Execute python -r requirements.txt to install the dependencies



2. Install the appropriate files on your system if not present.
    
   
    On a Mac Computer
    --------------------
   
    1. brew install node
    1. brew install python
    1. brew install pipenv
    1. brew cask install postman
    1. brew cask install chromedriver


    Installing on a Windows
    --------------------------

    Download and install choco

    choco install selenium-chrome-driver
    choco install nodejs
    choco install postman
    choco install python
    python -m pip install -U pip
    pip install pipenv



## Running the tests
##

1. cd into test\behave\features\ and run the tests by hitting *behave*


## Completed tasks
##

Complete Behave tests

    1. Fix broken tests - completed
    
    2. What changes would you make to the features to make them better for testing?
    
       The changes I would make are
            1. Scenerio outline for tests that are the same but with different parameters
               For example:
                    1. username with blank password
                    2. incorrect username with right password
                    3. correct username with wrong password
            2. Implement Background where certains actions are performed before a given scenerio 
               e.g opening an closing a web page               
    
    3. Are there any features that you think should be added to improve the testing?
       
       There are a couple of features that I think can be added to improve the tests
       
           1. Checking the format an incorrect email
           1. Checking whether the username is case-sensitive
           1. Checking if a password is alphanumeric or numeric
           1. Password minimum and maximum length
           1. Check for blank fields


Fix broken Postman tests (completed)

    
## Technologies used for the test
1. Python 3.6
2. Selenium
3. The Test Framework Behave
4. Postman
5. Nodejs
# Create-Project-Automation

## Description
This is a litte Python-Bash-Powershell project that create a repo on your github account and clone it on your computer, so you no more need to do it yourself.

This project automates the project creation :  
    - creates the repository in your github account 
    - creates the folder in the directory you indicates by cloning the repo
    - creates the files you indicates according to the project type
    - and open the project with your IDE

I used Python with Selenium for web scraping 
I used bash and powershell scripts 


## Python Script
This script uses Selenium to create a repository in your github account
It does not work all the time because Github can use double auth when Python log in

You need the driver of your browser to make it work, check the Selenium doc [here](https://selenium-python.readthedocs.io/).

<code>
    python main.py repo_name project_type github_pwd
<code>

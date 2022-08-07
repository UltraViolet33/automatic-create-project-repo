# Create-Project-Automation

## Description
This is a little Python-Bash-Powershell project that creates a repo on your Github account and clone it on your computer, so you no more need to do it yourself.

This project automates the project creation :  
- creates the repository in your Github account 
- creates the folder in the directory you indicates by cloning the repo
- creates the files you indicates according to the project type
- and open the project with your IDE

I used Python with Selenium for web scraping to log in Github and create the repository and bash and powershell scripts to clone the repository. 


## Python Script
This script uses Selenium to create a repository in your Github account.
It does not work everytime because Github can use double auth when Python log in but it is funny to look at.

## Steps

1.  You need the driver of your browser to make it work, (chrome, firefox...) check the Selenium doc
[here](https://selenium-python.readthedocs.io/)


2. Put your Github pseudo or email in the main python file line 34
```python
    input_login.send_keys("your_email")
```

3. Put your Github pseudo in the URL so Python can go to your new repo line 53
```py
    driver.get("https://github.com/" + "your_pseudo/" + repo_name)
```
4. Update the scipt call line 59 :

if you use bash :

```py
   subprocess.call(['bash', './scripts/commands_create_project.sh', repo_name, project_type, url_to_clone])
```
if you use powershell : 
```py
    subprocess.call(['powershell', './scripts/commands_create_project.ps1', repo_name, project_type url_to_clone])
```

5. Then either in the bash or powershell script, update the path you want the repo will be cloned

```sh
    cd your_path/$project_type
```

6. Test it in a terminal

```sh
    >python main.py repo_name project_type github_pwd
```



import sys
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PROJECT_TYPES = {"js", "python", "html-css"}

repo_name = "default-repo-name"
project_type = ""
github_pwd = ""

if len(sys.argv) == 4:
    repo_name = sys.argv[1]
    project_type = sys.argv[2]
    if project_type not in PROJECT_TYPES:
        sys.exit("Error, invalid project_type")
    github_pwd = sys.argv[3]
elif len(sys.argv) > 4:
    sys.exit("Error, too many arguments")
else:
    sys.exit("Error, project name, project type or github password is missing")

# You need the chrome driver
driver = webdriver.Chrome()
driver.get("https://github.com/login")
time.sleep(1)

input_login = driver.find_element(By.ID, "login_field")
input_pwd = driver.find_element(By.ID, "password")
btn_submit = driver.find_element(By.NAME, "commit")

# Your pseudo or email
input_login.send_keys("")
time.sleep(5)
# Your password
input_pwd.send_keys(github_pwd)
time.sleep(5)
# btn_submit.click()

driver.get("https://github.com/new")

input_repo_name = driver.find_element(By.ID, 'repository_name')
input_repo_name.send_keys(repo_name)

# You repository will be private
btn_radio_private_repo = driver.find_element(
    By.ID, "repository_visibility_private")
btn_radio_private_repo.click()
driver.find_element(By.ID, "new_repository").submit()

# Put your pseudo
driver.get("https://github.com/" + "your_pseudo/" + repo_name)

url_to_clone = driver.find_element(
    By.ID, "empty-setup-clone-url").get_attribute('value')

# call the script to clone the repo
subprocess.call(['powershell', './commands_create_project.ps1',
                repo_name, project_type, url_to_clone])

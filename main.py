from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import subprocess

name_repo = "repo"

if len(sys.argv) > 0:
    name_repo = sys.argv[1]


driver = webdriver.Chrome()
driver.get("https://github.com/login")

inputLogin = driver.find_element(By.ID, "login_field")
inputPwd = driver.find_element(By.ID, "password")
btnSubmit = driver.find_element(By.NAME, "commit")

element = driver.find_element(By.ID, "login_field")

inputLogin.send_keys()
inputPwd.send_keys()
btnSubmit.click()


driver.get("https://github.com/new")

inputRepoName = driver.find_element(By.ID, 'repository_name')
inputRepoName.send_keys(name_repo)

btnRadioPrivate = driver.find_element(By.ID, "repository_visibility_private")
btnRadioPrivate.click()

createRepoBtn = driver.find_element(By.XPATH, "//button[@type='submit']")
# print(createRepoBtn)

driver.find_element(By.ID, "new_repository").submit()

driver.get("https://github.com/UltraViolet33/" + name_repo)

urlGitClone = driver.find_element(By.ID, "empty-setup-clone-url").get_attribute('value')

# print(urlGitClone)

subprocess.call(['powershell', './command.ps1', name_repo, urlGitClone])

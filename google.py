from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.get("https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=MA&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&dsh=S-1174042992%3A1679244799900505&emr=1&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AWnogHf9SKOHNR6OISXfxTSTzfZD5HBvEEU8yqVvLo20runfzh2b-164fdSYN2z37LEMPB6nDomKVA&osid=1&service=mail")
browser.maximize_window()

firstname = browser.find_element(By.ID, "firstName")
lastname = browser.find_element(By.ID, "lastName")
username = browser.find_element(By.ID, "username")
password = browser.find_element(By.XPATH, value="//input[@name='Passwd']")
password_confirm = browser.find_element(By.XPATH,value="//input[@name='ConfirmPasswd']")
button = browser.find_element(By.XPATH, value="//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']")

firstname.send_keys("mohamed")
lastname.send_keys("mossa")
username.send_keys("mohamedmossa51912")
password.send_keys("Mohamed_77")
password_confirm.send_keys("Mohamed_77")
button.click()

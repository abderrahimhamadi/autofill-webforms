
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.get("https://www.oncf-voyages.ma/creation-compte")
browser.maximize_window()

first_name = browser.find_element(By.ID, "createAccountFieldsFirstName")
last_name = browser.find_element(By.ID, "createAccountFieldsLastname")
birthdate = browser.find_element(By.XPATH, value="//input[@placeholder='Ma date de naissance']")
telephone = browser.find_element(By.XPATH, value="//input[@placeholder='Mon téléphone']")
city = browser.find_element(By.XPATH, value="//div[@class='ant-select-selection__placeholder']")
email = browser.find_element(By.ID, "createAccountFieldsUserRegisterEmail")
email_confirm = browser.find_element(By.ID, "createAccountFieldsRegisterConfirmationEmail")
password = browser.find_element(By.ID, "createAccountFieldsRegisterPassword")
password_confirm = browser.find_element(By.ID, "createAccountFieldsRegisterConfirmationPassword")
# This means that we are looking for an element in the page, that is a
# “label” that has an attribute called “for” with the value “input-newsletter-yes”
chechboxs = browser.find_element(By.XPATH, value="//input[@type='checkbox']")
create_acc = browser.find_element(By.XPATH, value="//button[@class='ant-btn btn-default CreateAccountFooter_confirm ant-btn-default ant-btn-round']")


first_name.send_keys("Abderrahim")
last_name.send_keys("Hamadi")
birthdate.send_keys("05/02/2002")
telephone.send_keys("0664251951")
city.send_keys("Rabat")
email.send_keys("a19@gmail.com")
email_confirm.send_keys("a19@gmail.com")
password.send_keys("hamadi")
password_confirm.send_keys("hamadi")
checkboxs.click()
create_acc.click()

#assert browser.title == "Your Account Has Been Created!"

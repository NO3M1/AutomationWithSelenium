
# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://the-internet.herokuapp.com/login')

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

#completam username
chrome.find_element(By.ID, 'username').send_keys('tomsmith')

#completam parola
chrome.find_element(By.ID,'password').send_keys('SuperSecretPassword!')

#dam click pe login button
chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()

#dam click pe logout

chrome.find_element(By.XPATH, '//*[@id="content"]/div/a/i').click()

sleep(3)

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')
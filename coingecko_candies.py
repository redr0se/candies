from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from credentials import *
from selenium.webdriver.firefox.options import Options

def getSomeCandies(mail, password):
    print("Script running...")
    options = Options()
    options.headless = True #allow headless mode
    #Launch webdriver
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.coingecko.com/fr")
    #Get css elements for connection
    elem = driver.find_element_by_css_selector("div.mr-3:nth-child(7) > a:nth-child(1)")
    time.sleep(2)
    elem.click()
    time.sleep(2)
    elem = driver.find_element_by_css_selector("#signInEmail").send_keys(mail)
    elem1 = driver.find_element_by_css_selector("#signInPassword").send_keys(password + Keys.ENTER)
    time.sleep(4)
    #Connected then get candies
    candiesBox = driver.find_element_by_css_selector("div.candy-notification-icon-section:nth-child(4) > a:nth-child(2)")
    candiesBox.click()
    time.sleep(1)
    getCandies = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[3]/div[3]/div/form/input[1]")
    getCandies.click()
    #Quiting selenium windows
    driver.quit()
    print(f'Script done for {mail} !')
    
i = 0
while i < len(mail):
    getSomeCandies(mail[i], password[i])
    i = i+1
print("Récupération terminée !")

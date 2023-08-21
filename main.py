from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def launchBrowser():
    #Get user input
    search = input("What do you want to search for?")
    
    #Init. driver + go to amazon
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get("http://www.amazon.com/")

    #Get search bar element and search for user's input
    search_bar = driver.find_element(By.ID, 'twotabsearchtextbox')
    search_bar.send_keys(search)
    search_bar.submit()

    while(True):
        pass
   
launchBrowser()
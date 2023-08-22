from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep

def launchBrowser():
    #Get user input
    search = input("What do you want to search for?")
    
    #Init. driver + go to amazon
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get("http://www.amazon.com/")

    #Get search bar element and search for user's input
    search_bar = driver.find_element(By.ID, 'twotabsearchtextbox')
    search_bar.clear()
    search_bar.send_keys(search)
    search_bar.submit()
    
    names = []
    prices = []

    product_elements = driver.find_elements(By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']")
    for element in product_elements:
        names.append(element.text)

    price_whole_elements = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")
    price_decimal_elements = driver.find_elements(By.XPATH, "//span[@class='a-price-fraction']")

    for i in range(max(len(price_whole_elements), len(price_decimal_elements))):
        prices.append("$" + price_whole_elements[i].text + "." + price_decimal_elements[i].text)

    print(prices[:10])

    while(True):
        pass
   
launchBrowser()
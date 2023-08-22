from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd

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
    
    search_results = driver.find_elements(By.XPATH,'//div[@data-component-type="s-search-result"]')

    names = []
    prices = []

    for result in search_results:
        try:
            if len(result.find_elements(By.XPATH,".//span[@class='a-size-base-plus a-color-base a-text-normal']"))>0:
                result_name = result.find_element(By.XPATH,".//span[@class='a-size-base-plus a-color-base a-text-normal']")

            elif len(result.find_elements(By.XPATH,".//span[@class='a-size-medium a-color-base a-text-normal']"))>0:
                result_name = result.find_element(By.XPATH,".//span[@class='a-size-medium a-color-base a-text-normal']")
            
            names.append(result_name.text)

        except:
            pass

        try:
            if len(result.find_elements(By.XPATH,".//span[@class='a-price-whole']"))>0:
                result_price = result.find_element(By.XPATH,".//span[@class='a-price-whole']")
                prices.append(result_price.text)

            else:
                prices.append("0")
                
        except:
            pass

    print(len(names), len(prices))
    df = pd.DataFrame({"Product Names": names, "Prices": prices})
    df.to_excel(r"C:\Users\colby\Desktop\Web-Scraper-1\list.xlsx")

    while True:
        pass

launchBrowser()
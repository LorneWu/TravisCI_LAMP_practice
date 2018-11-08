from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
import os

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.binary_location = '/usr/local/bin'    

driver =webdriver.Chrome(chrome_options=chrome_options)  
driver.get("https://www.google.com.tw/search?q=chrome")
print(browser.current_url)

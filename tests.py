from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.binary_location = '/usr/local/share/chromedriver'    

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),chrome_options=chrome_options)  

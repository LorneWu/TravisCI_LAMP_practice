import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME
)
search_input = driver.find_element_by_name('q') # 取得搜尋框
search_input.send_keys('Python') # 在搜尋框內輸入 'Python'
search_input.submit() # 令 chrome driver 按下 submit
time.sleep(5)
driver.quit() # 關閉 chromedriver

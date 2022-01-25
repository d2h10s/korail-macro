import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

url="https://www.letskorail.com/ebizprd/prdMain.do"
driver = webdriver.Chrome(executable_path='chromedriver')
driver.implicitly_wait(time_to_wait=5)
driver.get(url=url)
windows = driver.window_handles
for w in windows[1:]:
    driver.switch_to.window(w)
    driver.close()
driver.switch_to.window(windows[0])
while True:
    pass

driver.close()

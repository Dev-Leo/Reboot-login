import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://i.caisan.net/login')
username = "18229298314"
password = "dengziqi520"
assert "登录 - 彩伞中心" in browser.title
browser.find_element_by_name("username").send_keys(username)
browser.find_element_by_name("password").send_keys(password)
browser.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(5)
browser.find_element_by_xpath('//div[2]/div/div[2]/ul/li/a').click()

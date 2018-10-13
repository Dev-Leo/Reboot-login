from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://i.caisan.net/login')
username = "18888888888"
password = "88888888"
assert "登录 - 彩伞中心" in browser.title
browser.find_element_by_name("username").send_keys(username)
browser.find_element_by_name("password").send_keys(password)
browser.find_element_by_name("password").send_keys(Keys.ENTER)

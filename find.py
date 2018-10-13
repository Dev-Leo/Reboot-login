from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://www.baidu.com')
browser.find_element_by_id('kw').send_keys('test')
browser.find_element_by_id('su').click()

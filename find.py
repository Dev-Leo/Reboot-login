from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.baidu.com')
browser.find_element_by_id('kw').send_keys('test')
browser.find_element_by_id('su').click()

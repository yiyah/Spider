from selenium import webdriver

url = 'https://www.baidu.com'
browser = webdriver.Firefox()
browser.get(url)
browser.close()
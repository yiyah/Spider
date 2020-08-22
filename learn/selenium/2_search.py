from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def SearchInPython():
    driver = webdriver.Firefox()
    driver.get("https://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")  # locate the searching box
    elem.send_keys("pycon")  # input searching keywords
    elem.send_keys(Keys.RETURN)  # get the result


def SearchInBaidu():
    driver = webdriver.Firefox()
    driver.get('https://www.baidu.com/')
    elem = driver.find_element_by_xpath('//*[@id="kw"]')
    elem.send_keys('ardupilot')
    elem.send_keys(Keys.RETURN)
    for i in range(3, -1, -1):
        elem.clear()
        str = 'close after: %d s' % i
        elem.send_keys(str)
        time.sleep(1)
    driver.close()


if __name__ == "__main__":
    SearchInBaidu()
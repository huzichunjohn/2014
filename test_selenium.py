#!/bin/env python
from selenium import webdriver

driver = webdriver.PhantomJS('phantomjs')

driver.get('http://www.qq.com')
print driver.title

driver.quit()







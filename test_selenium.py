#!/bin/env python
from selenium import webdriver

driver = webdriver.PhantomJS('phantomjs')

driver.get('http://www.sina.com.cn')
print driver.title

driver.quit()







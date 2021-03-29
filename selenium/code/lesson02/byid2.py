# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/selector/s1.html') # 打开网址






print '-------------------------'
ele = driver.find_element_by_id("baidulink")
print ele.get_attribute('href')


print '-------------------------'
ele = driver.find_element_by_id("food")
print ele.get_attribute('style')









driver.quit()


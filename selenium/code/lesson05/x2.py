# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson05/xpath.html')



ele = driver.find_element_by_xpath("//span[@id='pork']/..")
print ele.text.split('#')[1]


driver.quit()


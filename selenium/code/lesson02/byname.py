# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/selector/s1.html') # 打开网址

# -----------------------------------



eles = driver.find_elements_by_name("button22")
print eles


# -----------------------------------


# raw_input('press any key to quit...')
driver.quit()


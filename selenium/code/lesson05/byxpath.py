# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson05/s1.html')



eles = driver.find_elements_by_xpath("/html/body/div")

for ele in eles:
    print '----------'
    print ele.get_attribute('outerHTML')




# raw_input('press any key to quit...')
driver.quit()


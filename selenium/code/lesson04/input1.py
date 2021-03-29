# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
sys.path.append('..')
from settings import  executable_path
driver = webdriver.Chrome(executable_path) #初始化，运行chrome driver

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/input/input1.html') # 打开网址


input1 = driver.find_element(By.ID,"input1")
input1.send_keys(u'输入我想输入的字符222')
input1.clear()
input1.send_keys(u'what')


ta1 = driver.find_element(By.ID,"ta1")
ta1.send_keys(u'春眠不觉晓\n处处闻啼鸟')



raw_input('press any key to quit...')


driver.quit()   # 浏览器退出
# Appium 作业 2 

<br>

- 到如下网址下载 多多计算器 <br>

http://android.myapp.com/myapp/detail.htm?apkName=com.ibox.calculators&ADTAG=mobile
 

- 用 aapt.exe 命令查看 apk包的 appPackage 信息和  主 Activity 信息
- 用 UIAutomator Viewer 查看应用界面元素信息
- 编写python程序，完成一个 计算 3+9 ，结果 再乘以5 的自动化功能. 最后判断计算结果是否为60，如果是，测试通过；否则测试不通过



#### 参考答案，往下翻


<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

```python
# coding=utf8

from appium import webdriver
import time,traceback



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = r'd:\apk\duoduoCalculators.apk'
desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity'] = '.SplashActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

try:
    # -----------------



    num3 = driver.find_element_by_id("com.ibox.calculators:id/digit3")
    num5 = driver.find_element_by_id("com.ibox.calculators:id/digit5")
    num9 = driver.find_element_by_id("com.ibox.calculators:id/digit9")
    plus = driver.find_element_by_id("com.ibox.calculators:id/plus")
    mul = driver.find_element_by_id("com.ibox.calculators:id/mul")
    equal = driver.find_element_by_id("com.ibox.calculators:id/equal")

    num3.click()
    plus.click()
    num9.click()
    equal.click()
    mul.click()
    num5.click()
    equal.click()


    # 检查结果，需要我们去找结果对应的界面元素，发现是下面这个TextView
    # 研究发现没有特点，大家想想我们该怎么办
    # 可以看看父节点有没有唯一标识，发现 父节点是有id的，
    # 就可以怎么样？
    # 先查找父节点，
    # 再根据父节点元素 调用 find element 就是在父节点的范围内 查找
    retLayout = driver.find_element_by_id('com.ibox.calculators:id/cv')
    retTvs     = retLayout.find_elements_by_class_name('android.widget.TextView')
    retStr = retTvs[1].text
    print(retStr)

    if retStr == '60':
        print('pass')
    else:
        print('fail')




        # -----------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()
```




 


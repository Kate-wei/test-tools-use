# Appium 作业 5 

<br>
作业1

- 安装开发者头条应用
- 打开该应用，在阅读标签页中，点击 精选文章的第一篇，验证确实能打开同名文章
- 按返回键， 验证能够正确返回 阅读标签页


<br>

作业2

- 安装 wv 应用，下载地址如下：https://github.com/jcyrss/songqin-testdev/raw/master/appium/uploads/wv.apk
- 自动化在手机上运行该应用， 切换到webview
- 百度搜索 "松勤"
- 切换回native界面，点击 通知 按钮 

## 参考答案，往下翻
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>


```python
# coding=utf8

from appium import webdriver
import time,traceback

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = r'e:\apk\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print driver.session_id
driver.implicitly_wait(10)

try:
    # -----------------

    # 用下面的表达式，也可以用xpath

    code = u'new UiSelector().resourceId("io.manong.developerdaily:id/btn_item").instance(0).childSelector(new UiSelector().className("android.widget.TextView"))'
    ele1 = driver.find_element_by_android_uiautomator(code)
    
    text1 = ele1.text
    print text1

    ele1.click()

    time.sleep(2)

    ele2 = driver.find_element_by_id('io.manong.developerdaily:id/tv_title')
    text2 = ele2.text
    print text2

    if text2 == text1:
        print 'pass'
    else:
        print 'fail'


    driver.press_keycode(4)

    #  检查是否回到刚才的页面
    ele2 = driver.find_elements_by_id('io.manong.developerdaily:id/tab_bar_plus')

    if ele2:
        print 'we return back'

    # -----------------

except:
    print traceback.format_exc()

driver.quit()
```

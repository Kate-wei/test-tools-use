#### 0001


```java
问题：

用adb devices 能找到虚拟手机设备，appium server也在运行中，
当运行自动化测试脚本时，跑不起来。换成真实手机也同样跑不起来。
appium server报错信息为：
[ADB] Could not find devices, restarting adb server...
[ADB] Restarting adb
[ADB] Error killing ADB server, going to see if it's online anyway
[ADB] Getting connected devices...
[ADB] Error: Error while getting connected devices. Original error: Command 'C:\Users\HJN\AppData\Local\Android\sdk\platform-tools\adb.exe
C:\Program Files (x86)\AllWinnerTech\PhoenixSuit\adb.exe' not found. Is it installed?

回答：

在系统变量中添加一个环境变量
变量名为： ANDROID_HOME 
值为：android sdk 的安装路径  （例如： C:\Users\HJN\AppData\Local\Android\sdk）

特别注意的是： 设置好以后 Appium Desktop 要重新启动一下

```



<br><br><br>
#### 0002
```java
问题：

Appium Server 报类似 

ENOENT: no such file or directory, scandir '/Users/vikram-anna/Library/Android/sdk/platform-tools/build-tools' 

回答：

一般是 ANDROID_HOME  环境变量设置有误导致的
```

<br><br><br>
#### 0003

```java
问题：

运行UIAutomatorviewer，出现 awt异常

回答：

JDK 版本安装 最新的 1.8的版本
```



<br><br><br>
#### 0004
使用安卓模拟器 ，运行自动化程序出现如下错误

Failure [INSTALL_FAILED_NO_MATCHING_ABIS]

需要刷入Genymotion-ARM-Translation_v1.1.zip

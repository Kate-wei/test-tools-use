#### Q
```python
问题：

我已经添加了 文件 test.py 到环境变量 path中， 为什么执行命令 python test.py ，
解释器还是提示 can't open file 'test.py' :[Errno 2] No such file or directory

=========================================
答： 

环境变量 path 是针对命令中 可执行程序(比如上述的 python) 设置的搜索路径, 
不是 命令中的参数文件 （比如上述的 test.py）设置的搜索路径.
参数文件必须使用正确的相对路径或者绝对路径。
```


<br><br><br>
#### Q
```python
问题：

执行pip命令为什么报错？

d:\>python
Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (
Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> pip install selenium
  File "<stdin>", line 1
    pip install selenium
              ^
SyntaxError: invalid syntax
>>>

=========================================
答： 

pip命令是在命令行窗口中执行的，不是Python解释器shell里面执行的。应该如下

d:\>pip install selenium

```




<br><br><br>
#### Q
```python
问题：
list、dict里面有中文的时候，为什么print 它们，显示的是像二进制的数字呢？

=========================================
答： 
print 一个对象，其实就是调用这个对象的__str__方法或者__repr__方法。
列表、字典的__str__方法，就是这样实现的，对于不在acii范围内的字节，就显示为16进制的数字
```





<br><br><br>
#### Q
```python
问题：

import paramiko 出现如下错误

result_path = result_path + p_path
UnicodeDecodeError: 'ascii' codec can't decode byte .....

=========================================
答： 
这是环境变量 path 里面有中文导致的
```


<br><br><br>
#### Q
```python
问题：
Win7上 安装Python3，最后提示 "api-ms-win-crt-runtime-l1-1-0.dll 丢失"


=========================================
答： 
这是Win7 补丁包导致的
可以下载安装 Microsoft Visual C++ Redistributable for Visual Studio 2015 Update 1
在这里下载
https://www.microsoft.com/en-us/download/details.aspx?id=49984

参考 https://github.com/winpython/winpython/issues/245


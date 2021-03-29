# Python 作业 10



```java



获取统计 远程Linux主机的 可用内存率。


请大家先安装 paramiko :  执行pip install paramiko


请大家自行百度搜索，安装虚拟机管理器 virtualbox 或者 vmvareplayer， 创建 64位 虚拟机，
安装centos镜像

cetos6.9 下载地址 :
http://mirrors.163.com/centos/6.9/isos/x86_64/CentOS-6.9-x86_64-bin-DVD1.iso

Putty 下载地址 :
https://the.earth.li/~sgtatham/putty/0.70/w32/putty-0.70-installer.msi

    
    
然后编写一个python程序，代码文件名为 memory.py , 该代码文件 计划在远程Linux机器运行。该程序做如下的事情：
    每隔5秒钟 打开文件 /proc/meminfo，该文件包含了系统内存使用信息，前面数行内容如下
    
MemTotal:        1920648 kB
MemFree:           87788 kB
Buffers:          229704 kB
Cached:          1180244 kB

    memory.py 程序要将 memFree 、buffers、cached 的值 相加 （结果是可用内存的数量）。
    然后除以 MemTotal的值， 得到可用内存占的百分比（赋值给变量 avaMem）。
    将 avaMem 的数值存入 结果文件ret.txt中。
    
    上面的程序一直运行，每隔 5秒钟 获取记录一次 avaMem 对应的时间戳， 格式如下
    20170315_12:10:00  77%
    20170315_12:10:05  74%
    20170315_12:10:10  70%
    20170315_12:10:15  72%
    
    


再编写一个python程序，代码文件名为 auto.py，该程序运行起来做如下工作：
    以自己名字的拼音（比如lixia） 在远程机器建立一个目录 。如果该目录已经存在则跳过此步骤
    拷贝文件memory.py 到远程机器该目录下面，
    远程在Linux主机执行文件 memory.py 
    过5分钟后，将远程文件memory.py执行产生的结果文件ret.txt 内容拷贝回本机


```


## 参考答案，往下翻
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

#### memory.py
```python
# coding=utf8
import time

# MemTotal:        1920648 kB
# MemFree:           87788 kB
# Buffers:          229704 kB
# Cached:          1180244 kB
def getContent(lines,field):
    for line in lines:
        if field in line:
            value = line.split(':')[1].split('kB')[0].strip()
            return int(value)

# count 用来时间上计数，防止一直运行
count = 0
while True:
    count += 1

    with open('/proc/meminfo') as f:
        beginlines = f.readlines()[:8]

    memTotal = getContent(beginlines,'MemTotal')
    memFree  = getContent(beginlines,'MemFree')
    buffers  = getContent(beginlines,'Buffers')
    cached   = getContent(beginlines,'Cached')

    # print memTotal,memFree,buffers,cached
    # 别忘了 * 100
    memUsage = (memFree + buffers + cached) *100.0/memTotal
    # 搜索时间格式
    memUsage = '%s     %.2f%%' % (time.strftime('%Y%m%d_%H:%M:%S'),memUsage)
    print(memUsage)

    with open('ret.txt','a') as f:
        f.write(memUsage+'\n')

    time.sleep(5)

    # 防止一直运行
    if count>15:
        break
```


#### auto.py
```python

# coding=utf8
import paramiko,time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("120.26.96.231",22,"stt", "stt0707")


# 创建自己名字的目录
dirName =  "jcy"

# 先检查 是否已经存在同名目录了， 如果没有则创建
stdin, stdout, stderr = ssh.exec_command("ls")
# exec_command 返回的是bytes类型，需要解码
dircontent =  stdout.read().decode()

print(dircontent)
if dirName in dircontent.splitlines():
    print('{} already exists'.format(dirName))
else:
    print('make dir {}'.format(dirName))
    ssh.exec_command("mkdir {}".format(dirName))

# 传输文件
sftp = ssh.open_sftp()
sftp.put('memory.py', '{}/memory.py'.format(dirName))
sftp.close()


# 检查文件是否传输成功，可以将检查文件是否存在机器，做成一个函数。。。


# 执行脚本


# 考虑到长时间没有消息，网络连接可能会被断开。 到网上搜索一番后。
# 设置一个保持连接的参数
transport = ssh.get_transport()
transport.set_keepalive(30)

print('remote exec python memory.py')
ssh.exec_command("cd %s; python memory.py" % dirName)

print('wait for 30 seconds...')
time.sleep(30)


# 传输文件
sftp = ssh.open_sftp()
sftp.get('{}/ret.txt'.format(dirName),'ret.txt')
sftp.close()

ssh.close()


```

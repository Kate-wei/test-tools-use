## 安装虚拟机，虚拟机中安装Linux

请大家自行百度搜索，安装虚拟机管理器 virtualbox 或者 vmvareplayer， 创建 64位 虚拟机，
安装centos镜像

cetos6.5 下载地址 :
http://archive.kernel.org/centos-vault/6.5/isos/x86_64/CentOS-6.5-x86_64-bin-DVD1.iso


安装好以后，以root用户登录

## 安装 Mysql 服务

1 执行下面命令安装mysql 5.6 基于 centos 6.5 的yum源

```
wget http://repo.mysql.com/mysql-community-release-el6-5.noarch.rpm
rpm -ivh mysql-community-release-el6-5.noarch.rpm
```
	
2 执行下面命令安装 mysql server 和 mysql devel


```
yum install mysql-server
yum install mysql-devel
```


## 启动mysql

执行命令 service mysqld start


## 创建 数据库用户 账号

执行命令 mysql 启动 mysql 命令行客户端，在交互式命令行输入

```
CREATE USER 'songqin'@'localhost' IDENTIFIED BY 'songqin';   
CREATE USER 'songqin'@'%' IDENTIFIED BY 'songqin';
```

然后 给 数据库用户 账号 songqin 赋予超级权限

```
GRANT ALL ON *.* TO 'songqin'@'localhost';
GRANT ALL ON *.* TO 'songqin'@'%';
```

执行quit 退出 mysql client


## 创建数据库

下载数据库文件 

wget --no-check-certificate https://github.com/jcyrss/songqin-testdev/raw/master/webapi/doc/plesson.sql


执行如下命令，将plesson.sql文件 导入数据库中

mysql -usongqin -psongqin < plesson.sql

执行如下命令，让mysqld服务开机启动
	
chkconfig --level 2345 mysqld on

## 修改教管系统配置文件

将教管系统 访问数据库从本地的sqlite改为使用远程mysql 服务

修改配置文件
restapi-teach\backend\project\settings.py

注意，下面的ip地址一定要写对

```py
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'plesson',
       'USER': 'songqin',
       'PASSWORD': 'songqin',
       'HOST': '你机器的ip地址',
       'PORT': '3306',
       'CONN_MAX_AGE': 0, 
       'OPTIONS': {
              "init_command": "SET storage_engine=INNODB",
       }
   }
}
```

重新启动


## 打开防火墙端口

iptables -I INPUT -p TCP --dport 3306 -j ACCEPT;/sbin/service iptables save

## Heidisql工具连接访问数据库

打开 https://www.heidisql.com/

下载安装portableversion


## 安装 mysqlclient 客户端库

在自己的客户端机器上，通常也就是教管系统所在机器上，运行如下命令， mysqlclient 客户端库

pip install mysqlclient==1.3.12


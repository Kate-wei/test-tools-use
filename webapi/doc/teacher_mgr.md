# 老师管理API接口

### 增加老师接口

用来创建一个新的培训老师

#### 请求语法
```java
POST /api/mgr/sq_mgr/ HTTP/1.1
Host:           restapi-teach.com
Content-Type:   application/x-www-form-urlencoded
```

##### url请求参数
无url请求参数


##### 请求体内容

```python
action	必填	填写add_teacher，表明是为了创建老师

data	必填	存储创建老师的信息，包括登录名、密码、真实姓名、描述信息、教授课程、显示次序。
为json格式。例如：
{
    "username":"lishiming",
    "password":"sq888",
    "realname":"李世民",
    "desc":"李世民老师",
    "courses":[{"id":419,"name":"初中数学"},{"id":420,"name":"初中英语"}],
    "display_idx":1
}

注意 上面教授课程字段courses里面填写的是这个老师 教授的每门课程的 id 号 和 课程名称
```

#### 响应语法
```java
HTTP/1.1 200 OK
Content-Type: application/json
```

##### 头部信息

Content-Type	必填 	正常情况下该值将被设为application/json，表示返回 JSON 格式的文本信息。

##### 响应内容
如果请求成功，返回json格式的消息体，如下所示，retcode值为0表示添加成功，id表示创建的老师的id号
```json
{
    "retcode": 0, 
    "id": 143
}
```

##### 说明
增加老师登录名如果已经存在，则会创建失败返回结果为
```json
{
    "reason": "登录名 xxxx 已经存在",
    "retcode": 1
}
```





<br><br><br><br>
### 列出老师接口
用来列出系统里所有的老师信息

#### 请求语法
```java
GET /api/mgr/sq_mgr/?action=list_teacher&pagenum=1&pagesize=20 HTTP/1.1
Host:           restapi-teach.com
Content-Type:   application/x-www-form-urlencoded
```

##### url请求参数
```python
action	填写list_teacher，表明是要列出所有老师信息

pagenum	表示当前要显示的是第几页，目前固定填写1

pagesize	表示一页最多显示多少条老师信息，目前固定填写20
```

##### 请求体内容
该请求无需指定请求内容。

#### 响应语法
```java
HTTP/1.1 200 OK
Content-Type: application/json
```

##### 头部信息

Content-Type	正常情况下该值将被设为application/json，表示返回 JSON 格式的文本信息。

##### 响应内容
如果请求成功，返回json格式的消息体，如下所示
```json
{
    "retlist": [
        {
            "username": "lishiming",
            "realname": "李世民",
            "display_idx": 1,
            "courses": [
                {
                    "course_id": 419
                },
                {
                    "course_id": 420
                }
            ],
            "id": 143,
            "desc": "李世民老师"
        },
        {
            "username": "zhuyuanzhang",
            "realname": "朱元璋",
            "display_idx": 1,
            "courses": [
                {
                    "course_id": 419
                },
                {
                    "course_id": 420
                }
            ],
            "id": 144,
            "desc": "朱元璋老师"
        }
    ],
    "total": 2,
    "retcode": 0
}

retcode值为0表示查询成功。
total 值表示总共有多少个老师
retlist的内容是一个数组，其中每个元素对应一位老师信息。
```









<br><br><br><br>
### 修改老师接口
用来修改一位培训老师的信息

#### 请求语法
```java
PUT /api/mgr/sq_mgr/ HTTP/1.1
Host:           restapi-teach.com
Content-Type:   application/x-www-form-urlencoded
```

##### url请求参数
无url请求参数

##### 请求体内容
```python
action	填写modify_teacher，表明是为了修改老师信息

id	 填写要修改的老师的id号
newdata	 存储创建修改后老师的信息，包括名称、描述、显示次序,为json格式。例如：
{
    "username":"lishiming",
    "password":"sq888",
    "realname":"李世民",
    "desc":"李世民老师",
    "courses":[{"id":419,"name":"初中数学"},{"id":420,"name":"初中英语"}],
    "display_idx":1
}
```

#### 响应语法
```java
HTTP/1.1 200 OK
Content-Type: application/json
```

##### 头部信息

Content-Type	正常情况下该值将被设为application/json，表示返回 JSON 格式的文本信息。

##### 响应内容
如果请求成功，返回json格式的消息体，如下所示，retcode值为0表示修改成功
```python
{
    "retcode": 0
}
```





<br><br><br><br>
### 删除老师接口
用来删除一位培训老师
#### 请求语法
```java
DELETE /api/mgr/sq_mgr/ HTTP/1.1
Host:           restapi-teach.com
Content-Type:   application/x-www-form-urlencoded
```

##### url请求参数
无url请求参数

##### 请求体内容
```python
action	是	填写delete_teacher，表明是为了删除老师信息
id	是	填写要删除的老师的id号
```


#### 响应语法
```java
HTTP/1.1 200 OK
Content-Type: application/json
```

##### 头部信息

Content-Type	正常情况下该值将被设为application/json，表示返回 JSON 格式的文本信息。

##### 响应内容
如果删除成功，返回json格式的消息体，如下所示，retcode值为0表示删除成功
```python
{
    "retcode": 0
}
```

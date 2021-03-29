# 登录认证API接口



用来进行用户登录认证

#### 请求语法
```java
POST /api/mgr/loginReq HTTP/1.1
Host:           restapi-teach.com
Content-Type:   application/x-www-form-urlencoded
```

##### url请求参数
无url请求参数


##### 请求体内容

```python
username	必填	填写用户名

password	必填	填写用户密码
```

#### 响应语法
```java
HTTP/1.1 200 OK
Content-Type: application/json
```

##### 头部信息

```java
Content-Type	必填   该字段值为application/json，表示返回 JSON 格式的文本信息。
Set-Cookie      必填   该字段保存本次登录的sessionid，比如：sessionid=89emkau5vhyg8vcwfwvq2pvr7ul2t5sc
```

##### 响应内容
如果请求成功，返回json格式的消息体，如下所示，retcode值为0表示登录认证成功
```json
{
    "retcode": 0
}
```

##### 说明
如果输入的用户名或者密码错误，则返回结果为

```json
{
    "retcode": 1,
    "reason": "用户或者密码错误"
}
```



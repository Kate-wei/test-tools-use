# Python 练习 4 



### 不定项选择

```python

- 一个变量a定义如下
    a = ['this', 'test', 4.56, ['inner', 'list']]
    下面的表达式结果为False 的有   
    
A)   'this' in a
    
B)   'test' in a
    
C)   't' not in a
    
D)   'inner' in a



- 下面的表达式结果为False的有 
    
A)    (2 > 1 or 3 > 4) and 5 > 4    
    
B)    2 > 1 or (3 > 4 and 5 > 4)

C)    1 > 2 or (3 > 4 and 5 > 4)
    
D)    (1 > 2 or 3 > 4) and 5 > 4




```


### 判断题

```java

- 和算术表达式一样，我们可以用括号，来提升 布尔表达式的 运算优先级   

- 比较（英文）字符串的大小，是根据其ASCII码的大小 来决定的 ， ASCII大的认为值是大的 

- if 语句成立后面要执行的代码块，缩进必须是4个空格 

- 下面的代码，解释器运行时， 如果条件1 为True， 后面 条件2 条件3 解释器都不会去执行做判断
if 条件1:
    <执行的内容1>
elif 条件2:
    <执行的内容2>
elif 条件3：
    <执行的内容3>
else:
    <执行的内容4>
    
    
- 下面的两种代码写法，执行效果是相同的

方法一：    
if a>1:
    if b>2:
        print('a,b both > 1')
        
方法二：    

if a>1 and b>2:
    print('a,b both > 1') 


        
    
- 下面的代码一，和代码二 是等价的 
       
代码一：    
score = 90
if score >= 90:
    print('your score is', score)
    print('excellent')
elif score >= 60:
    print('your score is', score)
    print('ok')
else:
    print('your score is', score)
    print('you have trouble')
    

代码二：        
   
score = 90
print('your score is', score)

if score >= 90:
    print('excellent')
elif score >= 60:
    print('ok')
else:
    print('you have trouble') 


```



<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>



### 不定项选择

```python

    - 一个变量a定义如下
        a = ['this', 'test', 4.56, ['inner', 'list']]
        下面的表达式结果为False 的有   (d)

    A)   'this' in a

    B)   'test' in a

    C)   't' not in a

    D)   'inner' in a


    - 下面的表达式结果为False的有 (cd)
    
    (2 > 1 or 3 > 4) and 5 > 4    
    
    2 > 1 or (3 > 4 and 5 > 4)

    1 > 2 or (3 > 4 and 5 > 4)
    
    (1 > 2 or 3 > 4) and 5 > 4

```


### 判断题

```java

- 和算术表达式一样，我们可以用括号，来提升 布尔表达式的 运算优先级   （T）

- 比较（英文）字符串的大小，是根据其ASCII码的大小 来决定的 ， ASCII大的认为值是大的 （T）

- if 语句成立后面要执行的代码块，缩进必须是4个空格 （F）

- 下面的代码，解释器运行时， 如果条件1 为True， 后面 条件2 条件3 解释器都不会去执行做判断 (T)
if 条件1:
    <执行的内容1>
elif 条件2:
    <执行的内容2>
elif 条件3：
    <执行的内容3>
else:
    <执行的内容4>
    
    
- 下面的两种代码写法，执行效果是相同的（T）

方法一：    
if a>1:
    if b>2:
        print('a,b both > 1')
        
方法二：    

if a>1 and b>2:
    print('a,b both > 1')


        
    
- 下面的代码一，和代码二 是等价的 (T)
       
代码一：    
score = 90
if score >= 90:
    print('your score is', score)
    print('excellent')
elif score >= 60:
    print('your score is', score)
    print('ok')
else:
    print('your score is', score)
    print('you have trouble')    
    

代码二：        
   
score = 90
print('your score is', score)

if score >= 90:
    print('excellent')
elif score >= 60:
    print('ok')
else:
    print('you have trouble')    


```

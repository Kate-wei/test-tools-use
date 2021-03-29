# Python 练习 3 

### 不定项选择

```java

- 一个变量a定义如下
    a = ['this', 'test', 4.56, ['inner', 'list']]
    那么 a[1][2] 的结果是  
    
A)   'h'
    
B)    'e'
    
C)    's'
    
D)    'i'
    

- 变量a定义如下
    a = [1,2,3,4,5,6,7,8,9]
    要获取包含a 的最后两个元素的列表，下面写法正确的是 
    
A)   a[-1:]
    
B)   a[-2:]
    
C)   a[-2:-0]
    
D)   a[-2:0]

   
        
    
- 下面哪些代码语句执行时，会报错  
    
A)   a = [1,3.5,5,6]
    
B)   [1,3,5,8][1] = 4
    
C)   (1,3,5,8)[1] = 4    
    
D)  a = 'my name is jcy'
    a[1] = '4'
    
    
    
- 一个变量定义如下
    a = ['this', 'test', 4.56, ['inner', 'list']]
    那么 修改其中的最后一个List元素的第二个元素 值为 8 ，下面的写法正确的是
    
A)   a[4][2] = 8
    
B)   a[-1][-1] = 8
    
C)   a[3][1] = 8
    
D)   a[-1][1] = 8
    
    




- 定义一个变量var1 其值是一个字符串 what's your name， 下面哪些是错误的 

A)  var1 = "what's your name"
B)  var1 = what's your name
C)  var1 = 'what's your name'
D)  var1 = '''what's your name'''

```

### 判断题
```python
- 列表中的元素 除了不可以是tuple，可以是任意其它类型的对象  
    
- 列表中元素 既可以用逗号，也可以用分号  隔开  
    
- 由于tuple 是不可改变的，所以 我们不能用切片操作在tuple 对象上，比如 (3,4,5)[1:2]   
    
- 定义tuple 中只有一个元素 3， 可以这样定义 (3,)   
    
- 由于list 是可以改变元素的，当我们对list 进行切片（slice）操作的时候，原来的list 对象就改变了。 比如 执行下面代码后
a = [1,2,3,4]
a[1:3]
    
对象a 的内容就改变为[2,3]  

- 下面的字符串列出了人的名字 和体重，

str1 = 'name: Micle, weight: 130kg'

要用切片的方式从str1中取出体重（包括kg部分） 可以是  str1[-5:] 


- 下面的字符串列出了人的名字 和体重，

str1 = 'name: Jack, weight: 130kg'

要用切片的方式从str1中取出人名  可以是  str1[7:11]   


- 长度为n的字符串str1，最后一个元素 的代码表示可以是str1[-1]也可以是str1[n]

```


<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### 不定项选择

```java

- 一个变量a定义如下
    a = ['this', 'test', 4.56, ['inner', 'list']]
    那么 a[1][2] 的结果是  (c)
    
A)   'h'
    
B)    'e'
    
C)    's'
    
D)    'i'
    

- 变量a定义如下
    a = [1,2,3,4,5,6,7,8,9]
    要获取包含a 的最后两个元素的列表，下面写法正确的是 （b）
    
A)   a[-1:]
    
B)   a[-2:]
    
C)   a[-2:-0]
    
D)   a[-2:0]

      
        
    
- 下面哪些代码语句执行时，会报错   (c,d)
    
A)   a = [1,3.5,5,6]
    
B)   [1,3,5,8][1] = 4
    
C)   (1,3,5,8)[1] = 4    
    
D)  a = 'my name is jcy'
    a[1] = '4'
    
    
    
- 一个变量定义如下
    a = ['this', 'test', 4.56, ['inner', 'list']]
    那么 修改其中的最后一个List元素的第二个元素 值为 8 ，下面的写法正确的是(b,c,d)
    
A)   a[4][2] = 8
    
B)   a[-1][-1] = 8
    
C)   a[3][1] = 8
    
D)   a[-1][1] = 8
    
    
- 一个变量a定义如下
    a = ['this', 'test', 4.56, ['inner', 'list']]
    下面的表达式结果为False 的有   (d)
    
A)   'this' in a
    
B)   'test' in a
    
C)   't' not in a
    
D)   'inner' in a

 
- 定义一个变量var1 其值是一个字符串 what's your name， 下面哪些是错误的  (B,C)


A)  var1 = "what's your name"
B)  var1 = what's your name
C)  var1 = 'what's your name'
D)  var1 = '''what's your name'''


```

### 判断题
```python
- 列表中的元素 除了不可以是tuple，可以是任意其它类型的对象  （错）
    
- 列表中元素 既可以用逗号，也可以用分号  隔开  （错）
    
- 由于tuple 是不可改变的，所以 我们不能用切片操作在tuple 对象上，比如 (3,4,5)[1:2]   （错）
    
- 定义tuple 中只有一个元素 3， 可以这样定义 (3,)   （对）
    
- 由于list 是可以改变元素的，当我们对list 进行切片（slice）操作的时候，原来的list 对象就改变了。 比如 执行下面代码后
a = [1,2,3,4]
a[1:3]
    
对象a 的内容就改变为[2,3]  （错）

- 下面的字符串列出了人的名字 和体重，

str1 = 'name: Micle, weight: 130kg'

要用切片的方式从str1中取出体重（包括kg部分） 可以是  str1[-5:]    （对）


- 下面的字符串列出了人的名字 和体重，

str1 = 'name: Jack, weight: 130kg'

要用切片的方式从str1中取出人名  可以是  str1[7:11]   （错误，应该是str1[6:10]）


- 长度为n的字符串str1，最后一个元素 的代码表示可以是str1[-1]也可以是str1[n] （错误：应该是str1[n-1]）

```

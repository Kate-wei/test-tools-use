
# Python 练习 6

### 不定项选择

```python
- 下面格式化字符串的代码，哪些是错误的 

A) 'my name is %s' % 'Mike'   
B) 'my name is %d' % 'Mike'     
C) "my name is %s, I'm %s years old." % ['Mike',6]  
D) "my name is %s, I'm %s years old." % ('Mike',6)  
    
    
- 下面格式化字符串的代码，哪些是错误的 

A) 'my name is %s'.format('Mike')
B) 'my name is {}{}'.format('Mike')   
C) "my name is {}, I'm {} years old.".format('Mike',5)     
D) "my name is {}, I'm {} years old.".format(['Mike',5])  


- python3.6 执行下面格式化字符串的代码，哪些是会报错的
A) "my name is {0}, I'm {1} years old.".format('Mike',5)  
B) "my name is {}, I'm {1} years old.".format('Mike',5)   
C) "I'm {1} years old, my name is {0}".format('Mike',5)   
D) "my name is {0}, his name is also {0}".format('Mike')   
E) f"my name is {'Mike'}, his name is also {{Mike}}"  
```



### 判断题
```python

- 格式化字符串 '%10d' 表示参数显示的宽度至少为10个字符，不足10个字符用空格补齐 

- 格式化字符串 '%010d' 表示参数显示的宽度至少为10个字符，不足10个字符用字符0补齐
    
- 格式化字符串 "%06X" 表示参数以8进制显示，显示的宽度至少为10个字符，不足10个字符用字符0补齐

- 格式化字符串'%9.2f'表示参数数字的小数部分保留2位， 同时还指明了最小宽度是9，不足补空格

- '{:<10}'.format(8) 表示最小宽度是10，同时数字显示在左边，不足10位右边补空格


- 下面代码中变量var1 的长度为4个字符 
  var1 =  'a\nb' 
  
  
- 代码的注释，不影响代码的执行，项目开发中我们不写没关系 

  
  
```



<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

### 不定项选择

```python
- 下面格式化字符串的代码，哪些是错误的  (bc)

A) 'my name is %s' % 'Mike'   
B) 'my name is %d' % 'Mike'     
C) "my name is %s, I'm %s years old." % ['Mike',6]  
D) "my name is %s, I'm %s years old." % ('Mike',6)  
    
    
- 下面格式化字符串的代码，哪些是错误的  (abd)

A) 'my name is %s'.format('Mike')
B) 'my name is {}{}'.format('Mike')   
C) "my name is {}, I'm {} years old.".format('Mike',5)     
D) "my name is {}, I'm {} years old.".format(['Mike',5])  


- python 3 执行下面格式化字符串的代码，哪些是会报错的   (b)
A) "my name is {0}, I'm {1} years old.".format('Mike',5)  
B) "my name is {}, I'm {1} years old.".format('Mike',5)   
C) "I'm {1} years old, my name is {0}".format('Mike',5)   
D) "my name is {0}, his name is also {0}".format('Mike')   
E) f"my name is {'Mike'}, his name is also {{Mike}}" 
```



### 判断题
```python

- 格式化字符串 '%10d' 表示参数显示的宽度至少为10个字符，不足10个字符用空格补齐 (对) 

- 格式化字符串 '%010d' 表示参数显示的宽度至少为10个字符，不足10个字符用字符0补齐 (对) 
    
- 格式化字符串 "%06X" 表示参数以8进制显示，显示的宽度至少为10个字符，不足10个字符用字符0补齐 (错 16进制)

- 格式化字符串'%9.2f'表示参数数字的小数部分保留2位， 同时还指明了最小宽度是9，不足补空格。    (对) 

- '{:<10}'.format(8) 表示最小宽度是10，同时数字显示在左边，不足10位右边补空格 (对) 


- 下面代码中变量var1 的长度为4个字符  (错)
  var1 =  'a\nb' 
  
  
- 代码的注释，不影响代码的执行，项目开发中我们不写没关系  (错)

  
  
```

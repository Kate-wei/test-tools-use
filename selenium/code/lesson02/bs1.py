# coding=utf8

# 获取html内容字符串，进行分析
with open('bs1.html') as f:
    html_doc = f.read()

# 导入 bs4
from bs4 import BeautifulSoup

# 指定用html5lib来解析html文档
soup = BeautifulSoup(html_doc.decode('utf8'), "html5lib")

# print(soup.prettify())

# 查找 标签名为title的第一个元素 ，
# 返回一个 <class 'bs4.element.Tag'> 实例
# print soup.title




# # 获取tag名
# print soup.title.name
#
# # 获取 tag内容
# print soup.title.string



# # 获取 tag 的父节点tag
# print soup.title.parent
# print soup.title.parent.name



# # 查找标签名为p的第一个元素 ，
# # 返回一个 <class 'bs4.element.Tag'> 实例
# print soup.p
#
# # 获取元素的属性值
# print soup.p['style']
# print soup.p.get('style')



# # 获取元素的text内容
# # 并将结果作为Unicode字符串返回:
# print soup.p.get_text()
# # 也可以
# print soup.p.string

# # 两者的区别是
# # string 要求 当前的tag对象只有一个 包含文字内容的 类型子节点，
# # 如果有多个就不行,比如
# print soup.div.string
# # 但是get_text()却可以
# print soup.div.get_text("|")
# # 也可以使用contents方法
# # print soup.div.contents




#   是查找标签名为a的第一个元素
# print soup.a

# # 查找所有的 a元素
# print soup.find_all('a')

# # 根据id属性查找a元素
# print soup.find('a',id="link3")
#
# # 根据其他html属性查找 a元素
# print soup.find('a',href="http://example.com/lacie")

# 查找所有div 的子元素中的 a tag
baiduDiv = soup.find('div',id="d1")
print baiduDiv.find_all('a')
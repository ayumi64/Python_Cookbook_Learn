"""
问题
你用 lambda 定义了一个匿名函数，并想在定义时捕获到某些变量的值。 
解决方案
先看下下面代码的效果
"""

x = 10
a = lambda y : x + y
x = 20
b = lambda y : x + y

#  lambda 表达式中的 x 是一个自由变量，在运行时绑定值
print(a(10))
x=1
print(a(10))
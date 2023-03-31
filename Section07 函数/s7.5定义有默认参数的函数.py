"""
问题
你想定义一个函数或者方法，它的一个或多个参数是可选的并且有一个默认值。
解决方案
定义一个有可选参数的函数是非常简单的，直接在函数定义中给参数指定一个默 认值，并放到参数列表最后就行了。例如:
"""

def spam(a, b=42):
    print(a, b)

spam(1)
spam(1, 3)

# 如果默认参数是一个可修改的容器比如一个列表、集合或者字典，可以使用 None 作为默认值

def spam(a, b=None):
    if b is None:
        b = []

_no_value = object()

def spam(a, b=_no_value): 
    if b is _no_value:
        print('No b value supplied')

spam(1) # b = _no_value
spam(1, _no_value)
spam(1, None)  # b = None

"""
讨论
定义带默认值参数的函数是很简单的，但绝不仅仅只是这个，还有一些东西在这里 也深入讨论下。
首先，默认参数的值仅仅在函数定义的时候赋值一次。试着运行下面这个例子:
"""

x=42
# 在函数定义 的时候就已经确定了它的默认值了。

def spam(a, b=x):
    print(a, b)

spam(2) # 42

x = 23
spam(2) # 42

## 千万不要像下面这样写代码:

def spam(a, b=[]): 
    print(b)
    return b

x = spam(5)
x # []

x.append(99)
print(x) # 99
spam(5) # 99 


def spam(a, b=None):
    # 不要写成 if not b 因为b=[]也会true
    if b is None:
        b = []

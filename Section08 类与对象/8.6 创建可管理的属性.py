"""
问题
你想给某个实例 attribute 增加除访问与修改之外的其他处理逻辑，比如类型检查 或合法性验证。
解决方案
自定义某个属性的一种简单方法是将它定义为一个 property。
"""

class Person:
    def __init__(self, first_name) -> None:
        self.first_name = first_name
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value
    
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

"""
上述代码中有三个相关联的方法，这三个方法的名字都必须一样。
第一个方法是一 个 getter 函数，它使得 first_name 成为一个属性。
其他两个方法给 first_name 属 性添加了 setter 和 deleter 函数。
需要强调的是只有在 first_name 属性被创建后， 后面的两个装饰器 @first_name.setter 和 @first_name.deleter 才能被定义。
"""

a = Person('Guido')
print(a.first_name)
# a.first_name = 42
# del a.first_name

# property 的一个关键特征是它看上去跟普通的 attribute 没什么两样，但是访问它 的时候会自动触发 getter 、setter 和 deleter 方法。

# 一个 property 属性其实就是一系列相关绑定方法的集合。


"""
Properties 还是一种定义动态计算 attribute 的方法。这种类型的 attributes 并不会 被实际的存储，而是在需要的时候计算出来。
"""

import math

class Circle:
    
    def __init__(self, radius) -> None:
        self.radius = radius
    
    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

r = Circle(1)
print(r.diameter)
print(r.area)
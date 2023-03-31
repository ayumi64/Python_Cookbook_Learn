"""
问题
你想将一个只读属性定义成一个 property，并且只在访问的时候才会计算结果。
但 是一旦被访问后，你希望结果值被缓存起来，不用每次都去计算。
解决方案
定义一个延迟属性的一种高效方法是通过使用一个描述器类    
"""

class lazyproperty:
    def __init__(self, func):
        self.func = func
        
    def __get__(self, instance, cls): 
        if instance is None:
            return self 
        else:
            value = self.func(instance) 
            setattr(instance, self.func.__name__, value) 
            return value
        

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2
    @lazyproperty
    def perimeter(self): 
        print('Computing perimeter') 
        return 2 * math.pi * self.radius

c = Circle(4)
print(c.radius)
print(c.area)
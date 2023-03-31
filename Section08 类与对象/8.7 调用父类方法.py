"""
问题
你想在子类中调用父类的某个已经被覆盖的方法。
解决方案
为了调用父类 (超类) 的一个方法，可以使用 super() 函数    
"""

class A:
    def spam(self):
        print('A.spam')
    
class B(A):
    def sapm(self):
        print('B.spam')
        super().spam()

r = B()
r.sapm()

# super() 函数的一个常见用法是在 __init__() 方法中确保父类被正确的初始化 了:

class A:
    def __init__(self):
        self.x = 0
        
class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1

r = B()
print(r.y)

# super() 的另外一个常见用法出现在覆盖 Python 特殊方法的代码中
# 如果某个属性名以下划 线 (_) 开头，就通过 super() 调用原始的 __setattr__() ，否则的话就委派给内部的 代理对象 self._obj 去处理。
class Proxy:
    
    def __init__(self, obj):
        self._obj = obj
    # Delegate attribute lookup to internal obj
    def __getattr__(self, name): 
        return getattr(self._obj, name)
    # Delegate attribute assignment
    def __setattr__(self, name, value): 
        if name.startswith('_'):
            super().__setattr__(name, value) # Call original __setattr__ 
        else:
            setattr(self._obj, name, value)

"""对于你 定义的每一个类，Python 会计算出一个所谓的方法解析顺序 (MRO) 列表。这个 MRO 列表就是一个简单的所有基类的线性顺序表。"""


class A:
    def spam(self):
        print('A.spamm') 
        super().spam()

# a= A()
# a.spam() # AttributeError: 'super' object has no attribute 'spam'

class B:
    def spam(self):
        print('B.spamm')

class C(A, B):
    pass

c = C()
c.spam()

print(C.__mro__)
"""
(<class '__main__.C'>, 
<class '__main__.A'>, 
<class '__main__.B'>, 
<class 'object'>)
"""
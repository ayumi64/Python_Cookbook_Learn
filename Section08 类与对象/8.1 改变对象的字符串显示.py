"""
问题
你想改变对象实例的打印或显示输出，让它们更具可读性。
解决方案
要改变一个实例的字符串表示，可重新定义它的 __str__() 和 __repr__() 方法。
"""

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return 'object Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self) -> str:
        return 'str:({0.x!s}, {0.y!s})'.format(self)

"""
__repr__() 方法返回一个实例的代码表示形式，通常用来重新构造这个实例。 
内置的 repr() 函数返回这个字符串，跟我们使用交互式解释器显示的值是一样的。 
__str__() 方法将实例转换为一个字符串，使用 str() 或 print() 函数会输出这个字 符串。
"""

"""
python 中，repr是一个特殊的方法，用于将类（class）的一个实例表示为字符串。 repr即represent
简言之，就是 对象的字符串表示 。 对象通过 __repr__ 方法转化为字符串后，该字符串又可以用来创建该对象。 
在类中定义了 __repr__ 方法后， 可以通过python内置的 repr () 函数来调用。 常用于debug。
"""

p = Pair(3, 4)
print(p)
print(repr(p))
print(p.__repr__)
print(p.__str__)

# Before Override __repr__ & __str__
"""
<__main__.Pair object at 0x109a4cfd0>
<__main__.Pair object at 0x109a4cfd0>
<method-wrapper '__repr__' of Pair object at 0x10ce97790>
<method-wrapper '__str__' of Pair object at 0x10ce97790>
"""

# After Overrride ...
"""
(3, 4)
Pair(3, 4)
<bound method Pair.__repr__ of Pair(3, 4)>
<bound method Pair.__str__ of Pair(3, 4)>
"""

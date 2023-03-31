"""
问题
你想创建一个新的拥有一些额外功能的实例属性类型，比如类型检查。
解决方案
如果你想创建一个全新的实例属性，可以通过一个描述器类的形式来定义它的功 能。
"""

class Integer:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        del instance.__dict__[self.name]

"""
一个描述器就是一个实现了三个核心的属性访问操作 (get, set, delete) 的类，分别 为 __get__() 、__set__() 和 __delete__() 这三个特殊的方法。
这些方法接受一个实 例作为输入，之后相应的操作实例底层的字典。

通过定义一个描述器，你可以在底层捕获核心的实例操作 (get, set, delete)，并且 可完全自定义它们的行为。
这是一个强大的工具，有了它你可以实现很多高级功能，并 且它也是很多高级库和框架中的重要工具之一。

描述器的一个比较困惑的地方是它只能在类级别被定义，而不能为每个实例单独 定义。
"""
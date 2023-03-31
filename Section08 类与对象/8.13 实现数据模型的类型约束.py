"""
问题
你想定义某些在属性赋值上面有限制的数据结构。
解决方案
在这个问题中，你需要在对某些实例属性赋值时进行检查。
所以你要自定义属性赋值函数，这种情况下最好使用描述器。

"""


# 类装饰器

# Specialized descriptors

# Decorator for applying type checking
def Typed(expected_type, cls=None): 
    if cls is None:

        return lambda cls: Typed(expected_type, cls) 
    super_set = cls.__set__
    
    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError('expected ' + str(expected_type)) 
        super_set(self, instance, value)
        cls.__set__ = __set__ 
        return cls


@Typed(int)
class Integer(Descriptor):
    pass

@Unsigned
class UnsignedInteger(Integer): 
    pass
"""
问题
你想实现一个自定义的类来模拟内置的容器类功能，比如列表和字典。但是你不确 定到底要实现哪些方法。
解决方案
collections 定义了很多抽象基类，当你想自定义容器类的时候它们会非常有用。 
"""

# 比如你想让你的类支持迭代，那就让你的类继承 collections.Iterable 即可

import collections
from contextlib import _T_co
from typing import Iterator

class A(collections.Iterable):

    def __iter__(self) -> Iterator[_T_co]:
        return super().__iter__()


# 不过你需要实现 collections.Iterable 所有的抽象方法，否则会报错:
a = A()


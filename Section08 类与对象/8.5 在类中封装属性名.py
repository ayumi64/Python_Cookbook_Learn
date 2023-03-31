"""
问题
你想封装类的实例上面的“私有”数据，但是 Python 语言并没有访问控制。
解决方案
Python 程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命 名规约来达到这个效果。第一个约定是任何以单下划线 _ 开头的名字都应该是内部实 现。
"""

class A:
    def __init__(self) -> None:
        self._internal = 0
        self.public = 1
        
    def public_method(self):
        pass
    
    def _internal_method(self):
        pass
    
    
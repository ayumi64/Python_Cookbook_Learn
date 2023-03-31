"""
问题
你的程序要创建大量 (可能上百万) 的对象，导致占用很大的内存。 
解决方案
对于主要是用来当成简单的数据结构的类而言，你可以通过给类添加 __slots__ 属性来极大的减少实例所占的内存。
"""

class Date:
    __slots__ = ['year', 'month', 'day'] 
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

#当你定义 __slots__ 后，Python 就会为实例使用一种更加紧凑的内部表示。实 例通过一个很小的固定大小的数组来构建，而不是为每个实例定义一个字典
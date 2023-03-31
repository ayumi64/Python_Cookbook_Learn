"""
问题
你想要扩展函数中的某个闭包，允许它能访问和修改函数的内部变量。
解决方案
通常来讲，闭包的内部变量对于外界来讲是完全隐藏的。但是，你可以通过编写访 问函数并将其作为函数属性绑定到闭包上来实现这个目的
"""

def sample():
    n = 0
    def func():
        print('n=', n)
    
    def get_n():
        return n
    
    def set_n(value):
        nonlocal n
        n = value
    
    func.get_n = get_n
    func.set_n = set_n
    
    return func

f = sample()
f()
f.set_n(10)
f()


import sys

class ClosureInsatance:
    def __init__(self, locals=None) -> None:
        if locals is None:
            locals = sys._getframe(1).f_locals
            
        self.__dict__.update((key, value) for key, value in locals.items()
                             if callable(value))
        
    def __len__(self):
        return self.__dict__['__len__']()
    

def Stack():
    items = []
    def push(item):
        items.append(item)
    
    def pop():
        return items.pop()
    
    def __len__():
        return len(items)
    
    return ClosureInsatance()

s = Stack()
print(s)
print(s.push(10))
print(s.push(10))
print(s.push(20))
print(len(s))
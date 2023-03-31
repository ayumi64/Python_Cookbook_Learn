"""
问题
你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不 一样。
解决方案
如果你想实现一种新的迭代模式，使用一个生成器函数来定义它。下面是一个生产 某个范围内浮点数的生成器:

"""


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

# for n in frange(0, 4 ,0.5):
#     print(n)

# print(list(frange(0, 4, 0.5)))


""" 
讨论
一个函数中需要有一个 yield 语句即可将其转换为一个生成器。跟普通函数不同 的是，
生成器只能用于迭代操作。下面是一个实验，向你展示这样的函数底层工作机制:
"""

def countdown(m):
    print('Starting to count from', m)

    while m > 0:
        yield m
        m -= 1
    print('Done!')

def print_m():
    c = countdown(3)
    print(next(c))
    print(next(c))
    print(next(c))

print_m()

# def yield_func(c):
#     try:
#         while True:
#             next(c)
#     except StopIteration:
#         pass

"""
问题
你想得到一个由迭代器生成的切片对象，但是标准切片操作并不能做到。
解决方案
函数 itertools.islice() 正好适用于在迭代器和生成器上做切片操作。
"""

def count(n):
    while True:
        yield n
        n += 1

c = count(11)
c[10:20]
# TypeError: 'generator' object is not subscriptable

import itertools

for x in itertools.islice(c, 10, 20):
    print(x)

# print(c)
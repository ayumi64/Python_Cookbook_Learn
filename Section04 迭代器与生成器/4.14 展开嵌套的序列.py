"""
问题
你想将一个多层嵌套的序列展开成一个单层列表
解决方案
可以写一个包含 yield from 语句的递归生成器来轻松解决这个问题。比如:
"""

from collections.abc import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
print(items)
for x in flatten(items):
    print(x)

for y in items:
    print(y)
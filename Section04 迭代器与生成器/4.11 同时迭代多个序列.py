"""
问题
你想同时迭代多个序列，每次分别从一个序列中取一个元素。
解决方案
为了同时迭代多个序列，使用 zip() 函数。比如:
"""

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99] 
for x, y in zip(xpts, ypts):
    print(x, y)

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
    print(i)

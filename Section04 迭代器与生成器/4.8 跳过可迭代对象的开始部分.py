"""
问题
你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们。
解决方案
itertools 模块中有一些函数可以完成这个任务。首先介绍的是 itertools. dropwhile() 函数。
使用时，你给它传递一个函数对象和一个可迭代对象。它会返回一个迭代器对象，丢弃原有序列中直到函数返回 Flase 之前的所有元素，然后返回后 面所有元素。
为了演示，假定你在读取一个开始部分是几行注释的源文件。
"""

with open('Course/Python_Cookbook/somefile.txt') as f:
    for line in f:
        print(line, end='')

# 如果你想跳过开始部分的注释行的话，可以这样做:

from itertools import dropwhile

with open('Course/Python_Cookbook/somefile.txt') as f:
    for line in dropwhile(lambda line: line.startswith('一'), f):
        print(line, end='')

from itertools import islice

items = ['a', 'b', 'c', 1, 4, 10, 15]

# 如果你已经明确知道了要跳 过的元素的个数的话
for x in islice(items, 1, None):
    print(x)


v1 = range(10)
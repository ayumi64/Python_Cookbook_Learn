"""
问题
你想为 sort() 操作创建一个很短的回调函数，但又不想用 def 去写一个单行函 数，而是希望通过某个快捷方式以内联方式来创建这个函数。
解决方案
当一些函数很简单，仅仅只是计算一个表达式的值的时候，就可以使用 lambda 表 达式来代替了
"""

add = lambda x, y : x + y

print(add(2, 3))
print(add("hello", "world"))

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
sorted(names, key=lambda name: name.split()[-1].lower())
print(sorted(names, key=lambda name: name.split()[-1].lower()))
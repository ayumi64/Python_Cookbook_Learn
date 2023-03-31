"""
问题
你想使用 Unix Shell 中常用的通配符 (比如 *.py , Dat[0-9]*.csv 等) 去匹配文 本字符串
解决方案
fnmatch 模块提供了两个函数——fnmatch() 和 fnmatchcase() ，可以用来实现 这样的匹配。用法如下:
"""

from fnmatch import fnmatch, fnmatchcase

fnmatch('foo,txt', '*.txt')

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
print(fnmatch('foo.txt', '*.TXT')) # 操作系统不一样 表现也不一样

print(fnmatchcase('foo.txt', '*.TXT'))


addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

a = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(a)

b = [addr for addr in addresses if fnmatchcase(addr, '* W *')]
print(b)

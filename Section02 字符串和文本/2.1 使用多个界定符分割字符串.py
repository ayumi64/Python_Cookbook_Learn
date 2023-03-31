"""
问题:
你需要将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定 的。
解决方案:
string 对象的 split() 方法只适应于非常简单的字符串分割情形，
它并不允许有 多个分隔符或者是分隔符周围不确定的空格。
当你需要更加灵活的切割字符串的时候， 最好使用 re.split() 方法:

"""

line = 'asdf fjdk; afed, fjek:asdf, foo'

import re

line = re.split(r'[;, : \s]\s*', line)

print(line)


line = 'asdf fjdk; afed, fjek:asdf, foo'

# 保留分隔符

line = re.split(r'(;|,|:|\s)\s*', line)

print(line)

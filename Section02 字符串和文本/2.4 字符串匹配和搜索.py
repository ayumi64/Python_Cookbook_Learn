"""
问题
你想匹配或者搜索特定模式的文本
解决方案
如果你想匹配的是字面字符串，那么你通常只需要调用基本字符串方法就行，
比如 str.find(), str.endswith(), str.startswith() 或者类似的方法:
"""

text = 'yeah, but no, but yeah, but no, but yeah'


a = text.startswith('yeah')
print(a)

a = text.endswith('yeah')
print(a)

a = text.find('no')
print(a)


"""
对于复杂的匹配需要使用正则表达式和 re 模块。为了解释正则表达式的基本原理，
假设你想匹配数字格式的日期字符串比如 11/27/2012 ，你可以这样做:
"""

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

# Simple matching: \d+ means match one or more digits

if re.match(r'\d+/\d+', text1):
    print('yes')
else:
    print('no')

# 如果你想使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对 象。比如:

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
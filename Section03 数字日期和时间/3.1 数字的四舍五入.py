"""
问题
你想对浮点数执行指定精度的舍入运算。
解决方案
对于简单的舍入运算，使用内置的 round(value, ndigits) 函数即可。
"""

a = round(1.232, 2)
print(a)

a = round(1.237, 2)
print(a)

a = round(1.5,0)
print(a)

a = round(162778, -3)
print(a)

x = 1.23456
print(format(x, '0.2f'))

print('value is {:0.3f}'.format(x))
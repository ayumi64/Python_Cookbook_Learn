
"""
问题
你需要对浮点数执行精确的计算操作，并且不希望有任何小误差的出现。
解决方案
浮点数的一个普遍问题是它们并不能精确的表示十进制数。
并且，即使是最简单的 数学运算也会产生小的误差
"""

a = 4.2 
b = 2.1

print(a + b)

print((a+b) == 6.3)


from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')

print(a + b)

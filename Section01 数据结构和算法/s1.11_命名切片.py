#   你的程序已经出现一大堆已无法直视的硬编码切片下标，然后你想清理下代码。

record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)

SHARES = slice(20, 23)

"""
slice()语法：slice(start, end, step)
"""
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3) # 在位置0启动，位置8结束，步进值为3
print("slice:", a[x])
print(x.step)
s = 'Hello'
y = x.indices(len(s))
print(y) # (0,3,1)


print(SHARES)  # slice(20, 23, None)
PRICE = slice(31, 37)
print(SHARES, PRICE)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)
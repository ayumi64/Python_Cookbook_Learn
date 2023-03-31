p = (4, 5)
x , y = p
print(x) # 4
print(y) # 5

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)
name, shares, price, (year, month, day) = data
print(year, month, day)

s = 'HELLO'
a, b, c, d, e= s
print(c) # L

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)  # 50
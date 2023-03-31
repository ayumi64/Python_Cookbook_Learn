# 怎样在两个字典中寻寻找相同点(比如相同的键、相同的值等等)?

a = {
    'x': 1,
    'y': 2,
    'z': 3}

b = {
    'w': 10,
    'x': 11,
    'y': 2}

x = a.keys() & b.keys()  # {'y', 'x'}
y = a.keys() - b.keys() # {z}
z = a.items() & b.items()
print(x, y, z)

m = {key: a[key] for key in a.keys() - {'z', 'w'}}  # {'y': 2, 'x': 1}
print(m)

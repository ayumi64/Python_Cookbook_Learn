# 怎样实现一个键对应多个值的字典(也叫 multidict)?

d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

d = {}
# paris???
pairs = {
    'a': 1,
    'b': 2
}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

d = defaultdict(list)
for key, value in pairs:
    d[key.append(value)]

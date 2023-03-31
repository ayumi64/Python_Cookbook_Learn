# 怎样在一个序列上面保持元素顺序的同时消除重复的值?

# 如果序列上的值都是 hashable 类型
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))
print(set(a))


# 如果你想消除元素不可哈 希(比如 dict 类型)的序列中重复元素的话
def dedupe(items, key=None): 
    seen = set()
    for item in items:
        val = item if key is None else key(item) 
        if val not in seen:
            yield item 
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
list(dedupe(a, key=lambda d: (d['x'],d['y'])))
list(dedupe(a, key=lambda d: d['x']))

"""
问题
你想迭代遍历一个集合中元素的所有可能的排列或组合

"""

item = ['a', 'b', 'c']
from itertools import permutations

for p in permutations(item):
    print(p)

# 指定长度
for p in permutations(item, 1):
    print(p)

from itertools import combinations
for a in combinations(item, 4):
    print(a)

from itertools import combinations_with_replacement
for c in combinations_with_replacement(item, 3):
    print(c)
    
"""
当我们碰到看上去有些复杂的迭 代问题时，最好可以先去看看 itertools 模块。
如果这个问题很普遍，那么很有可能会在 里面找到解决方案!
"""

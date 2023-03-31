"""
问题
你有一系列排序序列，想将它们合并后得到一个排序序列并在上面迭代遍历。
解决方案
heapq.merge() 函数可以帮你解决这个问题。比如:
"""

import heapq

a = [1, 12, 4, 7, 10]
b = [2, 5, 6, 11]

for c in heapq.merge(a, b):
    print(c)

# with open('sorted_file_1', 'rt') as file1, open('sorted_file_2', 'rt') as file2, open('merged_file', 'wt') as outf:
#     for line in heapq.merge(file1, file2): 
#         outf.write(line)
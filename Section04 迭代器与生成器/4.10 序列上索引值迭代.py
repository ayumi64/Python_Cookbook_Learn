
"""
问题
你想在迭代一个序列的同时跟踪正在被处理的元素索引。
解决方案
内置的 enumerate() 函数可以很好的解决这个问题
"""


from collections import defaultdict


my_l = ['a', 'b', 'c']

for idx, val in enumerate(my_l):
    print(idx, val)

# 为了按传统行号输出 (行号从 1 开始)，你可以传递一个开始参数
for idx, val in enumerate(my_l, 1):
    print(idx, val)


def parse_data(filename):

    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[0])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))

filename = r"/Users/sonic/ProjectA/Python/Course/Python_Cookbook/somefile.txt"

# parse_data(filename)


word_summary = defaultdict(list) 

with open(filename, 'r') as f:
    lines = f.readlines()
for idx, line in enumerate(lines):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()] 
    for word in words:
        word_summary[word].append(idx)




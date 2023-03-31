# 在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录?

# 下面的代码 在多行上面做简单的文本匹配，并返回匹配所在行的最后 N 行:
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open(r'Course/Python_Cookbook/somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
                print(line, end='')
                print('-'*20)

# 使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并 且这个队列已满的时候，最老的元素会自动被移除掉。

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)  # deque([1, 2, 3], maxlen=3)
deque([1, 2, 3], maxlen=3)
q.append(4)
print(q)  # deque([2, 3, 4], maxlen=3)

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4) 
print(q)  # deque([4, 1, 2, 3])
q.pop()
print(q)  # deque([4, 1, 2])
q.popleft()
print(q)

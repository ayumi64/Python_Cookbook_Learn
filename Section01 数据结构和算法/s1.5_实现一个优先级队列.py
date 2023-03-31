# 怎样实现一个按优先级排序的队列?并且在这个队列上面每次 pop 操作总是返回 优先级最高的那个元素
import heapq


# 下面的类利用 heapq 模块实现了一个简单的优先级队列:

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        # 优先级为负 数的目的是使得元素按照优先级从高到低排序。这个跟普通的按优先级从低到高排序 的堆排序恰巧相反。
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:

    def __init__(self, name) -> None:
        self.name = name 
    def __repr__(self):
        return 'Item({!r})'.format(self.name)
#函数 heapq.heappush() 和 heapq. heappop() 分别在队列 _queue 上插入和删除第一个元素，并且队列 _queue 保证第一 个元素拥有最高优先级
q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('grok'), 1)
q.pop()
Item('bar')
q.pop()
print(Item('foo'))



a = Item('foo')
b = Item('bar')

# print(a < b) # error
# 如果你使用元组 (priority, item) ，只要两个元素的优先级不同就能比较。
a = (1, Item('foo'))
b = (5, Item('bar'))
c = (1, Item('stu'))
print(a < b) # True
# print(a > c) # error

a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('stu'))
print(a > c)
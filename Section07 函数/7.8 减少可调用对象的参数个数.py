"""
问题
你有一个被其他 python 代码使用的 callable 对象，可能是一个回调函数或者是一 个处理器，但是它的参数太多了，导致调用时出错。
解决方案
如果需要减少某个函数的参数个数，你可以使用 functools.partial() 。partial() 函数允许你给一个或多个参数设置固定的值，减少接下来被调用时的参数个数。
"""

def spam(a, b, c, d): 
    print(a, b, c, d)
    
from functools import partial

s1 = partial(spam, 1) # a = 1
s1(2, 3, 4)
s2 = partial(spam, 1, 2, d=42) # a = 1
s2("c")


"""
第一个例子是，假设你有一个点的列表来表示 (x,y) 坐标元组。
现在假设你想以某个点为基点，根据点和基点之间的距离来排序所有的这些点。
列 表的 sort() 方法接受一个关键字参数来自定义排序逻辑，但是它只能接受一个单个参 数的
函数 (distance() 很明显是不符合条件的)。现在我们可以通过使用 partial() 来解 决这个问题:
"""
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

import math
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

pt = (4, 3)
points.sort(key=partial(distance, pt))
# points.sort()
print(points)

"""
更进一步，partial() 通常被用来微调其他库函数所使用的回调函数的参数。
例 如，下面是一段代码，使用 multiprocessing 来异步计算一个结果值，
然后这个值被 传递给一个接受一个 result 值和一个可选 logging 参数的回调函数
"""

def output_result(result, log=None): 
    if log is not None:
        log.debug('Got: %r', result)
# A sample function
def add(x, y): 
    return x + y
if __name__ == '__main__': 
    import logging
    from multiprocessing import Pool 
    from functools import partial
    
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')
    
    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()


"""
partial() 通常被用来微调其他库函数所使用的回调函数的参数。
例 如，下面是一段代码，使用 multiprocessing 来异步计算一个结果值，
然后这个值被 传递给一个接受一个 result 值和一个可选 logging 参数的回调函数:
"""

def output_result(result, log=None): 
    if log is not None:
        log.debug('Got: %r', result)
# A sample function
def add(x, y): 
    return x + y

if __name__ == '__main__': 
    import logging
    from multiprocessing import Pool 
    from functools import partial
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')
    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()
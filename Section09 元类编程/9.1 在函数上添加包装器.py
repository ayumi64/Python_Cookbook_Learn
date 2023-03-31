"""
问题
你想在函数上添加一个包装器，增加额外的操作处理 (比如日志、计时等)。
"""

import time
from functools import wraps

def timethis(func):
    
    # @wraps(func) 注解是很重要的，它能保留原始函数的元数据
    # @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()

        print(func.__name__, t2 - t1)
        
    return wrapper

@timethis
def func(n): # func = timethis(func(n))
    for i in range(n):
        pass
        
func(3)

func.__wrapped__(3)

print(func.__name__, func.__doc__, func.__annotations__)

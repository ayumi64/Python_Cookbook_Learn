import time
from functools import wraps

def param(method):
        
    def timethis(func):

        # @wraps(func) 注解是很重要的，它能保留原始函数的元数据
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("This is %s" % method)
            t1 = time.time()
            func(*args, **kwargs)
            t2 = time.time()

            print(func.__name__, t2 - t1)

        return wrapper
    
    return timethis
    

@param("For")
def func_for(n):  # func = timethis(func(n))
    for i in range(n):
        print(i)
        
@param("While")
def func_while(n):  # func = timethis(func(n))
    i = 0
    while i <= n:
        print(i)
        i += 1



func_for(3)
func_while(3)
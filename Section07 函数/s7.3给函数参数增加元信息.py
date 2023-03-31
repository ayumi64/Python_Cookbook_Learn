# 你写好了一个函数，然后想为这个函数的参数增加一些额外的信息，这样的话其他 使用者就能清楚的知道这个函数应该怎么使用。

def add(x:int, y:int) -> int:
    return x + y

help(add)

# 函数注解只存储在函数的 __annotations__ 属性中。例如:
add.__annotations__
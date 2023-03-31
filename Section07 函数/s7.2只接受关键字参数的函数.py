# 你希望函数的某些参数强制使用关键字参数传递

def recv(maxsize, *, block):
    'Receives a message'
    pass


recv(1024, True)  # TypeError 
recv(1024, block=True) # Ok


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m 
    return m


minimum(1, 5, 2, -5, 10, clip=0)  # Returns 0
minimum(1, 5, 2, -5, 10)  # Returns 0

# 很多情况下，使用强制关键字参数会比使用位置参数表意更加清晰，程序也更加具 有可读性。例如，考虑下如下一个函数调用:
msg = recv(1024, False)
# 如果调用者对 recv 函数并不是很熟悉，那他肯定不明白那个 False 参数到底来干嘛用的。但是，如果代码变成下面这样子的话就清楚多了:
msg = recv(1024, block=False)
# 另外，使用强制关键字参数也会比使用 **kwargs 参数更好，因为在使用函数 help的时候输出也会更容易理解:

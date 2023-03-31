"""
问题
你想让你的对象支持上下文管理协议 (with 语句)。
解决方案
为了让一个对象兼容 with 语句，你需要实现 __enter__() 和 __exit__() 方法
"""

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:

    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None


    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected') 
        self.sock = socket(self.family, self.type) 
        self.sock.connect(self.address)
        return self.sock
        
    def __exit__(self, exc_ty, exc_val, tb): 
        self.sock.close()
        self.sock = None

conn = LazyConnection(('www.python.org'), 80)

with conn as s:
    s.send()
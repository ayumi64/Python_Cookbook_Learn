import os, sys

"""
问题
你需要写一个涉及到文件查找操作的脚本，比如对日志归档文件的重命名工具， 
你不想在Python脚本中调用shell，或者你要实现一些shell不能做的功能。

解决方案
查找文件，可使用 os.walk() 函数，传一个顶级目录名给它。 
下面是一个例子，查找特定的文件名并答应所有符合条件的文件全路径：
"""

#!/usr/bin/env python3.3

def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))


if __name__ == '__main__':
    findfile(sys.argv[1], sys.argv[2])

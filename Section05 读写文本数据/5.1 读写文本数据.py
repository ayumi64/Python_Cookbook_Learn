"""
问题
你需要读写各种不同编码的文本数据，比如 ASCII，UTF-8 或 UTF-16 编码等。
解决方案
使用带有 rt 模式的 open() 函数读取文本文件。如下所示
"""

with open('somefile.txt', 'rt') as f:
    data = f.read()

with open('somefile.txt', 'rt') as f:
    for line in f:
        pass

with open('somefile.txt', 'wt') as f:
    f.write('text1')
    f.write('text2')

# with 语句给被使用到的文件创建了一个上下文环境，但 with 控制块结束时， 文件会自动关闭。你也可以不使用 with 语句，但是这时候你就必须记得手动关闭文件
f = open('somefile.txt', 'rt')
data = f.read()
f.close()

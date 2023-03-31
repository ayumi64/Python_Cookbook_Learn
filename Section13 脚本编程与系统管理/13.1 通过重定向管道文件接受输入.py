"""
问题
你希望你的脚本接受任何用户认为最简单的输入方式。
包括将命令行的输出通过管道传递给该脚本、 重定向文件到该脚本，或在命令行中传递一个文件名或文件名列表给该脚本。

解决方案
Python内置的 fileinput 模块让这个变得简单。如果你有一个下面这样的脚本：
"""

import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')
        

"""
问题
你的程序如何能够解析命令行选项（位于sys.argv中）

解决方案
argparse 模块可被用来解析命令行选项。下面一个简单例子演示了最基本的用法：
"""


# search.py
'''
Hypothetical command-line tool for searching a collection of
files for one or more text patterns.
'''
import argparse
parser = argparse.ArgumentParser(description='Search some files')

parser.add_argument(dest='filenames', metavar='filename', nargs='*')

parser.add_argument('-p', '--pat', metavar='pattern', required=True,
                    dest='patterns', action='append',
                    help='text pattern to search for')

parser.add_argument('-v', dest='verbose', action='store_true',
                    help='verbose mode')

parser.add_argument('-o', dest='outfile', action='store',
                    help='output file')

parser.add_argument('--speed', dest='speed', action='store',
                    choices={'slow', 'fast'}, default='slow',
                    help='search speed')

args = parser.parse_args()

# Output the collected arguments
print(args.filenames)
print(args.patterns)
print(args.verbose)
print(args.outfile)
print(args.speed)


"""
该程序定义了一个如下使用的命令行解析器：

bash % python3 search.py -h
usage: search.py [-h] [-p pattern] [-v] [-o OUTFILE] [--speed {slow,fast}]
            [filename [filename ...]]

Search some files

positional arguments:
filename

optional arguments:
-h, --help            show this help message and exit
-p pattern, --pat pattern
                text pattern to search for
-v                    verbose mode
-o OUTFILE            output file
--speed {slow,fast}   search speed
    """


"""
argparse 模块是标准库中最大的模块之一，拥有大量的配置选项。 本节只是演示了其中最基础的一些特性，帮助你入门。

为了解析命令行选项，你首先要创建一个 ArgumentParser 实例， 并使用 add_argument() 方法声明你想要支持的选项。
在每个 add_argument() 调用中，dest 参数指定解析结果被指派给属性的名字。 metavar 参数被用来生成帮助信息。
action 参数指定跟属性对应的处理逻辑， 通常的值为 store ,被用来存储某个值或将多个参数值收集到一个列表中。 
下面的参数收集所有剩余的命令行参数到一个列表中。在本例中它被用来构造一个文件名列表：
"""
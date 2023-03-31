"""
问题
你想向标准错误打印一条消息并返回某个非零状态码来终止程序运行

解决方案
你有一个程序像下面这样终止，抛出一个 SystemExit 异常，使用错误消息作为参数。
"""

import sys
sys.stderr.write('It failed!\n')
raise SystemExit(1)

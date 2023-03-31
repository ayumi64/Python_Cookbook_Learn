"""
问题
你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL Scheme 等等。
解决方案
检查字符串开头或结尾的一个简单方法是使用 str.startswith() 或者是 str. endswith() 方法。比如:
"""

filename = 'span.txt'

print(filename.endswith('.txt'))

print(filename.startswith('file:'))



from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http', 'https', 'ftp')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


choices = ('http:', 'ftp:')
url = 'http://www.python.org'
url.startswith(choices)

import re

url = 'http://www.python.org'
print(re.match('http', url))

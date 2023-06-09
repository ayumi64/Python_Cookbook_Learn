"""
问题
你有一个除 __init__() 方法外只定义了一个方法的类。为了简化代码，你想将它 转换成一个函数。
解决方案
大多数情况下，可以使用闭包来将单个方法的类转换成函数。举个例子，下面示例 中的类允许使用者根据某个模板方案来获取到 URL 链接地址。
"""

from urllib.request import urlopen

class UrlTemplate:
    def __init__(self, template):
        self.template = template 
        
def open(self, **kwargs):
    return urlopen(self.template.format_map(kwargs))

# Example use. Download stock data from yahoo
yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f= ,→{fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'): 
    print(line.decode('utf-8'))
    

def urltemplate(template): 
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs)) 
    return opener
# Example use
yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f= ,→{fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'): 
    print(line.decode('utf-8'))
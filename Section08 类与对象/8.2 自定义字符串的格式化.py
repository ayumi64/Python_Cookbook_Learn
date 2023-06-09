"""
问题
你想通过 format() 函数和字符串方法使得一个对象能支持自定义的格式化。
解决方案
为了自定义字符串的格式化，我们需要在类上面定义 __format__() 方法。
"""

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d = Date(2012, 12, 31)
print(format(d))
print(format(d, 'dmy'))
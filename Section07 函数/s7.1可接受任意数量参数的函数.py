# 你想构造一个可接受任意数量参数的函数。

def f(*args, **kwargs):
    pass

def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))
# rest 是由所有其他位置参数组成的元组
avg(1, 2, 3)


import html

def make_element(name, value, **attrs):
    keyvals = ['%s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element

make_element('item', 'Albatross', size='large', quantity=6)

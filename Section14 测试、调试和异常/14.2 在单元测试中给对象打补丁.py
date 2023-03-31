"""
问题
你写的单元测试中需要给指定的对象打补丁， 用来断言它们在测试中的期望行为（比如，断言被调用时的参数个数，访问指定的属性等）。

解决方案
unittest.mock.patch() 函数可被用来解决这个问题。 patch() 还可被用作一个装饰器、上下文管理器或单独使用，尽管并不常见。 例如，下面是一个将它当做装饰器使用的例子
"""

from unittest.mock import patch
import example

@patch('example.func')
def test_1(x, mock_func):
    example.func(x)
    mock_func.assert_called_with(x)
    
if __name__ == '__main__':
    test_1()

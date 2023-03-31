"""
问题
你想写个测试用例来准确的判断某个异常是否被抛出。

解决方案
对于异常的测试可使用 assertRaises() 方法。 
例如，如果你想测试某个函数抛出了 ValueError 异常，像下面这样写：
"""

import unittest

def parse_int(s):
    return int(s)

class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, 'N/A')

import errno

class TestIO(unittest.TestCase):
    def test_file_not_found(self):
        try:
            f = open('Course/Python_Cookbook/somefile.txt')
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)
        else:
            self.fail('IOError not raise')

if __name__ == '__main__':
    T = TestConversion()
    T.test_bad_int()
"""
问题
你的程序中有个方法会输出到标准输出中（sys.stdout）。也就是说它会将文本打印到屏幕上面。
你想写个测试来证明它，给定一个输入，相应的输出能正常显示出来。

解决方案
使用 unittest.mock 模块中的 patch() 函数， 使用起来非常简单，可以为单个测试模拟 sys.stdout 然后回滚， 
并且不产生大量的临时变量或在测试用例直接暴露状态变量。    
"""

def urlprint(protocol, host, domain):
    url = '{}://{}.{}'.format(protocol, host, domain)
    print(url)

# 默认情况下内置的 print 函数会将输出发送到 sys.stdout
urlprint('http', 'baidu', 'wenku.com')

from io import StringIO
from unittest import TestCase
from unittest.mock import patch

class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'baidu'
        domain = 'yun.com'
        expected_url = 'http://baidu.wenku.com'
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)

if __name__ == '__main__':
    test = TestURLPrint()
    test.test_url_gets_to_stdout()

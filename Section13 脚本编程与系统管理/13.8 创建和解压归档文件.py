"""
问题
你需要创建或解压常见格式的归档文件（比如.tar, .tgz或.zip）

解决方案
shutil 模块拥有两个函数—— make_archive() 和 unpack_archive() 可派上用场。
"""


# >> > import shutil
# >> > shutil.unpack_archive('Python-3.3.0.tgz')

# >> > shutil.make_archive('py33', 'zip', 'Python-3.3.0')
# '/Users/beazley/Downloads/py33.zip'

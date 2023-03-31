"""
问题
你写了个脚本，运行时需要一个密码。此脚本是交互式的，因此不能将密码在脚本中硬编码， 而是需要弹出一个密码输入提示，让用户自己输入。

解决方案
这时候Python的 getpass 模块正是你所需要的。你可以让你很轻松的弹出密码输入提示， 并且不会在用户终端回显密码。下面是具体代码：
"""

import getpass

user = getpass.getuser()
passwd = getpass.getpass()


def svc_login():
    pass

if svc_login(user, passwd):    # You must write svc_login()
   print('Yay!')
else:
   print('Boo!')

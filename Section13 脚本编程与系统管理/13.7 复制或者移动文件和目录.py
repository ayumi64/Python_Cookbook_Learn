"""
问题
你想要复制或移动文件和目录，但是又不想调用shell命令。

解决方案
shutil 模块有很多便捷的函数可以复制文件和目录。使用起来非常简单，比如：
"""

import shutil

# Copy src to dst. (cp src dst)
shutil.copy(src, dst)

# Copy files, but preserve metadata (cp -p src dst)
shutil.copy2(src, dst)

# Copy directory tree (cp -R src dst)
shutil.copytree(src, dst)

# Move src to dst (mv src dst)
shutil.move(src, dst)

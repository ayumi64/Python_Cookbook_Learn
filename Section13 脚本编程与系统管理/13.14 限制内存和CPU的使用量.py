"""
问题
你想对在Unix系统上面运行的程序设置内存或CPU的使用限制。

解决方案
resource 模块能同时执行这两个任务。例如，要限制CPU时间，可以像下面这样做：
"""

import signal
import resource
import os


def time_exceeded(signo, frame):
    print("Time's up!")
    raise SystemExit(1)


def set_max_runtime(seconds):
    # Install the signal handler and set a resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


if __name__ == '__main__':
    set_max_runtime(15)
    while True:
        pass

import resource


def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))

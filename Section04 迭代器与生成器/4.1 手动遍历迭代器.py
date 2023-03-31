"""
问题
你想遍历一个可迭代对象中的所有元素，但是却不想使用 for 循环。 
解决方案
为了手动的遍历可迭代对象，使用 next() 函数并在代码中捕获 StopIteration 异 常。
比如，下面的例子手动读取一个文件中的所有行:
"""


def manual_iter():
    with open('/Users/sonic/ProjectA/Python/Course/Python_Cookbook/somefile.txt') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
                print(type(f))
        except StopIteration:
            pass


        # for i in range(10):
        #     print(f.readline())



    # with open('/ect/passwd') as f:
    #     while True:
    #         line = next(f, None)
    #         if line is None:
    #             break
    #         print(line, end='')


def iterator():
    it = [1, 2, 3]  # 'list' object is not an iterator
    it = iter(it)   # iterator lize
    try:
        while True:
            line = next(it)
            print(line)
    except StopIteration:
        pass



if __name__ == '__main__':
    # manual_iter()
    iterator()

"""

>> > items = [1, 2, 3]
>> > it = iter(items)
>> > next(it)
1
>> > next(it)
2
>> > next(it)
3
>> > next(it)
Traceback(most recent call last):
  File "<stdin>", line 1, in <module >
StopIteration

"""

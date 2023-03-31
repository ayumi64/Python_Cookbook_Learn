# 你希望构造一个可以返回多个值的函数

def myf():
    return 1, 2, 3

a, b, c = myf()
print(a) # 1

x = myf()
print(x)
 
# 尽管 myfun() 看上去返回了多个值，实际上是先创建了一个元组然后返回的。
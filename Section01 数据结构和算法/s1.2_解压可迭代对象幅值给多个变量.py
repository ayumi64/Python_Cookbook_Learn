from audioop import avg
from hashlib import sha1

grades = [1,2,3,4,5]

def drop_first_last(grades):
    first, *middle, last = grades
    return middle

print(drop_first_last(grades))


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone = record
print(phone)  # ['773-555-1212', '847-555-1212']

# 你有一个公司前 8 个月销售数据的 序列，但是你想看下最近一个月数据和前面 7 个月的平均值的对比。

sales_all = [10, 8, 7, 1, 9, 5, 10, 3]

*trailing_qtrs, current_qtr = sales_all
print(current_qtr)

def ccc():
    trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
    if trailing_avg > current_qtr:
        print("大于当月")
ccc()


# 星号表达式在迭代元素为可变长元组的序列时是很有用的
# 下面是一个带有标签的元组序列:
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]
def do_foo(x, y): 
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args) 
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':') # 先line.split
print(uname,'\n',fields,'\n',homedir,'\n',sh)


record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year) # ACME, 2012

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head, tail) # 1 , 10,7...

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))

"""
# Python 中三元运算符的语法是：
# X是条件
# Y是 运算表达式1
# Z是 运算表达式2
# 如果X为True，则运行 Y ，否则运行 Z

Y if X else Z
equls:
if X:
    Y
else:
    Z
"""

"""
要看懂这个迭代需要分布解析：
第一次：

head = 1 , tail = [10,7,4,5,9]
return 1 + sum([10,7,4,5,9]) if [10,7,4,5,9] else 1
#当前结果
return 1 + sum([10,7,4,5,9])

第二次：

head = 10 , tail = [7,4,5,9]
return 10 + sum([7,4,5,9]) if [7,4,5,9] else 10
# 将此时return的内容带入第一次的 sum([10,7,4,5,9])
# 当前结果：
return 1 + ( 10 + sum([7,4,5,9]))

第三次：

head = 7 , tail = [4,5,9]
return 7 + sum([4,5,9]) if [4,5,9] else 7
# 将此时return的内容带入上一次的 sum([7,4,5,9])
# 当前结果：
return 1 + ( 10 + (7 + sum([4,5,9])))

第四次：

head = 4 , tail = [5,9]
return 4 + sum([5,9]) if [5,9] else 4
# 将此时return的内容带入上一次的 sum([4,5,9])
# 当前结果：
return 1 + ( 10 + (7 + (4 + sum([5,9]))))

第五次：

head = 5 , tail = [9]
return 5 + sum([9]) if [9] else 5
# 将此时return的内容带入上一次的 sum([5,9])
# 当前结果：
return 1 + ( 10 + (7 + (4 + (5 + sum([9])))))

第六次：
此时数组tail 已经为null ， 在执行三元运算符时，会得到False，执行else后的语句，也就是head
那么sum([9]) 就会直接返回 9

head = 9 , tail = []
return 9 + sum([]) if [] else 9
# 将此时return的内容带入上一次的 sum([9])
# 当前结果：
return 1 + ( 10 + (7 + (4 + (5 + 9))))

如此一来，就得到最终迭代的结果36。

"""



items = 1, 10
def sum(items):
  head, *tail = items
  #return 11 + 100000 if 0 else 0
  return head + sum(tail) if tail else 0
print(sum(items))  # 1

#而执行逻辑如下
#return  1 + sum([10])
#return  1 + (10 + sum([]) if [] else 0)
#return  1

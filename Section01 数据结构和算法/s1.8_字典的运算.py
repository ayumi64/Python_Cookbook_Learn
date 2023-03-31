# 怎样在数据字典中执行一些计算操作(比如求最小值、最大值、排序等等)?

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象
zip_prices = zip(prices) 
print(zip_prices)  # <zip object at
print(list(zip_prices)) # list
print(set(zip_prices))  # {} 需要注意的是 zip() 函数创建的是一个只能访问一次的迭 代器。

min_price = min(zip(prices.values(), prices.keys()))  # 'FB': 10.75
max_price = max(zip(prices.values(), prices.keys()))  # 'AAPL': 612.78,

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

print(min(prices))  # AAPL 如果你在一个字典上执行普通的数学运算，你会发现它们仅仅作用于键，而不是 值。
print(min(prices.values())) #  10.75

# 当多个实体拥有相同的值的时 候，键会决定返回结果。
print(min(zip(prices.values(), prices.keys())))
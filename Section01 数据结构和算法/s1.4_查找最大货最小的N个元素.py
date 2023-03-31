# 怎样从一个集合中获得最大或者最小的 N 个元素列表?

# heapq
import heapq
from operator import index
from tkinter import N

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums), heapq.nsmallest(5, nums))

# 排序解法
for i in range(len(nums)):
    for j in range(len(nums) - 1):
        # if nums[j] > nums[j+1]:
        if nums[j] < nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums[0:3])


portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(1, portfolio, key=lambda s:s['price'])
expensive = heapq.nlargest(1, portfolio, key=lambda s:s['shares'])

print(cheap, expensive)

#在一个集合中查找最小或最大的 N 个元素
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

heap = list(nums)
heapq.heapify(heap)
print(heap)
heapq.heappop(heap)
print(heap)

print(sorted(nums)[:3])
print(sorted(nums)[-3:])
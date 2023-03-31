# 怎样找出一个序列中出现次数最多的元素呢?

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
print(word_counts)
top_three = word_counts.most_common(3)
print(top_three)

print(word_counts['not'])

print(hash('string'))
# print(hash((1, 2, [2, 3])))  # TypeError: unhashable type: 'list'

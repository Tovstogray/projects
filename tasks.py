import operator
from heapq import nlargest


# 1---------------------------------------------------------------------------------------------------------------------
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for elem in a:
    if elem < 5:
        print(elem)

print(list(filter(lambda elem: elem < 5, a)))

print([elem for elem in a if elem < 5])
"""
# 2---------------------------------------------------------------------------------------------------------------------
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = []
for elem in a:
    if elem in b:
        result.append(elem)

result = list(filter(lambda elem: elem in b, a))

result_list = [elem for elem in a if elem in b]

result_new = list(set(a) & set(b))
"""
# 3---------------------------------------------------------------------------------------------------------------------
"""
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
result_up = print(dict(sorted(d.items(), key=operator.itemgetter(1))))
result_down = print(dict((sorted(d.items(), key=operator.itemgetter(1), reverse=True))))
"""
# 4---------------------------------------------------------------------------------------------------------------------
"""
dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}

result = {}
for d in (dict_a, dict_b, dict_c):
    result.update(d)
    
result = {**dict_a, **dict_b, **dict_c}
"""
# 5---------------------------------------------------------------------------------------------------------------------
"""
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

result = print(sorted(my_dict, key=my_dict.get, reverse=True)[:3])

result_heapq = print(nlargest(3, my_dict, key=my_dict.get))
"""
# 6---------------------------------------------------------------------------------------------------------------------
"""
print(int('ABC', 16))
"""
# 7---------------------------------------------------------------------------------------------------------------------
"""

def pascal_triangle(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]


pascal_triangle(6)
"""
# 8---------------------------------------------------------------------------------------------------------------------
"""

def is_palindrome_reversed(string):
    return string == ''.join(reversed(string))

print(is_palindrome_reversed('abba'))


def is_palindrome_slice(string):
    return string == string[::-1]

print(is_palindrome_slice('abba'))
"""
# 9---------------------------------------------------------------------------------------------------------------------


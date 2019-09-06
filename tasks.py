import operator
from heapq import nlargest
from os import listdir

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
"""

def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')


convert(1234565)
"""
# 10--------------------------------------------------------------------------------------------------------------------
"""
numbers = input("Type numbers with comma: ")
ints_as_strings = numbers.split(',')
ints = map(int, ints_as_strings)
lst = list(ints)
tup = tuple(lst)
print('List: ', lst)
print('Cortege: ', tup)
"""
# 11--------------------------------------------------------------------------------------------------------------------
"""
list = [1, 2, 3, 4, 5]
print(list[0], '', list[-1])
"""
# 12--------------------------------------------------------------------------------------------------------------------
"""

def file_name(name):
    name_part = name.split('.')
    if len(name_part) < 2:
        raise ValueError
    first, *middle, last = name_part
    if not last or not first and not middle:
        raise ValueError('The file has no extension')
    return name_part[-1]


print(file_name('abc.py'))
print(file_name('abc'))  # ValueError
print(file_name('.abc'))  # ValueError
print(file_name('.abc.def'))  #ValueError
"""
# 13--------------------------------------------------------------------------------------------------------------------
"""

def n_stick(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)


n_stick(2)
"""
# 14--------------------------------------------------------------------------------------------------------------------
"""
list = [1, 2, 3, 4, 5, 6, 7, 237, 8, 9, 10, 11, 12]
for i in list:
    if i == 237:
        break
    elif i % 2 == 0:
        print(i)
"""
# 15--------------------------------------------------------------------------------------------------------------------
"""
print(listdir("C:\\Music"))
"""
# 16--------------------------------------------------------------------------------------------------------------------
"""
objects = list(input())
a = 0
for obj in objects:
    a += int(obj)

print(a)


def sum_digits(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)


print(sum_digits(1234))
"""
# 17--------------------------------------------------------------------------------------------------------------------

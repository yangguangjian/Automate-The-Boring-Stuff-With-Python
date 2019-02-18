import copy

'''
变量包含对列表值的引用， 而不是列表值本身。但对于字符串和整数值， 变量
就包含了字符串或整数值。在变量必须保存可变数据类型的值时， 例如列表或字典，
Python 就使用引用。对于不可变的数据类型的值， 例如字符串、 整型或元组， Python
变量就保存值本身。
'''

'''
虽然 Python 变量在技术上包含了对列表或字典值的引用，但人们通常随意地
说，该变量包含了列表或字典。
'''

'''
要理解参数如何传递给函数，引用就特别重要。当函数被调用时， 参数的值被
复制给变元。对于列表（以及字典， 我将在下一章中讨论）， 这意味着变元得到的
是引用的拷贝。 
'''

def func():
    pass

def eggs(para):
    para.append('Hello')

spam=[1,2,3]
eggs(spam)
print(spam)

print(dir(func))

# copy.copy copy.deepcopy
'''
>>> import copy
>>>
>>>
>>>
>>> list=[1,2,[3,4,5]]
>>> list
[1, 2, [3, 4, 5]]
>>> cp1=list
>>> list[0]=0
>>> cp1
[0, 2, [3, 4, 5]]
>>> cp2=copy.copy(list)
>>> list
[0, 2, [3, 4, 5]]
>>> cp2
[0, 2, [3, 4, 5]]
>>> list[0]=10
>>> list
[10, 2, [3, 4, 5]]
>>> cp2
[0, 2, [3, 4, 5]]
>>> list[2][0]=0
>>> list
[10, 2, [0, 4, 5]]
>>> cp2
[0, 2, [0, 4, 5]]
>>> cp3=copy.deepcopy(list)
>>> list
[10, 2, [0, 4, 5]]
>>> cp3
[10, 2, [0, 4, 5]]
>>> list[2][0]=10
>>> list
[10, 2, [10, 4, 5]]
>>> cp3
[10, 2, [0, 4, 5]]
>>> cp2
[0, 2, [10, 4, 5]]
>>> cp
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cp' is not defined
>>> cp1
[10, 2, [10, 4, 5]]
>>>
'''
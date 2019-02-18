# 下标
# 负数下标
# 切片(省略前后索引)
# 通过下标赋值
# 列表连接
# 列表赋值
# del删除列表值

cats = []

while True:
    print('Enter the name of cat ' + str(len(cats) + 1) + ' (Or enter nothing to stop.):')

    name = input()
    if name == '':
        break

    cats += [name]
    # cats += name

print('The cat names are:')
for name in cats:
    print(' ' + name)

print('-------------------')

for i in range(len(cats)):
    print(' ' + cats[i])

print('--------------------')

myPets = ['daxian', 'yinzi', 'tuomi']
print('enter a pet name:')
name = input()
if name not in myPets:
    print('i dont hav3e a pet named ' + name)
else:
    print(name + ' is my pet')

a,b,c=myPets #unpack list
print(a,b,c)

'''
# sort():不能对数字,字符混合的列表排序
>>> list=['b','a','z','B','Z','A']
>>> list
['b', 'a', 'z', 'B', 'Z', 'A']
>>> list.sort() # 字符排序是使用ascii字符顺序
>>> list
['A', 'B', 'Z', 'a', 'b', 'z']
>>> list.sort(key=str.lower) # 按照普通的字典顺序来排序,将所有的表项当成小写字母,所以'A'和'a'的相对位置没有变化
>>> list
['A', 'a', 'B', 'b', 'Z', 'z']
>>> list=['b','a','z','B','Z','A']
>>> list.sort(key=str.lower)
>>> list
['a', 'A', 'b', 'B', 'z', 'Z'] # 'A'和'a'的相对位置发生了变化
>>>



'''
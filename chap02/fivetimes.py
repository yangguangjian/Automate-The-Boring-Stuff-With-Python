for i in range(5):
    print('cnt ' + str(i))

print('------')

for i in range(5, -1, -1): # 起始,停止,步长
    print('cnt' + str(i))

print('------')

cnt=0
for i in range(101):
    cnt += i
print('sum: ' + str(cnt))
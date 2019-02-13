var = 'global'

def local():
    var='local'
    print('in local: ' + var)

def local2():
    var='local2'
    local()
    print('in local2: ' + var)

def local3():
    global var
    var = 'local3'

def local4():
    # 发生这个错误是因为， Python看到spam()函数中有针对gs的赋值语句，因此认为eggs变量是局部变量。
    # 但是因为print(eggs)的执行在eggs赋值之前，局部变量eggs并不存在。 Python不会退回到使用全局eggs变量
    # print('use global var in local4: ' + var)
    var = 'local4'
    print('use local var in local4: ' + var)

local2()
print('in global: ' + var)

local3()
print('in global after invoke local3: ' + var)

local4()
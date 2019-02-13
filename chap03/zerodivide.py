def spam(num):
    # try:
        return 45 / num
    # except ZeroDivisionError:
    #    print('zero unsupported')


try:
    print(spam(10))
    print(spam(0)) # 抛出异常
    print(spam(20))
except ZeroDivisionError:
    print('wrong num')

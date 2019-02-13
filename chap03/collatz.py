import sys

def collatz(number):
    ret = 0

    if number % 2 == 0:
        ret = number // 2
    else:
        ret = 3 * number + 1

    print(ret)
    return ret

print('Input a number:')
try:
    number = int(input())
except:
    print('Only number supported')
    sys.exit(-1)

while True:
    number = collatz(number)
    if number == 1:
        break
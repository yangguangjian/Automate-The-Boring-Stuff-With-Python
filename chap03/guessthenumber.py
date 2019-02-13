import random


def guessNumber():
    print('I am thinking a number between 1 and 20.')
    myNumber = random.randint(1, 20)
    guessCnt = 0

    while True:
        print('Take a guess.')
        guessCnt += 1

        try:
            yourNumber = int(input())
        except:
            print('Wrong Input')
            guessCnt -= 1
            continue

        if yourNumber < myNumber:
            print('Your guess is too low')
            continue
        elif yourNumber > myNumber:
            print('Your guess is to high')
            continue
        else:
            print('Good job! you guessed my number in ' + str(guessCnt) + ' guesses')
            break


guessNumber()

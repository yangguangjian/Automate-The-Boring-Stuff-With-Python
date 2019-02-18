grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def printSentences(words):
    sentence=''

    try:
        for i in range(len(words)):
            sentence += str(words[i])

            if i == len(words) - 2:
                sentence += ' and '
            else:
                sentence += ', '
    except:
        print('only pure list supported')
        return

    print('words to sentence: ' + sentence)
    return

def printCharGrid(grid):
    print('you may see a zero heart below:')

    for j in range(len(grid[0])):
        for i in range(len(grid)):
            print(grid[i][j], end='')

        print()
    pass

printSentences(['a', 'b', 3, 'c'])
printSentences(['a', 'b', [3, 'c']]) # 注意到，[3, 'c']也可以转换成相应的字符串
printCharGrid(grid)
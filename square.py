def printSquares():
    '''
    Objective : To print squares of positive numbers entered by the user. The program terminates if user enters null string.
    Input Parametes : None
    Return Value : None
    '''
    while True:
        numString = input('Enter an integer, to end press Enter:')
        if numString =='':
            break
        number = int(numString)
        print(number, '^2=', number ** 2)
    print('End of input!!')

if __name__ == '__main__':
    printSquares()

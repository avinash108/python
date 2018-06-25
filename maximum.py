def maximum3(n1,n2,n3):
    '''
    Objective:  To find maximum of three numbers
    Input Parameters : n1,n2,n3 - numeric values
    Return Value : maxNumber - numeric value
    '''

    if n1 > n2:
        if n1 > n3:
            maxNumber = n1
        else:
            maxNumber = n3
    elif n2 > n3:
        maxNumber = n2
    else:
        maxNumber = n3
    return maxNumber

def main():
    '''
    Objective : To find maximum of three numbers provided by user
    Input parameter : None
    Return Value : None
    '''

    n1 = int(input('Enter first number:'))
    n2 = int(input('Enter second number :'))
    n3 = int(input('Enter thrid number: '))

    maximum = maximum3(n1,n2,n3)
    print('Maximum number is', maximum)

if __name__ =='__main__':
    main()

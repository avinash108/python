def summation(n):
    '''
    Objective : To find sum of first n positive integers
    Input parameters : n - numeric value
    Return value  : total - numeric value
    '''

    total = 0
    for count in range(1,n+1):
        total += count
    return total


def main():
    '''
    Objective: To find sum of first n positive integers based on user input
    Input pararmeters:  None
    Return Value: None
    '''

    n = int(input('Enter number of terms:'))
    total  = summation(n)
    print('Sum of first', n , 'positive integers:', total )

if __name__=='__main__':
    main()

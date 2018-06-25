def prime(n):
    '''
    Objective : To check if a number is prime or not
    Input Parameter : n - numeric value
    Return Value : message - boolean value
    '''

    if n == 1 : # 1 is not prime
        return False

    for i in range(2,n):
        if n % i == 0:
            flag = False # n is not prime
            break
    else:
        flag = True # n is prime
    return flag

def main():
    '''
    Objective: To check if the number entered by the user is prime number
    Input Parameter: None
    Return Value : None
    '''
    n = int(input('Enter number'))
    result = prime(n)
    if result == True:
        print(n, 'is a prime number')
    else:
        print(n, 'is not a prime number')


if __name__ == '__main__':
    main()

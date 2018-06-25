def authenticateUser(password):
    '''
    Objective: To authenticate user and allow access to system
    Input parameters : password - string
    Return value : message - string
    '''
  
    if password == 'magic':
        message = ' Login successful !! \n Welcome to the system.'
    else:
        message = ' Password mismatch !!\n'
    return message


def main():
    '''
    Objective: To authenticate user
    Input Parameter : None
    Return value : None
    '''

    print('\t LOGIN SYSTEM ')
    print('========================')
    password = input('Enter Password:')
   
    message = authenticateUser(password)
    print(message)

    

if __name__=='__main__':
    main()
    

def moderate(marks, passMarks):
    '''
    Objective : To moderate result by 1 or 2 marks to achieve passMarks
    Input parameters : 
    marks - int
    passMarks - int
    Return value :
    marks - int
    '''

    if marks == passMarks - 1 or marks == passMarks -2:
        marks = passMarks
    return marks

def main():
    '''
    Objective : To moderate marks if a student just misses pass marks
    Input parameters : None
    Return value : None
    '''

    passMarks = 40
    marks = input('Enter marks ')
    intMarks = int(marks)
    moderatedMarks = moderate( intMarks , passMarks )
    print('Moderated marks:', moderatedMarks)

if __name__ =='__main__':
    main()

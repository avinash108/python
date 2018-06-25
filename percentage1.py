def main():
    '''
    Objective : To display percentage of marks scored by the student
    Input Parameters: None
    Return Value : None
    '''

    totalMarks = 0
    nSubjects  = 0
    while True:
        marks = input('Marks for subject ' + str(nSubjects + 1) + ':')
        if marks == '':  #End of input
            break
        marks = float(marks)
        if marks < 0 or marks > 100:
            print('INVALID MARKS !!')
            continue     # Marks to be entered again
        nSubjects = nSubjects + 1
        totalMarks+= marks
    percentage = totalMarks / nSubjects
    print('Total marks:', int(totalMarks))
    print('Number of subjects:', nSubjects)
    print('Percentage:', round(percentage,2))

if __name__ == '__main__':
    main()

def percent(marks, maxMarks):
    '''
    Purpose: To find percentage of marks obtained in a subject
    Input Parameters: marks, maxMarks - numeric value
    Return Value: percentage - numeric value
    '''
    percentage = (marks / maxMarks ) * 100
    return percentage

def main():
    # To compute percentage
    maxMarks = float(input('Enter total marks'))
    marks    = float(input('Enter marks'))
    percentage = percent(marks, maxMarks)
    print('Percentage is :', percentage)

if __name__=='__main__':
    main()

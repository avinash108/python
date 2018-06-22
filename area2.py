import sys
def main():
    '''
    Objective: To compute the are based on user input taken as command line arguments.
    Input parameter: none
    Return value : None
    '''
    if(len(sys.argv))==3:
        length = int(sys.argv[1])
        breadth = int(sys.argv[2])
        print(length)
        print(breadth)
        area = length * breadth
        print("Area: ", area)
    
if __name__ =='__main__':
    main()

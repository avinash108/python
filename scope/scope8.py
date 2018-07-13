def f():
    print('global f')

def g():
    global f
    print('before re-definition of f, id(f):', id(f))
    def f():
        print('inner f')
    print('after re-definition of f, id(f):', id(f))
    f()

def h():
    print('inside h:id(f)', id(f))
    f()
    fprime()

def main():
    print('in global namespace:id(f):', id(f))
    fprime = f
    f()
    g()
    print('in global namespace: id(f):', id(f))
    fprime()
    h()

if __name__=='__main__':
    main()

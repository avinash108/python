a=6
def f():
    a=5
    def g():
        b=a
        print('inside g, a & b:',a,b)
    g()
f()

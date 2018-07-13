a=4
def f():
    a=5
    def g():
        b=a
        print('inside g','a=',a, 'b=',b)
        a=5
    g()
f()

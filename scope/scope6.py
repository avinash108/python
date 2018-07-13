a=4
def f():
    a=5
    def g():
        nonlocal a
        print('inside g, before modifying a,','a=',a)
        a=10
        print('inside g, after modifying a,','a=',a)
    print('inside f, before calling g,','a=',a)
    g()
    print('inside f, after calling g,','a=',a)
f()
print('after calling f,','a=',a)

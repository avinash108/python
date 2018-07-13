a=3
def f():
    def g():
        global a
        a=4
        print('inside g, global a=',a)
    g()
    a=5
    print('inside f, local a=',a)
f()
print('outside of all functions definitions a=',a)

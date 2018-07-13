def f():
    def g():
        a=5
    g()
    print(' in outer function g, a=', a)
f()

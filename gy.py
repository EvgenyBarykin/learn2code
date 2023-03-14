x = 10

def c():
    print('olol')
    global x
    b = x
    print(b)

def b():
    x = 31

    def a():
        print(x)
        c()
    a()

b()

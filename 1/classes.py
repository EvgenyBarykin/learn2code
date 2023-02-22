class MyClass:
    # i = 0
    def __init__(self, num):
        self.i = num
    
    def f(self):
        print(self.i)
        return 'hello world'


var = MyClass(2)
var.f()
print(var.f())
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


class Testclass:

    test_param = 1

    def _init__(self, test_arg) -> None:
        self.test_param = test_arg

a = 1
print(a)
print(type(Testclass))

class Int:

    # задали начальные параметры
    def __init__(self, value) -> None:
        self.value = value

    # присвоили классу метод
    def get_value(self):
        return self.value
    
    # __repr__ возвращает отображение объекта в виде строки
    # когда мы его печатаем
    def __repr__(self) -> str:
        return str(self.value)

a = Int(1)

print(a.get_value())
print(a)
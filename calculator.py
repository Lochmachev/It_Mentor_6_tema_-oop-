# Реализуйте класс Calculator, в котором будет один метод, для вычисления суммы двух чисел.
# Реализуйте еще один класс, который будет наследоваться от класса Calculator и
# перегрузите метод для вычисления суммы двух чисел, чтобы он делал конкатенацию двух строк.

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum (self):
        print (self.x + self.y)

a = int(input())
b = int(input())
summa = Calculator (a,b)
summa.sum()

class Koncat(Calculator):
    def sum (self):
        x1 = str(self.x)
        x2 = str(self.y)
        print(x1 + x2)

k = Koncat(a,b)
k.sum()
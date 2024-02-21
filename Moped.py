# Реализуйте два класса Car и Moped, которые будут наследоваться от класса MeansOfTransport.
# При инициализации они должны принимать новый аргументы(количество колес.
# В классе {{Moped}}напишите статическую функцию, которая на вход будет принимать расстояние и максимальную скорость,
# а на выходе получать время, за которое проедет мопед это расстояние.

from car import MeansOfTransport

class Moped (MeansOfTransport):
    def __init__(self, brand, color, wheel):
        super().__init__(brand, color)
        self.wheel = wheel

    @staticmethod
    def time ( s, v):
        print(s // v,'Часов', int((s%v)*0.6), 'Минут')

moped = Moped ('Карпаты', 'Красный',2)

print(moped.__dict__)
Moped.time(50,3)
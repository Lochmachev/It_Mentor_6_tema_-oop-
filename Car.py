# Реализуйте два класса Car и Moped, которые будут наследоваться от класса MeansOfTransport.
# При инициализации они должны принимать новый аргументы(количество колес).
# Попробуйте инициализировать несколько любых переменных в классе Car и
# сделайте одну переменную приватной, одну защищенной. Попробуйте получить к ним доступ. Какой результат?
# В классе Car добавьте переменную класса car_drive = 4 и реализуйте classmethod,
# который выводит на экран переменную car_drive
# Реализуйте все возможные магические методы в классе Car.

from car import MeansOfTransport

class Car (MeansOfTransport):

    car_drive = 4
    @classmethod
    def car_d(cls):
        print(Car.car_drive)
    def __init__(self, brand, color, wheel):  # -делегирование
        super().__init__(brand, color)
        self._color = color
        self.__wheel = wheel

    def __getattr__(self, item):
        return self.__wheel

# Магические методы

    def __repr__(self):                           # вывод служебной информации
        return f"{self.__class__}:{self._color}"
    #avto

    def __str__(self):                             # вывод информации для пользователя
        return f"{self.brend}"
    #print(avto)



avto = Car ('УАЗ', 'Хакки',4)

print(avto.__dict__)
print(avto.brand)
print(avto.color)
print(avto.wheel)

#print(dir(avto))          # не используя: def __getattr__
#print(avto._Car__wheel)

#Car.car_d()



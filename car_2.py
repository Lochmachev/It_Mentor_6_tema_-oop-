# Работаем с классом из 3 пункта. Реализуйте сеттеры и геттеры для цвета и марки транспортного средства

class MeansOfTransport1:
    def __init__(self, brand, color):
        self.__brand = brand
        self.__color = color

    def set_transport (self, brand, color):
        self.__brand = brand
        self.__color = color

    def get_transport (self):
        return self.__brand, self.__color

car2 = MeansOfTransport1('ГАЗ','Серый')
car2.set_transport('ВАЗ 2106','Белый')
print(car2.get_transport())




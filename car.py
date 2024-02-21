# Создайте класс {{MeansOfTransport }}(для определения цвета и марки машины), принимающий 2 аргумента
# при инициализации (марка и цвет транспортного стредства). В этом классе реализуйте методы show_color(),
# выводящий на печать цвет транспортного средства и show_brand, для получения марки транспортного средства.

class MeansOfTransport:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_color(self):
        print("Цвет авто:", self.color)

    def show_brand(self):
        return ("Марка авто:", self.brand)



car = MeansOfTransport('ГАЗ 31105', 'Металик')


#print(car.__dict__)
#print(car.show_brand())
#car.show_color()

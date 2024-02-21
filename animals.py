# Реализуйте абстрактный класс Animals, создайте класс Cat,
# котрый будет наследоваться от класса Animals }}и реализуйте метод {{voice.

from abc import ABC, abstractmethod

class Animals(ABC):
    @abstractmethod
    def voice(self):
        pass

class Cat(Animals):
    def voice(self):
        print(" Мяу ")

cat = Cat()
cat.voice()
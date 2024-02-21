# Реализуйте класс Dog.
# Придумайте, какие переменные будет принимать данный класс и какие методы будут реализованы.
# Реализуйте в этом классе паттерн Singleton

class Dog:
    _instance = None

    def __init__(self, breed, name):
        if Dog._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.breed = breed
            self.name = name
            Dog._instance = self

    @staticmethod
    def get_instance():
        if not Dog._instance:
            Dog('Unknown', 'Unknown')
        return Dog._instance

    def bark(self):
        print(f"{self.name} ({self.breed}) - собака")

dog1 = Dog.get_instance()
dog1.breed = "Дог"
dog1.name = "Миша"
print(dog1.__dict__)

dog2 = Dog.get_instance()
dog2.name = "Лорд"
dog2.bark()

print(dog1.__dict__)
print(dog2.__dict__)
print(dog1)
print(dog2)









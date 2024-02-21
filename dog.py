# Реализуйте класс Dog.
# Придумайте, какие переменные будет принимать данный класс и какие методы будут реализованы.
# Реализуйте в этом классе паттерн Singleton

def singleton(cls):
    _instances = {}
    def get_instance(*args,**kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args,**kwargs)
        return _instances[cls]
    return get_instance

@singleton
class Dog:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def __str__(self):
        return (f'{self.breed} по кличке {self.name}')

dog1 = Dog ('Сенбернар', 'Малыш')
dog2 = Dog ('Спаниель','Бимка')
print(dog1)
print(dog2)
print(dog1 is dog2)
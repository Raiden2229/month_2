class Person:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        if age < 0:
            print("Ошибка: возраст не может быть отрицательным")
        else:
            self.__age = age

    def get_age(self):
        return self.__age


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return ("I am an animal")
class Dog(Animal):
    def speak(self):
        return "Woof"
class Cat(Animal):
    def speak(self):
        return "Meow"

class Venicle:
    def move(self):
        return "Venicle is moving"
class Car(Venicle):
    def move(self):
        return "Car is driving"
class Bicycle(Venicle):
    def move(self):
        return "Bicycle is driving"
    def move(venicle):
        return venicle.move()


class Shape("ABC"):
    def area(self):
        "Метод для вычисления площади фигур"
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        "Вычисление площади треуугольника"
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        "Вычисление площади круга"
        return math.pi * (self.radius ** 2)






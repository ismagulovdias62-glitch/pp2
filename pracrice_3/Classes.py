class Person:
    def say_hi(self):
        print("Hi")

p = Person()
p.say_hi()


class Student:
    def __init__(self, name):
        self.name = name

s = Student("Dias")
print(s.name)



class Dog:
    def bark(self):
        print("Woof")



class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

c1 = Car("BMW")
c2 = Car("Audi")

print(c1.wheels)

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if 0 <= score <= score:
            self.__score = score
        else:
            raise ValueError('bad score')
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        if 1915 <= value <= 2015:
            self._birth = value
    @property
    def age(self):
        return 2015 - self._birth
    def __str__(self):
        return 'Student object (name: %s)' % self.__name



bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print(bart.get_grade())
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
dog = Dog()
dog.run()
cat = Cat()
cat.run()
print(type(dog))

import types
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x*x)==types.LambdaType)
print(x for x in range(10))
print(dir(dog))
def set_age(self, age):
    self.age = age
from types import MethodType
#dog.set_age = MethodType(set_age, dog)#通过methodtype 给实例赋予方法
#dog.set_age(25)
#print(dog.age)
Animal.set_age = set_age
dog.set_age(22)
print(dog.age)
print(dir(Dog))
cat.set_age(19)
print(cat.age)#这东西能直接把方法传给类，然后各个实例都能用了。厉害

bart.birth = 2013
print(bart.birth)

print(bart.age)
print(bart)

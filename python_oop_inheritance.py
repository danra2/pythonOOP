#Inheritance
#Encapsulation is basiclaly how we store data in the form of an object, how we can access it
#Validating the integrity of the data via getter and setting methods.

class Date(object):
    def get_date(self):
        return '2014-10-13'

class Time(Date):
    def get_time(self):
        return '08:13:07'

dt = Date()
print(dt.get_date())

tm = Time()
print(tm.get_time())
print(tm.get_date())

#Object is a method built within inside python itself.

#Object attribute look up heirarchy:
#1.) The Instance
#2.) The class
#3.) Any class from which this class inherits from

#Polymorphism, many shapes, and objects have disimliar types can be treated as the same time.
#Two classes with the same interface (method name, both classes have the same method name
#Methods are typically different, but function very similiarly

class Animal(object):

    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print('%s is eating %s.') % (self.name, food)

class Dog(Animal):
    def fetch(self, thing):
        print('%s goes after the %s!' % (self.name, thing))

d = Dog('dogname')

print d.name

import random

class Animal(object):
    def __init__(self,name):
        self.name = name
class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
        #What this is doing is calling the super class, and saying hey super
        #The dog instance wants to call the init function in your class
        #We do this to further modularize our code, and make __init__ a genearl usage and not specific
    def fetch(self, thing):
        print '%s goes after the %s!' % (self.name, thing)

d = Dog('dogname')

print d.name
print d.breed

#The diamond shape inheritance pattern, essentially when you have two inherited classes
#But both refer back tot he parent, and have ambiguity, the initial instance of that class disappears.
#See notes for D > B > C > A
#Breath vs Depth search.
#Python is the only language that can inherit from two classes at the same Time
#This was created for code usability, and maintability, and no DRY


#There are different types of methods, for example instance methods are called instance, because they are instantly called
#Any method that passes the parameter self is an instance method

#class and static methods, that are not bound to the instance.

#class function has to be overrided with a declaractive
# @classmethod before the method itself
#This will make it so it passes class directly, instead of itself and self.
#Also there is another method called the utility methods, aka @staticmethod
#This method is used for utility classes, but still included within the class because it works in tandum with it
#When you are dealing with variables such as count etc, use a utility method.

@staticmethod
def filterint(value):
    if not isinstance(value, int):
        return 0
    else:
        return value

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter('hello')

print a.value
print c.vale

#Abstract base classes:

import abc

class GetterSetter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self,input):
        return
    @abc.abstractmethod
    def get_val(self):
        return

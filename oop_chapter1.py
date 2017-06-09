class MyClass(object):
    var = 10
    # pass


this_obj = MyClass()
that_obj = MyClass()

print this_obj
print this_obj.var
print that_obj.var

#This is an instance of MyClass.
#

class Joe(object):
    greeting = "hello, Joe"
    def callme(self):
        print('Calling call me method with instance:')

thisjoe = Joe()

print thisjoe.gretting
thisjoe.callme()

#When we call a method via an instance, the instance gets pass as the first parameter of that method.
#Implicit default behvaior, when we can all a method on an instance, the instance is passed
#This is why we need the self

#Three pillars of OOP:
#Encapsulation
#Inheritance
#Polymorphism


class MyClass(object):

    def set_val(self,val):
        self.value = val
    def get_val(self):
        return self.value

a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(100)

print(a.get_val())
print(b.get_val())

class MyInteger(object):
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val
#It's going to try the method set_val, if it can convert to an int then it will go to line 57
#And set the value, otherwise it will hit except, and just exit with the return statement.
#Encapsulation, is basically keeping the values and setting values within a particular class
#Because that class has specific rules, that the methods and functions might require it to be a specific saved value to work with
#IF your methods for this class can only work with Ints, and you bypass the encapsulation by setting your own values and you set a string
#The rest of the methods won't be able to work with your string because they require ints.


class MyNum(object):
    def __init__(self):
        print 'calling __init__'
        self.val = 0

    def increment(self):
        self.val = self.val + 1

dd = MyNum()
dd.increment()
dd.increment()
print dd.val
print
#The double underscores for __init__ sygnify a private method, or magic method
#Used internally not called by the user of the class, it's called automatically
#Any time a new instance is constructed, it's called

class MyNum(object):
    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value
    def increment(self):
        self.val = self.val + 1

aa = MyNum('hello')
bb = MyNum(100)

print aa.val
print bb.val
#It makes sense to do the gateway and validation in the __init__ version
#Because it's called either way at the start for each instance

class YourClass(object):
    classy = 10

    def set_val(self):
        self.insty = 100

dd = YourClass()
dd.set_val()
print(dd.classy)
print(dd.insty)

class InstanceCounter(object):
    count = 0

    def __init__(self,val):
        self.val = val
        InstanceCounter.count += 1
    def set_val(self, newval):
        self.val = newval
    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a,b,c):
    print "val of obj: %s" % (obj.get_val())
    print "count: %s % (obj.get_count())"

#Any variable that is going to be accessed from within the class, a global
#Has to be accessed via the classname.variablename
#. notation

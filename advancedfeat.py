var.__add__(var2)

var + var 2

var = 'hello'
var2 = 'world!'

#this is just a syntatic sugar method

#Old style "Classic" Classes
class OldClass():
    pass

#new style Classes
class NewClass(object):
    pass

oc = OldClass()

nc = NewClass()


mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key = raw_input('please input a key: ')
print('the value for {0} is {1}'.format(key,mydict[key]))

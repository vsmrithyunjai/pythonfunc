# import class.py
#PYTHONPATH=/pythonfunc game.py -- need to provide this when different path
#build in modules for python - https://docs.python.org/3/library/
#Two very important functions come in handy when exploring modules in Python - the dir and help functions.
#To import the module urllib, which enables us to create read data from URLs, we import the module:
#import urllib  dir(urllib) help(urllib.urlopen)
from classpy import *
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)





car1 = Vehicle()
car1.name = 'Fer'
car1.kind = "Convertible"
car1.color = "red"
car1.value = 60000
car2 = Vehicle()
car2.name = 'Jump'
car2.kind = "Van"
car2.color = "Blue"
car2.value = 10000
print(car1.description())
print(car2.description())
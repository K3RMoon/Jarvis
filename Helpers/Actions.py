# coding: utf-8
import math
import random
from random import randint

def Sum(a,b):
    return a+b
def Substract(a,b):
    return a-b
def Multiply (a,b):
    return a*b
def Divide (a,b):
    return int(a/b)
def RollDice ():
    return randint(1, 6)
def Modulo(a,b):
    return a%b
def Power (a,b):
    return math.pow(a, b)
def Root (a):
    return math.sqrt(a)
def Joke():
    return random.choice(jokes)
def Random():
    return random.randint(1,10000)
jokes = [
    "What did the dog say after a long day at work? Today was ruff.",
    "Knock, knock.\nWho’s there?\nKanye.\nKanye who?\nKanye believe it? I tell jokes too!",
    "What do you call a can opener that doesn’t work? A can’t opener.",
    "Why can’t you trust an atom? Because they make up literally everything.",
    "Kelvin",
    "What's the object-oriented way to become wealthy?\nInheritance",
    "Why did the programmer quit his job?\nBecause he didn't get arrays.",
    "0 is false and 1 is true, right?\n1",
    "Why do Java programmers have to wear glasses?\nBecause they don't C#"
    ]


'''
RollDice()
Random 
Sum
Multiply
Divide
Subvstract
modulo
power
root
fileshit #no
joke
image #no
'''
# ANDS and ORS of actions
# Parameter in responses "Hello ~name"
# Responses with more than one string

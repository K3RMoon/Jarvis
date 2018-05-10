import math
import random
from random import randint
def RollDice():
    return random.randint(1,6)
def Sum(a,b):
    return a+b
def Substract(a,b):
    return a-b
def Multiply (a,b):
    return a*b
def Divide (a,b):
    return a/b
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
    return random.randint()
jokes = [
    "What did the dog say after a long day at work? Today was ruff.",
    "Knock, knock.\nWho’s there?\nKanye.\nKanye who?\nKanye believe it? I tell jokes too!",
    "What do you call a can opener that doesn’t work? A can’t opener.",
    "Why can’t you trust an atom? Because they make up literally everything."
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
'''
RollDice XX done
Random XX (random NUMBER)
Sum XX done
Multiply XX
Divide XX
Subtract XX done
Modulo XX
Power Xx
Root XX
Save  **Save a file //Need to think through:
    where are we going to save things? always the same default directory?
    is the destination also a parameter? is the format always the same?

    Save (fileName, fileDirectory)  //just creates an empty file with that name at that directory? kk
Delete
    **same issues as above
    Delete (directory, name)  Delete(whole damn path)
Update
    **same issues as above (changes what's in a file)
    --this one is the most likely to eliminate, too complex---
Move
    **same issues as above
    move ( filename, oldDirectory, newDirectory) or move (oldFilePath, new filePath)
Joke XX
SearchImage ~~pretty damn complext, likely worse than file management
'''
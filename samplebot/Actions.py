import random
def RollDice():
    return random.randint(1,6)
def Sum(a,b):
    return a+b
def Substract(a,b):
    return a-b

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
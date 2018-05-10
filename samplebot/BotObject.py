from FileManager import FileManager
import Actions

class bot:
    def __init__(self, name):
        self.name = name
        self.rulesManager = FileManager(name+".bot")#rules files
        self.fileManager = FileManager("knowledge.bot") #knowledge file
        self.rules = self.rulesManager.getDictionary()
        self.knowledge = self.fileManager.getDictionary()
        # print(self.knowledge)

    def learn(self, attrName, attr):
        self.knowledge[attrName] = attr #allows overwrite
        self.fileManager.writeContent(self.knowledge)

    def addRule(self, phrase, RuleType, response):
        self.rules[phrase.lower()]= RuleType+'$'+response
        self.rulesManager.writeContent(self.rules)



#Nice, but we need to fix to adhere with project rules with one specific annoying thing...
    #we need to be able to give the input variables as part of the initial input, not just being asked after
    #so we need to tokenize it somehow, separate a specific symbol, like (%) for now [could and maybe should be changed]
    # in order to validate, go through all lists and check if equal
    # the symbol to use is now (~) because (%) is already used by python I guess


    #how does this work? it depends heavily on the ammount of arguments. as in, the ammount of tokens basically
    #it goes comparing token by token, if all (aka the size of ruleList) match, good. once any doesnt match resets to 0.
    def checkRule(self, rule, ruleList, params): #by Herbert, will try to do the new verification here
        trues = 0
        cindex2=-1
        for y in ruleList:
            cindex2+=1
            cindex = -1
            for x in rule:
                cindex+= 1
               # print(x)
               # print(ruleList[cindex2][cindex])
                if not (ruleList[cindex2][cindex][0]=='~' or x == ruleList[cindex2][cindex]):
                    trues = 0
                    params = []
                    #print(trues)
                else:
                    if(ruleList[cindex2][cindex][0]=='~'):
                        params.append(x)
                        #rule[cindex] = "~param"
                        # Quick fix to allos other parameter names!
                        rule[cindex] = ""+ruleList[cindex2][cindex]
                    trues+=1
                    #print(trues)
                    if (trues== rule.__len__()):
                        return True
        return False
    #very simple helper method
    @staticmethod
    def RepresentsInt(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def handleInput(self, r):

        rlist = r.split(" ")
        rlen = rlist.__len__()
        #print(rlen)

        samelenrules = []
        printme=list(self.rules.keys())
        #print(printme)
        for x in list(self.rules.keys()):
            xlist = (str(x)).split(" ")
            #print (xlist)
            #print (xlist.__len__())
            if xlist.__len__() == rlen:
                samelenrules.append(xlist)
                #print(xlist)
        #print(samelenrules)

        r = r.lower()
        #checks if rule is valid among same length rules.
        #WARNING OF POSSIBLE ISSUES: what if the input we want is a long string? as in, more than one token?
            # this might cause some issues since we separate stuff by spaces
        params = []
        status = self.checkRule(rlist, samelenrules, params)
        print(status)
        r = " ".join(str(e) for e in rlist)
        print(r)
        #if r in self.rules.keys():
        if status:
            rule = str(self.rules[r])
            rContent = rule.partition('$')
            rType = rContent[0]
            rValue = rContent[2]
            self.handleRule([rType, rValue], params)
        else:
            print("Rule unknown")
        

    def handleRule(self, rule, params):
        if(rule[0].lower()=="response"):
            print(rule[1])
        if(rule[0].lower()=="learn"):
            attrName = input(rule[1]+ ": ")
            attrVal = input("enter "+attrName+": ")
            self.learn(attrName, attrVal)
        if(rule[0].lower()=="action"):
            if(rule[1].lower()=="sum"):
                #WARNING: maybe will also have to verify that we have the correct ammount of arguments?
                    #tho maybe that should be verified in the yacc. we'll see.
                if not(self.RepresentsInt(params[0]) and self.RepresentsInt(params[1])):
                    print("Illegal Argument Type")
                else:
                    #numb1 = int(input("Enter the first number:" ))
                    numb1 = int(params[0])
                    #numb2 = int(input("Enter the second number: "))
                    numb2 = int(params[1])
                    print("The result is "+str(Actions.Sum(numb1, numb2)))

    def getAttr(self,attrName):
        return self.knowledge[attrName]

    def forget(self, attrName):
        keys = self.knowledge.keys()
        if attrName in keys:
            del self.knowledge[attrName]
            self.fileManager.writeContent(self.knowledge)

        else:
            print(attrName + " is not in knowledge")
        
    

b = bot("Jarvis")
b.addRule("Hey","Response","Hello")
b.addRule("How are u?", "Response","I'm doing just fine")
b.addRule("Learn something", "Learn", "What's should i learn")
#b.addRule("Add 2 numbers", "Action", "SUM") #outdated sum, no arguments
b.addRule("Add 2 numbers ~num1 ~num2", "Action", "SUM")
b.forget("name")

'''''
So...what Im thinking es tener ademas de los tipos que ya tenemos de "Response/Action/Learn", anadir uno que sea combination.
    *Justo despues de combination tiene el tipo de combination que es (Si hacemos AND y OR, si solo hacemos AND pichea eso)
    *despues de esto tenemos un numero, es la cantidad de cosas que se combinan
    *finally tenemos las cosas themselves, following el formato normal de "type:response"

"This is the user input ~NUM1 ~NUM2" "Combination" "3" "AND" "ACTION" "SUM" "Response" "doing number operations" "ACTION" "substract"

    this could work, but it would take quite a bit of time? I dunno.
-----------------------------------/////////----------------------------///////////--------------------------/////////-----------
Otra alternativa es anadirlos como sub comandos, y que se llamen cada uno. Like, idk, 

Si el usuario espera que el input "Do stuff" tire tres respuestas, el parser genera 

"Do stuff 1", "response", "blah"
"Do stuff 2", "response", "stuff"
"Do stuff 3", "response", "hi"

y corre las tres somehow. or something similar. 

pero no me gusta tanto esta idea pque either leads to confusion o causa issues al validar, cause people also might want to have
numbers in the title from the beginning sooo...pichea, me gusta mas la primera idea.
-----------------------------------/////////----------------------------///////////--------------------------/////////-----------

maybe anadir todas con el mismo nombre, y que si el programa detecta mas de una cosa con el mismo nombre, que corra todas? so poner AND
en el codigo que nosotros developed implica en el de Python ponerlo varias veces con el mismo nombre como rule? maybe?

"Do stuff", "response", "blah"
"Do stuff", "response", "stuff"
"Do stuff", "response", "hi"

>Do stuff
>>blah
>>stuff
>>hi


'''''

l=""
while not(l.lower() == "quit"):
    l = str(input("Enter a command: "))
    r = b.handleInput(l)



#formato de knowledge -->   attributeName:attributeValue
#formato de rule      -->   ruleName:RuleType$ruleValue



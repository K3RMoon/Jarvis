from FileManager import FileManager
import Actions
class bot:
    def __init__(self, name):
        self.name = name
        self.rulesManager = FileManager(name+".bot")
        self.fileManager = FileManager("knowledge.bot")
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
                        rule[cindex] = "~param"
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
b.addRule("Add 2 numbers ~param ~param", "Action", "SUM")
b.forget("name")


l=""
while not(l.lower() == "quit"):
    l = str(input("Enter a command: "))
    r = b.handleInput(l)



#formato de knowledge -->   attributeName:attributeValue
#formato de rule      -->   ruleName:RuleType$ruleValue



from samplebot.FileManager import FileManager
import samplebot.Actions

thebots = {}
currentBot = None

class Rule:

    def __init__(self, name, delimiter, responses):
        self.name = name
        self.delimiter = delimiter
        self.responses = responses

    def get_name(self):
        return self.name

    def get_delimiter(self):
        return self.delimiter

    def get_responses(self):
        return self.responses

    def set_name(self,name):
        self.name = name

    def set_delimiter(self, delimiter):
        self.delimiter = delimiter

    def set_responses(self, responses):
        self.responses = responses


class Response:

    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message

    def set_message(self, message):
        self.message = message



class Variable:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def set_name(self, name):
        self.name = name

    def set_value(self, value):
        self.value = value


class Learn:

    def __init__(self, var):
        self.var = var

    def get_var(self):
        return self.var

    def set_var(self, var):
        self.var = var


class Forget:

    def __init__(self, var):
        self.var = var

    def get_var(self):
        return self.var

    def set_var(self, var):
        self.var = var


class Action:

    def __init__(self, action, parameter):
        self.action = action
        self.parameter = parameter

    def get_action(self):
        return self.action

    def get_parameter(self):
        return self.parameter

    def set_action(self, action):
        self.action = action

    def set_parameter(self, parameter):
        self.parameter = parameter

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
        p = phrase.split('"')
        p = p[1]
        r = response.split('"')
        r = r[1]
        #print(r)
        #print(p)
        #self.rules[p.lower()] = RuleType+'$'+r
        self.rules.update({p.lower(): RuleType+'$'+r})
        self.rulesManager.writeContent(self.rules)
       # self.rulesManager.writeContent({p.lower(): RuleType+'$'+r}) #CHECK
       # self.rules = self.rulesManager.getDictionary()

    def handleInput(self, r):

        rlist = r.split(" ")
        rlen = rlist.__len__()
        #print(rlen)
        #print(self.rules)
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
from samplebot.FileManager import FileManager
from samplebot import Actions

thebots = {}
currentBot = None

class bot:
    def __init__(self, name):
        self.name = name
        self.rulesManager = FileManager("Bots\\" +name+".bot")#rules files
        self.fileManager = FileManager("Bots\\"+name+"knowledge.bot") #knowledge file
        self.rules = self.rulesManager.getDictionary()
        self.knowledge = self.fileManager.getDictionary()
        # print(self.knowledge)

    def learn(self, attrName, attr):
        self.knowledge[attrName] = attr #allows overwrite
        self.fileManager.writeContent(self.knowledge)

    def addRule(self, phrase, RuleType, response):

        self.rules[phrase.lower()]= RuleType+'$'+response
        self.rulesManager.writeContent(self.rules)
        #print (self.rules)



    #Nice, but we need to fix to adhere with project rules with one specific annoying thing...
    #we need to be able to give the input variables as part of the initial input, not just being asked after
    #so we need to tokenize it somehow, separate a specific symbol, like (%) for now [could and maybe should be changed]
    # in order to validate, go through all lists and check if equal
    # the symbol to use is now (~) because (%) is already used by python I guess


    #how does this work? it depends heavily on the ammount of arguments. as in, the ammount of tokens basically
    #it goes comparing token by token, if all (aka the size of ruleList) match, good. once any doesnt match resets to 0.
    def checkRule(self, rule, ruleList, params, paramDict): #by Herbert, will try to do the new verification here
        if (ruleList.__len__()==0) :
            return False
        if (rule.__len__()==0) :
            return False
        trues = 0
        cindex2=-1
        for y in ruleList:
            cindex2+=1  #rules with same legth
            cindex = -1 #arguments per rule
            for x in rule:
                cindex+= 1
                #print("rule part")
                #print(x)
                #print("other rule part")
                #print(ruleList[cindex2][cindex])
                if not (ruleList[cindex2][cindex][0]=='~' or x.lower() == ruleList[cindex2][cindex].lower()):
                    trues = 0
                    params[:] = []
                 #   print("trues")
                 #   print(trues)
                 #   print("params")
                 #   print(params)
                    break
                else:
                    if(ruleList[cindex2][cindex][0]=='~'):
                        params.append(x)
                        rule[cindex] = "~param"
                        # Quick fix to allos other parameter names!
                        ##**rule[cindex] = ""+ruleList[cindex2][cindex]
                        rule[cindex] = "~param"
                    trues+=1
                  #  print("trues")
                  #  print(trues)
                  #  print("params")
                  #  print(params)
                    if (trues== rule.__len__()):
                        cindex3 = -1 #index for fixing ~param
                        for v in ruleList[cindex2]:
                            cindex3+=1
                            if ruleList[cindex2][cindex3][0]=='~':
                                paramDict[ruleList[cindex2][cindex3][1:]] = rule[cindex3]
                                rule[cindex3] = ruleList[cindex2][cindex3]

                                #print(""+str(ruleList[cindex2][cindex3][1:])+" is "+paramDict.get(ruleList[cindex2][cindex3][1:]))
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
        r = r.lower()
        rlist = r.split(" ")
        rlen = rlist.__len__()
        #print(rlen)

        samelenrules = []
        # printme=list(self.rules.keys())
        #print(printme)
        for x in list(self.rules.keys()):
            xlist = (str(x)).split(" ")
            #print (xlist)
            # print (xlist.__len__())
            if xlist.__len__() == rlen:
                samelenrules.append(xlist)
                #print(xlist)
        # print(samelenrules)

        #checks if rule is valid among same length rules.
        #WARNING OF POSSIBLE ISSUES: what if the input we want is a long string? as in, more than one token?
        # this might cause some issues since we separate stuff by spaces
        params = []
        paramDict = {}
        status = self.checkRule(rlist, samelenrules, params, paramDict)
        #print(params)
        #print(status)
        r = " ".join(str(e) for e in rlist)
        r = r.lower()
        #print(r)
        #if r in self.rules.keys():
        if status:
           # print("this is R")
           # print(r)
           # print(r.lower())
            rule = str(self.rules[r.lower()])
            rContent = rule.partition('$')
            # print(rContent)
            rType = rContent[0]
            rValue = rContent[2]
            self.handleRule([rType, rValue], params, paramDict)
        else:
            if(r!='quit'):
                print("Rule unknown")

    def responseHandler(self, response, params):
        # keys = self.knowledge.keys()
        responseList = response.split(' ')
        returnable = ""
        #print(responseList)
        #print(params)
        pindex = 0
        for x in responseList:
        #     rindex+=1
        #     if (x[0]=='~'):
        #         if (x.split("~"))[1] in keys:
        #             responseList[rindex]=self.knowledge[(x.split("~"))[1]]
        #         else:
        #             return str((x.split("~"))[1] + " is not in knowledge")
        # returnable = " ".join(str(e) for e in responseList)
            # print(x)
            if(x!=''):
                vals = x.split(' ')
                #print(vals)
                
                for v in vals:
                    # print(v)
                    # returnable = returnable +v
                    k = v
                    if(k=='param'):
                        k = params[pindex]
                        pindex+=1
                        if(self.knowledge.get(k) == None):
                            return k +" is not in my knowledge yet"
                        else:
                            returnable = (returnable +self.knowledge.get(k))
                    else:
                        if(v!=''):
                            if(v[0]=='~'):
                                k = v[1:]
                                # print(v[1:])
                                if(self.knowledge.get(k) == None):
                                        return k +" is not in my knowledge yet"
                                else:
                                    returnable+=self.knowledge.get(k)
                            #     returnable+=k[1:]
                            # else:
                            #     if(v[-1]=='"'):
                            #         returnable+=k[:-1]
                            #     else:
                                    
                                    
                            else:
                                returnable += k
            returnable+=" "
                        
        return returnable


    def handleRule(self, rule, params, paramDict):
        # print(rule, params, paramDict)
        if(rule[0].lower()=="forget"):
            self.forget(paramDict[0])
            print(rule, paramDict, params)
        if(rule[0].lower()=="response"):
            # print(params, rule[1])
            print(self.responseHandler(rule[1], params))
        if (rule[0].lower() == "learn"):
            if params.__len__() < 1:
                print("Invalid Number of Parameters: Illegal Operation")
            else:
                self.learn(params[0], params[1])
        if(rule[0].lower()=="action"):
            if(rule[1].lower()=="multiply" or rule[1].lower()=="sum" or rule[1].lower() == "subtract" or rule[1].lower() == "divide" or rule[1].lower() == "modulo" or rule[1].lower() == "power"):
                if params.__len__() < 2:
                    print("Invalid Number of Parameters: Illegal Operation")
                else:
                    #WARNING: maybe will also have to verify that we have the correct ammount of arguments?
                    #tho maybe that should be verified in the yacc. we'll see.
                    #print(params)
                    if not(self.RepresentsInt(params[0]) and self.RepresentsInt(params[1])):
                        print("Illegal Argument Type")
                    else:
                        #numb1 = int(input("Enter the first number:" ))
                        numb1 = int(params[0])
                        #numb2 = int(input("Enter the second number: "))
                        numb2 = int(params[1])
                        if(rule[1].lower()=="sum"):
                            print("The result is "+str(Actions.Sum(numb1, numb2)))
                        elif(rule[1].lower() == "subtract"):
                            print("The result is "+str(Actions.Substract(numb1, numb2)))
                        elif (rule[1].lower() == "multiply"):
                            print("The result is " + str(Actions.Multiply(numb1, numb2)))
                        elif (rule[1].lower() == "divide"):
                            print("The result is " + str(Actions.Divide(numb1, numb2)))
                        elif (rule[1].lower() == "modulo"):
                            print("The result is " + str(Actions.Modulo(numb1, numb2)))
                        elif (rule[1].lower() == "power"):
                            print("The result is " + str(Actions.Power(numb1, numb2)))
        if (rule[1].lower() == "rolldice"):
            print("Your dice roll resulted in "+str(Actions.RollDice()))
        if (rule[1].lower() == "root"):
            if params.__len__()<1:
                print("Invalid Number of Parameters: Illegal Operation")
            else:
                if not (self.RepresentsInt(params[0])):
                    print("Illegal Argument Type")
                else:
                    numb1 = int(params[0])
                    print("The result is " + str(Actions.Root(numb1)))
        if (rule[1].lower() == "joke"):
            print(str (Actions.Joke()))
        if (rule[1].lower() == "random"):
            print("You got a "+str(Actions.Random()))

    def getAttr(self,attrName):
        return self.knowledge[attrName]

    def forget(self, attrName):
        keys = self.knowledge.keys()
        if attrName in keys:
            del self.knowledge[attrName]
            self.fileManager.writeContent(self.knowledge)

        else:
            print(attrName + " is not in knowledge")
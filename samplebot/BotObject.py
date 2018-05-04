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

    def handleInput(self, r):
        r = r.lower()
        if r in self.rules.keys():
            rule = str(self.rules[r])
            rContent = rule.partition('$')
            rType = rContent[0]
            rValue = rContent[2]
            self.handleRule([rType, rValue])
        else:
            print("Rule unknown")
        

    def handleRule(self, rule):
        if(rule[0].lower()=="response"):
            print(rule[1])
        if(rule[0].lower()=="learn"):
            attrName = input(rule[1]+ ": ")
            attrVal = input("enter "+attrName+": ")
            self.learn(attrName, attrVal)
        if(rule[0].lower()=="action"):
            if(rule[1].lower()=="sum"):
                numb1 = int(input("Enther the first number:" ))
                numb2 = int(input("Enter the second number: "))
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
b.addRule("Add 2 numbers", "Action", "SUM")
b.forget("name")


l = str(input("Enter a command: "))

r = b.handleInput(l)



#formato de knowledge -->   attributeName:attributeValue
#formato de rule      -->   ruleName:RuleType$ruleValue



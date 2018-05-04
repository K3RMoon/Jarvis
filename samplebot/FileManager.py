import os.path
class FileManager:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.isfile(filename):
            cont = open(filename, "w")
            cont.close()
            
    def writeContent(self, diction):
        with open(self.filename, "w") as cont:
            for k in diction.keys():
                cont.write(k+":"+diction[k]+"\n")
    
    def getDictionary(self):
        fileDict = {}
        with open(self.filename) as fileContent:
            for line in fileContent:
                part = line.partition(":")
                fileDict[part[0]]=part[2].partition("\n")[0]
        return fileDict


from JarvisYacc import parser
import JarvisTools as JT
from JarvisYacc import currentBot


def execute_lines(lines):
    for line in lines:
        if lines == 'quit': break
        if not line: continue
        print(parser.parse(line))

code = ""
with open('Test.txt', 'r') as test:
    for l in test:
        code = code + l
    print(code)
    parser.parse(code)


#b = JT.bot("Kelvin")
l=""
while not(l.lower() == "quit"):
    l = str(input("Enter a command: "))
    r = currentBot.handleInput(l)
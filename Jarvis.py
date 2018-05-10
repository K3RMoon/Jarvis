from JarvisYacc import parser
import sys

def execute_lines(lines):
    for line in lines:
        if lines == 'quit': break
        if not line: continue
        print(parser.parse(line))

with open('Test.txt','r') as test:
    for l in test:
        parser.parse(l)
    l=""
    while not(l.lower() == "quit"):
        l = str(input("Enter a command: "))
        r = b.handleInput(l)
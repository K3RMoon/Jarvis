from JarvisYacc import parser
import JarvisTools as JT
from JarvisYacc import find_bot
import sys



def run_program(name):

    code = ""
    try:
        with open(name + '.jvs', 'r') as test:
            for l in test:
                code = code + l
            print(code)
            parser.parse(code)
    except FileNotFoundError:
        print("File "+name+".jvs doesn't exist")
        sys.exit()



    l=""
    while not(l.lower() == "quit"):
        l = str(input(">> "))
        if l != "quit":
            name_until = l.find(',')
            bot_name = l[:name_until]
            bot = find_bot(bot_name)
            if not bot:
                print("Bot " + bot_name + " was not created.")
            else:
                r = bot.handleInput(l[name_until+2:])


if __name__ == "__main__":
    name = sys.argv[1]
    run_program(name)

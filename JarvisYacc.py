import ply.yacc as yacc
import JarvisTools as JT
from JarvisLex import tokens


variables = []
rules = []
currentBot = None
thebots = []

def bot_in_use(bot):
    for robot in thebots:
        if robot.name == bot.name:
            return True
    return False

def name_in_use(name):
    for word in variables:
        if word == name:
            return True
    return False

def find_bot(name):
    for robot in thebots:
        if name == robot.name:
            return robot
    return False

def p_statement(p):
    '''statement : create_bot'''
    p[0] = p[1]
    pass

def p_response_rule(p):
    '''response_rule : STRING COLON RESPONSE LP STRING RP SEMICOLON'''
    p[0] = [p[1], "Response", p[5]]

def p_rules(p):
    '''rules : response_rule
                | rules response_rule'''
    p[0] = []
    if(len(p) > 2):
        p[0] = p[1]
        p[0].append(p[2])
    else:
        p[0] = [p[1]]

def p_create_bot(p):
    '''create_bot : ID LC rules RC'''
    try:
        if bot_in_use(p[1]):
            print('Error: Bot ' + p[1] + ' already exists.')
            return
        currentBot = JT.bot(p[1])
        thebots.append(currentBot)
        for rule in p[3]:
            currentBot.addRule(rule[0], rule[1], rule[2])
        currentBot = None
    except:
        print("Error in definition, cannot create bot.")

def p_error(p):
    print("ERROR: ")
    print(p)

# Build the parser
parser = yacc.yacc()



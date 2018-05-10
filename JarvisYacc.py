import ply.yacc as yacc
import JarvisTools as JT
from JarvisLex import tokens

variables = []
rules = []
bot = JT.bot("Kelvin")

def variable_in_use(name):
    for variable in variables:
        if variable.get_name == name:
            return True

    return False

def rule_in_use(name):
    for rule in rules:
        if rule.get_name == name:
            return True

    return False

def search_variable(name):
    for variable in variables:
        if variable.get_name == name:
            return variable


def search_rule(name):
    for rule in rules:
        if rule.get_name == name:
            return rule

def add_variable(name, value):
    if variable_in_use(name):
        print("Error: Duplicate Variable: " + name) #We might not need to print it directly TODO: Change to Error

    v = JT.Variable(name, value)
    variables.append(v)

def add_rule(name, delimeter, responses):
    if rule_in_use(name):
        print("Error: Duplicate Rule: " + name) #We might not need to print directly TODO: Change to Error
        return False

    r = JT.Rule(name, delimeter, responses)
    rules.append(r)
    return True

def p_response_rule(p):
    '''response_rule : STRING COLON RESPONSE LP STRING RP SEMICOLON'''
    print(p[1])
    print(p[5])
    bot.addRule(p[1], "Response", p[5])


# Build the parser
parser = yacc.yacc()



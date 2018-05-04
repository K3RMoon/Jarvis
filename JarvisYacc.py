import ply.yacc as yacc
import JarvisTools
from JarvisLex import tokens

variables = []
rules = []

def variable_in_use(name):
    for variable in variables:
        if variable.name == name:
            return True

    return False

def rule_in_use(name):
    for rule in rules:
        if rule.name == name:
            return True

    return False

def search_variable(name):
    for variable in variables:
        if variable.name == name:
            return variable


def search_rule(name):
    for rule in rules:
        if rule.name == name:
            return rule

def add_variable(name, value):
    if variable_in_use(name):
        print("Error: Duplicate Variable: " + name) #We might not need to print it directly TODO: Change to Error

   # v = variable(name, value)
   # variables.append(v)

def add_rule(name, delimeter, responses):
    if rule_in_use(name):
        print("Error: Duplicate Rule: " + name) #We might not need to print directly TODO: Change to Error
        return False

    #r = rule(name, delimeter, responses)
    #rules.append(r)
    return True

#def string_to_rule(ruleString):



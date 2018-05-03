import ply.lex as lex

#RESERVED WORDS

actions = {
    'RollDice': 'ROLLDICE',
    'Random': 'RANDOM',
    'Sum': 'SUM',
    'Multiply': 'MULTIPLY',
    'Divide': 'DIVIDE',
    'Subtract': 'SUBTRACT',
    'Modulo': 'Modulo',
    'Power': 'POWER',
    'Root': 'ROOT',
    'Joke': 'JOKE',
    #will likely trim down by removing file management actions
    'Save': 'SAVE',
    'Delete': 'DELETE',
    'Update': 'UPDATE',
    'Move': 'MOVE',
    #SearchImage may also be removed
    'SearchImage': 'SEARCHIMAGE',

}

reserved = {
    'Create': 'CREATE',
    'rules': 'RULES',
    'Response': 'RESPONSE',
    'Learn': 'LEARN',
    'Forget': 'FORGET',
    'Action': 'ACTION',

}

reserved.update(actions)


# TOKENS


tokens = [
    'NUMBER',   #done
    'UNKNOWN',  #done
    'ID',       #done
    'STRING',   #done
    'LP',
    'RP',
    'LC',
    'RC',
    'COMMA',
    'SEMICOLON',
    'COLON',
    'ADD',
   # 'QUOTES', #removed because Kelvin
    'PERIOD',
    'PLUS',
    'OR',
    'AND',
    'NOT'

] + list(reserved.values())

# Regular expressions rules for simple tokens

#Rule for Numbers (INT)
def t_NUMBER(t):
    r'(\d+)'
    return t

# Rule for Variables and Reserved Words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID') #Check for reserved words
    return t

#Unknown Character Token
t_UNKNOWN = r'\?'

#Rule for Strings
def t_STRING(t):
    r'(\"[a-zA-Z0-9_?!@#$%&*-+().,]*\")'
    return t

#Left Parenthesis Token
t_LP = r'('

#Right Parenthesis Token
t_RP = r')'

#Left Curly Token
t_LC = r'{'

#Right Curly Token
t_RC = r'}'

#Comma Curly Token
t_COMMA = r','

#Semicolon Token
t_SEMICOLON = r';'

#Colon Token
t_COLON = r':'

#Address Symbol Token
t_ADD = r'@'

#QUOTES = r'\"' #LIKELY NEEDS TO BE REMOVED BECAUSE ALREADY IMPLEMENTED.

#Period Symbol Token
t_PERIOD = r'.'

#Plus Symbol Token
t_PLUS = r'+'

#Or Token
t_OR = r'or'

#And Token
t_AND = r'and'

#Not Token
t_NOT = r'not'

#Ignored Characters
t_ignore = ' \t\n'

#Error
def t_error(t):
    print("Illegal Character '%s'" % t.value[0])
    t.lexer.skip(1)

#Build Lexer
lexer = lex.lex()



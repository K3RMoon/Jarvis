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
    'NUMBER',
    'UNKNOWN',
    'ID',
    'STRING',
    'LP',
    'RP',
    'LC',
    'RC',
    'COMMA',
    'SEMICOLON',
    'COLON',
    'ADD',
    'QUOTES',
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

#Rule for unknown characters
t_UNKNOWN = r'\?'

def t_STRING(t):
    r'(\"[a-zA-Z0-9_?!@#$%&*-+().,]*\")'
    return t








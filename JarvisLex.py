import ply.lex as lex

#Reserved Words

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







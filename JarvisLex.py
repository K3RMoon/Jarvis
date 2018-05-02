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
    'Save': 'SAVE',
    'Delete': 'DELETE',
    'Update': 'UPDATE',
    'Move': 'MOVE',
    'Joke': 'JOKE',
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







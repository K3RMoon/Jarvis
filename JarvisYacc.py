import ply.yacc as yacc
import JarvisTools as JT
from JarvisLex import tokens


variables = []
rules = []
currentBot = None
thebots = []

def bot_in_use(bot):
    for robot in thebots:
        if robot.name == bot:
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


#Esto lo usa el parser pa saber cuales son las instrucciones basicas, que nadie depende de ellas. En este caso solo tenemos
#Una, que es la creacion del bot con todas sus reglas.
def p_statement(p):
    '''statement : create_bot
                    | statement create_bot'''
    p[0] = p[1]
    pass

#---------------------------------------------------------------------------------------------------------------

#RULES:





#Este seria el syntax de los rules que son Response.
#Por ejemplo: "Hi" : Response("Hello!"); <- el caso simple
#Pero hay que a~adir casos como Response(name) //Una variable
#Y Response("Hello " + name) <- este va a ser un poco mas tricky etc
def p_response_rule(p):
    '''response_rule : STRING COLON RESPONSE LP STRING RP SEMICOLON'''
    p[0] = [p[1], "Response", "\""+p[5]+"\""] #p[0] es lo que devuelve, y quiero devolver un array con los parametros que addRule
                                        #necesita, en este caso el String del usuario (p[1]), la palabra 'Response', y el String
                                        # de contestacion (p[5]
def p_response_rule1(p):
    '''response_rule : STRING COLON RESPONSE LP ID RP SEMICOLON'''
    # name =
    p[0] = [p[1], "Response", p[5]]
def p_response_rule2(p):
    '''response_rule : STRING COLON RESPONSE LP STRING PLUS ID RP SEMICOLON'''
    p[0] = [p[1], "Response", p[5]+" "+ p[7]]
def p_response_rule3(p):
    '''response_rule : STRING COLON RESPONSE LP ID PLUS STRING RP SEMICOLON'''
    p[0] = [p[1], "Response", p[5]+" "+ p[7]]





#Same as response but with learn
def p_learn_rule(p):
    '''learn_rule : STRING COLON LEARN LP ID RP SEMICOLON'''
    p[0] = [p[1], "Learn", p[5]]



def p_forget_rule(p):
    '''forget_rule : STRING COLON FORGET LP ID RP SEMICOLON'''
    p[0] = [p[1], "Forget", p[5]]


#Same as response pero con action
#Aqui hay diferentes posibilidades por cada action, pero en cuestion de lo que hay que mandar pa p[0], seria cambiar
#El tipo de action que es, sooo hay que verificar que esta en p[5] antes de mandarle al p[0] lo que es
def p_action_rule(p):
    '''action_rule : STRING COLON ACTION PERIOD SUM LP ID COMMA ID RP SEMICOLON
                    | STRING COLON ACTION PERIOD SUBTRACT LP ID COMMA ID RP SEMICOLON
                    | STRING COLON ACTION PERIOD MULTIPLY LP ID COMMA ID RP SEMICOLON
                    | STRING COLON ACTION PERIOD POWER LP ID COMMA ID RP SEMICOLON
                    | STRING COLON ACTION PERIOD JOKE LP RP SEMICOLON
                    | STRING COLON ACTION PERIOD ROLLDICE LP RP SEMICOLON
                    | STRING COLON ACTION PERIOD ROOT LP ID RP SEMICOLON
                    | STRING COLON ACTION PERIOD DIVIDE LP ID COMMA ID RP SEMICOLON
                    | STRING COLON ACTION PERIOD MODULO LP ID COMMA ID RP SEMICOLON
                    | STRING COLON ACTION PERIOD RANDOM LP RP SEMICOLON'''

    if p[5] == "Sum":
        p[0] = [p[1], "Action", "SUM"]
    elif p[5] == "Subtract":
        p[0] = [p[1], "Action", "SUBTRACT"]
    elif p[5] == "Multiply":
        p[0] = [p[1], "Action", "MULTIPLY"]
    elif p[5] == "Power":
        p[0] = [p[1], "Action", "POWER"]
    elif p[5] == "Joke":
        p[0] = [p[1], "Action", "JOKE"]
    elif p[5] == "RollDice":
        p[0] = [p[1], "Action", "ROLLDICE"]
    elif p[5] == "Root":
        p[0] = [p[1], "Action", "ROOT"]
    elif p[5] == "Divide":
        p[0] = [p[1], "Action", "DIVIDE"]
    elif p[5] == "Modulo":
        p[0] = [p[1], "Action", "MODULO"]
    elif p[5] == "Random":
        p[0] = [p[1], "Action", "RANDOM"]


#----------------------------------------------------------------------------------------------------------------------

#Estas son todas las posibilidades de rules que puede tener un bot: Response, Learn, Action y combinaciones de ellas
#Esto seria lo que iria dentro de los { } en el create_bot, y se le manda de aqui al create_bot.
def p_rules(p):
    '''rules : response_rule
                | learn_rule
                | action_rule
                | rules response_rule
                | rules action_rule
                | rules learn_rule'''
    p[0] = [] #IMPORTANT: p[0] es lo que este metodo devuelve, so en este caso, yo quiero que p[0] tenga un array con
                # todos los rules que el bot va a tener.
    if(len(p) > 2): #por si es mas de 1 rule
        p[0] = p[1]
        p[0].append(p[2])
    else:
        p[0] = [p[1]] #si es solo 1 rule (response, action, o learn)




#Basically el que hace el trabajo de crear los bots. Le llega algo como Jarvis{ rules } donde rules es la lista de
#rules que el tiene. En este caso rules devuelve un array con 3 valores, que deben ser los 4 parametros que van
#dentro del metodo addRule. El rebolu de los lengths es para cortar los strings y no tengan las comillas.
def p_create_bot(p):
    '''create_bot : ID LC rules RC'''
    try:
    #if True:
        if bot_in_use(p[1]): #para que no se permita crear 2 bots con el mismo nombre en el mismo file
            print('Error: Bot ' + p[1] + ' already exists.')
            return
        currentBot = JT.bot(p[1])
        thebots.append(currentBot)
        #A~adiendo las reglas al bot
        for rule in p[3]:
            rule2 = rule[2]
            if ((rule[2][0])=='\"' and (rule[2][(len(rule[2])-1)])=='\"'):
                rule2 = rule[2][1:(len(rule[2])-1)]

            currentBot.addRule(rule[0][1:(len(rule[0])-1)], rule[1], rule2)
        currentBot = None
    except:
        print("Error in definition, cannot create bot.")





#Por si se recibe un error
def p_error(p):
    print("ERROR: ")
    print(p)

# Build the parser
parser = yacc.yacc()



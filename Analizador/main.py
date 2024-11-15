import ply.yacc as yacc
from lexico import tokens

# def p_programa(p):
#     '''programa : sentencias
#     | sentencias programa'''

# def p_sentencias(p):
#     '''sentencias : asignacion
#             | impresion
#             | comparacionEntero'''


def p_asignacion(p):
    'asignacion : VARIABLE ASIG operaAritmetica'

def p_operaAritmetica(p):
    '''operaAritmetica : valor
                        | valor operadorArit operaAritmetica'''


def p_valor(p):
    '''valor : INTEGER
            | FLOAT
            | VARIABLE'''
def p_operadorArit(p):
    '''operadorArit : PLUS
                | MINUS
                | MULT
                | DIVIDE
                | MOD '''

# Regla para definir un error
def p_error(p):
    print("Error de sintaxis en la línea %d" % p.lineno)

# Construir el parser
parser = yacc.yacc()

while True:
    try:
        s = input('python > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
import ply.yacc as yacc
from lexico import tokens
import logGo as logGo

# Logger
logGo.setup_module_logger(__name__)

def p_programa(p):
    '''programa : sentencia
                | sentencia programa'''

def p_sentencia(p):
    '''sentencia : impresion
                | asignacion
                | declararVariables
                | defFuncion
                | funcion
                | for
                | incrementadores'''

def p_declararVariables(p):
    '''declararVariables : VAR VARIABLE tipo
                        | VAR VARIABLE LCORCH INTEGER RCORCH tipo
                        | VAR VARIABLE LCORCH RCORCH tipo'''

# IF-ELSE SWITCH FOR
# FOR
def p_for(p):
    '''for : forClasico
            | forTipoWhile
            | forRango'''

def p_cuerpoEstructura(p): #Se puede usar en todas
    '''cuerpoEstructura : L_LLAVE programa R_LLAVE'''

def p_forClasico(p):
    'forClasico : FOR asignacion PUNTO_Y_COMA expresionBooleana PUNTO_Y_COMA incrementadores cuerpoEstructura'

def p_forTipoWhile(p):
    'forTipoWhile : FOR expresionBooleana cuerpoEstructura'

def p_forRango(p):
    '''forRango : FOR parametros RANGE coleccion cuerpoEstructura'''

# ESTRUCTURA DE DATOS
def p_coleccion(p):
    '''coleccion : array
                | slice'''

def p_array(p):
    '''LCORCH INTEGER RCORCH tipo L_LLAVE parametros R_LLAVE'''

def p_slice(p):
    '''LCORCH RCORCH tipo L_LLAVE parametros R_LLAVE'''


# IMPRESION
def p_impresion(p):
    '''impresion : impresionSinSalto
                | impresionConSalto
                | impresionEspecial'''

def p_impresionSinSalto(p):
    '''impresionSinSalto : FMT PUNTO PRINT LPARENT parametros RPARENT
                | FMT PUNTO PRINT LPARENT RPARENT
                | FMT PUNTO PRINT LPARENT CADENA RPARENT
                | FMT PUNTO PRINT LPARENT CADENA COMMA parametros RPARENT'''

def p_impresionConSalto(p):
    '''impresionConSalto : FMT PUNTO PRINTLN LPARENT parametros RPARENT
                | FMT PUNTO PRINTLN LPARENT RPARENT
                | FMT PUNTO PRINTLN LPARENT CADENA RPARENT
                | FMT PUNTO PRINTLN LPARENT CADENA COMMA parametros RPARENT'''

def p_impresionEspecial(p):
    '''impresionEspecial : FMT PUNTO SPRINTF LPARENT CADENA COMMA parametros RPARENT
                | FMT PUNTO SPRINTF LPARENT RPARENT'''

# PEDIR DATOS POR CONSOLA
def p_pedirPorPantalla(p):
    'pedirPorPantalla : FMT PUNTO SCANFLN LPARENT AMPERSAND VARIABLE RPARENT'

# DEFINICIÓN DE UNA FUNCIÓN
def p_defFuncion(p):
    '''defFuncion : FUNC VARIABLE LPARENT defParametros RPARENT tipo L_LLAVE cuerpoFuncion R_LLAVE'''

def p_defParametros(p):
    '''defParametros : defParametro
                | defParametro COMMA defParametros'''

def p_defParametro(p):
    '''defParametro : VARIABLE tipo'''

def p_cuerpoFuncion(p):
    '''cuerpoFuncion : retorno
                | sentencia cuerpoFuncion'''

def p_retorno(p):
    '''retorno : RETURN expresion'''


# USO DE UNA FUNCIÓN
def p_funcion(p):
    '''funcion : VARIABLE LPARENT parametros RPARENT
                | VARIABLE LPARENT RPARENT'''

def p_parametros(p):
    '''parametros : parametro
                | parametro COMMA parametros'''

def p_parametro(p):
    '''parametro : expresion'''


#ASIGNACIÓN
def p_asignacion(p):
    '''asignacion : VARIABLE ASIG expresion
                | VARIABLE ASIG expresionBooleana'''

def p_expresion(p):
    '''expresion : valor
                | valor operadorArit expresion
                | VARIABLE operadorArit expresion'''

def p_expresionBooleana(p):
    '''expresionBooleana : VARIABLE operadorMat VARIABLE
                            VARIABLE operadorMat Valor'''

def p_valor(p):
    '''valor : INTEGER
                | booleano
                | FLOAT
                | STRING
                | VARIABLE
                | coleccion'''

def p_tipo(p):
    '''tipo : INT
            | INT16
            | INT32
            | INT64
            | UINT
            | UINT16
            | UINT32
            | UINT64
            | BOOL
            | FLOAT32
            | FLOAT64
            | COMPLEX64
            | COMPLEX128
            | STRING
            '''

def p_operadorArit(p):
    '''operadorArit : PLUS
                | MINUS
                | MULT
                | DIVIDE
                | MOD '''

def p_operadorMat(p):
    '''operadorMat : EQ
                | MENOR_QUE
                | MAYOR_QUE
                | MAYOR_IGUAL
                | MENOR_IGUAL
                '''

def p_incrementadores(p):
    '''incrementadores : VARIABLE INCREMENTADOR
                        | VARIABLE DECREMENTADOR
                        '''

def p_booleano(p):
    '''booleano : TRUE
                | FALSE'''

# Regla para definir un error
def p_error(p):
    logGo.log_warning(__name__, "Error de sintaxis en la línea %d" %p.lineno)

# Construir el parser
parser = yacc.yacc()

while True:
    try:
        s = input('python > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    logGo.log_info(__name__, result)
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
                | if_else
                | for
                | pedirPorPantalla
                | incrementadores
                | map
                | asignarValoresMap
                | switch
                | casos
                | expresionBooleana
                | struct
                | package
                | imports'''

# VARIABLES
def p_declararVariables(p):
    '''declararVariables : VAR VARIABLE tipo
                        | VAR VARIABLE LCORCH INTEGER RCORCH tipo
                        | VAR VARIABLE LCORCH RCORCH tipo
                        | claveValorMap'''

def p_package(p):
    '''package : PACKAGE VARIABLE'''

def p_imports(p):
    '''imports : IMPORT LPARENT variasCadenas RPARENT'''

def p_variasCadenas(p):
    '''variasCadenas : CADENA
                    | CADENA COMA variasCadenas'''

# STRUCTs

def p_struct(p):
    '''struct : defStruct
                | newStructInst
                | structInst'''

def p_defStruct(p):
    '''defStruct : TYPE VARIABLE STRUCT L_LLAVE defCampos R_LLAVE
                | VAR VARIABLE IGUAL STRUCT L_LLAVE defCampos R_LLAVE L_LLAVE campos R_LLAVE'''

def p_defCampos(p):
    '''defCampos : defCampo
                | defCampo COMA defCampos'''

def p_defCampo(p):
    '''defCampo : VARIABLE tipo'''

def p_campos(p):
    '''campos : campo
                | campo COMA campos'''

def p_campo(p):
    '''campo : VARIABLE DOS_PUNTOS valor'''

def p_newStructInst(p):
    '''newStructInst : VARIABLE ASIG NEW LPARENT VARIABLE RPARENT'''

def p_structInst(p):
    '''structInst : VARIABLE L_LLAVE campos R_LLAVE
                | VARIABLE L_LLAVE parametros R_LLAVE'''


# IF-ELSE
def p_if_else(p):
    '''if_else : estructuraIf
                | estructuraIf estructuraElse'''

def p_estructuraIf(p):
    '''estructuraIf : IF expresionBooleana cuerpoEstructura'''

def p_estructuraElse(p):
    '''estructuraElse : ELSE estructuraIf
                | ELSE cuerpoEstructura
                | ELSE estructuraIf estructuraElse'''

def p__switch(p):
    '''switch : switchNoParametros
                | switchParametro'''
# SWITCH
def p_switchParametro(p):
    '''switchParametro : SWITCH parametros L_LLAVE casos R_LLAVE'''
def p_switchNoParametros(p):
    '''switchNoParametros : SWITCH  L_LLAVE casos R_LLAVE'''

def p_casos(p):
    '''casos : CASE expresionBooleana DOS_PUNTOS  programa
    | CASE parametros DOS_PUNTOS  programa'''

# FOR
def p_for(p):
    '''for : forClasico
            | forTipoWhile
            | forRango'''

# Se puede usar en todas
def p_cuerpoEstructura(p):
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
    '''array : LCORCH INTEGER RCORCH tipo L_LLAVE parametros R_LLAVE'''

def p_slice(p):
    '''slice : LCORCH RCORCH tipo L_LLAVE parametros R_LLAVE'''

def p_map(p): 
    '''map : declaracionMap 
            | makeMap '''
    
def p_declaracionMap(p):
    '''declaracionMap : VAR VARIABLE MAP LCORCH tipo RCORCH tipo
                    | VARIABLE ASIG MAP LCORCH tipo RCORCH tipo
                    | VARIABLE ASIG MAP LCORCH tipo RCORCH tipo cuerpoEstructura'''
def p_makeMap(p):
    '''makeMap : VARIABLE ASIG MAKE LPARENT MAP LCORCH tipo RCORCH tipo RPARENT
            | VARIABLE ASIG MAKE LPARENT MAP LCORCH tipo RCORCH tipo RPARENT cuerpoEstructura'''
def p_asignarValoresMap(p):
    '''asignarValoresMap : asignarValorMap 
                        | asignarValorMap  asignarValoresMap'''
def p_asignarValorMap(p):
    '''asignarValorMap : valor DOS_PUNTOS valor
                | valor DOS_PUNTOS valor COMA'''
def p_claveValorMap(p):
    '''claveValorMap : VARIABLE LCORCH CADENA RCORCH IGUAL valor'''



# IMPRESION
def p_impresion(p):
    '''impresion : impresionSinSalto
                | impresionConSalto
                | impresionEspecial'''

def p_impresionSinSalto(p):
    '''impresionSinSalto : FMT PUNTO PRINT LPARENT parametros RPARENT
                | FMT PUNTO PRINT LPARENT RPARENT
                | FMT PUNTO PRINT LPARENT CADENA RPARENT
                | FMT PUNTO PRINT LPARENT CADENA COMA parametros RPARENT'''

def p_impresionConSalto(p):
    '''impresionConSalto : FMT PUNTO PRINTLN LPARENT parametros RPARENT
                | FMT PUNTO PRINTLN LPARENT RPARENT
                | FMT PUNTO PRINTLN LPARENT CADENA RPARENT
                | FMT PUNTO PRINTLN LPARENT CADENA COMA parametros RPARENT'''

def p_impresionEspecial(p):
    '''impresionEspecial : FMT PUNTO SPRINTF LPARENT CADENA COMA parametros RPARENT
                | FMT PUNTO SPRINTF LPARENT RPARENT'''


# PEDIR DATOS POR CONSOLA
def p_pedirPorPantalla(p):
    'pedirPorPantalla : FMT PUNTO SCANLN LPARENT AMPERSAND VARIABLE RPARENT'


# DEFINICIÓN DE UNA FUNCIÓN
def p_defFuncion(p):
    '''defFuncion : FUNC VARIABLE LPARENT defParametros RPARENT tipo L_LLAVE cuerpoFuncion R_LLAVE'''

def p_defParametros(p):
    '''defParametros : defParametro
                | defParametro COMA defParametros'''

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
                | parametro COMA parametros'''

def p_parametro(p):
    '''parametro : expresion'''


# ASIGNACIÓN
def p_asignacion(p):
    '''asignacion : VARIABLE ASIG expresion
                | VARIABLE ASIG expresionBooleana'''


# EXPRESIONES
def p_expresion(p):
    '''expresion : valor
                | expresion operadorArit expresion'''

def p_expresionBooleana(p):
    '''expresionBooleana : booleano
                | expresion operadorOrd expresion'''


# VALORES Y TIPOS DE DATOS
def p_valor(p):
    '''valor : INTEGER
                | FLOAT
                | CADENA
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


# OPERADORES
def p_operadorArit(p):
    '''operadorArit : SUM
                | MENOS
                | MULT
                | DIVISION
                | MOD '''

def p_operadorOrd(p):
    '''operadorOrd : EQ
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
    if p:
        error = f"Error de sintaxis de token '{p.value}' de tipo: '{p.type}' en la línea {p.lineno}"
    else:
        error= "Error de sintaxis en EOF"
    logGo.log_warning(__name__, error)

# Construir el parser
parser = yacc.yacc()

print("Ingresa tu código. Finaliza con una línea vacía o EOF (Ctrl+D/Ctrl+Z).")

while True:
    try:
        print("python > ", end="")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        s = "\n".join(lines)  # Combina todas las líneas en una sola entrada
    except EOFError:
        break

    if not s.strip():
        continue  # Si no hay entrada real, pasa al siguiente ciclo

    try:
        result = parser.parse(s)
        print("Resultado:", result)
    except Exception as e:
        print("Error al analizar:", e)
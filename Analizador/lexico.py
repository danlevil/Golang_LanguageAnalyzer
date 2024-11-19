import ply.lex as lex
import leerGo as leerGo
import logGo as logGo

# ALEX PEÑAFIEL
reservadas = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'true': 'TRUE',
    'false': 'FALSE',
    'struct':'STRUCT',
    'switch':'SWITCH',
    'break':'BREAK',
    'case':'CASE',
    'const':'CONST',
    'continue':'CONTINUE',
    'default':'DEFAULT',
    'func':'FUNC',
    'import':'IMPORT',
    'inteface':'INTERFACE',
    'map':'MAP',
    'new': 'NEW',
    'range':'RANGE',
    'return':'RETURN',
    'type':'TYPE',
    'var':'VAR',
    'package':'PACKAGE',
    'int':'INT',
    'int16':'INT16',
    'int32':'INT32',
    'int64':'INT64',
    'uint':'UINT',
    'uint16':'UINT16',
    'uint32':'UINT32',
    'uint64':'UINT64',
    'bool':'BOOL',
    'float32':'FLOAT32',
    'float64':'FLOAT64',
    'complex64':'COMPLEX64',
    'complex128':'COMPLEX128',
    'string':'STRING',
    'fmt':'FMT',
    'Println':'PRINTLN',
    'Print':'PRINT',
    'Sprintf':'SPRINTF',
    'Scanln':'SCANLN',
    'make' : 'MAKE'
}
# Daniel Villamar
tokens = (
    "INCREMENTADOR",
    "DECREMENTADOR",
    "COMENTARIO_LINEA",
    "COMENTARIO_BLOQUE",
    "PLACEHOLDER",
    "CADENA",
    "VARIABLE",
    "INTEGER",
    "FLOAT",
    "SUM",
    "MENOS",
    "MULT",
    "DIVISION",
    "MOD",
    "EQ",
    "ASIG",
    "LPARENT",
    "RPARENT",
    "LCORCH",
    "RCORCH",
    "L_LLAVE",
    "R_LLAVE",
    "PUNTO",
    "DOS_PUNTOS",
    "COMA",
    "COMILLA",
    "COMILLA_SIMPLE",
    "IGUAL",
    "SEPARADOR",
    "PUNTO_Y_COMA",
    "MAYOR_IGUAL",
    "MENOR_IGUAL",
    "MENOR_QUE",
    "MAYOR_QUE",
    "AMPERSAND",
) + tuple(reservadas.values())

#Alex Peñafiel
t_AMPERSAND = r'&'
t_INCREMENTADOR = r'\+\+'
t_DECREMENTADOR = r'--'
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='

# Daniel Villamar
t_SUM = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_MOD = r"%"
t_EQ = r"=="
t_ASIG = r":="
t_IGUAL = r"="
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LCORCH = r"\["
t_RCORCH = r"\]"
t_L_LLAVE = r"\{"
t_R_LLAVE = r"\}"
t_PUNTO = r"\."
t_DOS_PUNTOS = r":"
t_COMA = r","
t_COMILLA = r'"'
t_COMILLA_SIMPLE = r"'"
t_SEPARADOR = r"\|"
# Ronald Gaibor
t_PUNTO_Y_COMA = r";"
t_MENOR_QUE = r"<"
t_MAYOR_QUE = r">"





#INICIO DE LAS EXPRESIONES REGULARES

def t_COMENTARIO_LINEA(t):
    r'//.*'
    pass

def t_COMENTARIO_BLOQUE(t):
    r'/\*([\s\S]*?)\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

def t_DIVISION(t):
    r'/'
    return t

def t_FLOAT(t):
    r'[0-9]*\.[0-9]+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PLACEHOLDER(t):
    r'%[sdf]'  # Captura %s, %d, %f, etc.
    return t

def t_CADENA(t):
    r'"([^"\\]|\\.)*"'
    return t

def t_VARIABLE(t):
    r'[a-zA-Z]\w*'
    t.type = reservadas.get(t.value, "VARIABLE")
    return t

def t_nuevaLinea(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    logGo.logging.warning("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

#FIN DE LAS EXPRESIONES REGULARES


"""
Daniel Villamar:
Esta línea de codigo hace uso de la función para leer el codigo Go, retornando en un string largo el cual será analizado por el lexer"
"""


'''  <----PARA PROBAR LA FUNCIONALIDAD DEL LEXER DESCOMENTAR
data=leerGo.codigo_go

lexer.input(data)
while True:

    tok = lexer.token()
    if not tok:
        break  # No more input
    logGo.logging.info(tok)
    
    <----PARA PROBAR LA FUNCIONALIDAD DEL LEXER DESCOMENTAR
'''
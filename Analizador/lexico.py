import ply.lex as lex
import leerGo as leerGo
import logGo as logGo

# ALEX PEÑAFIEL
reserved = {
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
    'Scanln':'SCANLN'
}
# Daniel Villamar
tokens = (
    "COMMENT_LINE",
    "COMMENT_BLOCK",
    "PLACEHOLDER",
    "CADENA",
    "VARIABLE",
    "INTEGER",
    "FLOAT",
    "PLUS",
    "MINUS",
    "MULT",
    "DIVIDE",
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
    "COMMA",
    "COMILLA",
    "COMILLA_SIMPLE",
    "IGUAL",
    "SEPARADOR",
    "PUNTO_Y_COMA",
    "MENOR_QUE",
    "MAYOR_QUE",
    "AMPERSAND",
) + tuple(reserved.values())

# Daniel Villamar
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_MOD = r"%"
t_EQ = r"=="
t_ASIG = r":="
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LCORCH = r"\["
t_RCORCH = r"\]"
t_L_LLAVE = r"\{"
t_R_LLAVE = r"\}"
t_PUNTO = r"\."
t_DOS_PUNTOS = r":"
t_COMMA = r","
t_COMILLA = r'"'
t_COMILLA_SIMPLE = r"'"
t_IGUAL = r"="
t_SEPARADOR = r"\|"

# Ronald Gaibor
t_PUNTO_Y_COMA = r";"
t_MENOR_QUE = r"<"
t_MAYOR_QUE = r">"

t_AMPERSAND = r'&'

#INICIO DE LAS EXPRESIONES REGULARES

def t_COMMENT_LINE(t):
    r'//.*'
    pass

def t_COMMENT_BLOCK(t):
    r'/\*([\s\S]*?)\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

def t_DIVIDE(t):
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
    t.type = reserved.get(t.value, "VARIABLE")
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    logGo.logging.warning("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

#FIN DE LAS EXPRESIONES REGULARES

"""Daniel Villamar:
Esta línea de codigo hace uso de la función para leer el codigo Go, retornando en un string largo el cual será analizado por el lexer"
"""
# data=leerGo.codigo_go

'''
lexer.input(data)
while True:

    tok = lexer.token()
    if not tok:
        break  # No more input
    logGo.logging.info(tok)
'''
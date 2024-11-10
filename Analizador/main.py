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
    'return':'return',
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
    'fmt.Println':'FMT.PRINTLN',
    'fmt.Print':'FMT.PRINT',
    'fmt.Sprintf':'FMT.SPRINTF'
}
# Daniel Villamar
tokens = (
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
    "COMA",
    "COMILLA",
    "COMILLA_SIMPLE",
)

# Daniel Villamar
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIVIDE = r'/'
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
t_COMA = r","
t_COMILLA = r'"'
t_COMILLA_SIMPLE = r"'"


#INICIO DE LAS EXPRESIONES REGULARES

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    logGo.logging.warning("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



#FIN DE LAS EXPRESIONES REGULARES

"""Daniel Villamar:
Esta línea de codigo hace uso de la función para leer el codigo Go, retornando en un string largo el cual será analizado por el lexer"
"""
data=leerGo.codigo_go


lexer = lex.lex()
lexer.input(data)
while True:

    tok = lexer.token()
    if not tok:
        break  # No more input
    logGo.logging.info(tok)

import ply.lex as lex

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
    'Println':'PRINTLN'
}
# Daniel Villamar
tokenslist = (
    "INTEGER",
    "FLOAT",
    "PLUS",
    "MINUS",
    "MULT",
    "DIVIDE",
    "MOD",
    "EQ",
    "ASIG",
    "LPARENT"
    "DPARENT"
    "LCORCH",
    "RCORCH",
    "L_LLAVE",
    "R_LLAVE",
    "PUNTO",
    "DOS_PUNTOS"
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
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCORCH = r"["
t_RCORCH = r"]"
t_L_LLAVE = r"{"
t_R_LLAVE = r"}"
t_PUNTO = r"."
t_DOS_PUNTOS = r":"
t_COMA = r","
t_COMILLA = r'"'
t_COMILLA_SIMPLE = r"'"


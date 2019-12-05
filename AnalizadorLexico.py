# -*- coding: utf-8 -*-
# desarollo de aanalizardor lexico
#liga https://github.com/GeovaniTuz/PythonU4and5

import ply.lex as lex  # inportacion de librerias necesarias
import re

resultado_lexema = []


tokens = [
    # inicio y final
    'TAGINICIO', 'TAG_FINAL',

    'IDENTIFICADOR', 'ENTERO', 'ASIGNAR', 'SUMA', 'RESTA', 'MULT', 'DIV', 'POTENCIA', 'MODULO',
    'MINUSMINUS', 'PLUSPLUS','PUNTOYCOMA','PUNTO','COMA','DECIMAL','VARIABLE','COMENTARIO',
    # Condiones
    'SI', 'SINO', 'SIErr',
    # Ciclos
    'MIENTRAS', 'PARA',
    # logica
    'AND', 'OR', 'NOT', 'MENORQUE', 'MENORIGUAL', 'MAYORQUE', 'MAYORIGUAL', 'IGUAL', 'DISTINTO',
    # Symbolos
    'NUMERAL', 'PARIZQ', 'PARDER', 'CORIZQ', 'CORDER', 'LLAIZQ', 'LLADER'
]

# Reglas de Expresiones Regualres para token de Contexto simple
#t_PUNTO = r'[+,-]?[[0-9]*[.]]?[0-9]+'
#[+,-]?[[0-9]*[.]]?[0-9]+t__COMA = r'\,'
t_PUNTOYCOMA = r';'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MINUSMINUS = r'\-\-'
#t_PUNTO = r'\.'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'
t_ASIGNAR = r'='
# Expresiones
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'

# --------------------------------------------------
# desarrollo de tag_inicio y final
# no solucionado

# def t_TAGINICIO(t):
#  r'(<+[php]>)'
# return t

# tag final
# --------------------------------------------------

def t_TAGINICIO(t):
    r'(<+[\?+php]+)'
    return t

def t_TAG_FINAL(t):
    r'([\?>]+)'
    return t

def t_DECIMAL(t):
    r'([0-9][.]]?[0-9]+)'
    return t

def t_VARIABLE(t):
    r'([\$]+[A-Za-z]+)'
    return t

def t_SINO(t):
    r'else'
    return t

#recorte

#recorte
text = ""
for linea in archivo:
    text += linea
prueba(text)
print('\n'.join(list(map(''.join, resultado_lexema)))) #AL IMPRIMIR LOS DATOS, ESTO LO ORDENA DE MANERA ESTRUCTURADA

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import ply.lex as lex
import src.tokrules

import ply.yacc as yacc
from src.parser import *

lexer = lex.lex(module=src.tokrules)
parser = yacc.yacc()

from src.repr import λ_term_to_str

tests = [
        "test = 5 .",
        "test = 5+c : nil .",
        "test = (\\x.x) .",
        'test = (λx.λy.y+x) .',
        'test = (a b) c .',
        'test = a b c .',
        'test = λx.λy.y+x 3 /= 6 .',
        "test = λx.λy.y+x' 3 .",
        'test = λx.λy.y+x l .',
        'test = (λx.λy.y+x) 3 .',
        'test = (λx. λy. x y x) (λy. λx. y (x y x)) .',
        'test = (λx.(λy.((x) (y)(x)))) (λy.(λx.((y) ((x) (y)(x))))) .',
        'test = λf.(λx.x x) (λx.f (x x)) .',
        "test = \"hi\": ' another string' .",
        "test = (f) a b c .",
        "test = (\\x.x) a b c .",
        "test = (f x) a b c .",
]

for s in tests:
    print()
    print("expresion:", repr(s))

    print()
    ast = parser.parse(s)
    print( λ_term_to_str(ast['test']) )
    print()
    print( ast['test'] )
    print()

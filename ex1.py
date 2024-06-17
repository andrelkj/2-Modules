"""
Módulo de strings

Escreva um módulo em python para tratar algumas strings e que possua as seguintes funcionalidades:

1. Inverter uma string de trás pra frente.
2. Retornar apenas letras com índice par.
3. Retornar apenas letras com índice ímpar.

string.py module created
"""

import strings

sentence = input("Enter a sentence:\n")

print(strings.invert(sentence))
print(strings.even_character(sentence))
print(strings.odd_character(sentence))

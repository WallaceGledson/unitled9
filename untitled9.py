# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yVd9xnoVrey2jVunlP5bHX_04N3QGQG4
"""

from random import randint 
frutas = ['manga','abacaxi','morango','maracuja','melao']
times = ['flamengo','botafogo','fluminense','vasco','gremio']
pessoas = ['davi','lucas','samuel','wollas','beatriz']
listadeacerto = []
listadeerro = []
categorias=randint(1,3)
if categorias == 2:
    davi = 'pessoas'
    nSecreta = pessoas[randint(0,4)]
    print(f'a categoria e {davi} e tem {len(x)} letras')

elif categorias == 3:
    davi = 'times'
    nSecreta = times[randint(0,4)] 
    print(f'a categoria e {davi} e tem {len(x)} letras') 
elif categorias == 1: 
    nSecreta = frutas[randint(0,4)]
    davi = 'frutas'
    print(f'a categoria e {davi} e tem {len(x)} letras')
print(nSecreta)
x = nSecreta.replace(' ', '')
print(f'a categoria e {davi} e tem {len(x)} letras')
c = 5 
while
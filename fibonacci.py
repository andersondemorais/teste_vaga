# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "20-jun-2022"
__version__ = ""
__status__ = ""

"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
"""

# inserir o valor a ser testado nesta variavel
valor = 59

anterior, atual = 0,1

def fib(numero: int)-> int:
    global anterior
    global atual
    
    while anterior < numero:
        anterior, atual = atual, anterior+atual
     
    return anterior

def main():
    if fib(valor)==valor:
        print(f'O numero {valor} pertence a sequencia de fibonacci')
    else:
        print(f'O numero {valor} nao pertence a sequencia de fibonacci')

if __name__=="__main__":
    main()

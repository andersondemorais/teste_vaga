# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "20-jun-2022"
__version__ = ""
__status__ = ""

"""
Escreva um programa que inverta os caracteres de um string.
"""

# string a ser invertida
frase = "Porcentagem de SP = 37.53"

def inverte_str(frase: str)-> str:
    ultima_letra: int = len(frase) - 1
    frase_inversa: str = ""
    
    while ultima_letra >= 0:
        frase_inversa += frase[ultima_letra]
        ultima_letra-= 1
    return frase_inversa

def main():
    print(inverte_str(frase))

if __name__=="__main__":
    main()

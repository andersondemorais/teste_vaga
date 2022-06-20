# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "20-jun-2022"
__version__ = ""
__status__ = ""

"""
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53
Escreva um programa na linguagem que desejar onde calcule o percentual de representação 
que cada estado teve dentro do valor total mensal da distribuidora.
"""

faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53,
}
porcentagem = {
    'SP': 0, 'RJ': 0, 'MG': 0, 'ES': 0, 'Outros': 0,
}

def calcula_percentual()-> None:
    soma_total: int = sum(faturamento.values())
    soma_perc: float = 100/soma_total
    
    for key, value in faturamento.items():
        porcentagem[key] = round(value * soma_perc, 2)

def main():
    calcula_percentual()
    
    for key, value in porcentagem.items():
        print(f'Porcentagem de {key} = {value}')

if __name__=="__main__":
    main()

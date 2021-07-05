"""
Descrição do problema:
Na matemática, um número perfeito é um número inteiro em que a soma de seus divisores (exceto ele mesmo)
é igual ao próprio número.
Por exemplo, o número 6 é perfeito, pois a soma de seus divisores (1 + 2 + 3) é igual a 6.

Escreva um algoritmo que consiga identificar se um número é perfeito ou não.

Entrada:
Seu algoritmo receberá, como entrada, várias linhas com um número inteiro positivo cada.

Saída:
Para cada linha da entrada, haverá uma linha na saída. Cada uma das linhas deverá exibir uma mensagem
indicando se o número oferecido na entrada é perfeito ou não. Para números perfeitos, a mensagem deverá ser
a string “Perfeito”. Para números imperfeitos, a mensagem deverá ser a string “Nao perfeito”.
"""

import sys

for entrada in sys.stdin:
    entrada = entrada.split(' ')

    n = int(entrada[0])
    n_final = int(entrada[1])
    I = 0
    lista = []

    while(n <= n_final): 
        primo = True  
        divisor = 2
        while((divisor < n) and primo):
            if(n % divisor == 0):
                primo = False
            divisor = divisor + 1
        if(primo and (n != 1)):
            lista.insert(I, n)
            I = I + 1
        n = n + 1

    lista_print = " ".join(map(str,lista))
    print(lista_print)

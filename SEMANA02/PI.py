"""
Descriçãao do problema:
Na matemática, o número π pode ser calculado pela fórmula de Leibniz. A fórmula é uma série infinita definida
por Gottfried Wilhelm Leibniz:

pi/4 = 1 − 1/3 + 1/5 − 1/7 + 1/9 + . . .

Entrada:
Seu algoritmo receberá, como entrada, várias linhas com um número inteiro positivo n em cada uma.

Saída:
A saída será uma aproximaçãao do valor de π, representada pela aplicaçãao da fórmula de Leibniz sobre os n
primeiros termos da série.
Em cada linha, deverá aparecer a mensagem “pi(n) = v”, onde n é o valor da linhas correspondente na entrada
e v é o valor calculado, com exatamente quatro casas decimais.

"""
import sys

for n in sys.stdin:
    n = int(n)
    x = 1

    lista = [1]

    I = 0
   
    while ((I + 1) < n):
        I = I + 1
        x = x + 2
        if (n != 1):
            if(I % 2 == 0):
                parte = 1 / x
                lista.insert(I, parte)
            else:
                parte = - (1 / x)
                lista.insert(I, parte)
    soma = sum(lista)
    pi = soma * 4
    
    print("pi(", n, ") = %.4f" %pi)
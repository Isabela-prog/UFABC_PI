"""
Descrição do problema:
Neste exercício, você deverá escrever um algoritmo capaz de identificar todos os números primos dentro de um
intervalo de números.
Lembre-se de que um número é primo se sua divisão só é exata para dois números: 1 e ele próprio. Por exemplo,
11 é um número primo, pois só pode ser dividido exatamente por 1 e por 11. O número 12 não é primo, pois
pode ser dividido de forma exata por vários números além de 1 e 12 (2, 3, 4 e 6).

Entrada:
Seu algoritmo receberá, como entrada, várias linhas com dois números inteiros em cada uma. Em cada linha,
os números x1 e x2 aparecerão em ordem crescente, separados por um espaço branco.

Saída:
A saída também possui várias linhas. Cada linha corresponde a uma linha fornecida na entrada. Em cada linha,
deverá ser apresentada uma lista com todos os n números primos entre x1 e x2. 
Ou seja x1 ≤ p1 < p2 < . . . < pn ≤ x2, onde pi, 1 ≤ i ≤ n é primo. 
Os números devem ser separados por um espaço branco.

"""

import sys

for n in sys.stdin:
    n = int(n)
    lista = []
    divisor = 1
    I = 0

    while(divisor < n):
        if(n % divisor == 0):
            lista.insert(I, divisor)
            I = I + 1
        divisor = divisor + 1

    if(sum(lista) == n):
        print('Perfeito')
    else:
        print('Nao perfeito')
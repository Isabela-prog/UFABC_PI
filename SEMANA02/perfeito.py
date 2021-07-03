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
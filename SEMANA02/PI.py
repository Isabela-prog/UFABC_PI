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
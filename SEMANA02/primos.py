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
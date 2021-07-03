"" Desceição do problema:
Neste exercício, vamos construir uma calculadora simples, que realiza opera¸cões aritméticas básicas. As
operações disponíveis em sua calculadora são:

Operação    Expressão    Cálculo
Soma        SUM          x + y
Subtração   DIF          x − y 
Multipl     MULT         x × y
Divisão     DIV          x/y
Potenc      POT          x**y
Raiz quad   RAIZ         √x
Log 10      LOG10        log10x

Sua calculadora receberá um código e o número de operandos correspondentes à operação matemática indicada.
Seu programa deve interpretar o código e realizar a operação, exibindo seu resultado na saída. """

import math

entrada = input()
entrada_split = entrada.split(' ')

operation = entrada_split [0]
n1_str = entrada_split [1]
n1 = float(n1_str)

if((operation == "RAIZ") or (operation == "LOG10")):
    if (operation == "RAIZ"):
        RAIZ = n1 ** 0.5
        print("%.2f" %(RAIZ))
    else:
        LOG10 = math.log(n1, 10)
        print("%.2f" %(LOG10))
else:
    n2_str = entrada_split [2]
    n2 = float(n2_str)
    if(operation == "SUM"):
        SUM = n1 + n2
        print("%.2f" %(SUM))
    elif(operation == "DIF"):
        DIF = n1 - n2
        print("%.2f" %(DIF))
    elif(operation == "DIV"):
        DIV = n1 / n2
        print(DIV)
    elif(operation == "MULT"):
        MULT = n1 * n2
        print("%.2f" %(MULT))
    else:
        POT = n1 ** n2
        print("%.2f" %(POT))

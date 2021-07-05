"""
Descrição do problema:
Neste exercício, vamos construir uma calculadora simples, que realiza operações aritméticas básicas. As
operações disponíveis em sua calculadora são:
Operação Expressão Cálculo

Operação    Expressão    Cálculo
Soma        SUM          x + y
Subtração   DIF          x − y 
Multipl     MULT         x × y
Divisão     DIV          x/y
Potenc      POT          x**y
Raiz quad   RAIZ         √x
Log 10      LOG10        log10x

Sua calculadora receberá um conjunto de operações (várias operações) em sequência. Cada operação possui
um código e o número de operandos correspondentes à operação matemática indicada. Seu programa deve
interpretar o código e realizar a operação, exibindo seu resultado na saída.

Entrada:
Seu programa receberá, como entrada uma lista de operações matemáticas, sendo uma em cada linha. Cada
operação possui um código (SUM, DIF, MULT, DIV, POT, RAIZ ou LOG10). Na mesma linha, serão informados os operandos separados por um espa¸co branco cada. As operações de código RAIZ e LOG10 possuem
somente um operando numérico. As demais possuem dois operandos numéricos.

Saída:
A saída exibirá o resultado da operação matemática indicada na entrada. Cada linha da entrada terá uma linha
correspondente na saída com o resultado produzido pela operação matemática solicitada. O resultado é um
número real com exatamente 2 casas decimais.
Caso a operação pedida seja inválida, deve ser exibida a seguinte mensagem: “Operacao Invalida”. A operação
é considera inválida se o código é desconhecido (diferente de SUM, DIF, MULT, DIV, POT, RAIZ e LOG10)
ou quando, na divisão, o divisor for zero (0).
"""

import math
import sys

for entrada in sys.stdin:
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
    elif((operation == "SUM") or (operation == "DIF") or (operation == "DIV") or (operation == "MULT") or (operation == "POT")):
        n2_str = entrada_split [2]
        n2 = float(n2_str)
        if(operation == "SUM"):
            SUM = n1 + n2
            print("%.2f" %(SUM))
        elif(operation == "DIF"):
            DIF = n1 - n2
            print("%.2f" %(DIF))
        elif(operation == "DIV"):
            if(n2 == 0):
                print("Operacao Invalida")
            else:
                DIV = n1 / n2
                print(DIV)
        elif(operation == "MULT"):
            MULT = n1 * n2
            print("%.2f" %(MULT))
        else:
            POT = n1 ** n2
            print("%.2f" %(POT))
    else:
        print("Operacao Invalida")

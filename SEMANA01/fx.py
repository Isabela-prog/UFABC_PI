"""
Descrição do problema:
Escreva um algoritmo que calcula o resultado de uma função f(x), definido da seguinte forma

f(x) =
1, se x ≤ 1,
x, se 1 < x ≤ 5,
x**2, se 5 < x ≤ 10,
x**3, se x > 10

Entrada:
Seu programa receberá um número real x como entrada

Saída:
A saída exibirá o valor de f(x), com exatamente duas casas decimais.
"""
var = input()
var_str = var.split(' ')

x = float(var_str[2])

if(x <= 1):
    print("f(x) = %.2f" %1)
elif((x > 1) and (x <= 5)):
    print("f(x) = %.2f" %x)
elif((x > 5) and (x <= 10)):
    x = x ** 2
    print("f(x) = %.2f" %x)
else:
    x = x ** 3
    print("f(x) = %.2f" %x)
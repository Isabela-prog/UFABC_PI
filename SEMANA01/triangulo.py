"""
Descrição do problema:

Um triângulo pode ser classificado em três categorias, baseado na relação entre as medidas de seus lados:
equilátero, isósceles e escaleno. Eles são definidos da seguinte forma:

• Triângulo escaleno: todos os lados são diferentes.
• Triângulo isósceles: possui dois lados iguais.
• Triângulo equilátero: todos os lados são iguais.

Você deve construir um algoritmo que, dadas as medidas dos três lados de uma figura geométrica, identifica
se ela é um triângulo e, caso seja, qual sua classificação considerando os critérios acima. Em um triângulo,
nenhum dos lados pode ser maior que a soma dos outros dois. Além disso, todas as medidas dos lados devem
ser positivas.

Entrada:
Seu programa receberá três n´umeros (inteiros ou reais) separados por espa¸cos brancos.

Saída:
A saída deverá exibir a classificação do triângulo formado pelas medidas dos lados informados na entrada. As
mensagens exibidas podem ser:

• Triangulo escaleno
• Triangulo isosceles
• Triangulo equilatero

Caso as medidas informadas na entrada não possam formar um triângulo, o algoritmo deve exibir a mensagem:
• Medidas nao formam um triangulo
"""

medidas = input()
medidas_split = medidas.split(' ')

x = float(medidas_split[0])
y = float(medidas_split[1])
z = float(medidas_split[2])

s_1 = x + y
s_2 = x + z
s_3 = y + z

if((y <= s_2) and (x <= s_3) and (z <= s_1) and (x, y, z > 0)):
    if((x != y) and (x != z) and (y != z)):
        print("Triângulo escaleno")
    elif((x == y) and (x != z) and (y != z)):
        print("Triângulo isósceles")
    elif((x != y) and (x == z) and (y != z)):
        print("Triângulo isósceles")
    elif((x != y) and (x != z) and (y == z)):
        print("Triângulo isósceles")
    else:
        print("Triângulo equilátero")
else:
    print('Medidas nao formam um triangulo')    

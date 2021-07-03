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
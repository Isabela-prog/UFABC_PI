import math

entrada = input()
saida = input()

entrada = entrada.split(':')
saida = saida.split(':')

minuto_entrada = float(entrada[1]) / 60
hora_entrada = float(entrada[0]) + minuto_entrada

minuto_saida = float(saida[1]) / 60
hora_saida = float(saida[0]) + minuto_saida

periodo = hora_saida - hora_entrada

if(periodo <= 0.25):
    custo = 0
    print("R$ = %.2f" %custo)
else:
    periodo = math.ceil(periodo)
   
    if(periodo < 2.00):
        custo = 5 * periodo
        print("R$ = %.2f" %custo)
    elif((periodo > 2.00) and (periodo <= 4.00)):
        custo = 5 + (3 * (periodo - 1))
        print("R$ = %.2f" %custo)
    else:
        custo = 14 + (2 * (periodo - 4))
        print("R$ = %.2f" %custo)
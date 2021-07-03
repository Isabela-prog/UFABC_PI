"""
Descri¸cão do problema:
Você foi contratado para montar um sistema de parquímetro, que calcula a taxa cobrada por estacionamento
de veículos em um via da cidade. O sistema recebe os horários de entrada e saída do veículo, e deve calcular o
valor a ser pago usando o seguinte critério:

• 1 hora: R$ 5,00
• De 2 a 4 horas: R$ 3,00 por hora
• 5 horas ou mais: R$ 2,00 por hora
• Tolerância de 15min. a partir da chegada.

O valor a ser pago sempre considera a hora cheia, ou seja, se o veículo ficar estacionado durante 1,5 horas, será
cobrado o valor equivalente a 2 horas.
O parquímetro registra os horários de chegada e saída do veículo, no formato HH:MM. Considere, por simplicidade, que o parquímetro só registra veículos estacionados no mesmo dia. Dessa forma, o horário de saída
sempre é superior ao horário de chegada e correspondem ao mesmo dia. O horário pode variar de 00:00 a 23:59.

Entrada:
Seu programa receberá, como entrada, duas linhas de valores. Cada uma delas possui um horário no formato
HH:MM. A primeira linha refere-se ao horário de chegada do veículo e a segunda linha refere-se ao horário de
saída do mesmo.
Saída:
A saída exibirá o valor de deve ser cobrado como taxa de estacionamento, em Reais (R$).
"""

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
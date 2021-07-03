data = input()

data_split = data.split("/")

dia = int(data_split[0])
mes = int(data_split[1])
ano = int(data_split[2])

if ((dia == 1) or (dia == 2) or (dia == 3) or (dia == 4) or (dia == 5) or (dia == 6)  or (dia == 7) or (dia == 8) or (dia == 9)):
    dia = dia + 1
    if(mes == 1) or (mes == 2) or (mes == 3) or (mes == 4) or (mes == 5) or (mes == 6) or (mes == 7) or (mes == 8) or (mes == 9):
        dia_seguinte = '0{}/0{}/{}'.format(dia, mes, ano)
        print(dia_seguinte)
    else:
        dia_seguinte = '0{}/{}/{}'.format(dia, mes, ano)
        print(dia_seguinte)
else:
    if(mes == 2):
        if(dia == 28):
            mes = mes + 1
            dia_seguinte = '{}/0{}/{}'.format('01', mes, ano)
            print(dia_seguinte)
        else:
            dia = dia + 1
            dia_seguinte = '{}/0{}/{}'.format(dia, mes, ano)
            print(dia_seguinte)
    elif((mes == 1) or (mes == 3) or (mes == 4) or (mes == 5) or (mes == 7) or (mes == 8)):
        if(dia == 31):
            mes = mes + 1
            dia_seguinte = '{}/0{}/{}'.format('01', mes, ano)
            print(dia_seguinte)
        else:
            dia = dia + 1
            dia_seguinte = '{}/0{}/{}'.format(dia, mes, ano)
            print(dia_seguinte)
    elif((mes == 10) or (mes == 12)):
        if((dia == 31) and (mes == 12)):
            ano = ano + 1
            dia_seguinte = '{}/{}/{}'.format('01', '01', ano)
        elif(dia == 31):
            mes = mes + 1
            dia_seguinte = '{}/{}/{}'.format('01', mes, ano)
            print(dia_seguinte)
        else:
            dia = dia + 1
            dia_seguinte = '{}/{}/{}'.format(dia, mes, ano)
            print(dia_seguinte)
    elif((mes == 4) or (mes == 6) or (mes == 9)):
        if(dia == 30):
            mes = mes + 1
            dia_seguinte = '{}/0{}/{}'.format('01', mes, ano)
            print(dia_seguinte)
        else:
            dia = dia + 1
            dia_seguinte = '{}/0{}/{}'.format(dia, mes, ano)
            print(dia_seguinte)
    else:
        if(dia == 30):
            mes = mes + 1
            dia_seguinte = '{}/{}/{}'.format('01', mes, ano)
            print(dia_seguinte)
        else:
            dia = dia + 1
            dia_seguinte = '{}/{}/{}'.format(dia, mes, ano)
            print(dia_seguinte)
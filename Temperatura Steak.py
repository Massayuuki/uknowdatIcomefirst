# Temperatura x Cozimento

'''
120ºF ou 48ºC - Rare (Selada)
130ºF ou 54ºC - Medium rare (Ao ponto para o mal)
140ºF ou 60ºC - Medium (Ao ponto)
150ºF ou 65ºC - Medium well (Ao ponto para o bem)
160ºF ou 71ºC - Well done (Bem passada)
'''
medida = str(input('Digite se o valor está em fahrenheit (f) ou celsius (c):\n')).lower()
temperatura = int(input('Digite aqui a temperatura da carne:\n'))

if (medida == 'fahrenheit') or (medida == 'f'):
    if temperatura >= 160:
        print('Sua carne está bem passada')

    elif temperatura >= 150:
        print('Sua carne está ao ponto para o bem.')

    elif temperatura >= 140:
        print('Sua carne está ao ponto.')

    elif temperatura >= 130:
        print('Sua carne está ao ponto para o mal.')

    elif temperatura >= 120:
        print('Sua carne está selada.')

    else:
        print('Não está pronta ainda.')

elif (medida == 'celsius') or (medida == 'c'):
    if temperatura >= 71:
        print('Sua carne está bem passada')

    elif temperatura >= 65:
        print('Sua carne está ao ponto para o bem.')

    elif temperatura >= 60:
        print('Sua carne está ao ponto.')

    elif temperatura >= 54:
        print('Sua carne está ao ponto para o mal.')

    elif temperatura >= 48:
        print('Sua carne está selada.')

    else:
        print('Não está pronta ainda.')

else:
    print('Medida inválida.')

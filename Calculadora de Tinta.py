'''
Calcular quantidade de lata de tinta necesária para pintar x metros quadrados.
Usuário deve fornecer:

>Tamanho da parede (altura e largura)
>Rendimento da tinta

E imprimir quantidade de latas de tinta.
'''


def calculadora(altura, largura, rendimento_tinta):
    area = altura * largura
    qntd_latas = area // rendimento_tinta
    resto = area % rendimento_tinta
    if resto == 0:
        return qntd_latas
    else:
        qntd_latas += 1
        return qntd_latas


x = int(input('Digite a altura da parede (apenas números):\n'))
y = int(input('Digite a largura da parede (apenas números):\n'))
z = int(input('Digite o rendimento da tinta em m² (apenas números):\n'))

print(f'Vai ser necessário {calculadora(x, y, z)} lata(s) de tinta.')

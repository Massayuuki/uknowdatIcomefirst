''' Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo

Listal = Funcionårios que tem carro e trabalham a noite
Lista2 = Funcionårios que tem carro e trabalham durante o dia
Lista3 = Funcionårios que näo tem carro
'''


funcionarios = ['Ana', 'Marcos', 'Alice','Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

f1 = set(funcionarios)
f2 = set(turno_dia)
f3 = set(turno_noite)
f4 = set(tem_carro)

print(f3 & f4)
print(f2 & f4)
print(f1 - f4)
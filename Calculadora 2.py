def soma(a,b,c):
    resultado = a+b+c
    return(resultado)


def sub(a,b,c):
    resultado = a-b-c
    return(resultado)


def multi(a,b,c):
    resultado = a*b*c
    return(resultado)


def div(a,b,c):
    resultado = a/b/c
    return(resultado)


choice = input("Digite a alternativa desejada:\n1.Soma\n2.Subtração\n3.Multiplicação\n4.Divisão\n\n")

if choice in ('1', '2', '3', '4'):
    x = int(input("Digite o primeiro número:"))
    y = int(input("Digite o segundo número:"))
    z = int(input("Digite o terceiro número:"))

    if choice == '1':
        print(f'O resultado da soma entre {x}, {y} e {z} é igual a {soma(x,y,z)}.')

    elif choice == '2':
        print(f'O resultado da subtração entre {x}, {y} e {z} é igual a {sub(x,y,z)}.')

    elif choice == '3':
        print(f'O resultado da multiplicação entre {x}, {y} e {z} é igual a {multi(x,y,z)}.')

    elif choice == '4':
        print(f'O resultado da divisão entre {x}, {y} e {z} é igual a {div(x,y,z)}.')
    
else:
    print('Escolha inválida')
valor = int (input("qual o valor que deseja retirar entre 10 e 600 (presisa ser numero inteiro)? "))

if valor < 10 or valor > 600:

    print(f" valor a ser sacado é invalido!")


elif valor >= 10 and valor <= 600:

    notas100 = valor // 100  
    valor = valor % 100

    notas50 = valor // 50
    valor = valor % 50

    notas20 = valor // 20
    valor = valor % 20

    notas10 = valor // 10
    valor = valor % 10

    notas5 = valor // 5
    valor = valor % 5

    notas2 = valor // 2
    valor = valor % 2

    notas1 = valor // 1
    valor = valor % 1

    if notas100 == 0:
        notas100 = "nenhuma"

        
    if notas50 == 0:
        notas50 = "nenhuma"

        
    if notas20 == 0:
        notas20 = "nenhuma"

        
    if notas10 == 0:
        notas10 = "nenhuma"

        
    if notas5 == 0:
        notas5 = "nenhuma"

        
    if notas2 == 0:
        notas2 = "nenhuma"

        
    if notas1 == 0:
        notas1 = "nenhuma"





print(f"o caixa eletronico retornou {notas100} notas de 100, {notas50} notas de 50, {notas20} notas de 20, {notas10} notas de 10, {notas5} notas de 5, {notas2}notas de 2 e {notas1} notas de 1")


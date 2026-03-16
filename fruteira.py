qmaca = float(input("quantos quilos de maça foi comprado? "))
qmorango = float(input("quantos quilos de morango foi comprado? "))
qfrutas = qmaca + qmorango

if qmaca >= 5:
    vmaca = 1.50
else:
    vmaca = 1.80

if qmorango >= 5:
        vmorango =  2.20
else:
        vmorango =  2.50

valor = (qmorango * vmorango) + (qmaca * vmaca)

if qfrutas > 8 or valor > 25:
        valor = valor * 0.90


print(f"o valor total de sua compra deu {valor:g}")
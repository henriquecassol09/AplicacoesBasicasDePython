deposito = float (input("qual o deposito feito? "))
taxa = float (input("qual a taxa de juros por mes (sem o simbolo de porcentagem) ?"))
mes = 1
saldo = deposito
while mes <= 24:
    saldo = saldo + (saldo * (taxa/100))
    print(f"o saldo do mês {mes} é de {saldo:5.2f} reais")
    mes = mes + 1
    resultado = saldo - deposito
print(f" o ganho dos juros foi de {resultado:5.2f} reais")
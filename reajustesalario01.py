salario =  float (input("qual seu salario atual? "))

if salario <= 300:
    reajuste = salario * 1.15
    print(f"seu salario pos reajuste é {reajuste:g}")
elif salario > 300 and salario <= 600:
    reajuste = salario * 1.10
    print(f"seu salario pos reajuste é {reajuste:g}")
elif salario > 600 and salario <= 900:
    reajuste = salario * 1.05
    print(f"seu salario pos reajuste é {reajuste:g}")
else:
    print("seu salario esta dentro das normas, você não haverá reajuste")

    #henriquecassol09
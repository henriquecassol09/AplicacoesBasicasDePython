salario = float(input("qual seu salario atual? "))
salario2 = salario * 0.93

if salario <= 350:
    reajuste = salario2 + 100
    print(f"seu salario pos reajuste com o desconto do imposto de 7% é {reajuste:g}")
elif salario > 350 and salario <= 600:
    reajuste = salario2 + 75
    print(f"seu salario pos reajuste com o desconto do imposto de 7% é {reajuste:g}")
elif salario > 600 and salario <= 900:
    reajuste = salario2 + 50
    print(f"seu salario pos reajuste e desconto do imposto de 7% é {reajuste:g}")
else:
    reajuste = salario2 + 35
    print(f"seu salario pos reajuste e desconto do imposto de 7% é {reajuste:g}")

#henriquecassol09
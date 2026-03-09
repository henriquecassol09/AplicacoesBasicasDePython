preco = float(input("qual seu preço atual do produto atual? "))

if preco <= 50:
    reajuste = preco * 1.05
    print(f"o novo preço do produto é {reajuste:g}")
elif preco > 50 and preco < 100:
    reajuste =  preco * 1.10
    print(f"o novo preço do produto é {reajuste:g}")
elif preco >= 100:
    reajuste = preco * 1.15
    print(f"o novo preço do produto é {reajuste:g}")

if reajuste <= 80:
        print("o produto é barato")
elif reajuste > 80 and reajuste <= 120:
        print(f" o produto esta em um preço normal")
elif reajuste > 120 and reajuste <= 200:
        print(f"o produto está caro")
else:
        print(f"o produto é muito caro")
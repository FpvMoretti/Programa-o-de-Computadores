valor = float(input("Digite o valor: "))


if valor > 200:
    desconto = valor * 0.1
    print(f"Desconto: R${desconto:.2f}")
    print(f"Valor final: R${valor - desconto:.2f}")
else:
    print("Não há desconto.")   
valor = float(input("Digite o valor: "))
vip = input("O cliente é VIP? (s/n): ").lower()

if valor > 300 or vip == 's':
    print("Cliente Recebe Desconto.")
else:
    print("Cliente Não Recebe Desconto.")
total = 0
menor = float('inf')
qtd = 0
while True:
    v = float(input("Valor dos gastos (-1 fim): "))
    if v == -1: break
    total += v
    if v < menor: menor = v
    if v % 2 == 0 and v % 1 == 0: qtd += 1
print(f"Total: R$ {total}, Menor valor: R${menor} Quantidade de itens: {qtd}" )
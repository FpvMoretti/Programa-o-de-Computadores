soma = 0

num = int(input("Digite um número: "))
for i in range(2, num, +1):
    if i % 2 == 0:
        soma = soma + i

print("A soma dos pares é: ", soma)
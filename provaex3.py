soma = 0

num = int(input("Digite um número inteiro: "))
for i in range(4, num+1, 4):
        soma = soma + i
        print(i)

print("A soma dos termos é: ", soma)
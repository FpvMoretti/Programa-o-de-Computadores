for i in range(5):
    num=float(input("Digite 5 números: "))
    if i == 0:
        menor=num
    elif num < menor:
        menor = num

print("O menor é:", menor)
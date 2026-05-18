contagem=0

for i in range(5):
    num=int(input("Digite 5 números: "))
    if num >= 10 and num <= 20:
        contagem = contagem + 1

print("Números dentro do intervalo: ", contagem)
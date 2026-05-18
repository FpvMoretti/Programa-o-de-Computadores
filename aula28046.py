num = 0

while True:
    n = int(input("Digite os números: "))
    if n > num:
        num = n

    if n == 0:
        break 

print("Encerrando sistema, o maior número é: ", num)
cont = 0
med = 0

while True:
    n = int(input("Digite os números: "))
    
    if n == 0:
        break 

    cont += n
    med += 1
    media = cont/med

print("Encerrando programa, média: ", media)
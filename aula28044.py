cont = 0


while True:
    n = int(input("Digite números continuamente: "))
    cont += 1

    if n < 0:
        break 

print("Encerrando programa, números positivos: ", cont -1)
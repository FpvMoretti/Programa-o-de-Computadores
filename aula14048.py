contador=0

for i in range(5):
    valor=int(input("Digite os valores: "))
    if valor >= 0:   
        contador+=1
print("Os números positivos são:", contador)
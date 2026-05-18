acumulador=0
cont=0
for i in range(5):
    nota=int(input("Digite uma nota: "))
    acumulador=acumulador+nota
    cont=cont+1
    print("Soma das notas: ", acumulador)
    print("Quantidade: ", cont)
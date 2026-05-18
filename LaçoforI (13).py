aprovados=0
recuperação=0
reprovados=0

for i in range(5):
    valores=int(input("Digite os números: "))

    if valores >=7:
        print("Você está aprovado")
        aprovados +=1 

    elif valores >= 5 and valores <7:
        print("Você está de recuperação")
        recuperação +=1 

    else:
        print("Você foi reprovado")
        reprovados +=1 

print("Você está aprovado em: ", aprovados)
print("Você está de recuperação em: ", recuperação)
print("Você foi reprovado em: ", reprovados)
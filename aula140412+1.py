n =0

num=int(input("Digite um número par: "))
for i in range(1, num+1):
    if (i %2==0):
        n += i
print("O soma dos pares é de:", n)
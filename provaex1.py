estoque = int(input("Digite o valor de estoque: "))
if estoque < 20:
    print("Necessário reabastecimento, número em estoque: ", estoque)
else: 
    print("Estoque suficiente, não é necessário reposição", estoque)
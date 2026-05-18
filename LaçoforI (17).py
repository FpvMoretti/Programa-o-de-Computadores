nome=input("Digite seu nome: ")
if len(nome) >= 3 and nome.isalpha():
    print("Nome válido")
else:
    print("Nome inválido")
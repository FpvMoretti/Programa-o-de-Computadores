erros = 0

for i in range(5):
    senha = input("Digite uma senha: ")
    
    if len(senha) >= 8:
        print("Senha válida")
    else:
        print("Senha inválida")
        erros = erros + 1

print("Quantidade de senhas inválidas:", erros)
senha_correta = "1234"
tentativas = 0

while True:
    senha= input("Digite a senha: ")
    tentativas +=1

    if senha == senha_correta:
        break

print("Tentativas: ", tentativas)
while True:  # <--- O loop precisa estar aqui!
    nota = float(input("Digite a nota do aluno (0 a 10): "))
    
    if 0 <= nota <= 10:
        print("Nota válida!")
        break  # Agora ele sabe que deve parar o 'while' acima
    else:
        print("Erro: A nota deve estar entre 0 e 10. Tente de novo.")

while True:  # <--- O loop precisa estar aqui!
    frequencia = int(input("Digite a frequência do aluno: "))
    if 0 <= frequencia <= 100:
        print("Frequência válida!")
        break
    else:
        print("Erro: A frequência deve estar entre 0 e 100. Tente de novo.")

if nota >= 7 and frequencia >= 75:
    print("Aluno aprovado.")
else:
    print("Aluno em recuperação.") 

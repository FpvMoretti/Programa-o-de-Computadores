while True:
    nota = float(input("Digite a nota do aluno (0 a 10): "))
    
    if 0 <= nota <= 10:
        print("Nota válida!")
        break
    else:
        print("Erro: A nota deve estar entre 0 e 10. Tente de novo.")
nota= float(input("Digite a nota: "))

if nota >= 7:
    print("Aprovado!")
else:
    print("Reprovado.")
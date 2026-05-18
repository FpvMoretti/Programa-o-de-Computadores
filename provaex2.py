tempo = int(input("Digite o tempo de atendimento em minutos: "))
if tempo <= 5:
    print("Tempo de atendimento rápido")
elif tempo >= 6 and tempo <=15:
    print("Tempo de atendimento normal")
else:
    print("Tempo de atendimento demorado")
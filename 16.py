while True:
    n = float(input("Digite sua nota: "))
    if n < 0 or n > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
    else:
        break

if 9 <= n <= 10:
    print("Nota A.")
elif 7 <= n < 8.9:
    print("Nota B.")
elif 5 <= n < 6.9:
    print("Nota C.")
else:
    print("Nota D.")
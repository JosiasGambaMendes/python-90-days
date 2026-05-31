port = int(input("Digite o número da porta: "))

if port == 22:
    print("SSH")

elif port == 80:
    print("HHTP")

elif port == 443:
    print("HTTPS")

else:
    print("Porta Desconhecida")
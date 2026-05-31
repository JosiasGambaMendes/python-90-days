latencia = float(input("Digite o valor da latência em MS: "))

if latencia > 200:
    print("Problema")

elif latencia > 100:
    print("Média")

elif latencia > 50:
    print("Boa")

else:
    print("Excelente")
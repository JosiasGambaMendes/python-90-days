hostname = input("Digite o hostname: ")
cpu = float(input("Digite o valor da CPU: "))
ram = float(input("Digite o valor da RAM: "))

if cpu > 80:
    print("CPU Crítica")

elif ram > 80:
    print("RAM Crítica")

else:
    print("Servidor saudável")
hostname = input("Digite o hostname: ")
cpu = float(input("Digite o valor da CPU: "))
ram = float(input("Digite o valor da RAM: "))

if cpu > 80:
    print("CPU Crítica")

if ram > 80:
    print("RAM Crítica")

if cpu <= 80 and ram <= 80:
    print("SERVIDOR SAUDÁVEL")
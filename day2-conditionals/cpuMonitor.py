cpuUsage = float(input("Digite o valor da CPU: "))

if cpuUsage > 80:
    print("Crítico")

elif cpuUsage > 50:
    print("Atenção")

else:
    print("Normal")
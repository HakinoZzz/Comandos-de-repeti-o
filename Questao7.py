temperaturas = []
while True:
    try:
        temp = float(input("Digite uma temperatura (ou digite 999 para encerrar): "))
        if temp == 999:
            break
        temperaturas.append(temp)
    except ValueError:
        print("Valor inválido. Encerrando.")
        break

if temperaturas:
    total = len(temperaturas)
    media = sum(temperaturas) / total
    acima_de_30 = sum(1 for t in temperaturas if t > 30)
    abaixo_de_15 = sum(1 for t in temperaturas if t < 15)
    
    print(f"Quantas temperaturas foram registradas: {total}")
    print(f"Média das temperaturas: {media:.2f}°C")
    print(f"Quantas estão acima de 30°C: {acima_de_30}")
    print(f"Quantas estão abaixo de 15°C: {abaixo_de_15}")
else:
    print("Nenhuma temperatura foi registrada.")

input("Pressione Enter para sair...")

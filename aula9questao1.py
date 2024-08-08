a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))

if a < b:
    soma = 0
    for i in range(a, b + 1):
        soma += i
    print(f"A soma dos números inteiros no intervalo [{a}, {b}] é: {soma}")
else:
    print("Erro: O primeiro número deve ser menor que o segundo.")

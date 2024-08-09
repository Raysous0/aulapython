medicamentos = []
for i in range(5):
    nome = input("Digite o nome do medicamento {}: ".format(i + 1))
    preco = float(input("Digite o preço do medicamento {}: ".format(i + 1)))
    medicamentos.append((nome, preco))

medicamento_mais_barato = medicamentos[0]
for medicamento in medicamentos:
    if medicamento[1] < medicamento_mais_barato[1]:
        medicamento_mais_barato = medicamento
soma_precos = 0
for medicamento in medicamentos:
    soma_precos += medicamento[1]
media_precos = soma_precos / len(medicamentos)

print("Medicamento mais barato:", medicamento_mais_barato[0], " - R$", medicamento_mais_barato[1])
print("Média dos preços: R$", media_precos)

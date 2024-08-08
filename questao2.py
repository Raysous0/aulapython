def soma_intervalo(a, b):
  return sum(range(a, b + 1))

try: 
  a = int(input("Digite o primeiro número inteiro (a): "))
  b = int(input("Digite o segundo número inteiro (b): "))

  if a < b:
    resultado = soma_intervalo(a, b)
    print(f"A soma dos números inteiros no intervalo [{a}, {b}] é: {resultado}")
  else:
    print("Erro: O primeiro número deve ser menor que o segundo.")
except  ValueError:
  print("Erro: Entrada inválida. Certifique-se de inserir números inteiros válidos.")
  
  

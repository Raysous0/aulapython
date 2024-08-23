produtos = []
while True: 
  produto=input("Digite o nome do produto: ")
  produtos.append(produto)
  continuar = input ("deseja adiciona outro produto? (sim/não): ")
  if continuar == "sim":
    break
  print("\nlista de produtos eletronicos:")
  for produto in produtos:
    print("-"+ produto)
  

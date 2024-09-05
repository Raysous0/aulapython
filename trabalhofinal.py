import calendar
from datetime import datetime

# Funções

def exibir_menu():
    print("\nMenu:")
    print("1. Mostrar calendário do mês atual")
    print("2. Adicionar evento")
    print("3. Listar eventos")
    print("4. Sair")

def mostrar_calendario():
    agora = datetime.now()
    ano = agora.year
    mes = agora.month
    print(f"\nCalendário para {calendar.month_name[mes]} {ano}")
    print(calendar.month(ano, mes))

def adicionar_evento(eventos):
    data = input("Digite a data do evento (YYYY-MM-DD): ")
    descricao = input("Digite a descrição do evento: ")
    if data not in eventos:
        eventos[data] = []
    eventos[data].append(descricao)
    print("Evento adicionado com sucesso!")

def listar_eventos(eventos):
    if not eventos:
        print("Não há eventos registrados.")
    else:
        print("\nEventos:")
        for data, descricoes in sorted(eventos.items()):
            print(f"{data}:")
            for descricao in descricoes:
                print(f"  - {descricao}")

# Função principal
def main():
    eventos = {}
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            mostrar_calendario()
        elif opcao == "2":
            adicionar_evento(eventos)
        elif opcao == "3":
            listar_eventos(eventos)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    main()

import calendar
from datetime import datetime

# Funções

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\nMenu:")
    print("1. Mostrar calendário do mês atual")
    print("2. Adicionar evento")
    print("3. Listar eventos")
    print("4. Sair")

def mostrar_calendario():
    """Exibe o calendário do mês atual."""
    agora = datetime.now()
    ano = agora.year
    mes = agora.month
    print(f"\nCalendário para {calendar.month_name[mes]} {ano}")
    print(calendar.month(ano, mes))

def validar_data(data_str):
    """Valida se uma string de data está no formato correto (YYYY-MM-DD)."""
    try:
        datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def adicionar_evento(eventos):
    """Permite ao usuário adicionar um evento a uma data específica."""
    while True:
        data = input("Digite a data do evento (YYYY-MM-DD): ")
        if not validar_data(data):
            print("Data inválida. Por favor, use o formato YYYY-MM-DD.")
            continue

        descricao = input("Digite a descrição do evento: ")
        if not descricao.strip():
            print("A descrição do evento não pode ser vazia.")
            continue

        if data not in eventos:
            eventos[data] = []

        eventos[data].append(descricao)
        print("Evento adicionado com sucesso!")
        break

def listar_eventos(eventos):
    """Lista todos os eventos armazenados."""
    if not eventos:
        print("Não há eventos registrados.")
    else:
        print("\nEventos:")
        for data, descricoes in sorted(eventos.items()):
            print(f"{data}:")
            for descricao in descricoes:
                print(f"  - {descricao}")

def processar_opcao(opcao, eventos):
    """Processa a opção escolhida pelo usuário."""
    if opcao == "1":
        mostrar_calendario()
    elif opcao == "2":
        adicionar_evento(eventos)
    elif opcao == "3":
        listar_eventos(eventos)
    elif opcao == "4":
        print("Saindo...")
        return False
    else:
        print("Opção inválida. Tente novamente.")
    return True

# Função principal
def main():
    """Executa o programa principal."""
    eventos = {}
    continuar = True
    while continuar:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        continuar = processar_opcao(opcao, eventos)

# Execução do programa
if __name__ == "__main__":
    main()

def main():
    senha_correta = "123456"
    tentativas_restantes = 3

    while tentativas_restantes > 0:
        senha_informada = input("Digite sua senha: ")
        if senha_informada == senha_correta:
            print(f"Olá, <SEUNOME>. SEJA BEM VINDO(A) AO NOSSO SISTEMA!")
            return
        else:
            tentativas_restantes -= 1
            if tentativas_restantes > 0:
                print(f"Senha incorreta! Você ainda tem {tentativas_restantes} tentativa(s).")
            else:
                print("Sua senha ESTÁ INCORRETA! Por favor, TENTE NOVAMENTE OU FAÇA UMA NOVA SENHA!.")
                return

if __name__ == "__main__":
    main()

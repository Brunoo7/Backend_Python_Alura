import os

def finalizar_app():
    print("Fechando o app...")
    os.system("cls")

def opcao_invalida():
    print("Opção inválida!")
    input("Selecione uma tecla para voltar ao menu principal: ")
    main()

def exibir_opcoes():
    print("1. Cadastrar restautante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair")

def escolher_opcao():
    try:
        opcao = int(input(print("Escolha uma opção:")))
        match opcao:
            case 1:
                print("1. Cadastrar restautante")
            
            case 2:
                print("2. Listar restaurantes")
            
            case 3:
                print("3. Ativar restaurante")

            case 4:
                finalizar_app()
            
            case _:
                print("Opção inválida")
    except:
        opcao_invalida

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
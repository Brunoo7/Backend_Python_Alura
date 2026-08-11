import os

restaurantes = ["Pizza Planet", "Los Pollos Hermanos", "Siri Cascudo"]

def finalizar_app():
    print("Fechando o app...")
    os.system("cls")

def voltar_menu():
    input("\nSelecione uma tecla para voltar ao menu principal: ")
    main()

def opcao_invalida():
    print("Opção inválida!")
    voltar_menu()

def exibir_opcoes():
    print("1. Cadastrar restautante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair")

def cadastrar_restaurante():
    os.system("cls")
    print("Cadastro de novos restaurantes\n")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso")
    voltar_menu()

def lista_restaurantes():
    os.system("cls")
    print("Lista de restaurantes cadastrados:\n")
    for restaurante in restaurantes:
        print(f"{restaurante}")
    voltar_menu()

def escolher_opcao():
    try:
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                cadastrar_restaurante()
            
            case 2:
                lista_restaurantes()
            
            case 3:
                print("3. Ativar restaurante")

            case 4:
                finalizar_app()

            case _:
                opcao_invalida()
    except:
        opcao_invalida()

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
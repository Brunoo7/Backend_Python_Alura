import os

restaurantes = [{"Nome":"Los Pollos Hermanos", "Categoria":"Frango Frito", "Ativo":False},
                {"Nome":"Siri Cascudo", "Categoria":"Hamburgueria", "Ativo":True},
                {"Nome":"Bar Do Moe", "Categoria":"Bar", "Ativo":False}]

def finalizar_app():
    subtitulo("Fechando app...")

def voltar_menu():
    input("\nSelecione uma tecla para voltar ao menu principal: ")
    main()

def subtitulo(texto):
    os.system("cls")
    print(texto)
    print()

def opcao_invalida():
    print("Opção inválida!")
    voltar_menu()

def exibir_opcoes():
    print("1. Cadastrar restautante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def cadastrar_restaurante():
    subtitulo("Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso")
    voltar_menu()

def lista_restaurantes():
    subtitulo("Lista de restaurantes cadastrados:")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["Nome"]
        Categoria = restaurante["Categoria"]
        Ativo = restaurante["Ativo"]
        print(f" - {nome_restaurante} | {Categoria} | {Ativo}")

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
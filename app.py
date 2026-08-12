import os

restaurantes = [{"Nome":"Los Pollos Hermanos", "Categoria":"Frango Frito", "ativo":False},
                {"Nome":"Siri Cascudo", "Categoria":"Hamburgueria", "ativo":True},
                {"Nome":"Bar Do Moe", "Categoria":"Bar", "ativo":False}]

def finalizar_app():
    subtitulo("Fechando app...")
    os.system("cls")

def voltar_menu():
    input("\nSelecione uma tecla para voltar ao menu principal: ")
    main()

def subtitulo(texto):
    os.system("cls")
    linha = "=" * len(texto) 
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    print("Opção inválida!")
    voltar_menu()

def exibir_opcoes():
    print("1. Cadastrar restautante")
    print("2. Listar restaurantes")
    print("3. Alterar estado do restaurante restaurante")
    print("4. Sair\n")

def cadastrar_restaurante():
    subtitulo("Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    Categoria = input(f"Digite a categoria do restaurante {nome_restaurante}: ")
    dados_restaurante = {"Nome":nome_restaurante, "Categoria":Categoria, "ativo":False}
    restaurantes.append(dados_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar_menu()

def lista_restaurantes():
    subtitulo("Lista de restaurantes cadastrados:")
    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["Nome"]
        Categoria = restaurante["Categoria"]
        Ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f" - {nome_restaurante.ljust(20)} | {Categoria.ljust(20)} | {Ativo}")
    voltar_menu()

def alterar_estado_restaurante():
    subtitulo("Alterando o estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["Nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
            print(mensagem)
    if not restaurante_encontrado:
        print("o restaurante não foi encontado")
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
                alterar_estado_restaurante()

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
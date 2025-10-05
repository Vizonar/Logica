import os
sair = ""
livros = []
Usuários = []

while True:
    os.system("cls")
    print("----------------------------------------")
    print("        Bem-Vindo a Biblioteca")
    print("----------------------------------------")
    print("Cadastrar Livro - 1")
    print("Listar Livros - 2")
    print("Buscar Livro por título - 3")
    print("Cadastrar Usuário - 4")
    print("Emprestar Livro - 5")
    print("Devolver Livro - 6")
    print("Sair - 7")
    print("-----------------------------------------")
    select = int(input("Selecione: "))  

    if select == 1:
        Titulo = input("Nome do Livro: ")
        Autor = input("Nome do Autor: ")
        Ano = input("Ano da Publição: ")
        Disp = input("Ele está disponivel? ").upper()
        if Disp == "SIM":
            livros.append([Titulo, Autor, Ano, Disp])
        else:
            Disp = "NAO"
            livros.append([Titulo, Autor, Ano, Disp])
    
    elif select == 2:
        if not livros:
            print("Nenhum livro foi cadastrado.")
        else:
            print("Livros Disponiveis")
            for livro in livros:
                print(livro[0])
            input("\nPrecione Entre para retornar ao menu: ")

    elif select == 3:
        busca = input("Digite o título do livro: ")
        encontrado = False
        for livro in livros[0]:
            if livro[0] == busca:
                print(f"O livro {livro[0]} está disponivel")
                encontrado = True
                break
        if not encontrado:
            print("Livro não encontrado")
        input("\nPrecione Entre para retornar ao menu: ")

    elif select == 4:
        Nome = input("Digite seu nome: ")
        Livros_Emp = []
        Usuários.append([Nome, Livros_Emp])

    elif select == 5:
        emprestimo = input("Digite o titulo do livro que gostaria de pegar emprestado: ")
        for livro in livros[3]:
            if livro[0] == emprestimo and livro[3] == "Sim":
                Livros_Emp.append(emprestimo)
                livro[3] = "NAO"
                print("Livro emprestado!")
                break
            else:
                print("Livro Indisponivel.")

    elif select == 6:
        devolver = input("DIgite o nome do livro que está devolvendo: ")
        for usuario in Usuários[1]:
            usuario[1].remove(devolver)
            for livro[0] in livros:    
                if livro[0] == devolver:
                    livro[3] = "SIM"
            print("Livro devolvido!")
            break
        else:
            print("Esse livro não está emprestado.")

    elif select == 7:
        print("Saindo do Sistema .....")
        break
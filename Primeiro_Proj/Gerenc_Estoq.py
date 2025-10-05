import os 

Produtos = []

while True:
    os.system("cls")
    print("-----------------")
    print("Gestão de Estoque")
    print("-----------------")
    print("1 - Cadastro de produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto nome ou id")
    print("4 - Atualizar estoque")
    print("5 - Vender produto")
    print("6 - Excluir do sistema")
    print("7 - Sair")

    select = int(input("Selecione: "))

    if select == 1:
        nome = input("Digite o nome do produto: ").upper()
        Id = input("Digite o numero do produto: ")
        quant = int(input("Digite o quanto em estoque: "))
        preco = float(input("Digite o valor: "))
        Produtos.append([nome, Id, quant,preco ])

    elif select == 2:
        for produtos in Produtos:
            print(f"Produtos: \n{produtos[0]}")

    elif select == 3:
        busca = input('Digite o nome ou id do produto: ')
        for produto in Produtos:
            if busca == produto[0] or busca == produto[1]:
                print(produto)

        input("\nPressione Enter para voltar ao menu")

    elif select == 4:
        busca = input('Digite o nome ou id do produto: ')
        for produto in Produtos:
            if busca == produto[0] or busca == produto[1]:
                print("1 - adicionar\n2 - remover ")
                select = int(input("Selecione: "))
                if select == 1:
                    valor = int(input("Digite o valor a adicionar: "))
                    produto[2] += valor
                elif select == 2:
                    valor = int(input("Digite o valor a remover: "))
                    produto[2] -= valor
                print("Estoque atualizado")
                break

        else:
            print("Produto não encontrado")
        input("\nPressione Enter para voltar ao menu")

    elif select == 5:
        busca = input('Digite o nome ou id do produto: ')
        for produto in Produtos:
            if busca == produto[0] or busca == produto[1]:
                venda = int(input("Quantos produtos: "))
                if venda > produto[2]:
                    print("Sem estoque o suficiente")
                    break
                else:
                    valorT = venda * produto[3]
                    produto[2] -= venda
                    print(f"Valor total da venda: {valorT: .2f}")
                    break
        else:
            print("Produto não encontrado")
        input("\nPressione Enter para voltar ao menu")


    elif select == 6:
        excluir = input('Digite o nome ou id do produto: ')
        for i, produto in enumerate(Produtos):
            if excluir == produto[0] or excluir == produto[1]:
                del Produtos[i]
                print("Produto removido")
                break
        else:
            print("Produto não encontrado")
        input("\nPressione Enter para voltar ao menu")

    elif select == 7:
        print("Saindo do sistema.....")
        break


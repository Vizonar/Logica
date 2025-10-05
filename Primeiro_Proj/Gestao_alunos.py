import os

Alunos = []

while True:
    os.system("cls")
    print("------------------------")
    print("Gerencimento de alunos")
    print("------------------------")
    print("1 - Cadastro do aluno")
    print("2 - Cadastro das notas")
    print("3 - Listar alunos")
    print("4 - Buscar aluno")
    print("5 - Calcular média")
    print("6 - Excluir aluno do sistema")
    print("7 - Sair")

    select = int(input("Selecione: "))

    if select == 1:
        nome = input("Nome do aluno: ")
        matricula = (input("Matrícula do aluno: "))
        notas = []
        media = 0
        Alunos.append([nome, matricula, notas, media])
    
    elif select == 2:
        matri = input("Digite a matricula do aluno: ")
        for aluno in Alunos:
            if aluno[1] == matri:
                nota = float(input("Adicione a nota: "))
                aluno[2].append(nota)
                break
        else:
            print("Aluno não encontrado")
        input("\nPressine enter para retornar ao menu")

    elif select == 3:
        if not Alunos:
            print("Nenhum aluno cadastrado")    
        else:
            for aluno in Alunos:
                print(f"Alunos cadastrados: {aluno[0]}\n Matricula: {aluno[1]}")
            

        input("\nPressine enter para retornar ao menu")

    elif select == 4:
        busca = input("Digite nome ou matricula do aluno: ")
        for aluno in Alunos:
            if aluno[0] == busca or aluno[1] == busca:
                print(f"Alunos cadastrados: {aluno[0]}\n Matricula: {aluno[1]}\n Notas: {aluno[2]}\n Média: {aluno[3]}")
                break
        else:
            print("Aluno não encontrado")
        input("\nPressine enter para retornar ao menu")

    elif select == 5:
        selecao = input("Digite a matricula do aluno: ")
        for aluno in Alunos:
            if aluno[1] == selecao:
                if aluno[2]:
                    media = sum(aluno[2])/len(aluno[2])
                    aluno[3] = media
                    print(f"Média = {media}")
                else:
                    print("Nenhuma nota encontrada")
                    break
        else:
            print("Matricula não encontrada")

        input("\nPressione Enter para voltar ao menu")

    elif select == 6:
        selecao = input("Digite a matricula do aluno: ")
        for i, aluno in enumerate(Alunos):
            if aluno[1] == selecao:
                del Alunos[i]
                print("Aluno removido com sucesso!")
                break       
        else:
            print("Matricula não encontrada")

    elif select == 7:
        print("Saindo do Sistema .....")
        break
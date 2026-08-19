estoque = []

while True:
    print(" Estoque Atual ")
    if not estoque:
        print("Estoque Vazio")
    else:
        P = 0
        while P < len(estoque):
            print(f"📦 Produto: {estoque[P][0]} | Categoria: {estoque[P][1]} | Qtd: {estoque[P][2]}")
            P += 1

    print("-" * 20)
    acao = input("Deseja adicionar(1), remover(2), alterar(3) ou sair(4)? ").lower()

    if acao == "4":
        print("Encerrando o programa, produtos atuais em estoque:", estoque)
        break


    elif acao == "2":
        produto = input("Digite o nome do produto que deseja remover ou dar baixa: ").lower()
        linhaencontrada = -1
        a = 0
        while a < len(estoque):
            if estoque[a][0] == produto:
                linhaencontrada = a
                break
            a += 1

        if linhaencontrada == -1:
            print("O produto não está em estoque!")
        else:
            quantidade = estoque[linhaencontrada][2]
            print("Quantidade do Produto em Estoque:", quantidade)

            escolha = input("Deseja remover tudo (1) ou apenas certa quantidade (2)? ")

            if escolha == "1":
                estoque.pop(linhaencontrada)
                print("Produto removido com sucesso!")

            elif escolha == "2":
                quantidadetirar = int(input("Digite a quantidade do produto para remover: "))

                if quantidadetirar > quantidade:
                    confirmar = input("Deseja remover TUDO? s/n: ").lower()

                    if confirmar == "s":
                        estoque.pop(linhaencontrada)
                        print("Produto removido com sucesso!")
                    else:
                        print("Operação Cancelada.")

                elif quantidadetirar <= quantidade:
                    estoque[linhaencontrada][2] = quantidade - quantidadetirar
                    print(f"Quantidade atualizada! Nova quantidade de {produto}: {estoque[linhaencontrada][2]}")

    elif acao == "1":
        produto = input("Digite o nome do produto que deseja adicionar: ").lower()
        existe = False
        a = 0
        while a < len(estoque):
            if estoque[a][0] == produto:
                existe = True
                break
            a += 1

        if not existe:
            categoria = input("Digite a categoria do produto: ").lower()
            quantidade = int(input("Digite a quantidade do produto: "))
            estoque.append([produto, categoria, quantidade])
            print("Produto adicionado com sucesso! Produtos no estoque:", estoque)
        else:
            print("O produto já está em estoque!")


    elif acao == "3":
        produto = input("Digite o nome do produto que deseja alterar: ").lower()

        if produto in estoque:
            novo_produto = input("Digite o novo nome do produto: ").lower()

            if novo_produto not in estoque:
                indice = estoque.index(produto)
                estoque[indice] = novo_produto
                print("Produto alterado com sucesso!", estoque)
            else:
                print("Esse produto já existe no estoque!")
        else:
            print("O produto não está em estoque!")

    else:
        print("Opção inválida! Escolha de 1 a 4.")

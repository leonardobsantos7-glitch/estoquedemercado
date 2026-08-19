estoque = []

try:
    arquivo = open("estoque.txt", "r")

    for linha in arquivo:
        dados = linha.strip().split("|")

        produto = dados[0]
        categoria = dados[1]
        quantidade = int(dados[2])

        estoque.append([produto, categoria, quantidade])

    arquivo.close()

except FileNotFoundError:
    print("Arquivo de estoque não encontrado. Iniciando com estoque vazio.")


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
        arquivo = open("estoque.txt", "w")

        P = 0

        while P < len(estoque):
            arquivo.write(f"{estoque[P][0]}|{estoque[P][1]}|{estoque[P][2]}\n")
            P += 1

        arquivo.close()

        print("Estoque salvo com sucesso!")
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

        linhaencontrada = -1
        a = 0

        while a < len(estoque):
            if estoque[a][0] == produto:
                linhaencontrada = a
                break
            a += 1

        if linhaencontrada == -1:
            print("O produto não foi encontrado no estoque!")

        else:
            novoproduto = input("Digite o novo nome do produto: ").lower()

            if novoproduto == produto:
                print("O novo nome é igual ao nome atual. Nenhuma alteração foi feita!")

            else:
                existe = False
                a = 0

                while a < len(estoque):
                    if estoque[a][0] == novoproduto:
                        existe = True
                        break
                    a += 1

                if existe:
                    print("Esse produto já existe no estoque!")

                else:
                    estoque[linhaencontrada][0] = novoproduto
                    print("Produto alterado com sucesso!")

    else:
        print("Opção inválida! Escolha de 1 a 4.")

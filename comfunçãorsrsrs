from operator import truediv

estoque = []

def carregar():
    try:
        arquivo = open("estoque.txt", "r")
        for linha in arquivo:
            dados = linha.strip().split("|")

            produtos = dados[0]
            categoria = dados[1]
            quantidade = int(dados[2])

            estoque.append([produtos, categoria, quantidade])
        arquivo.close()
    except FileNotFoundError:
        print("Arquivo de Estoque não encontrado. Iniciando com estoque vazio.")

def salvar():
    arquivo = open("estoque.txt", "w")
    P = 0
    while P < len(estoque):
        arquivo.write(f"{estoque[P][0]}|{estoque[P][1]}|{estoque[P][2]}\n")
        P += 1
    arquivo.close()
    print("Estoque salvo!")
    print("Encerrando programa, produtos atuais em estoque: ", estoque)

def exibir():
    print("\n--- Estoque Atual ---")
    if not estoque:
        print("Estoque Vazio")
    else:
        P = 0
        while P < len(estoque):
            print(f"📦 Produto: {estoque[P][0]} | Categoria: {estoque[P][1]} | Qtd: {estoque[P][2]}")
            P += 1
    print("-" * 20)

def buscar(nomepesquisado):
    a = 0
    while a < len(estoque):
        if estoque[a][0] == nomepesquisado:
            return a
        a += 1
    return -1

def definircategoria():
    categoria = input("Insira a categoria do produto: ").lower()
    return categoria

def definirquantidade():
    quantidade = int(input("Insira a quantidade do produto: "))
    return quantidade

def adicionar():
    produto = input("Insira o nome do produto que deseja adicionar: ").lower()
    linhaencontrada = buscar(produto)
    if linhaencontrada == -1:
        categoria = definircategoria()
        quantidade = definirquantidade()

        estoque.append([produto, categoria, quantidade])
        print("Produto adicionado com sucesso!")
    else:
        print("Já em estoque")

def remover():
    produto = input("Insira o nome do produto para remover ou apenas dar baixa: ").lower()
    linhaencontrada = buscar(produto)

    if linhaencontrada == -1:
        print("Não está em estoque")
    else:
        quantidade = estoque[linhaencontrada][2]
        print("Quantidade: ", quantidade)

        escolha = input("Deseja remover tudo (1) ou uma certa quantidade (2)? ").lower()

        if escolha == "1":
            estoque.pop(linhaencontrada)
            print("Produto removido com sucesso!")

        elif escolha == "2":
            while True:
                quantidadetirar = int(input("Insira a quantidade do produto para remover do estoque: "))

                if quantidadetirar > quantidade:
                    print(f"Aviso: Você tentou tirar {quantidadetirar}, mas só existem {quantidade} em estoque.")
                    confirmar = input("Remover tudo? s/n ").lower()

                    if confirmar == "s":
                        estoque.pop(linhaencontrada)
                        print("Produto removido com sucesso!")
                        break
                    else:
                        print("Digite uma quantidade válida abaixo")

                elif quantidadetirar <= quantidade:
                    estoque[linhaencontrada][2] = quantidade - quantidadetirar
                    print(f"Quantidade atualizada! Nova quantidade de {produto}: {estoque[linhaencontrada][2]}")
                    break

def alterar():
    produto = input("Digite o nome do produto que deseja alterar: ").lower()
    linhaencontrada = buscar(produto)

    if linhaencontrada == -1:
        print("O produto não foi encontrado!")
    else:
        print(f"\n✏️ Produto Encontrado: {estoque[linhaencontrada]}")
        print("O que você deseja alterar?")
        print("1 - Nome do Produto")
        print("2 - Categoria")
        print("3 - Quantidade (Definir novo valor)")

        opcao = input("Deseja alterar o que? 1-3 ").lower()

        if opcao == "1":
            novoproduto = input("Digite o nome novo do produto: ").lower()
            if novoproduto == produto:
                print("Nome igual, nada feito")
            else:
                if buscar(novoproduto) != -1:
                    print("Já existe no estoque")
                else:
                    estoque[linhaencontrada][0] = novoproduto
                    print("Produto alterado com sucesso!")

        elif opcao == "2":
            novacategoria = definircategoria()
            estoque[linhaencontrada][1] = novacategoria
            print("Categoria alterada com sucesso!")

        elif opcao == "3":
            novaquantidade = definirquantidade()
            estoque[linhaencontrada][2] = novaquantidade
            print("Quantidade updated com sucesso!")
        else:
            print("Inválido")

def sair():
    salvar()
    print("Obrigado por usar o sistema de estoque! Até logo.")


carregar()

while True:
    exibir()
    acao = input("Deseja adicionar(1), remover(2), alterar(3) ou sair(4)? ").lower()

    if acao == "1":
        adicionar()
    elif acao == "2":
        remover()
    elif acao == "3":
        alterar()
    elif acao == "4":
        sair()
        break
    else:
        print("Opção inválida! Escolha de 1 a 4.")

estoque = ["arroz"]

while True:
  acao = input("Deseja adicionar, remover, alterar ou sair? ").lower()

  if acao == "sair":
    print("Encerrando o programa, produtos atuais em estoque:", estoque)
    break

  elif acao == "remover":
    produto = input("Digite o nome do produto que deseja remover: ").lower()
    if produto in estoque:
      estoque.remove(produto)
      print("Produto removido com sucesso!", estoque)
    else:
      print("O produto não está em estoque!")

  elif acao == "adicionar":
    produto = input("Digite o nome do produto que deseja adicionar: ").lower()
    if produto not in estoque:
      estoque.append(produto)
      print("Produto adicionado com sucesso! Produtos no estoque:", estoque)
    else:
      print("O produto já está em estoque!")

  elif acao == "alterar":
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


estoque = ["arroz"]

while True:
  acao = input("Deseja adicionar, remover ou sair? ").lower()

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


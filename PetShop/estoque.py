from dados import atendimentoP, produtos


def verestoqueservicos():
    print("-----ESTOQUE DE SERVIÇOS--------")
    if len(atendimentoP) == 0:
        print("Não há serviço no estoque.")
    else:
        for s in atendimentoP:
            print(f'Serviço:{s["nome"]} | Preço:{s["preco"]} | Quantidade:{s["disponibilidade"]} ')


def verestoqueprodutos():
    print("-----ESTOQUE DE PRODUTOS--------")
    if len(produtos) == 0:
        print("Não há produtos no estoque.")
    else:
        for p in produtos:
            print(f'Produto:{p["nome"]} | Preço: {p["preco"]} | Quantidade:{p["estoque"]}')


def atualizarestoque():
    escolhaEstoque = input("Você quer atualizar 'a'(serviços) ou 'b'(produtos)? ").lower()

    if escolhaEstoque == "a":
        print("-----ATUALIZAR ESTOQUE DE SERVIÇOS--------")
        for indice in range(len(atendimentoP)):
            print(f"Serviço{indice} - Serviço{atendimentoP[indice]["nome"]}  (atual: {atendimentoP[indice]["disponibilidade"]})")

        indice = int(input("Digite o indice do serviço que você deseja atualizar: "))
        while indice < 0 or indice >= len(atendimentoP):
            print("Indice Inválido. Tente novamente!")
            indice = int(input("Digite o indice do serviço que você deseja atualizar: "))

        novaQuantidade = int(input("Digite a nova quantidade: "))
        atendimentoP[indice]["quantidade"] = novaQuantidade
        print("Estoque atualizado com sucesso.")

    elif escolhaEstoque == "b":
        print("-----ATUALIZAR ESTOQUE DE PRODUTOS--------")
        for indice in range(len(produtos)):
            print(f"Produto{indice} - Produtos{produtos[indice]["nome"]}  (atual: {produtos[indice]["estoque"]})")

        indice = int(input("Digite o indice do produto que você deseja atualizar: "))
        while indice < 0 or indice >= len(produtos):
            print("Indice Inválido. Tente novamente!")
            indice = int(input("Digite o indice do produto que você deseja atualizar: "))

        novaQuantidade = int(input("Digite a nova quantidade: "))
        produtos[indice]["estoque"] = novaQuantidade
        print("Estoque atualizado com sucesso.")


def removerestoque():
    escolhaEstoque = input("Você quer remover 'a'(serviços) ou 'b'(produtos)? ").lower()

    if escolhaEstoque == "a":
        print("-----REMOVER DE ESTOQUE DE SERVIÇOS--------")
        for indice in range(len(atendimentoP)):
            print(f"Serviço {indice} - Serviços {atendimentoP[indice]['nome']}")

        indice = int(input("Digite o indice do serviço que você deseja remover: "))
        while indice < 0 or indice >= len(atendimentoP):
            print("Indice Inválido. Tente novamente!")
            indice = int(input("Digite o indice do serviço que você deseja remover: "))

        atendimentoP.remove(atendimentoP[indice])

    if escolhaEstoque == "b":
        print("-----REMOVER DE ESTOQUE DE PRODUTOS--------")
        for indice in range(len(produtos)):
            print(f"Produto {indice} - Produtos {produtos[indice]['nome']}")

        indice = int(input("Digite o indice do produto que você deseja remover: "))
        while indice < 0 or indice >= len(produtos):
            print("Indice Inválido. Tente novamente!")
            indice = int(input("Digite o indice do produto que você deseja remover: "))

        produtos.remove(produtos[indice])


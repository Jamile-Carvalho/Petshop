from dados import atendimentoP, produtos


def verestoqueservicos():
    print("-----ESTOQUE DE SERVIÇOS--------")
    if len(atendimentoP) == 0:
        print("Não há serviço no estoque.")
    else:
        print("-----ESTOQUE DE SERVIÇOS--------")
        for s in atendimentoP:
            print(f"Serviço:{s[0]} | Preço:{s[1]} | Quantidade:{s[2]} ")


def verestoqueprodutos():
    print("-----ESTOQUE DE PRODUTOS--------")
    if len(produtos) == 0:
        print("Não há produtos no estoque.")
    else:
        print("-----ESTOQUE DE PRODUTOS--------")
        for p in produtos:
            print(f"Produto:{p[0]} | Preço: {p[1]} | Quantidade:{p[2]}")


def atualizarestoque():
    escolhaEstoque = input("Você quer atualizar 'a'(serviços) ou 'b'(produtos)? ").lower()

    if escolhaEstoque == "a":
        print("-----ATUALIZAR ESTOQUE DE SERVIÇOS--------")
        for indice in range(len(atendimentoP)):
            print(f"Serviço{indice} - Serviço{atendimentoP[indice][0]}  (atual: {atendimentoP[indice][2]})")

        indice = int(input("Digite o indice do serviço que você deseja atualizar: "))
        while indice < 0 or indice >= len(atendimentoP):
            print("Indice Inválido. Tente novamente!")
            indice = int(input("Digite o indice do serviço que você deseja atualizar: "))

        novaQuantidade = int(input("Digite a nova quantidade: "))
        atendimentoP[indice][2] = novaQuantidade
        print("Estoque atualizado com sucesso.")

    elif escolhaEstoque == "b":
        print("-----ATUALIZAR ESTOQUE DE PRODUTOS--------")
        for indice in range(len(produtos)):
            print(f"Produto{indice} - Produtos{produtos[indice][0]}  (atual: {produtos[indice][2]})")

        indice = int(input("Digite o indice do produto que você deseja atualizar: "))
        while indice < 0 or indice >= len(produtos):
            print("Indice Inválido. Tente novamente!")
            indice = int(input("Digite o indice do produto que você deseja atualizar: "))

        novaQuantidade = int(input("Digite a nova quantidade: "))
        produtos[indice][2] = novaQuantidade
        print("Estoque atualizado com sucesso.")


def removerestoque():
    escolhaEstoque = input("Você quer remover 'a'(serviços) ou 'b'(produtos)? ").lower()

    if escolhaEstoque == "a":
        print("-----REMOVER DE ESTOQUE DE SERVIÇOS--------")
        for indice in range(len(atendimentoP)):
            print(f"Serviço {indice} - Serviços {atendimentoP[indice][0]}")

        indice = int(input("Digite o indice do serviço que você deseja remover: "))
        while indice < 0 or indice >= len(atendimentoP):
            print("Indice Inválido. Tente novamente!")
            indice = int(input("Digite o indice do serviço que você deseja remover: "))

        atendimentoP.remove(atendimentoP[indice])

    if escolhaEstoque == "b":
        print("-----REMOVER DE ESTOQUE DE PRODUTOS--------")
        for indice in range(len(produtos)):
            print(f"Produto {indice} - Produtos {produtos[indice][0]}")

        indice = int(input("Digite o indice do produto que você deseja remover: "))
        while indice < 0 or indice >= len(produtos):
            print("Indice Inválido. Tente novamente!")
            indice = int(input("Digite o indice do produto que você deseja remover: "))

        produtos.remove(produtos[indice])

        # perguntar a Guilherme porque o print de toda a parte de estoque,
        # como, por exemplo, REMOVER ESTOQUE está ficando duplicado


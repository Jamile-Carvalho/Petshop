from dados import produtos, atendimentoP


def cadastrarprodutos():
    print("--------CADASTRAMENTO FLASH-------")
    print("---------NOVO PRODUTO------------")
    quantidadep = int(input("Digite a quantidade de produtos que você deseja cadastrar: "))
    
    for s in range(quantidadep):
        print(f"Serviço {s+1} de {quantidadep}")
        nomeatentimentoP = input("Digite o nome do novo produto:  ").lower()
        descricaoatentimentoP = input("Digite uma descrição para o novo produto cadastrado: ").lower()
        preco = float(input("Digite o valor do novo prduto R$: "))

        while preco < 0:
            print("Digite um preço inválido! Tente Novamente!")
            preco = float(input("Digite o valor do novo produto R$: "))

        HorariosS = int(input("Digite o horário do novo produto entre 10 da manhã e 18 da tarde: "))
        while HorariosS < 10 or HorariosS > 18:
            print("Horário inválido! Digite um horário entre 10 e 18.")
            HorariosS = int(input("Digite o horário do novo produto: "))
            print("Horário Válido")

        atendimentoP.append([nomeatentimentoP, descricaoatentimentoP, HorariosS, preco, quantidadep])

        print(f"O novo produto é {nomeatentimentoP}\n"
              f"Descrição: {descricaoatentimentoP}\n"
              f"Preço - R$: {preco}\n"
              f"Horário: {HorariosS}\n"
              f"Cadastrado com sucesso.")

    return quantidadep

def buscarprodutos():
    print("---------BUSCAR PRODUTOS------------")
    buscar = input('Digite o produto que deseja buscar: ').lower()
    produtoEncontrado = 0

    for p in produtos:
        if buscar in p[0].lower():
            print('------PRODUTO ENCONTRADO--------')
            print(f'Nome: {p[0]}')
            print(f'Preço R$: {p[1]}')
            produtoEncontrado = 1

    if produtoEncontrado == 0:
        print('Produto não encontrado')

def listarprodutos():
    print("---------LISTA DE PRODUTOS------------")
    for p in produtos:
        print(f"Produto: {p[0]} | Preço: {p[1]}")

def atualizarprodutos():
    print("---------ATUALIZAR LISTA DE PRODUTOS------------")
    for indice in range(len(produtos)):
        print(f"Produto {indice} - Produtos {produtos[indice][0]}")

    indice = int(input("Digite o indice do produto que você deseja atualizar: "))
    while indice < 0 or indice >= len(produtos):
        print("Indice Inválido. Tente novamente!")
        indice = int(input("Digite o indice do produto que você deseja atualizar: "))

    print(f"Produto Atual: {produtos[indice][0]}")
    print(f"Preço Atual: {produtos[indice][1]}")

    novo_nomeP = input("Digite o nome do novo produto: ").lower()
    novo_precoP = float(input("Digite o novo preço do produto: "))

    novaSublistaProdutos = [novo_nomeP, novo_precoP]
    produtos[indice] = novaSublistaProdutos

    print("Produto atualizado com sucesso!!")

def removerprodutos():
    print("---------REMOVER PRODUTOS------------")
    for indice in range(len(produtos)):
        print(f"Produto {indice} - Produtos {produtos[indice][0]}")

    indice = int(input("Digite o indice que você deseja remover: "))
    while indice < 0 or indice >= len(produtos):
        print("Indice Inválido. Tente novamente!")
        indice = int(input("Digite o indice que você deseja remover: "))

    produtos.remove(produtos[indice])

from dados import produtos 


def cadastrarprodutos():
    print("--------CADASTRAMENTO FLASH-------")
    print("---------NOVO PRODUTO------------")
    quantidadep = int(input("Digite a quantidade de produtos que você deseja cadastrar: "))
    
    for s in range(quantidadep):
        print(f"Serviço {s+1} de {quantidadep}")
        nomeproduto = input("Digite o nome do novo produto:  ").lower()
        descricaoproduto = input("Digite uma descrição para o novo produto cadastrado: ").lower()
        preco = float(input("Digite o valor do novo produto R$: "))

        while preco < 0:
            print("Digite um preço inválido! Tente Novamente!")
            preco = float(input("Digite o valor do novo produto R$: "))

        produtos.append({
            "nome": nomeproduto,
            "descriçãodoproduto": descricaoproduto,
            "preco": preco

        })
            
        print(f'O novo produto é {nomeproduto}\n Descrição: {descricaoproduto}\n Preço - R$: {preco}\n Cadastrado com sucesso.')

    return quantidadep

def buscarprodutos():
    print("---------BUSCAR PRODUTOS------------")
    buscar = input('Digite o produto que deseja buscar: ').lower()
    produtoEncontrado = 0
    for p in produtos:
        if buscar in p['nome'].lower():
            print('------PRODUTO ENCONTRADO--------')
            print(f'Nome: {p["nome"]}')
            print(f'Preço R$: {p["preco"]}')
            produtoEncontrado = 1

    if produtoEncontrado == 0:
        print('Produto não encontrado')

def listarprodutos():
    print("---------LISTA DE PRODUTOS------------")
    for p in produtos:
        print(f'Produto: {p["nome"]} | Preço: {p["preco"]}')

def atualizarprodutos():
    print("---------ATUALIZAR LISTA DE PRODUTOS------------")
    for indice in range(len(produtos)):
        print(f"Produto {indice} - Produtos {produtos[indice]['nome']}")

    indice = int(input("Digite o indice do produto que você deseja atualizar: "))
    while indice < 0 or indice >= len(produtos):
        print("Indice Inválido. Tente novamente!")
        indice = int(input("Digite o indice do produto que você deseja atualizar: "))

    print(f"Produto Atual: {produtos[indice]['nome']}")
    print(f"Preço Atual: {produtos[indice]['preco']}")

    novo_nomeP = input("Digite o nome do novo produto: ").lower()
    novo_precoP = float(input("Digite o novo preço do produto: "))

    produtos[indice]['nome'] = novo_nomeP
    produtos[indice]['preco'] = novo_precoP

    print("Produto atualizado com sucesso!!")

def removerprodutos():
    print("---------REMOVER PRODUTOS------------")
    for indice in range(len(produtos)):
        print(f'Produto {indice} - Produtos {produtos[indice]['nome']}')
    indice = int(input("Digite o indice que você deseja remover: "))
    while indice < 0 or indice >= len(produtos):
        print("Indice Inválido. Tente novamente!")
        indice = int(input("Digite o indice que você deseja remover: "))

    produtos.remove(produtos[indice])

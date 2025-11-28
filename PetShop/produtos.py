from dados import produtos, atendimentoP


def cadastrarprodutos():
    print("--------CADASTRAMENTO FLASH-------")
    print("---------NOVO SERVIÇO------------")
    quantidadep = int(input("Digite a quantidade de serviços que você deseja cadastrar:"))
    for s in range(quantidadep):
        print(f'Serviço {s+1} de {quantidadep}')
        nomeatentimentoP = input("Digite o nome do novo serviço:  ").lower()
        descricaoatentimentoP = input("Digite uma descrição para o novo serviço cadastrado:").lower()
        preco = float(input("Digite o valor do novo serviço R$: "))
    while preco < 0:
        print("Digite um preço inválido!Tente Novamente!")
        preco = float(input("Digite o valor do novo serviço R$: "))
                                        
        HorariosS = int(input("Digite o horário do novo serviço entre 10 da manhã e 18 da tarde:"))
        while HorariosS < 10 or HorariosS > 18:
            print("Horário inválido! Digite um horário maior que 0.")
            HorariosS = int(input("Digite o horário do novo serviço:"))
            print("Horário Válido")

        atendimentoP.append([nomeatentimentoP,descricaoatentimentoP,HorariosS, preco, quantidadep])
        print(f"O novo serviço é {nomeatentimentoP}\n Descrição: {descricaoatentimentoP}\n Preço - R$:{preco}\n Horário: {HorariosS}\n Cadastrados com sucesso.")
        return quantidadep
    
def buscarprodutos(): 
    print("---------BUSCAR SERVIÇOS------------")
    buscar = input('Digite o produto que deseja buscar:').lower()
    produtoEncontrado = 0
    for p in produtos:
        if buscar.lower() in p[0].lower():
            print('------PRODUTO ENCONTRADO--------')
            print(f'Nome:{p[0]}')
            print(f'Preço R$:{p[1]}')
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
    while indice < 0 or indice >= (len(produtos)):
        print("Indice Inválido.Tente novamente!")
        indice = int(input("Digite o indice do produto que você deseja atualizar: "))

    print(f"Produto Atual: {produtos[indice][0]}")
    print(f"Preço Atual: {produtos[indice][1]}")

    novo_nomeP = input("Digite o nome do novo produto: ").lower()
    novo_precoP = float(input("Digite o novo preço do produto: "))

    novaSublistaProdutos = [novo_nomeP, novo_precoP,]
    produtos[indice] = novaSublistaProdutos
    print("Produto atualizado com sucesso!!")

def removerprodutos():
    print("---------REMOVER PRODUTOS------------")
    for indice in range(len(produtos)):
        print(f"Produto {indice} - Produtos {produtos[indice][0]}")

    indice = int(input("Digite o indice que você deseja remover: "))
    while indice < 0 or indice >= (len(produtos)):
        print("Indice Inválido.Tente novamente!")
        indice = int(input("Digite o indice que você deseja remover: "))

    produtos.remove(produtos[indice])
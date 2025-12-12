from dados import atendimentoP


def cadastrarservicos():
    print("--------CADASTRAMENTO FLASH-------")
    print("---------NOVO SERVIÇO------------")
    quantidade = int(input("Digite a quantidade de serviços que você deseja cadastrar:"))
    for s in range(quantidade):
        print(f'Serviço {s+1} de {quantidade}')
        nomeatentimentoP = input("Digite o nome do novo serviço:  ").lower()
        descricaoatentimentoP = input("Digite uma descrição para o novo serviço cadastrado:").lower()
        preco = float(input("Digite o valor do novo serviço R$: "))
        while preco < 0:
            print("Preço inválido!Tente Novamente!")
            preco = float(input("Digite o valor do novo serviço R$: "))
            print("Preço Válido!")
                                        
        HorariosS = int(input("Digite o horário do novo serviço entre 10 da manhã e 18 da tarde:"))
        while HorariosS < 10 or HorariosS > 18:
            print("Horário inválido! Digite um horário maior que 0.")
            HorariosS = int(input("Digite o horário do novo serviço:"))
            print("Horário Válido")

        atendimentoP.append({
            "atendimento":nomeatentimentoP,
            "descrição":descricaoatentimentoP,
            "horario":HorariosS, 
            "preco":preco, 
            "quantidade":quantidade,
            "disponibilidade":3
            })
        
        print(f'O novo serviço é {nomeatentimentoP}\n Descrição: {descricaoatentimentoP}\n Preço - R$:{preco}\n Horário: {HorariosS}\n Cadastrados com sucesso.')

def buscarservicos():
    print("---------BUSCAR SERVIÇOS------------")
    buscar = input('Digite o produto que deseja buscar:').lower()
    for s in atendimentoP:
        if buscar.lower() in s['atendimento'].lower():
            print('------SERVIÇO ENCONTRADO--------')
            print(f"Nome:{s['atendimento']}")
            print(f"Preço R$:{s['preco']}")
        atentimentoPEncontrado = 1
        
        if atentimentoPEncontrado == 0:
            print('Serviço não encontrado')

def listarservicos():
    print("---------LISTA DE SERVIÇOS------------") 
    for s in atendimentoP: 
        print(f"Serviço: {s['atendimento']} | Preço: {s['preco']}")

def atualizarservicos():
    print("---------ATUALIZAR LISTA DE SERVIÇOS------------")
    for indice in range(len(atendimentoP)):
        print(f"Serviço {indice} - Serviços {atendimentoP[indice]['atendimento']}")

    indice = int(input("Digite o indice que você deseja atualizar: "))
    while indice < 0 or indice >= len(atendimentoP):
        print("Indice Inválido. Tente novamente!")
        indice = int(input("Digite o indice que você deseja atualizar: "))

    print(f"Servico Atual: {atendimentoP[indice]['atendimento']}")
    print(f"Preço Atual: {atendimentoP[indice]['preco']}")

    novo_nome = input("Digite o nome do novo serviço: ").lower()
    novo_HorariosS = int(input("Digite o novo horário do novo serviço entre 10 da manhã e 18 da tarde: "))
    while novo_HorariosS < 10 or novo_HorariosS > 18:
        print("Horário inválido! O horário deve estar entre 10 e 18.")
        novo_HorariosS = int(input("Digite o horário do novo serviço: "))
    print("Horário Válido!")

    novo_preco = float(input("Digite o novo preço do serviço: "))
    while novo_preco < 0:
        print("Digite um preço válido! Tente novamente!")
        novo_preco = float(input("Digite o valor do novo serviço R$: "))

    atendimentoP[indice]['atendimento'] = novo_nome
    atendimentoP[indice]['horario'] = novo_HorariosS
    atendimentoP[indice]['preco'] = novo_preco

    print("Serviço atualizado com sucesso!!")

def removerservicos():
    print("---------REMOVER SERVIÇOS------------")
    for indice in range(len(atendimentoP)):
        print(f"Serviço {indice} - Serviços {atendimentoP[indice]['atendimento']}")

    indice = int(input("Digite o indice que você deseja remover: "))
    while indice < 0 or indice >= (len(atendimentoP)):
        print("Indice Inválido.Tente novamente!")
        indice = int(input("Digite o indice que você deseja remover: "))
    atendimentoP.remove(atendimentoP[indice])

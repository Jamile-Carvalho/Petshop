from dados import animaisAdocoes

def cadastrarPets():
    print("--------CADASTRAMENTO FLASH-------")
    print("--------PETS---------")
    quantidadePets = int(input("Digite a quantidade de pets que você deseja cadastrar:"))
    for a in range(quantidadePets):
        print(f'Pet {a+1} de {quantidadePets}')
        nomePet = input("Digite o nome do pet:  ").lower()
        especiePet = input("Digite a espécie de pet:")
        descricaoPet = input("Digite uma descrição do pet:").lower()
        idadePet = float(input("Digite a idade do pet: "))
        while idadePet < 0:
            print("Digite uma idade válida!Tente Novamente!")
            idadePet = float(input("Digite a idade do pet: "))
                                        
        animaisAdocoes.append({
            "nome":nomePet, 
            "especie":especiePet, 
            "descricao":descricaoPet, 
            "idade":idadePet

            })

        print(f"O nome do pet é {nomePet}\n Espécie do Pet: {especiePet}\n Descrição do Pet:{descricaoPet}\n Idade do Pet: {idadePet}\n Cadastrados com sucesso.")

def listarPets():
    print("-----LISTAR DE PETS DISPONIVEIS--------")
    if len(animaisAdocoes) == 0:
        print("Nenhum animal está disponível para ser adotado!")
                                    
    else:
        for a in animaisAdocoes: 
           print(f"Nome: {a['nome']} | Espécie: {a['especie']} | Idade: {a['idade']}")

def atualizarPets():
    print("-----ATUALIZAR PETS--------")
    for indice in range(len(animaisAdocoes)):
        print(f"Animal {indice} - Animais {animaisAdocoes[indice]['nome']}")
    indice = int(input("Digite o indice que você deseja atualizar: "))
    while indice < 0 or indice >= (len(animaisAdocoes)):
        print("Indice Inválido.Tente novamente!")
        indice = int(input("Digite o indice que você deseja atualizar: "))

    print(f"Nome do Pet Atual: {animaisAdocoes[indice]['nome']}")
    print(f"Espécie do Pet Atual: {animaisAdocoes[indice]['especie']}")
    print(f"Idade Atual: {animaisAdocoes[indice]['idade']}")

    novo_nomePet = input("Digite o nome do pet: ").lower()
    nova_especiePet = input("Digite a espécie do Pet:")
    nova_idadePet = float(input("Digite a idade do pet: "))

    while nova_idadePet < 0:
        print("Digite uma idade válida!Tente Novamente!")
        nova_idadePet = float(input("Digite a idade do pet: "))

    animaisAdocoes[indice]['nome'] = novo_nomePet
    animaisAdocoes[indice]['especie'] = nova_especiePet
    animaisAdocoes[indice]['idade'] = nova_idadePet

    print("Lista de Pets Disponiveís atualizada com sucesso!!")

def removerPets():
    print("---------REMOVER PETS------------")
    for indice in range(len(animaisAdocoes)):
        print(f"Animal {indice} - Animais {animaisAdocoes[indice]['nome']}")

    indice = int(input("Digite o indice do pet que você deseja remover: "))
    while indice < 0 or indice >= (len(animaisAdocoes)):
        print("Indice Inválido.Tente novamente!")
        indice = int(input("Digite o indice do produto que você deseja remover: "))

    animaisAdocoes.remove(animaisAdocoes[indice])
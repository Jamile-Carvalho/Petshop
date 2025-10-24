usuario = []
servicos = []
while True:
    print("Bem Vindo ao Pet & Cia")
    print("Escolha uma das seguintes opções para prosseguir:")
    print("1-Novo Login")
    print("2-Login")
    print("3-Sair")
    opcao = input("Digite uma opção:")
    if opcao == "3":
        break
    elif opcao != 1 and opcao != 2 and opcao != 0:
        print("Digite uma opção que seja válida!")

    elif opcao == "1":
        print("---------------------------------")
        nome = input("Digite seu nome completo:")
        nascimento = input("Digite sua data de nascimento:")
        idade = int(input("Digite sua idade:"))
        nomepet = input("Digite o nome e a espécie de seu pet:")
        perfil = input("Você é administrador ou cliente: ")
        senha = input("Digite sua senha:")
        confirmarSenha = input("Digite sua senha novamente:")
        usuario.append([nome, nascimento, idade, nomepet, perfil, senha, confirmarSenha])
        print("----------------------------------")

    while True:

        if perfil != "Administrador" and perfil != "Cliente":
            print("Perfil Inválido,tente novamente")
            perfil = input("Digite se você é Administrador ou Cliente: ")

        elif idade < 0 or idade > 105:
            print("Idade Inválida!Veja de novo e digite uma idade válida!")
            idade = int(input("Digite sua idade:"))

        elif senha != confirmarSenha:
            print("As senhas digitas não condizem,tente novamente!")
            senha = input("Digite sua senha:")
            confirmarSenha = input("Digite sua senha novamente:")
            if senha == confirmarSenha:
                break

        elif perfil != "Administrador" and perfil != "Cliente":
            print("Perfil Inválido,tente novamente")
            perfil = input("Digite se você é Administrador ou Cliente: ")
            if perfil == "Administrador" or perfil == "Cliente":
                print("Login concluido com sucesso!")

        elif opcao == "2":
            print("Realize o cadrastro")
            nome = input("Digite seu nome:")
            senha = input("Digite sua senha:")
            confirmarSenha = input("Digite novamente sua senha:")
            perfil = input("Digite se você é Administrador ou Cliente: ")

        while True:
            if senha != confirmarSenha:
                print("As senhas digitas não condizem,tente novamente!")
                senha = input("Digite sua senha:")
                confirmarSenha = input("Digite sua senha novamente:")
            elif senha == confirmarSenha:
                break

            elif perfil != "Administrador" and perfil != "Cliente":
                print("Perfil Inválido,tente novamente")
                perfil = input("Digite se você é Administrador ou Cliente: ")
            if perfil == "Administrador" and perfil == "Cliente":
                print("Login concluido com sucesso!")

        while True:
            print("Escolha uma das seguintes opções para prosseguir:")
            print("1-Gerenciamente de Serviços")
            print("2-Gerenciameto de Produtos")
            print("3-Sair")
            opcao = input("Digite uma das opções para continuar: ")
            if opcao == "3":
                break

            elif opcao == "1":
                while True:
                    print("---------GERENCIADOR DE SERVIÇOS------------")
                    print("Escolha uma das seguintes opções para prosseguir:")
                    print("A-Cadrastrar Serviço")
                    print("B-Buscar/Listar Serviços")
                    print("C-Atualizar Serviço")
                    print("D-Remover Serviço")
                    print("E-Nenhuma das opções acima")
                    opcao_servicos = input("Escolha uma das seguintes opções para prosseguir:")
                    if opcao_servicos == "E":
                        break

                    elif opcao_servicos == "A":
                        print("---------NOVO SERVIÇO------------")
                        nomeServico = input("Digite o nome do novo serviço:  ")
                        preco = float(input("Digite o valor do novo serviço R$: "))
                        servicos.append([nomeServico, preco])
                        print(f"Produto {nomeServico} - R$:{preco} Cadastrado com sucesso.")

                    elif opcao_servicos == "B":
                        print("---------LISTA DE SERVIÇOS------------")
                        for s in servicos:
                            print(f"Serviço: {s[0]} | Preço: {s[1]}")

                    elif opcao_servicos == "C":
                        print("---------ATUALIZAR LISTA DE SERVIÇOS------------")
                        for indice in range(len(servicos)):
                            print(f"Código {indice} - Serviços {servicos[indice][0]}")

                        indice = int(input("Digite o indice que você deseja atualizar: "))
                        while indice < 0 or indice >= (len(servicos)):
                            print("Indice Inválido.Tente novamente!")
                            indice = int(input("Digite o indice que você deseja atualizar: "))

                        print(f"Servico Atual: {servicos[indice][0]}")
                        novo_nome = input("Digite o nome do novo serviço: ")
                        novo_preco = float(input("Digite o novo preço do serviço: "))

                        novaSublistaServicos = [novo_nome, novo_preco]
                        servicos[indice] = novaSublistaServicos
                        print("Serviço atualizado com sucesso!!")

                    elif opcao_servicos == "D":
                        print("---------REMOVER SERVIÇOS------------")
                        for indice in range(len(servicos)):
                            print(f"Código {indice} - Serviços {servicos[indice][0]}")

                        indice = int(input("Digite o indice que você deseja remover: "))
                        while indice < 0 or indice >= (len(servicos)):
                            print("Indice Inválido.Tente novamente!")
                            indice = int(input("Digite o indice que voc~e deseja remover: "))

                            servicos.remove(servicos[indice])

                    else:
                        print("Erro.Escolha uma opção válida!")

                    print("---------------------------------")

                    

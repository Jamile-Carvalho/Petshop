usuario = []
servicos = []
perfil = []
produtos = []
while True:
    print('Bem vindo ao Pet e Cia!!!')
    print('Escolha uma das opções abaixo: ')
    print('1 - Cadastro')
    print('2 - login')
    print('0 - Sair')

    opcao = int(input('digite uma opcao: '))

    if opcao == 0:
        break

    elif opcao != 1 and opcao != 2 and opcao != 0:
        print('digite uma opcao valida!!')

    elif opcao == 1:
        print('efetue seu cadastro!')
        nome = input('nome: ').strip()
        senha = input('senha: ')
        senha2 = input('confirme sua senha: ')
        tipo = input('digite se voce é administrador ou cliente: ').strip()
        idade = int(input('idade: ')) 
        nomePet = input('digite o nome do seu pet: ').strip()

        while True:
            if tipo != 'administrador' and tipo != 'cliente':
                print('tipo invalido,digite o tipo novamente!!')
                tipo = input('digite se voce é administrador ou cliente: ')

            elif senha != senha2:
                print('tem certeza que digitou as duas senhas iguais? Tente novamente')
                senha = input('senha: ')
                senha2 = input('confirme sua senha: ')

            elif idade < 0 or idade > 110:
                print('idade invalida!!Digite novamente!!')
                idade = int(input('idade: '))

            else:
                possuiNome = 0
                for n in usuario:
                    if nome == n[0]:
                        print('Esse nome ja exite!!!Tente outro nome!!!')
                        possuiNome = 1
                        nome = input('nome: ')
                    
                if possuiNome == 0:
                    usuario.append([nome , senha , tipo , idade , nomePet])  
                    print(f'Parabens {nome}, voce foi cadastrado com sucesso!!')
                    break
    if opcao == 2:
        print('faça o seu login!!')
        nome = input('digite seu nome: ')
        senha = input('digite sua senha: ')
        logado = 0
        for i in usuario:
            if i[0] == nome and i[1] == senha:
                logado = 1

        if logado == 0:
            print('usuario nao encontrado!!!login invalido!!!')
        else:
            print(f'login efetuado com sucesso!!Bem vindo {nome}!!')

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
                    print("Bem Vindo ao Gerenciador de Serviços")
                    print("Escolha uma das seguintes opções para prosseguir:")
                    print("a-Cadrastro Flash de Serviço")
                    print("b-Buscar Serviço")
                    print("c-Listar Serviços")
                    print("d-Atualizar Serviço")
                    print("e-Remover Serviço")
                    print("f-Nenhuma das opções acima")
                    opcao_servicos = input("Escolha uma das seguintes opções para prosseguir:").lower()
                    if opcao_servicos == "f":
                        break

                    elif opcao_servicos == "a":
                        print("--------CADASTRAMENTO FLASH-------")
                        print("---------NOVO SERVIÇO------------")
                        quantidade = int(input("Digite a quantidade de serviços que você deseja cadastrar:"))
                        for s in range(quantidade):
                            print(f'Serviço {s+1} de {quantidade}')
                            nomeServico = input("Digite o nome do novo serviço:  ").strip().lower()
                            descricaoServico = input("Digite uma descrição para o novo serviço cadastrado:").strip().lower()
                            preco = float(input("Digite o valor do novo serviço R$: "))
                            while preco < 0:
                                print("Digite um preço válido!Tente Novamente!")
                                preco = float(input("Digite o valor do novo serviço R$: "))
                            
                            HorariosS = int(input("Digite o horário do novo serviço entre 10 da manhã e 18 da tarde:"))
                            while HorariosS < 0:
                                print("Horário inválido! Digite um horário maior que 0.")
                                HorariosS = int(input("Digite o horário do novo serviço:"))
                            if HorariosS > 0 and HorariosS <=18:
                                print("Horário Válido")
                            else:
                                print("Horário Inválido")
                                HorariosS = int(input("Digite o horário do novo serviço:"))

                            servicos.append([nomeServico,descricaoServico,HorariosS, preco])
                            print(f"O novo serviço é {nomeServico}\n Descrição: {descricaoServico}\n Preço - R$:{preco}\n Horário: {HorariosS}\n Cadastrados com sucesso.")

                    elif opcao_servicos =="b":
                        print("---------BUSCAR SERVIÇOS------------")
                        buscar = input('Digite o produto que deseja buscar:')
                        servicosEncontrado = 0
                        for s in servicos:
                          if buscar.lower() in s[0].lower():
                            print('------SERVIÇO ENCONTRADO--------')
                            print(f'Nome:{s[0]}')
                            print(f'Descrição:{s[1]}')
                            print(f'Horário:{s[2]}')
                            print(f'Preço R$:{s[3]}')
                            servicosEncontrado = 1
                        if servicosEncontrado == 0:
                            print('Serviço não encontrado')

                    elif opcao_servicos == "c":
                        print("---------LISTA DE SERVIÇOS------------")
                        for s in servicos:
                            print(f"Serviço: {s[0]} | Descrição: {s[1]} | Horário: {s[2]} | Preço: {s[3]}")

                    elif opcao_servicos == "d":
                        print("---------ATUALIZAR LISTA DE SERVIÇOS------------")
                        for indice in range(len(servicos)):
                            print(f"Código {indice} - Serviços {servicos[indice][0]}")

                        indice = int(input("Digite o indice que você deseja atualizar: "))
                        while indice < 0 or indice >= (len(servicos)):
                            print("Indice Inválido.Tente novamente!")
                            indice = int(input("Digite o indice que você deseja atualizar: "))

                        print(f"Servico Atual: {servicos[indice][0]}")
                        print(f"Descrição Atual: {servicos[indice][1]}")
                        print(f"Horário Atual: {servicos[indice][2]}")
                        print(f"Preço Atual: {servicos[indice][3]}")

                        novo_nome = input("Digite o nome do novo serviço: ")
                        nova_descricao = input("Digite a nova descrição do novo serviço:")
                        novo_HorariosS = int(input("Digite o novo horário do novo serviço entre 10 da manhã e 18 da tarde:"))
                        while novo_HorariosS < 0:
                                print("Horário inválido! Digite um horário maior que 0.")
                                novo_HorariosS = int(input("Digite o horário do novo serviço:"))
                                if novo_HorariosS > 0 and novo_HorariosS <=18:
                                    print("Horário Válido")
                                else:
                                    print("Horário Inválido")
                                    novo_HorariosS = int(input("Digite o horário do novo serviço:"))

                        novo_preco = float(input("Digite o novo preço do serviço: "))
                        while novo_preco < 0:
                                print("Digite um preço válido!Tente Novamente!")
                                novo_preco = float(input("Digite o valor do novo serviço R$: "))

                        novaSublistaServicos = [novo_nome, nova_descricao, novo_HorariosS, novo_preco]
                        servicos[indice] = novaSublistaServicos
                        print("Serviço atualizado com sucesso!!")

                    elif opcao_servicos == "e":
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

            elif opcao == "2":
                while True:
                    print("---------GERENCIADOR DE PRODUTOS------------")
                    print("Bem Vindo ao Gerenciador de Produtos")
                    print("Escolha uma das seguintes opções para prosseguir:")
                    print("a-Cadrastro Flash de Produto")
                    print("b-Buscar Produto")
                    print("c-Listar Produto")
                    print("d-Atualizar Produto")
                    print("e-Remover Produto")
                    print("f-Nenhuma das opções acima")
                    opcao_produtos = input("Escolha uma das seguintes opções para prosseguir:").strip().lower()
                    if opcao_produtos == "f":
                        break

                    elif opcao_produtos == "a":
                        print("--------CADASTRAMENTO FLASH-------")
                        print("---------NOVO PRODUTO------------")
                        quantidade = int(input("Digite a quantidade de produtos que você deseja cadastrar:"))
                        for p in range(quantidade):
                            print(f'Serviço {p+1} de {quantidade}')
                            nomeProduto = input("Digite o nome do novo produto:  ").strip().lower()
                            descricaoProduto = input("Digite uma descrição para o novo produto cadastrado:").strip().lower()
                            preco = float(input("Digite o valor do novo produto R$: "))
                            while preco < 0:
                                print("Digite um preço válido!Tente Novamente!")
                                preco = float(input("Digite o valor do novo produto R$: "))

                            produtos.append([nomeProduto,descricaoProduto, preco])
                            print(f"O novo Produto é {nomeProduto}\n Descrição: {descricaoProduto}\n Preço - R$  {preco}\n Cadastrados com sucesso.")

                    elif opcao_produtos =="b":
                        print("---------BUSCAR PRODUTOS------------")
                        buscar = input('Digite o produto que deseja buscar:').lower().strip()
                        produtoEncontrado = 0
                        for p in produtos:
                            if buscar.lower() in p[0].lower():
                                print('------PRODUTO ENCONTRADO--------')
                                print(f'Nome:{p[0]}')
                                print(f'Descrição:{p[1]}')
                                print(f'Preço R$:{p[2]}')
                                produtoEncontrado = 1
                            if produtoEncontrado == 0:
                                print('Produto não encontrado')

                    elif opcao_produtos == "c":
                        print("---------LISTA DE PRODUTOS------------")
                        for p in produtos:
                            print(f"Produto: {p[0]} | Descrição: {p[1]} | Preço: {p[2]}")

                    elif opcao_produtos == "d":
                        print("---------ATUALIZAR LISTA DE PRODUTOS------------")
                        for indice in range(len(produtos)):
                            print(f"Produto {indice} - Produtos {produtos[indice][0]}")

                        indice = int(input("Digite o indice do produto que você deseja atualizar: "))
                        while indice < 0 or indice >= (len(produtos)):
                            print("Indice Inválido.Tente novamente!")
                            indice = int(input("Digite o indice do produto que você deseja atualizar: "))

                        print(f"Produto Atual: {produtos[indice][0]}")
                        print(f"Descrição Atual: {produtos[indice][1]}")
                        print(f"Preço Atual: {produtos[indice][2]}")

                        novo_nomeP = input("Digite o nome do novo produto: ")
                        nova_descricaoP = input("Digite a nova descrição do novo produto: ")
                        novo_precoP = float(input("Digite o novo preço do produto: "))

                        novaSublistaProdutos = [novo_nomeP, nova_descricaoP, novo_precoP]
                        produtos[indice] = novaSublistaProdutos
                        print("Produto atualizado com sucesso!!")

                    elif opcao_produtos =="e":
                        print("---------REMOVER PRODUTOS------------")
                        for indice in range(len(produtos)):
                            print(f"Produto {indice} - Produtos {produtos[indice][0]}")

                        indice = int(input("Digite o indice do produto que você deseja remover: "))
                        while indice < 0 or indice >= (len(produtos)):
                            print("Indice Inválido.Tente novamente!")
                        indice = int(input("Digite o indice do produto que você deseja remover: "))

                        produtos.remove(produtos[indice])
                        #perguntar a Guilherme porque quando rodo o código aparece a pergunta de qual indice quero remover duas vezes

                    else:
                        print("Erro.Escolha uma opção válida!")
                    print("---------------------------------")
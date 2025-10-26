usuario = []
servicos = []
produtos = []
perfil = []

while perfil !='Administrador' and perfil !='Cliente':
    print('Perfil Inválido,tente novamente')
    perfil = input('Digite se você é Administrador ou Cliente: ')
    if perfil == 'Administrador' and perfil =='Cliente':
        print('Login concluido com sucesso!')


while True:
    print('Escolha uma das seguintes opções para prosseguir:')
    print('1-Gerenciamente de Serviços')
    print('2-Gerenciameto de Produtos')
    print('3-Sair')
    opcao = input('Digite uma das opções para continuar: ')
    if (opcao == '3'):
        break
         
    elif (opcao == '1'):
        while True:
            print('---------GERENCIADOR DE SERVIÇOS------------')
            print('Escolha uma das seguintes opções para prosseguir:')
            print('A-Cadrastrar Serviço')
            print('B-Buscar/Listar Serviços')
            print('C-Atualizar Serviço')
            print('D-Remover Serviço')
            print('E-Nenhuma das opções acima')
            opcao_servicos = input('Escolha uma das seguintes opções para prosseguir:')
            if (opcao_servicos == 'E'):
                break

            elif (opcao_servicos == 'A'):
                print('---------NOVO SERVIÇO------------')
                nomeServico =input('Digite o nome do novo serviço:  ')
                descricao = input('Digite a descrição de seu serviço: ')
                preco = float(input('Digite o valor do novo serviço R$: '))
                servicos.append([nomeServico, descricao, preco])
                print(f'Produto {nomeServico}\n Descrição: {descricao}\n e Preço - R$:{preco} \nCadastrado com sucesso.')

            elif (opcao_servicos == 'B'):
                print('---------LISTA DE SERVIÇOS------------')
                for s in servicos:
                    print(f'Serviço: {s[0]} | Descrição {s[1]} | Preço: {s[2]}')

            elif (opcao_servicos == 'C'):
                print('---------ATUALIZAR LISTA DE SERVIÇOS------------')
                for indice in range(len(servicos)):
                    print(f'Serviço {indice} - Serviços {servicos[indice][0]}')

                indice = int(input('Digite o indice do serviço que você deseja atualizar: '))
                while indice < 0 or indice >= (len(servicos)):
                     print('Indice Inválido.Tente novamente!')
                     indice = int(input('Digite o indice do serviço que você deseja atualizar: '))

                print(f'Servico Atual: {servicos[indice][0]}')
                novo_nome = input('Digite o nome do novo serviço: ')
                nova_descricao = input('Digite a nova descrição de seu serviço: ')
                novo_preco = float(input('Digite o novo preço do serviço: '))

                novaSublistaServicos = [novo_nome, nova_descricao, novo_preco]
                servicos[indice] = novaSublistaServicos
                print('Serviço atualizado com sucesso!!')

            elif (opcao_servicos == 'D'):
                print('---------REMOVER SERVIÇOS------------')
                for indice in range(len(servicos)):
                    print(f'Serviço {indice} - Serviços {servicos[indice][0]}')

                indice = int(input('Digite o indice do serviço que você deseja remover: '))
                while indice < 0 or indice >= (len(servicos)):
                    print('Indice Inválido.Tente novamente!')
                    indice = int(input('Digite o indice do serviço que você deseja remover: '))

                servicos.remove(servicos[indice])

            else:
                print('Erro.Escolha uma opção válida!')

            print('---------------------------------')
    
    elif (opcao == '2'):
        while True:
            print('---------GERENCIADOR DE PRODUTOS------------')
            print('Escolha uma das seguintes opções para prosseguir:')
            print('A-Cadrastrar Produto')
            print('B-Buscar/Listar Produtos')
            print('C-Atualizar Produto')
            print('D-Remover Produto')
            print('E-Nenhuma das opções acima')
            opcao_produtos = input('Escolha uma das seguintes opções para prosseguir:')
            if (opcao_produtos == 'E'):
                break

            elif (opcao_produtos == 'A'):
                print('---------NOVO PRODUTO------------')
                nomeProduto =input('Digite o nome do novo produto:  ')
                descricao = input('Digite a descrição de seu produto: ')
                preco = float(input('Digite o valor do novo produto R$: '))
                produtos.append([nomeProduto, descricao, preco])
                print(f'Produto {nomeProduto}\n Descrição: {descricao}\n e Preço - R$:{preco} \nCadastrado com sucesso.')

            elif (opcao_produtos == 'B'):
                print('---------LISTA DE PRODUTOS------------')
                for s in produtos:
                    print(f'Produto: {s[0]} | Descrição {s[1]} | Preço: {s[2]}')

            elif (opcao_produtos == 'C'):
                print('---------ATUALIZAR LISTA DE PRODUTOS------------')
                for indice in range(len(produtos)):
                    print(f'Produto {indice} - Produtos {produtos[indice][0]}')

                indice = int(input('Digite o indice do produto que você deseja atualizar: '))
                while indice < 0 or indice >= (len(produtos)):
                     print('Indice Inválido.Tente novamente!')
                     indice = int(input('Digite o indice do produto que você deseja atualizar: '))

                print(f'Produto Atual: {produtos[indice][0]}')
                novo_nomeP = input('Digite o nome do novo produto: ')
                novo_precoP = float(input('Digite o novo preço do produto: '))
                nova_descricaoP = input('Digite a nova descrição de seu produto: ')

                novaSublistaProdutos = [novo_nomeP, novo_precoP, nova_descricaoP]
                produtos[indice] = novaSublistaProdutos
                print('Produto atualizado com sucesso!!')

            elif (opcao_produtos == 'D'):
                print('---------REMOVER PRODUTOS------------')
                for indice in range(len(produtos)):
                    print(f'Produto {indice} - Produtos {produtos[indice][0]}')

                indice = int(input('Digite o indice do produto que você deseja remover: '))
                while indice < 0 or indice >= (len(produtos)):
                    print('Indice Inválido.Tente novamente!')
                    indice = int(input('Digite o indice do produto que você deseja remover: '))

                produtos.remove(produtos[indice])
            
            else:
                print('Erro.Escolha uma opção válida!')

            print('---------------------------------')





            

        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            








                


        


#Importando LISTAS GLOBAIS

import dados

#Impotando os MENUS:
import menus 

#Importando as FUNÇÕES:
import servicos 

import produtos 

import estoque 

import adocoes

import backup

import importarbackup

import tabelas

import funcoescami



usuario = []
produtos = [
    {'nome': 'ração', 'preco': 150, 'estoque': 70},
    {'nome': 'shampoo', 'preco': 30, 'estoque': 70},
    {'nome': 'condicionador', 'preco': 30, 'estoque': 70},
    {'nome': 'brinquedo', 'preco': 20, 'estoque': 70},
    {'nome': 'coleira', 'preco': 20, 'estoque': 70},
    {'nome': 'casinha', 'preco': 80, 'estoque': 70},
    {'nome': 'caminha', 'preco': 100, 'estoque': 70},
    {'nome': 'caixa de transporte', 'preco': 210, 'estoque': 70},
    {'nome': 'escova', 'preco': 25, 'estoque': 70},
    {'nome': 'kit de perfume', 'preco': 150, 'estoque': 70}
]

atendimentoP = [
    {'nome': 'banho', 'preco': 70, 'disponibilidade': 3},
    {'nome': 'tosa', 'preco': 40, 'disponibilidade': 3},
    {'nome': 'banho e tosa', 'preco': 100, 'disponibilidade': 3},
    {'nome': 'consulta', 'preco': 120, 'disponibilidade': 3}
]

HorariosD = [
    {'horario': '10h'},
    {'horario': '12h'},
    {'horario': '16h'},
    {'horario': '18h'}
]

animaisAdocoes = []
listaD = []
servicos = []
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
avaliacao = []
valort = 0


while True:
    funcoescami.menuinicial()
    opcao = int(input('digite uma opcao: '))

    if opcao == 0:
        break

    elif opcao != 1 and opcao != 2 and opcao != 0:
        print('digite uma opcao valida!!')

    elif opcao == 1:
        funcoescami.cadastrarUsuario(usuario)

    elif opcao == 2:
        if funcoescami.login(usuario):
            funcoescami.menucompra()

            opcao = int(input('digite que opcao deseja realizar: '))

            if opcao == 0:
                break

            elif opcao != 0 and opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
                print('opcao invalida digite novamente')
                opcao = int(input('digite que opcao deseja realizar: '))

            elif opcao == 1:
                print('Realize sua compra agora mesmo!')
                funcoescami.listaProdutos(produtos)
                funcoescami.compraraP(produtos)

            elif opcao == 2:
                print('escolha seu atendimento:')
                valort = 0

                funcoescami.listaratendimento(atendimentoP)

                print('Qual atendimento deseja realizar?')
                atendimento = input(
                    'digite o atendimento que deseja realizar: ').lower()

                if funcoescami.acharAtendimento(atendimentoP, atendimento) == True:
                    for h in range(len(HorariosD)):
                        print(f"horarios: {HorariosD[h]['horario']}")

                    horario = input('digite o horario que deseja marcar: ')

                    while horario not in HorariosD:
                        print('horario invalido!!')
                        horario = input('digite o horario que deseja marcar: ')

                    if horario == '10h':
                        if contador1 < 3:
                            contador1 += 1
                            funcoescami.paghorario(atendimentoP, valort, atendimento)
                        else:
                            print('esse horario esta cheio!')

                    elif horario == '12h':
                        if contador2 < 3:
                            contador2 += 1
                            funcoescami.paghorario(atendimentoP, valort, atendimento)
                        else:
                            print('esse horario esta cheio!')

                    elif horario == '16h':
                        if contador3 < 3:
                            contador3 += 1
                            funcoescami.paghorario(atendimentoP, valort, atendimento)
                        else:
                            print('esse horario esta cheio!')

                    elif horario == '18h':
                        if contador4 < 3:
                            contador4 += 1
                            funcoescami.paghorario(atendimentoP, valort, atendimento)
                        else:
                            print('esse horario esta cheio!')

            elif opcao == 3:
                funcoescami.av(avaliacao)

            elif opcao == 4:
                funcoescami.desejo(produtos, listaD)

        else:
            print('Login não exite!')


while True:

    opcao = menus.menuGeralAdm()

    if opcao =="8":
        print("Saindo...")
        break

    elif opcao == "1":
        while True:
            opcao_atendimentoP = menus.menuservicos()

            if opcao_atendimentoP == "f":
                break

            elif opcao_atendimentoP == "a":
                servicos.cadastrarservicos()

            elif opcao_atendimentoP =="b":
                servicos.buscarservicos()

            elif opcao_atendimentoP == "c":
                servicos.listarservicos()

            elif opcao_atendimentoP == "d":
                servicos.atualizarservicos()

            elif opcao_atendimentoP == "e":
                servicos.removerservicos()

            else:
                print('Erro, escolha uma opção correta')


    elif opcao == "2":
        while True:
            opcao_produtos = menus.menuprodutos()

            if opcao_produtos == "f":
                break

            elif opcao_produtos == "a":
                produtos.cadastrarprodutos()

            elif opcao_produtos =="b":
                produtos.buscarprodutos()

            elif opcao_produtos == "c":
                produtos.listarprodutos()

            elif opcao_produtos == "d":
                produtos.atualizarprodutos()

            elif opcao_produtos =="e":
                produtos.removerprodutos()

            else:
                print('Erro, escolha uma opção correta')


    elif opcao =="3":
        while True:
            opcao = menus.menuestoque()

            if opcao == "e":
                break

            elif opcao == "a":
                estoque.verestoqueservicos()

            elif opcao == "b":
                estoque.verestoqueprodutos()

            elif opcao == "c":
                estoque.atualizarestoque()

            elif opcao == "d":
                estoque.removerestoque()

            else:
                print('Erro, escolha uma opção correta')


    elif opcao =="4":
        while True:
            opcao = menus.menuAdocoes()

            if opcao == "e":
                break

            elif opcao =="a":
                adocoes.cadastrarPets()

            elif opcao =="b":
                adocoes.listarPets()

            elif opcao =="c":
                adocoes.atualizarPets()

            elif opcao =="d":
                adocoes.removerPets()
            else:
                print('Erro, escolha uma opção correta')


    elif opcao == "5":
        while True:
            opcao = menus.menubackup()

            if opcao == "e":
                break

            elif opcao == "a":
                backup.gerarbackupservicos()

            elif opcao == "b":
                backup.gerarbackupprodutos() 


    elif opcao == "6":
        while True:
            opcao = menus.menuGeralAdm()

            if opcao == "8":
                break 

            elif opcao == "6":
                importarbackup.importarbackup()


    elif opcao == "7":
        while True:
            opcao = menus.menutabelas()

            if opcao == "f":
                break

            elif opcao == "a":
                tabelas.tabela_estoque_servicos()

            elif opcao == "b":
                tabelas.tabela_estoque_produtos()
            
            elif opcao == "c":
                tabelas.tabela_estoque_servicos()
              
            elif opcao == "d":
                tabelas.tabela_estoque_produtos()

            elif opcao == "e":
                tabelas.tabela_adocoes()

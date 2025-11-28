#Impotando os MENUS:

from menus import menuGeralAdm, menuservicos, menuprodutos, menuestoque, menuAdocoes

#Importando as FUNÇÕES:
from servicos import cadastrarservicos, buscarservicos, listarservicos,atualizarservicos, removerservicos

from produtos import cadastrarprodutos, buscarprodutos, listarprodutos, atualizarprodutos,removerprodutos

from estoque import verestoqueservicos, verestoqueprodutos, atualizarestoque, removerestoque

from adocoes import cadastrarPets, listarPets, atualizarPets, removerPets

#Importando LISTAS GLOBAIS:
from dados import atendimentoP, servicos, produtos, animaisAdocoes


while True:

    opcao = menuGeralAdm()

    if opcao =="5":
        print("Saindo...")
        break

    elif opcao == "1":
        while True:
            opcao_atendimentoP = menuservicos()

            if opcao_atendimentoP == "f":
                break

            elif opcao_atendimentoP == "a":
                cadastrarservicos()

            elif opcao_atendimentoP =="b":
                buscarservicos()

            elif opcao_atendimentoP == "c":
                listarservicos()

            elif atendimentoP == "d":
                atualizarservicos()

            elif opcao_atendimentoP == "e":
                removerservicos()

            else:
                print('Erro, escolha uma opção correta')

    elif opcao == "2":
        while True:
            opcao_produtos = menuprodutos()

            if opcao_produtos == "f":
                break

            elif opcao_produtos == "a":
                cadastrarprodutos()

            elif opcao_produtos =="b":
                buscarprodutos()

            elif opcao_produtos == "c":
                listarprodutos()

            elif opcao_produtos == "d":
                atualizarprodutos()

            elif opcao_produtos =="e":
                removerprodutos()

            else:
                print('Erro, escolha uma opção correta')

    elif opcao =="3":
        while True:
            opcao = menuestoque()

            if opcao == "e":
                break

            elif opcao == "a":
                verestoqueservicos()

            elif opcao == "b":
                verestoqueprodutos()

            elif opcao == "c":
                atualizarestoque(opcao, atendimentoP, produtos)

            elif opcao == "d":
                removerestoque(opcao, atendimentoP, produtos)

            else:
                print('Erro, escolha uma opção correta')

    elif opcao =="4":
        while True:
            opcao = menuAdocoes()

            if opcao == "e":
                break

            elif opcao =="a":
                cadastrarPets()

            elif opcao =="b":
                listarPets()

            elif opcao =="c":
                atualizarPets()

            elif opcao =="d":
                removerPets()

    else:
        print('Erro, escolha uma opção correta')
                                
                                
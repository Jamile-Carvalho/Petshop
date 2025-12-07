#Impotando os MENUS:

import menus 

#Importando as FUNÇÕES:
import servicos 

import produtos 

import estoque 

import adocoes

import backup

#Importando LISTAS GLOBAIS:
import dados 


while True:

    opcao = menus.menuGeralAdm()

    if opcao =="6":
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

            if opcao == "c":
                break

            elif opcao == "a":
                backup.gerarbackup()

            elif opcao == "b":
                backup.importarbackup()                

                                
    
              
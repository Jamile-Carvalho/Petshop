#Importando LISTAS GLOBAIS

import dados

#Impotando os MENUS:
import menus 

#Importando as FUNÇÕES:
import servicos_funcoes 

import produtos_funcoes 

import estoque_funcoes 

import adocoes_funcoes

import backup

import importarbackup

import tabelas

import funcoescami

while True:
    funcoescami.menuinicial()
    opcao = int(input('digite uma opcao: '))

    if opcao == 0:
        break

    elif opcao == 1:
        funcoescami.cadastrarUsuario(dados.usuario)

    elif opcao == 2:
        tipo = funcoescami.login(dados.usuario)
        if tipo == 'cliente':
            while True:
                funcoescami.menucompra()
                opcao = int(input('digite que opcao deseja realizar: '))

                if opcao == 0:
                    break

                elif opcao == 1:
                    print('Realize sua compra agora mesmo!')
                    funcoescami.listaProdutos(dados.produtos)
                    funcoescami.compraraP(dados.produtos)

                elif opcao == 2:
                    print('Escolha seu atendimento:')
                    funcoescami.listaratendimento(dados.atendimentoP)

                elif opcao == 3:
                    funcoescami.av(dados.avaliacao)

                elif opcao == 4:
                    funcoescami.desejo(dados.produtos, dados.listaD)

        elif tipo == 'administrador':
            while True:
                opcao = menus.menuGeralAdm()

                if opcao == "8":
                    break

                elif opcao == "1":
                    while True:
                        opcao_atendimentoP = menus.menuservicos()

                        if opcao_atendimentoP == "f":
                            break
                        elif opcao_atendimentoP == "a":
                            servicos_funcoes.cadastrarservicos()
                        elif opcao_atendimentoP == "b":
                            servicos_funcoes.buscarservicos()
                        elif opcao_atendimentoP == "c":
                            servicos_funcoes.listarservicos()
                        elif opcao_atendimentoP == "d":
                            servicos_funcoes.atualizarservicos()
                        elif opcao_atendimentoP == "e":
                            servicos_funcoes.removerservicos()

                elif opcao == "2":
                    while True:
                        opcao_produtos = menus.menuprodutos()

                        if opcao_produtos == "f":
                            break
                        elif opcao_produtos == "a":
                            produtos_funcoes.cadastrarprodutos()
                        elif opcao_produtos == "b":
                            produtos_funcoes.buscarprodutos()
                        elif opcao_produtos == "c":
                            produtos_funcoes.listarprodutos()
                        elif opcao_produtos == "d":
                            produtos_funcoes.atualizarprodutos()
                        elif opcao_produtos == "e":
                            produtos_funcoes.removerprodutos()

                elif opcao == "3":
                    while True:
                        opcao = menus.menuestoque()

                        if opcao == "e":
                            break
                        elif opcao == "a":
                            estoque_funcoes.verestoqueservicos()
                        elif opcao == "b":
                            estoque_funcoes.verestoqueprodutos()
                        elif opcao == "c":
                            estoque_funcoes.atualizarestoque()
                        elif opcao == "d":
                            estoque_funcoes.removerestoque()

                elif opcao == "4":
                    while True:
                        opcao = menus.menuAdocoes()

                        if opcao == "e":
                            break
                        elif opcao == "a":
                            adocoes_funcoes.cadastrarPets()
                        elif opcao == "b":
                            adocoes_funcoes.listarPets()
                        elif opcao == "c":
                            adocoes_funcoes.atualizarPets()
                        elif opcao == "d":
                            adocoes_funcoes.removerPets()

                elif opcao == "5":
                    while True:

                        opcao = menus.menubackup()

                        if opcao == "e":
                            break

                        elif opcao == "a":
                            backup.gerarbackupservicos()
                            print("Backup de serviços criado com sucesso!")

                        elif opcao == "b":
                            backup.gerarbackupprodutos()
                            print("Backup de produtos criado com sucesso!")

                        elif opcao == "c":
                            backup.gerarbackupestoque()
                            print("Backup de estoque criado com sucesso!")

                        elif opcao == "d":
                            backup.gerarbackupadocoes()
                            print("Backup de adoções criado com sucesso!")


                elif opcao == "6":
                    importarbackup.importarbackup()
                    print("Backup Geral criado com sucesso!")

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
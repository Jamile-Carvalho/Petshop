def menuGeralAdm():
    print("Escolha uma das seguintes opções para prosseguir:")
    print("1-Gerenciamento de Serviços")
    print("2-Gerenciameto de Produtos")
    print("3-Estoque")
    print("4-Adoções de Pets")
    print("5-Sair")
    opcao = input("Digite uma das opções para continuar: ")
    return opcao

def menuservicos():
    print("---------GERENCIADOR DE SERVIÇOS------------")
    print("Bem Vindo ao Gerenciador de Serviços")
    print("Escolha uma das seguintes opções para prosseguir:")
    print("a-Cadastro Flash de Serviço")
    print("b-Buscar Serviço")
    print("c-Listar Serviços")
    print("d-Atualizar Serviço")
    print("e-Remover Serviço")
    print("f-Nenhuma das opções acima")
    opcao_atendimentoP = input("Escolha uma das seguintes opções para prosseguir:").lower()
    return opcao_atendimentoP

def menuprodutos():
    print("---------GERENCIADOR DE PRODUTOS------------")
    print("Bem Vindo ao Gerenciador de Produtos")
    print("Escolha uma das seguintes opções para prosseguir:")
    print("a-Cadastro Flash de Produto")
    print("b-Buscar Produto")
    print("c-Listar Produtos")
    print("d-Atualizar Produto")
    print("e-Remover Produto")
    print("f-Nenhuma das opções acima")
    opcao_atendimentoP = input("Escolha uma das seguintes opções para prosseguir:").lower()
    return opcao_atendimentoP

def menuestoque():
    print("------ESTOQUE------")
    print("Bem Vindo ao Estoque Geral")
    print("a-Ver Estoque de Serviço")
    print("b-Ver Estoque de Produto")
    print("c-Atualizar Estoque")
    print("d-Remover do Estoque")
    print("e-Sair")
    opcao = input("Digite uma das opções para continuar: ")
    return opcao

def menuAdocoes():
    print("------GERENCIAMENTO DE ADOÇÕES PET & CIA------")
    print("Bem Vindo ao Adoções & Cia")
    print("Adote um bichinho,alegre sua vida e mude a vida dele!")
    print("a-Cadastrar Pets")
    print("b-Listar Pets Disponiveis")
    print("c-Atualizar Pets Disponiveís")
    print("d-Remover Pets")
    print("e-Sair")
    opcao = input("Digite uma das opções para continuar: ")
    return opcao
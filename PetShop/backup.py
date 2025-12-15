import dados
from dados import atendimentoP
from dados import produtos
from dados import estoque


def gerarbackupservicos():

    caminho_servicos = "servicos.txt"

    with open(caminho_servicos, "w", encoding="utf-8") as arq:
        for s in dados.atendimentoP:
            linha = f'{s["nome"]},{s["preco"]},{s["disponibilidade"]}'
            linha = linha.replace("\n", "")
            arq.write(linha + '\n')
            

def atualizarbackupservicos(nome, nome_procurado, novo_preco,disponibilidade):

    caminho_servicos = "servicos.txt"

    with open(caminho_servicos, "r", encoding="utf-8") as arq:
        linha = arq.readlines()

    with open(caminho_servicos, "w", encoding="utf-8") as arq:
        for linha in linha:
            nome_procurado, novo_preco, disponibilidade = linha.strip().split(",")

            if nome == nome_procurado:
                    arq.write(f"{nome_procurado},{novo_preco},{disponibilidade}\n")

            else:
                arq.write(linha)
            

def removerbackupservicos (nome_procurado):

    caminho_servicos = "C:\\Users\\Maria Jamile\\OneDrive\\Documentos\\Faculdade\\Algoritmos\\Projeto-PetShop-Modularizado\\servicos.txt"

    with open(caminho_servicos, "r", encoding="utf-8") as arq:
        linha = arq.readlines()

    with open(caminho_servicos, "w", encoding="utf-8") as arq:
        for linha in linha:
            nome = linha.split(",")

        if nome != nome_procurado:
            arq.write(linha)
            

def gerarbackupprodutos():

    caminho_produtos = "produtos.txt"

    with open(caminho_produtos, "w", encoding="utf-8") as arq:
        for p in dados.produtos:
            linha = f'{p["nome"]},{p["preco"]},{p["estoque"]}'
            linha = linha.replace("\n", "")
            arq.write(linha + '\n')
            

def atualizarbackupprodutos(nome, nome_procurado, novo_precoP,disponibilidade):

    caminho_produtos = "produtos.txt"

    with open(caminho_produtos, "r", encoding="utf-8") as arq:
        linha = arq.readlines()

    with open(caminho_produtos, "w", encoding="utf-8") as arq:
        for linha in linha:
            nome_procurado, novo_precoP, disponibilidade = linha.strip().split(",")

            if nome == nome_procurado:
                arq.write(f"{nome_procurado},{novo_precoP},{disponibilidade}\n")

            else:
                arq.write(linha)
            

def removerbackupprodutos(nome_procurado):

    caminho_produtos = "C:produtos.txt"

    with open(caminho_produtos, "r", encoding="utf-8") as arq:
        linha = arq.readlines()

    with open(caminho_produtos, "w", encoding="utf-8") as arq:
        for linha in linha:
            nome = linha.split(",")

            if nome != nome_procurado:
                arq.write(linha)
            

def gerarbackupestoque():

    caminho_estoque = "C:estoque.txt"

    with open(caminho_estoque, "w", encoding="utf-8") as arq:
        arq.write("\n========ESTOQUE SERVIÇOS========\n")
        for s in atendimentoP:
            linha = f'{s["nome"]},{s["preco"]},{s["disponibilidade"]}'
            linha = linha.replace("\n", "")
            arq.write(linha + '\n')

        arq.write("\n========ESTOQUE PRODUTOS========\n")
        for p in produtos:
            linha = f'{p["nome"]},{p["preco"]},{p["estoque"]}'
            linha = linha.replace("\n", "")
            arq.write(linha + '\n')
        

def atualizarbackupestoqueS(nome_servico, novo_preco, nova_disponibilidade):
    for s in dados.atendimentoP:
        if s["nome"] == nome_servico:
            s["preco"] = novo_preco
            s["disponibilidade"] = nova_disponibilidade
        

def atualizarbackestoqueP(novo_produto, novo_preco, novo_estoque):
    for p in dados.produtos:
        if p["nome"] == novo_produto:
            p["preco"] = novo_preco
            p["estoque"] = novo_estoque
          

def removerbackupestoqueS(nome_servico):
    for s in dados.atendimentoP:
        if s["nome"] == nome_servico:
            dados.atendimentoP.remove(s)
        

def removerbackupestoqueP(nome_produto):
    for p in dados.produtos:
        if p["nome"] == nome_produto:
            dados.produtos.remove(p)
        

def gerarbackupadocoes():

    caminho_adocoes ="C:adocoes.txt"

    with open(caminho_adocoes, "w", encoding="utf-8") as arq:
        for a in dados.animaisAdocoes:
            linha = f'{a["nome"]},{a["especie"]}, {a["idade"]}'
            linha = linha.replace("\n", "")
            arq.write(linha + '\n')
        

def atualizarbackadocoes(nome,nome_procurado, nova_especiePet, nova_idadePet):

    caminho_adocoes ="adocoes.txt"

    with open(caminho_adocoes, "r", encoding="utf-8") as arq:
        linha = arq.readlines()

    with open(caminho_adocoes, "w", encoding="utf-8") as arq:
        for linha in linha:
            nome_procurado, nova_especiePet, nova_idadePet = linha.strip().split(",")

            if nome == nome_procurado:
                arq.write(f"{nome_procurado},{nova_especiePet},{nova_idadePet}\n")

            else:
                arq.write(linha)
        

def removerbackupadocoes(nome_procurado):

    caminho_adocoes ="C:adocoes.txt"

    with open(caminho_adocoes, "r", encoding="utf-8") as arq:
        linha = arq.readlines()

    with open(caminho_adocoes, "w", encoding="utf-8") as arq:
        for linha in linha:
            nome = linha.split(",")

        if nome != nome_procurado:
            arq.write(linha)
        
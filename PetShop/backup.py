from dados import atendimentoP
from dados import produtos
import dados


def gerarbackup():
    caminho = "C:\\Users\\Maria Jamile\\OneDrive\\Documentos\\Faculdade\\Algoritmos"
    with open(caminho, "a", encoding="utf-8") as arq:
        for s in dados.atendimentoP:
            arq.write(f"{s['atendimento']},{s['preco']},{s['disponibilidade']}")

    with open("produtos.txt", "a", encoding="utf-8") as arq:
        for p in dados.produtos:
            arq.write(f"{p['nome']},{p['preco']},{p['estoque']}")

    print("Backup gerado com sucesso!")

def importarbackup():
    dados.servicos()
    caminho = "C:\\Users\\Maria Jamile\\OneDrive\\Documentos\\Faculdade\\Algoritmos"
    with open(caminho, "a", encoding="utf-8") as arq:
        for linha in arq:
            atendimentoP, preco, disponibilidade = linha.strip().split(",")
            dados.atendimentoP.append({
                "atendimento": nomeatendimentoP,
                "preco": preco,
                "disponibilidade":disponibilidade

            })

    with open("produtos.txt", "a", encoding="uft-8") as arq:
        for linha in arq:
            produto,preco,estoque = linha.strip().split(",")
            dados.produtos.append ({
                "produto": nomeproduto,
                "preco": preco,
                "estoque": estoque

            })

    print("Dados importados com sucesso!")
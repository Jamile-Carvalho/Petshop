from dados import atendimentoP
from dados import produtos
import dados


def gerarbackup():
    caminho = "C:\\Users\\Maria Jamile\\OneDrive\\Documentos\\Faculdade\\Algoritmos\\backup.tx"
    with open(caminho, "a", encoding="utf-8") as arq:
        for s in dados.atendimentoP:
            arq.write(f"{s['atendimento']},{s['preco']},{s['disponibilidade']}")

    with open("produtos.txt", "a", encoding="utf-8") as arq:
        for p in dados.produtos:
            arq.write(f"{p['nome']},{p['preco']},{p['estoque']}")

    print("Backup gerado com sucesso!")

def importarbackup():
    caminho = "C:\\Users\\Maria Jamile\\OneDrive\\Documentos\\Faculdade\\Algoritmos\\backup.txt"
    with open(caminho, "a", encoding="utf-8") as arq:
        for s in atendimentoP:
            linha = f'{["atendimento"], ["preco"], ["estoque"]}'
            linha = linha.replace("\n", "")
            arq.write(linha + '\n')

    caminho = "C:\\Users\\Maria Jamile\\OneDrive\\Documentos\\Faculdade\\Algoritmos\\backup.txt"
    with open(caminho, "a", encoding="utf-8") as arq:
        for p in produtos:
            linha = f'{["produto"], ["preco"], ["estoque"]}'
            linha = linha.replace("\n", "")
            arq.write(linha + '\n')

    print("Dados importados com sucesso!")
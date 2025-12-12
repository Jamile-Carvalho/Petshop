from dados import atendimentoP
from dados import produtos
import dados


def gerarbackup():

    caminho_servicos = "C:\\Users\\Maria Jamile\\OneDrive\\Documentos\\Faculdade\\Algoritmos\\Projeto-PetShop-Modularizado\\servico.txt"

    caminho_produtos = "C:\\Users\\Maria Jamile\\OneDrive\\Documentos\\Faculdade\\Algoritmos\\Projeto-PetShop-Modularizado\\produtos.txt"

    with open(caminho_servicos, "a", encoding="utf-8") as arq:
        for s in dados.atendimentoP:
            linha = f'{s["atendimento"]},{s["preco"]},{s["disponibilidade"]}'
            linha = linha.replace("\n", "")
            arq.write(linha + '\n')
            
    with open(caminho_produtos, "a", encoding="utf-8") as arq:
        for p in dados.produtos:
            linha = f'{p["nome"]},{p["preco"]},{p["estoque"]}'
            linha = linha.replace("\n", "")
            arq.write(linha + '\n')

    print("Backup gerado com sucesso!")

def importarbackup():
    caminho_backup = "C:\\Users\\Maria Jamile\\OneDrive\\Documentos\\Faculdade\\Algoritmos\\Projeto-PetShop-Modularizado\\backup.txt"
    with open(caminho_backup, "a", encoding="utf-8") as arq:
        for s in atendimentoP:
            linha = f'{s["atendimento"]},{s["preco"]}, {s["disponibilidade"]}'
            linha = linha.replace("\n", "")
            arq.write(linha + '\n')

    caminho_backup = "C:\\Users\\Maria Jamile\\OneDrive\\Documentos\\Faculdade\\Algoritmos\\Projeto-PetShop-Modularizado\\backup.txt"
    with open(caminho_backup, "a", encoding="utf-8") as arq:
        for p in produtos:
            linha = f'{p["nome"]}, {p["preco"]}, {p["estoque"]}'
            linha = linha.replace("\n", "")
            arq.write(linha + '\n')

    print("Backup criado com sucesso!")
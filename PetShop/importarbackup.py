import dados
from dados import atendimentoP
from dados import produtos
from dados import animaisAdocoes
from dados import estoque


def importarbackup():
    caminho_backup = "C:\\Users\\Maria Jamile\\OneDrive\\Documentos\\Faculdade\\Algoritmos\\Projeto-PetShop-Modularizado\\importar.txt"

    with open(caminho_backup, "w", encoding="utf-8") as arq:
        arq.write("\n========LISTA DE SERVIÇOS========\n")
        for s in atendimentoP:
            linha = f'{s["nome"]},{s["preco"]}, {s["disponibilidade"]}'
            linha = linha.replace("\n", "")
            arq.write(linha + '\n')

        arq.write("\n========LISTA DE PRODUTOS========\n")
        for p in produtos:
            linha = f'{p["nome"]}, {p["preco"]}, {p["estoque"]}'
            linha = linha.replace("\n", "")
            arq.write(linha + '\n')

        arq.write("\n========ESTOQUE========\n")

        for item in estoque:
            if item["tipo"] == "servico":
                arq.write(
                    f'SERVIÇO, {item["nome"]}, {item["preco"]}, {item["disponibilidade"]}\n'
                )

            elif item["tipo"] == "produto":
                arq.write(
                    f'PRODUTO, {item["nome"]}, {item["preco"]}, {item["estoque"]}\n'
                )

        arq.write("\n========ADOÇÕES========\n")
        for a in animaisAdocoes:
            linha = f'{a["nome"]}, {a["especie"]}, {a["idade"]}'
            linha = linha.replace("\n", "")
            arq.write(linha + '\n')

    print("Backup criado com sucesso!")
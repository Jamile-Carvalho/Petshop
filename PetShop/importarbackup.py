import dados 

def importarbackup():
    caminho_backup = "importar.txt"

    with open(caminho_backup, "w", encoding="utf-8") as arq:

        arq.write("========LISTA DE SERVIÇOS========\n")
        for s in dados.atendimentoP:
            arq.write(f'{s["nome"]},{s["preco"]},{s["disponibilidade"]}\n')

        arq.write("\n========LISTA DE PRODUTOS========\n")
        for p in dados.produtos:
            arq.write(f'{p["nome"]},{p["preco"]},{p["estoque"]}\n')

        arq.write("\n========ESTOQUE========\n")
        for item in dados.estoque:
            if item["tipo"] == "servico":
                arq.write(f'SERVIÇO,{item["nome"]},{item["preco"]},{item["disponibilidade"]}\n')
            else:
                arq.write(f'PRODUTO,{item["nome"]},{item["preco"]},{item["estoque"]}\n')

        arq.write("\n========ADOÇÕES========\n")
        for a in dados.animaisAdocoes:
            arq.write(f'{a["nome"]},{a["especie"]},{a["idade"]}\n')

    print("Backup geral criado com sucesso!")

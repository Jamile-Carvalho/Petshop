from dados import atendimentoP, produtos, animaisAdocoes
from rich.console import Console
from rich.table import Table

console = Console()

def tabela_servicos():
    table = Table(
        title="📋 Serviços do Petshop",
        show_header=True,
        header_style="bold magenta"
    )

    table.add_column("Serviço", style="cyan")
    table.add_column("Preço (R$)", justify="right", style="green")
    table.add_column("Disponibilidade", justify="center", style="yellow")

    for s in atendimentoP:
        table.add_row(
            s["nome"],
            f"{s['preco']}",
            str(s["disponibilidade"])
        )

    console.print(table)


def tabela_produtos():
    table = Table(
        title="📋 Produtos do Petshop",
        show_header=True,
        header_style="bold magenta"
    )

    table.add_column("Produto", style="cyan")
    table.add_column("Preço (R$)", justify="right", style="green")
    table.add_column("Disponibilidade", justify="center", style="yellow")

    for p in produtos:
        table.add_row(
            p["produto"],
            f"{p['preco']}",
            str(p["disponibilidade"])
        )

    console.print(table)

def tabela_estoque_servicos():
    table = Table(
        title="📋 Estoque de serviços do Petshop",
        show_header=True,
        header_style="bold magenta"
    )

    table.add_column("Serviço", style="cyan")
    table.add_column("Preço (R$)", justify="right", style="green")
    table.add_column("Disponibilidade", justify="center", style="yellow")

    for s in atendimentoP:
        table.add_row(
            s["nome"],
            f"{s['preco']}",
            str(s["disponibilidade"])

        )

    console.print(table)

def tabela_estoque_produtos():
    table = Table(
        title="📋 Estoque de Produtos do Petshop",
        show_header=True,
        header_style="bold magenta"
    )

    table.add_column("Produto", style="cyan")
    table.add_column("Preço (R$)", justify="right", style="green")
    table.add_column("Disponibilidade", justify="center", style="yellow")

    for p in produtos:
        table.add_row(
            p["nome"],
            f"{p['preco']}",
            str(p["estoque"])

        )

    console.print(table)

def tabela_adocoes():
    table = Table(
        title="📋 Adoções do Petshop",
        show_header=True,
        header_style="bold magenta"
    )

    table.add_column("nome", style="cyan")
    table.add_column("especie", style="green")
    table.add_column("idade", justify="center", style="yellow")

    for d in animaisAdocoes:
        table.add_row(
            d["nome"],
            f"{d['especie']}",
            str(d["idade"])

        )

    console.print(table)
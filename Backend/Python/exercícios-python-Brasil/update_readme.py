import os

def gerar_links():
    conteudo = "# Exercícios Python Brasil\n\n"
    conteudo += "Repositório com exercícios originalmente postados em [Python.org](https://wiki.python.org.br/ListaDeExercicios). Atualmente rodando direto no browser em [Exercicios Dunossauro](https://exercicios.dunossauro.com)\n\n"
    conteudo += "Aqui estão as resoluções feitas por mim para os exercícios dessa fonte.\n\n"
    conteudo += "## 📑 Temas\n"

    for pasta in sorted(os.listdir()):
        if os.path.isdir(pasta) and not pasta.startswith("."):
            arquivos_py = sorted([f for f in os.listdir(pasta) if f.endswith(".py")])
            if arquivos_py:
                conteudo += f"### `{pasta}`\n"
                for arq in arquivos_py:
                    nome = arq.replace(".py", "").replace("_", " ").title()
                    link = f"{pasta}/{arq}"
                    conteudo += f"- [{nome}]({link})\n"
                conteudo += "\n"

    conteudo += "\n---\n## Créditos\nTestes feitos pelo repositório [lista-de-exercicios-python-brasil](https://github.com/devpro-br/lista-de-exercicios-python-brasil.git)."
    return conteudo

with open("README.md", "w", encoding="utf-8") as f:
    f.write(gerar_links())

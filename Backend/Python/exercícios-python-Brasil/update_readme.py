import os

SECTIONS = {
    "estrutura-sequencial": "Estrutura Sequencial",
    "estrutura-decisao": "Estrutura de Decisão",
    "estrutura-de-repeticao": "Estrutura de Repetição",
    "listas": "Listas"
}

def gerar_links():
    conteudo = "# Exercícios Python Brasil\n\n"
    conteudo += "Repositório com exercícios originalmente postados em [Python.org](https://wiki.python.org.br/ListaDeExercicios). Atualmente rodando direto no browser em [Exercicios Dunossauro](https://exercicios.dunossauro.com)\n\n"
    conteudo += "Aqui estão as resoluções feitas por mim para os exercícios dessa fonte.\n\n"
    conteudo += "## 📑 Temas\n"

    for pasta, titulo in SECTIONS.items():
        conteudo += f"### `{titulo}`\n"
        caminho = os.path.join(pasta)
        if os.path.exists(caminho):
            arquivos = sorted(os.listdir(caminho))
            for arq in arquivos:
                if arq.endswith(".py"):
                    nome = arq.replace(".py", "").replace("_", " ").title()
                    link = f"{pasta}/{arq}"
                    conteudo += f"- [{nome}]({link})\n"
                    
    conteudo += "\n---\n## Créditos\nTestes feitos pelo repositório [lista-de-exercicios-python-brasil](https://github.com/devpro-br/lista-de-exercicios-python-brasil.git)."
    return conteudo

with open("README.md", "w", encoding="utf-8") as f:
    f.write(gerar_links())
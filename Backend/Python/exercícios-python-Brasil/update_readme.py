import os
import urllib.parse

def listar_certificados():
    conteudo = "# 📄 Certificados\n\n"
    conteudo += "> Aréa para salvar meus certificados adquiridos ao longo do curso\n\n"
    conteudo += "## Módulos\n"

    modulos = sorted([d for d in os.listdir() if os.path.isdir(d) and "Módulo" in d])

    for modulo in modulos:
        conteudo += f"- ### {modulo}\n"
        arquivos = sorted(os.listdir(modulo), key=lambda f: os.path.getctime(os.path.join(modulo, f)))
        for arq in arquivos:
            if arq.endswith(".pdf"):
                nome = arq.replace(".pdf", "").replace("%", "%%")
                link = f"{modulo}/{urllib.parse.quote(arq)}"
                conteudo += f"    - [{nome}]({link})\n"
        conteudo += "\n"

    return conteudo

with open("README.md", "w", encoding="utf-8") as f:
    f.write(listar_certificados())

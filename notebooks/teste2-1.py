import json
from pathlib import Path
import pandas as pd

# 1. Caminho para a pasta de arquivos JSON
json_dir = Path("caminho/dos/json")

linhas = []

# Varre todos os arquivos .json da pasta
for f in json_dir.glob("*.json"):
    # Carrega o arquivo de texto bruto e converte em dicionário Python
    conteudo = json.loads(f.read_text(encoding="utf-8"))

    # Captura os metadados principais da pessoa
    nome = conteudo.get("nome_completo", "")
    id_lattes = conteudo.get("id_lattes", "")

    # 2. Varre a lista aninhada de artigos e monta as linhas planas
    artigos = conteudo.get("producao_bibliografica", {}).get("artigos_publicados", [])
    for artigo in artigos:
        linhas.append({
            "id_lattes": id_lattes,
            "pesquisador": nome,
            "titulo_artigo": artigo.get("titulo", ""),
            "ano": artigo.get("ano", "")
        })

# 3. Converte a lista plana de dicionários diretamente em um DataFrame
df = pd.DataFrame(linhas)
df.head()
import pandas as pd

# Carregando um arquivo estruturado do tipo Parquet (muito comum em análise de dados)
df = pd.read_parquet("teste.parquet")

# Visualizando as 5 primeiras linhas da tabela para analisarmos os dados brutos
df.head()

df.info()

df.describe()

# isna() identifica células vazias e sum() soma a quantidade de vazios por coluna
df.isna().sum()


# 1. Caminho do arquivo de análise
arquivo_parquet = "teste.parquet"

# 2. Carrega a tabela
df = pd.read_parquet(arquivo_parquet)

# 3. Exibe o diagnóstico estrutural
print("--- INFORMAÇÕES GERAIS ---")
df.info()

print("\n--- RESUMO ESTATÍSTICO ---")
print(df.describe(include="all")) # include='all' inclui colunas de texto no resumo

print("\n--- CONTAGEM DE VALORES NULOS ---")
print(df.isna().sum())
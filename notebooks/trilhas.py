import pandas as pd

# Definição do dicionário com listas de dados
dados = {
    'Nome': ['Marcos', 'Carlos', 'Fabiana', 'Lúcia'],
    'Profissão': ['Encanador', 'Mecânico', 'Diplomata', 'Designer'],
    'Idade': [55, 43, 31, 25],
    'Altura': [1.85, 1.78, 1.63, 1.67],
    'Cor Favorita': [['N/A'], ['Verde'], ['Azul', 'Vermelho'], ['Preto', 'Branco']]
}

# A função pd.DataFrame() converte a estrutura em uma tabela
df = pd.DataFrame(dados)
print(df)

# Selecionando apenas uma coluna (retorna uma Series)
df_nomes = df['Nome']
print(df_nomes)

# Selecionando múltiplas colunas (retorna um novo DataFrame)
df_resumo = df[['Nome', 'Idade', 'Profissão']]
print(df_resumo)
# Criar uma nova coluna calculando o ano aproximado de nascimento
df['Ano de Nascimento'] = 2025 - df['Idade']
print(df)


# Criando uma Series a partir de uma lista comum
nomes = ['Marcos', 'Carlos', 'Fabiana', 'Lúcia']
nomes_series = pd.Series(nomes, name='Nomes')
print("Series de Nomes:\n", nomes_series)

# Extraindo uma Series a partir de um DataFrame existente
nomes_df = df['Nome']
print("Series Extraída do DataFrame:\n", nomes_df)

# Definindo índices personalizados
idades_series = pd.Series([55, 43, 31, 25], index=nomes)
print("Series de Idades com Índices Personalizados:\n", idades_series)
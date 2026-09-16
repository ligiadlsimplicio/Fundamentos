import pandas as pd
import plotly.express as px

# 1. DECLARAÇÃO DE DADOS DE PROPORÇÃO (MÁXIMO 3 CATEGORIAS)
dados_status = {
    "Projetos Ativos": 45,
    "Em Avaliação": 18,
    "Finalizados": 12,
}

# Conversão do dicionário em DataFrame do Pandas
df_proporcoes = pd.DataFrame(
    list(dados_status.items()), columns=["status", "quantidade"]
)

# --- AUDITORIA DE DADOS ---
print("=" * 65)
print("1. AUDITORIA DE PROPORÇÕES CATEGÓRICAS (GRÁFICO DE ROSCA)")
print("=" * 65)
print(f"✓ Volume total consolidado: {df_proporcoes['quantidade'].sum()} projetos")
print("\nDistribuição de Frequência por Status:")
print(df_proporcoes.to_string(index=False))
print("=" * 65 + "\n")

# 2. PLOTAGEM DO GRÁFICO DE ROSCA (DOUGHNUT CHART)
fig = px.pie(
    df_proporcoes,
    values="quantidade",
    names="status",
    hole=0.4,  # Define o raio do furo interno (40%)
    title="Proporção do Status dos Projetos de Pesquisa do Campus",
    color_discrete_sequence=["#0E4D92", "#2E8B57", "#A6A6A6"],
)

fig.update_traces(textposition="inside", textinfo="percent+label")
fig.update_layout(template="plotly_white")

# Abre a visualização no navegador padrão
fig.show()
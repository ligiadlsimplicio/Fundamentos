from pathlib import Path
import pandas as pd
import plotly.express as px

# 1. CARREGAMENTO E ESTRUTURAÇÃO DOS DADOS
caminho = (
    Path("artigos.parquet")
    if Path("artigos.parquet").exists()
    else Path("../../artigos.parquet")
)

if caminho.exists():
    df_raw = pd.read_parquet(caminho)
    col_pesquisador = (
        "pesquisador" if "pesquisador" in df_raw.columns else "nome_completo"
    )

    # Agrupa por docente para obter o volume total de publicações
    df_docentes = (
        df_raw.groupby(col_pesquisador)
        .size()
        .reset_index(name="n_artigos")
        .rename(columns={col_pesquisador: "nome"})
    )
else:
    # Dados de fallback caso o arquivo parquet não esteja no caminho local
    df_docentes = pd.DataFrame(
        [
            {"nome": "Docente A", "n_artigos": 12},
            {"nome": "Docente B", "n_artigos": 15},
            {"nome": "Docente C", "n_artigos": 14},
            {"nome": "Docente D", "n_artigos": 16},
            {"nome": "Docente E", "n_artigos": 11},
            {"nome": "Docente F", "n_artigos": 13},
            {"nome": "Docente G", "n_artigos": 15},
            {"nome": "Docente H", "n_artigos": 48},  # Outlier
            {"nome": "Docente I", "n_artigos": 52},  # Outlier
            {"nome": "Docente J", "n_artigos": 2},
        ]
    )

# 2. AUDITORIA ESTATÍSTICA E IDENTIFICAÇÃO DE OUTLIERS
q1 = df_docentes["n_artigos"].quantile(0.25)
mediana = df_docentes["n_artigos"].median()
q3 = df_docentes["n_artigos"].quantile(0.75)
iqr = q3 - q1
limite_superior = q3 + (1.5 * iqr)

outliers = df_docentes[df_docentes["n_artigos"] > limite_superior]

print("=" * 65)
print("1. AUDITORIA DE DISTRIBUIÇÃO E OUTLIERS DA PRODUÇÃO")
print("=" * 65)
print(f"✓ Total de docentes analisados: {len(df_docentes)}")
print(f"✓ Mediana do volume de artigos: {mediana:.1f}")
print(f"✓ Intervalo Interquartil (IQR): Q1={q1:.1f} | Q3={q3:.1f}")
print(f"✓ Limite Superior de Variabilidade Normal: {limite_superior:.1f}")
print(f"\n★ Outliers identificados (acima da curva do grupo): {len(outliers)}")
if not outliers.empty:
    print(outliers[["nome", "n_artigos"]].to_string(index=False))
print("=" * 65 + "\n")

# 3. PLOTAGEM DO HISTOGRAMA DE FREQUÊNCIA
fig_hist = px.histogram(
    df_docentes,
    x="n_artigos",
    nbins=15,
    title="Distribuição de Frequência de Artigos Publicados por Docente",
    labels={
        "n_artigos": "Quantidade de Artigos",
        "count": "Número de Docentes",
    },
    color_discrete_sequence=["#0E4D92"],
)
fig_hist.update_layout(
    xaxis_title="Quantidade de Artigos",
    yaxis_title="Número de Docentes",
    template="plotly_white",
)
fig_hist.show()

# 4. PLOTAGEM DO BOXPLOT INTERATIVO COM PONTOS INDIVIDUAIS
fig_box = px.box(
    df_docentes,
    y="n_artigos",
    points="all",
    hover_name="nome",
    title="Análise de Dispersão e Identificação de Outliers (Boxplot)",
    labels={"n_artigos": "Artigos Publicados"},
    color_discrete_sequence=["#2E8B57"],
)
fig_box.update_layout(yaxis_title="Artigos Publicados", template="plotly_white")
fig_box.show()

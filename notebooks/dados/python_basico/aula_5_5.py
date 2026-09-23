from pathlib import Path
import folium

# 1. CONFIGURAÇÃO DE COORDENADAS (Franca, SP)
LATITUDE_CENTRO = -20.5375
LONGITUDE_CENTRO = -47.4014

# Inicialização do mapa interativo
mapa_franca = folium.Map(
    location=[LATITUDE_CENTRO, LONGITUDE_CENTRO],
    zoom_start=14,
    tiles="OpenStreetMap",
)

# 2. ADIÇÃO DE MARCADORES COM POPUPS E ÍCONES PERSONALIZADOS
folium.Marker(
    location=[-20.5377, -47.4010],
    popup=(
        "<b>UNESP - Campus Franca</b><br>Faculdade de Ciências Humanas e"
        " Sociais"
    ),
    tooltip="Clique para ver o campus",
    icon=folium.Icon(color="green", icon="graduation-cap", prefix="fa"),
).add_to(mapa_franca)

folium.Marker(
    location=[-20.5330, -47.4040],
    popup="<b>Biblioteca Unesp Franca</b>",
    tooltip="Biblioteca do Campus",
    icon=folium.Icon(color="blue", icon="book", prefix="fa"),
).add_to(mapa_franca)

# 3. EXPORTAÇÃO PARA HTML
arquivo_saida = Path("meu_mapa_interativo.html")
mapa_franca.save(arquivo_saida)

print("=" * 65)
print("1. AUDITORIA DE MAPAS GEOESPACIAIS (FOLIUM)")
print("=" * 65)
print(f"✓ Coordenadas de origem: [{LATITUDE_CENTRO}, {LONGITUDE_CENTRO}]")
print("✓ Marcadores adicionados: UNESP Campus Franca e Biblioteca")
print(
    f"✓ Arquivo interativo salvo com sucesso em: {arquivo_saida.resolve()}"
)
print("=" * 65)
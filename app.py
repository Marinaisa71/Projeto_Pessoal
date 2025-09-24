import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

st.title("Lista de Feira Automatizada 🛒")

# Categorias e itens pré-definidos
feira = {
    "Frutas": ["Banana", "Maçã", "Laranja", "Uva", "Maracujá", "Abacaxi", "Manga", "Melancia", "Melão", "Pera", "Kiwi", "Morango", "Ameixa", "Caju", "Goiaba", "Limão", "Tangerina", "Abacate", "Coco"],
    "Verduras": ["Alface", "Cebolinha", "Cebola", "Tomate"],
    "Legumes": ["Cenoura", "Batata", "Abobrinha", "Chuchu", "Beterraba", "Pepino", "Brócolis", "Couve-flor", "Vagem", "Ervilha", "Milho", "Inhame", "Mandioca"],
    "Proteínas": ["Frango", "Carne", "Linguiça", "Ovos", "Peixe", "Atum", "Sardinha", "Carne Moída", "Carne de Porco"],
    "Bebidas": ["Água com gás", "Refrigerante", "Suco", "Cerveja", "Vinho", "Whisky", "Vodka", "Cachaça", "Energético", "Chá gelado"],
    "Frios": ["Queijo", "Presunto", "Requeijão", "Leite fermentado", "Iogurte", "Manteiga","Margarina", "Mortadela", "Salame", "Cream Cheese", "Ricota", "Cottage", "Peito de Peru", "Queijo Minas", "Queijo Prato", "Queijo Mussarela", "Queijo Parmesão", "Queijo Gorgonzola", "Queijo Brie", "Queijo Camembert"],
    "Mercearia": ["Arroz", "Feijão", "Macarrão", "Óleo", "Leite", "Açúcar", "Café", "Farinha de trigo", "Sal", "Pão", "Biscoito", "Molho de Tomate", "Cuscuz", "Fermento", "Amido de milho", "Leite condensado", "Creme de leite", "Achocolatado", "Chá", "Mel", "Granola", "Aveia", "Cereal", "Pipoca", "Farinha de rosca", "Farinha de mandioca", "Polvilho", "Gelatina", "Coco ralado", "Azeitona", "Extrato de tomate","Café solúvel ", "Leite em pó"],
    "Higiene": ["Papel higiênico", "Sabonete", "Shampoo", "Condicionador", "Creme dental", "Escova de dentes", "Fio dental", "Desodorante", "Absorvente", "Lâmina de barbear", "Espuma de barbear", "Protetor solar", "Hidratante", "Lenços umedecidos"],
    "Limpeza": ["Detergente", "Sabão Líquido", "Sabão em pó", "Amaciante", "Desinfetante", "Água sanitária", "Limpador multiuso", "Esponja de aço", "Esponja comum", "Vassoura", "Rodo", "Pano de chão", "Saco de lixo", "Luva de limpeza"],
}

st.sidebar.header("Escolha os produtos")

lista_final = []

# Loop pelas categorias
for categoria, itens in feira.items():
    st.sidebar.subheader(categoria)
    selecionados = st.sidebar.multiselect(f"Selecione {categoria}", itens)
    for item in selecionados:
        qtd = st.sidebar.number_input(f"Quantidade de {item}", min_value=1, step=1)
        lista_final.append({"Item": item, "Quantidade": qtd})

# Mostrar lista final
if lista_final:
    df = pd.DataFrame(lista_final)
    st.subheader("📝 Sua lista de feira:")
    st.table(df)
 # Criar figura do matplotlib
    fig, ax = plt.subplots(figsize=(6, len(df) * 0.5 + 1))
    ax.axis("off")  # remove os eixos
    tabela = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        loc="center",
        cellLoc="center"
    )
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(10)
    tabela.scale(1.2, 1.2)

    # Converter para bytes
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)

    # Exibir no app
    st.image(buf, caption="Lista de Feira")

    # Botão para baixar a imagem
    st.download_button(
        "📥 Baixar Lista como Imagem",
        buf,
        "lista_feira.png",
        "image/png"
    )
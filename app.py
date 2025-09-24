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

# Loop pelas categorias - VERSÃO MELHORADA
for categoria, itens in feira.items():
    st.sidebar.subheader(categoria)
    selecionados = st.sidebar.multiselect(f"Selecione {categoria}", itens, key=f"ms_{categoria}")
    
    for item in selecionados:
        # Usando uma chave única para cada número_input
        qtd = st.sidebar.number_input(
            f"Quantidade de {item}", 
            min_value=1, 
            value=1,  # Valor padrão
            step=1,
            key=f"qtd_{categoria}_{item}"  # Chave única
        )
        lista_final.append({"Item": item, "Quantidade": qtd, "Categoria": categoria})

# Mostrar lista final
if lista_final:
    df = pd.DataFrame(lista_final)
    
    st.subheader("📝 Sua lista de feira:")
    st.table(df)
    
    # Criar figura do matplotlib
    fig, ax = plt.subplots(figsize=(8, len(df) * 0.5 + 1))
    ax.axis("off")  # remove os eixos
    
    # Adicionar título
    ax.set_title("Lista de Feira", fontsize=16, pad=20)
    
    tabela = ax.table(
        cellText=df[["Item", "Quantidade"]].values,  # Mostrar apenas Item e Quantidade
        colLabels=["Item", "Quantidade"],
        loc="center",
        cellLoc="center"
    )
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(12)
    tabela.scale(1.2, 1.2)
    
    # Estilizar a tabela
    tabela.auto_set_column_width([0, 1])  # Ajustar largura das colunas

    # Converter para bytes
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", dpi=150)
    buf.seek(0)

    # Exibir no app
    st.subheader("🖼️ Versão para impressão:")
    st.image(buf, caption="Lista de Feira", use_column_width=True)

    # Botão para baixar a imagem
    st.download_button(
        "📥 Baixar Lista como Imagem",
        buf.getvalue(),
        "lista_feira.png",
        "image/png"
    )
    
    # Botão para limpar a lista
    if st.button("🗑️ Limpar Lista"):
        st.experimental_rerun()
        
else:
    st.info("👈 Selecione alguns itens na barra lateral para começar sua lista!")
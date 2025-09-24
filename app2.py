import streamlit as st
import pandas as pd
from io import StringIO

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
    selecionados = st.sidebar.multiselect(f"Selecione {categoria}", itens, key=f"ms_{categoria}")
    for item in selecionados:
        qtd = st.sidebar.number_input(f"Quantidade de {item}", min_value=1, step=1, value=1, key=f"qtd_{categoria}_{item}")
        lista_final.append({"Item": item, "Quantidade": qtd, "Categoria": categoria})

# Mostrar lista final
if lista_final:
    df = pd.DataFrame(lista_final)
    
    st.subheader("📝 Sua lista de feira:")
    st.table(df)
    
    # Criar versão para download sem matplotlib
    st.subheader("💾 Download da Lista")
    
    # Opção 1: CSV
    csv = df.to_csv(index=False)
    st.download_button(
        "📥 Baixar como CSV",
        csv,
        "lista_feira.csv",
        "text/csv"
    )
    
    # Opção 2: Texto simples
    texto_lista = "LISTA DE FEIRA:\n\n"
    for item in lista_final:
        texto_lista += f"✓ {item['Item']}: {item['Quantidade']} un\n"
    
    st.download_button(
        "📥 Baixar como Texto",
        texto_lista,
        "lista_feira.txt",
        "text/plain"
    )
    
    # Opção 3: HTML (para impressão)
    html = df.to_html(index=False)
    st.download_button(
        "📥 Baixar como HTML",
        html,
        "lista_feira.html",
        "text/html"
    )
    
    # Botão para limpar a lista
    if st.button("🗑️ Limpar Lista"):
        st.experimental_rerun()
        
else:
    st.info("👈 Selecione alguns itens na barra lateral para começar sua lista!") 
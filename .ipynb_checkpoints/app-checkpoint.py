import streamlit as st
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Judul aplikasi
st.title('Product Recommendation Based on Association Rules')

# Muat data rekomendasi dari file JSON
with open('item_sets.json', 'r') as f:
    recommendations = json.load(f)

# Sidebar untuk memilih produk
product_catalog = list(recommendations.keys())
selected_product = st.sidebar.selectbox('Select a Product', product_catalog)

# Menampilkan rekomendasi produk
if selected_product:
    recommended_products = recommendations[selected_product]
    
    if recommended_products:
        st.success(f"Orang-orang juga membeli ini: {', '.join(recommended_products)}")
        
        # Word Cloud dari rekomendasi
        st.write("Word Cloud Plot")
        wordcloud = WordCloud(background_color="white", max_words=100).generate(' '.join(recommended_products))
        
        # Membuat figure secara eksplisit
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        
        # Tampilkan plot
        st.pyplot(fig)
    else:
        st.warning("Oops! Tidak ada rekomendasi produk yang tersedia saat ini!")

# Pesan untuk pengguna
st.write("Pilih produk dari sidebar untuk melihat rekomendasi yang tersedia.")

import streamlit as st
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Judul aplikasi
st.title('Product Recommendation Based on Association Rules')

# Muat data rekomendasi dari file JSON
with open('item_sets.json', 'r') as f:
    recommendations = json.load(f)

# Mengambil semua kunci dari dictionary 'recommendations' yang berisi nama-nama produk
product_catalog = list(recommendations.keys())
# Membuat dropdown (selectbox) di sidebar aplikasi Streamlit untuk memilih produk
selected_product = st.sidebar.selectbox('Select a Product', product_catalog)

# Menampilkan rekomendasi produk
if selected_product:  # Jika pengguna telah memilih produk dari sidebar
    recommended_products = recommendations[selected_product]  # Mengambil daftar produk yang direkomendasikan untuk produk yang dipilih
    
    if recommended_products:  # Jika ada produk yang direkomendasikan
        st.success(f"Orang-orang juga membeli ini: {', '.join(recommended_products)}")  # Menampilkan pesan sukses dengan daftar produk yang direkomendasikan
        
        # Word Cloud dari rekomendasi
        st.write("Word Cloud Plot")  # Menampilkan teks "Word Cloud Plot" di aplikasi
        wordcloud = WordCloud(background_color="white", max_words=100).generate(' '.join(recommended_products))  
        # Membuat objek WordCloud dengan latar belakang putih dan maksimal 100 kata,
        # kemudian menghasilkan WordCloud dari daftar produk yang direkomendasikan
        
        # Membuat figure secara eksplisit
        fig, ax = plt.subplots()  # Membuat figure dan axis baru untuk plot
        ax.imshow(wordcloud, interpolation='bilinear')  # Menampilkan WordCloud di axis dengan interpolasi bilinear
        ax.axis("off")  # Menyembunyikan axis
        
        # Tampilkan plot
        st.pyplot(fig)  # Menampilkan figure yang mengandung WordCloud di aplikasi Streamlit
    else:  # Jika tidak ada produk yang direkomendasikan
        st.warning("Oops! Tidak ada rekomendasi produk yang tersedia saat ini!")  # Menampilkan pesan peringatan


# Pesan untuk pengguna
st.write("Pilih produk dari sidebar untuk melihat rekomendasi yang tersedia.")

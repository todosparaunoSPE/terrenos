# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 17:00:52 2025

@author: jperezr
"""

import streamlit as st

# Configurar la página
st.set_page_config(page_title="Venta de Terrenos en Tlaxcala", layout="centered")


# Estilo de fondo
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background:
radial-gradient(black 15%, transparent 16%) 0 0,
radial-gradient(black 15%, transparent 16%) 8px 8px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 0 1px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 8px 9px;
background-color:#282828;
background-size:16px 16px;
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Título llamativo
st.markdown("""
    <h1 style='text-align: center; color: green;'>🚨 ¡ÚLTIMA OPORTUNIDAD! 🚨</h1>
    <h2 style='text-align: center;'>🏡 4 terrenos en venta con alta plusvalía en Tlaxcala 🏡</h2>
""", unsafe_allow_html=True)

# Descripción del anuncio con cambio de tamaño de letra
st.markdown("""
 <span style='font-size: 30px; font-weight: bold;'>📍 **Ubicación estratégica:**</span> <span style='font-size: 30px;'>Cerca de hospitales, comercios y servicios.</span>  
<span style='font-size: 30px; font-weight: bold;'>💰 **Super precio:**</span> <span style='font-size: 30px;'>¡Solo $1,500/m²!</span>  
<span style='font-size: 30px; font-weight: bold;'>📏 **Terrenos ideales** </span> <span style='font-size: 30px;'>para inversión, casa habitación o negocio.</span>  
<span style='font-size: 30px; font-weight: bold;'>📜 **Documentación en regla**  </span> <span style='font-size: 30px;'>y entrega inmediata.</span>  

 <span style='font-size: 30px; font-weight: bold;'> 🔥 ¡No dejes pasar esta oportunidad! 🔥</span>  
""", unsafe_allow_html=True)

# Mostrar imágenes en una galería (2 columnas para imágenes más grandes)
image_names = [f"imagen{i}.jpg" for i in range(1, 8)]  # Asegúrate de que estos archivos existen

st.markdown("## 📸 Galería de Imágenes")
cols = st.columns(2)  # Solo 2 columnas para imágenes más grandes

for i, image in enumerate(image_names):
    with cols[i % 2]:  # Distribuir imágenes en 2 columnas
        st.image(image, use_container_width=True)  # Ajustar el tamaño de la imagen

# Pie de página
st.markdown("---")
st.markdown("### 📞 Contacto: 246-159-3018")
st.markdown("Sra. Alvarado")

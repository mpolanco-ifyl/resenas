import streamlit as st
import pandas as pd
from text_mining_function import generate_review

st.title("Generador de reseñas de libros")

uploaded_file = st.file_uploader("Cargar archivo de texto", type="txt")
if uploaded_file is not None:
    # Leer el texto del libro cargado
    text = uploaded_file.read().decode("utf-8")
    # Generar una reseña utilizando la función de text mining
    review = generate_review(text)
    # Mostrar la reseña generada al usuario
    st.write(review)

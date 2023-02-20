import streamlit as st
from textblob import TextBlob

st.title("Generador de reseñas de libros")

uploaded_file = st.file_uploader("Cargar archivo de texto", type="txt")
if uploaded_file is not None:
    # Leer el texto del libro cargado
    text = uploaded_file.read().decode("utf-8")
    # Analizar el sentimiento del texto del libro utilizando TextBlob
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    # Generar una reseña basada en el sentimiento detectado
    if sentiment > 0:
        review = "Me gustó mucho este libro, ¡lo recomiendo!"
    elif sentiment < 0:
        review = "No me gustó este libro, no lo recomendaría."
    else:
        review = "Este libro es neutral, no tengo una opinión fuerte al respecto."
    # Mostrar la reseña generada al usuario
    st.write(review)

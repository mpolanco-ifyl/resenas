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
    # Citas del libro
    quotes = ["La literatura es el arte de escribir algo que se lee dos veces; y la poesía, algo que se lee una y otra vez.",
              "Los libros siempre habían sido para mí una ventana a lugares maravillosos.",
              "En el futuro, todo el mundo será mundialmente famoso durante quince minutos."]
    # Generar una reseña citando partes del libro
    if sentiment > 0:
        review = f"Me encantó este libro. La prosa es hermosa y las historias son profundas. Como dijo Andy Warhol: '{quotes[2]}'."
    elif sentiment < 0:
        review = f"No me gustó este libro. La prosa es confusa y las historias son poco interesantes. Como dijo Oscar Wilde: '{quotes[0]}'."
    else:
        review = f"Este libro es neutral, no tengo una opinión fuerte al respecto. Como dijo Marcel Proust: '{quotes[1]}'."
    # Mostrar la reseña generada al usuario
    st.write(review)

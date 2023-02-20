import streamlit as st
import nltk
nltk.download('punkt')

st.title("Generador de reseñas de libros")

# Cargar el archivo de texto del libro
uploaded_file = st.file_uploader("Cargar libro en formato TXT", type=["txt"])
if uploaded_file is not None:
    book_text = uploaded_file.read().decode("utf-8")

    # Tokenizar el texto del libro en oraciones
    book_sentences = nltk.sent_tokenize(book_text)

    # Extraer las 15 citas más importantes del libro
    important_quotes = []
    for i in range(15):
        # Aquí se podrían utilizar diferentes criterios para identificar las citas importantes, como la longitud de la oración o la presencia de palabras clave
        important_quotes.append(book_sentences[i])

    # Crear una reseña resumida del libro basada en las citas importantes
    review_text = f"El libro cargado es una obra que explora temas como [tema 1], [tema 2] y [tema 3]. A lo largo del libro, el autor utiliza una serie de citas impactantes que ilustran la profundidad y la complejidad de estos temas. Por ejemplo, una cita importante del libro dice: '{important_quotes[0]}'. Otra cita interesante del libro es: '{important_quotes[1]}'. En general, el libro es una lectura interesante y bien escrita que ofrece una visión única sobre [tema 1], [tema 2] y [tema 3]."

    # Imprimir la reseña del libro
    st.write(review_text)

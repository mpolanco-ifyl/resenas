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

    # Crear una reseña del libro basada en las citas importantes
    intro_text = "El libro que se ha cargado es una obra que aborda varios temas importantes, incluyendo [tema 1], [tema 2] y [tema 3]. A lo largo del libro, el autor utiliza una serie de citas impactantes que ilustran la profundidad y la complejidad de estos temas. En este ensayo, se explorarán algunas de las citas más importantes del libro y se discutirá su relevancia y significado para los temas tratados."

    body_text = "Una de las citas más impactantes del libro dice: '{}'. Esta cita es importante porque ilustra claramente el [tema 1] que el autor está tratando de transmitir. Otra cita interesante del libro es: '{}'. Esta cita es importante porque muestra la conexión entre [tema 2] y [tema 3] en la obra. Además, la cita [cita 3] es un ejemplo claro de [tema 1]."

    conclusion_text = "En general, el libro es una lectura interesante y bien escrita que ofrece una visión única sobre [tema 1], [tema 2] y [tema 3]. Las citas seleccionadas para este ensayo ilustran la profundidad y la complejidad de los temas tratados en el libro y muestran el talento del autor para transmitir sus ideas de manera efectiva."

    # Imprimir la reseña del libro
    st.write(intro_text)
    st.write(body_text)
    st.write(conclusion_text)

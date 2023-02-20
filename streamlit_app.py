import streamlit as st
import nltk
from collections import Counter

nltk.download('punkt')

st.title("Generador de reseñas de libros")

# Cargar el archivo de texto del libro
uploaded_file = st.file_uploader("Cargar libro en formato TXT", type=["txt"])
if uploaded_file is not None:
    book_text = uploaded_file.read().decode("utf-8")

    # Tokenizar el texto del libro en oraciones
    book_sentences = nltk.sent_tokenize(book_text)

    # Extraer las palabras más importantes del libro
    important_words = []
    for sentence in book_sentences:
        # Tokenizar cada oración en palabras
        words = nltk.word_tokenize(sentence)
        # Eliminar las palabras vacías y los signos de puntuación
        words = [word.lower() for word in words if word.isalnum() and word.lower() not in nltk.corpus.stopwords.words('english')]
        # Añadir las palabras restantes a la lista de palabras importantes
        important_words.extend(words)

    # Calcular las palabras más comunes en el texto
    common_words = Counter(important_words).most_common(10)

    # Crear una reseña del libro basada en las palabras comunes
    intro_text = "El libro que se ha cargado es una obra que aborda varios temas importantes, incluyendo [tema 1], [tema 2] y [tema 3]. A lo largo del libro, el autor utiliza una serie de citas impactantes que ilustran la profundidad y la complejidad de estos temas. En este ensayo, se explorarán algunas de las citas más importantes del libro y se discutirá su relevancia y significado para los temas tratados."

    body_text = "Una de las citas más impactantes del libro dice: '{}'. Esta cita es importante porque [razón por la que la cita es importante]. Otra cita interesante del libro es: '{}'. Esta cita es importante porque [razón por la que la cita es importante]. Además, la cita '{}' es un ejemplo claro de [tema relacionado con la cita]."

    conclusion_text = "En general, el libro es una lectura interesante y bien escrita que ofrece una visión única sobre [tema 1], [tema 2] y [tema 3]. Las citas seleccionadas para este ensayo ilustran la profundidad y la complejidad de los temas tratados en el libro y muestran el talento del autor para transmitir sus ideas de manera efectiva. A través de estas citas, el autor nos invita a reflexionar sobre [tema general del libro] de una manera profunda y significativa. En general, este libro es una obra que vale la pena y que recomendaría a cualquier persona interesada en [tema 1], [tema 2] o [tema 3]."

    # Combinar las partes de la reseña en un solo texto
    review_text = intro_text + "\n\n" + body_text.format(common_words[0][0], common_words[1][0], common_words[2][0]) + "\n\n" + conclusion_text

    # Mostrar la reseña en la aplicación
    st.write(review_text)

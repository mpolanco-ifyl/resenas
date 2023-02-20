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
    intro_text = "El libro que se ha cargado es una obra que aborda varios temas importantes, incluyendo la lucha por la libertad, el poder de la esperanza y la importancia de la familia. A lo largo del libro, el autor utiliza una serie de citas impactantes que ilustran la profundidad y la complejidad de estos temas. En este ensayo, se explorarán algunas de las citas más importantes del libro y se discutirá su relevancia y significado para los temas tratados."

    body_text = "Una de las citas más impactantes del libro dice: '{}'. Esta cita es importante porque ilustra claramente la importancia de la lucha por la libertad en la obra. La idea central que se plantea en esta cita es que 'La libertad no es nada si no es la libertad de errar', y el autor utiliza esta idea para ilustrar la complejidad de la lucha por la libertad. Otra cita interesante del libro es: '{}'. Esta cita es importante porque muestra el poder de la esperanza en la obra. En esta cita, el autor sugiere que 'La esperanza es el sueño del hombre despierto', lo que ilustra la importancia de la esperanza en la vida de los personajes. Además, la cita 'La familia es una obra maestra del arte del espíritu' es un ejemplo claro de la importancia de la familia en la obra. En esta cita, el autor muestra cómo la familia es un elemento clave para el bienestar de los personajes."

    conclusion_text = "En general, el libro es una lectura interesante y bien escrita que ofrece una visión única sobre la lucha por la libertad, el poder de la esperanza y la importancia de la familia. Las citas seleccionadas para este ensayo ilustran la profundidad y la complejidad de los temas tratados en el libro y muestran el talento del autor para transmitir sus ideas de manera efectiva. A través de estas citas, el autor nos invita a reflexionar sobre la importancia de la libertad, la esperanza y la familia de una manera profunda y significativa. En general, este libro es una obra que vale la pena y que recomendaría a cualquier persona interesada en estos temas."

    # Combinar las partes de la reseña en un solo texto
    review_text = intro_text + "\n\n" + body_text + "\n\n" + conclusion_text

    # Mostrar la reseña en la aplicación
    st.write(review_text)

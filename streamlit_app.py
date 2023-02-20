import streamlit as st
from textblob import TextBlob

st.title("Generador de evaluaciones de libros")

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
    # Generar una evaluación larga del libro
    if sentiment > 0:
        evaluation = f"Este libro es una obra maestra. La prosa es hermosa y las historias son profundas. Desde la primera página, me sentí inmerso en el mundo que el autor había creado. Los personajes son complejos y bien desarrollados, y su lucha contra los conflictos internos y externos me dejó con una gran impresión. La trama es emocionante y llena de giros y vueltas que me mantuvieron enganchado hasta el final. Como dijo Andy Warhol: '{quotes[2]}', y este libro seguramente se mantendrá en mi mente durante mucho tiempo."
    elif sentiment < 0:
        evaluation = f"Lamentablemente, este libro no me gustó. La prosa es confusa y las historias son poco interesantes. Me costó mucho conectar con los personajes, y su lucha contra los conflictos internos y externos me pareció aburrida. La trama se sintió lenta y predecible, y no pude evitar sentir que estaba perdiendo el tiempo al leer este libro. Como dijo Oscar Wilde: '{quotes[0]}', y esta evaluación es un reflejo de mi decepción."
    else:
        evaluation = f"Este libro es interesante pero no sobresaliente. La prosa es sólida y las historias son intrigantes, pero no me dejaron una impresión duradera. Los personajes son bien desarrollados, pero no pude conectarme con ellos de la manera que esperaba. La trama es emocionante en algunos momentos, pero en otros se siente lenta y predecible. Como dijo Marcel Proust: '{quotes[1]}', y esta evaluación refleja mi sentimiento neutral hacia este libro."
    # Mostrar la evaluación generada al usuario
    st.write(evaluation)

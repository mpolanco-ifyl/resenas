import spacy
import random

nlp = spacy.load("es_core_news_sm")

# Texto del libro de ejemplo
texto_libro = """
[Inserta aquí el texto del libro]

"""

# Cargar el texto del libro
doc = nlp(texto_libro)

# Extraer las citas del libro
citas = [str(sent) for sent in doc.sents if "“" in sent.text]

# Generar la introducción
introduccion = f"El libro {doc[:10]} es un libro interesante que cubre varios temas importantes. "

# Generar el cuerpo del ensayo
cuerpo = "En este ensayo, se explorarán algunos de los temas clave del libro a través de las siguientes citas:\n\n"
citas_seleccionadas = random.sample(citas, 15)
for i, cita in enumerate(citas_seleccionadas):
    cuerpo += f"{i+1}. \"{cita}\"\n"

cuerpo += "Esas citas destacan la importancia de varios temas clave del libro, como la exploración del pasado, la naturaleza humana y la lucha por la libertad. "

# Generar la conclusión
conclusion = "En general, el libro es una lectura fascinante que ofrece una visión única del mundo. Los temas explorados en el libro son relevantes tanto hoy como en el pasado y nos obligan a considerar el mundo que nos rodea de una manera nueva y emocionante. Recomiendo encarecidamente este libro a cualquier persona interesada en la exploración del mundo y en la lucha por la libertad. "

# Combinar las partes en una reseña completa
reseña = introduccion + cuerpo + conclusion

print(reseña)

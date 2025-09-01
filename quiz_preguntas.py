import random

array_preguntas = [
    {
        "pregunta": "¿En qué año comenzó la Primera Guerra Mundial?",
        "opciones": ["1914", "1915", "1913", "1916"],
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "¿Quién pintó La Mona Lisa?",
        "opciones": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Miguel Ángel"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["Tierra", "Marte", "Júpiter", "Saturno"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿En qué continente se encuentra el río Nilo?",
        "opciones": ["Asia", "Europa", "África", "América"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿Cuál es el elemento químico más abundante en el universo?",
        "opciones": ["Helio", "Hidrógeno", "Carbono", "Oxígeno"],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Quién escribió 'Don Quijote de la Mancha'?",
        "opciones": ["Miguel de Cervantes", "William Shakespeare", "Dante Alighieri", "Johann Wolfgang von Goethe"],
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "¿Cuál es la moneda oficial de Japón?",
        "opciones": ["Yuan", "Won", "Yen", "Dólar"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿En qué año se fundó la ciudad de Roma?",
        "opciones": ["753 a.C.", "500 a.C.", "1000 a.C.", "200 a.C."],
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "¿Cuál es el animal terrestre más rápido del mundo?",
        "opciones": ["León", "Guepardo", "Leopardo", "Tigre"],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Quién fue el primer presidente de Estados Unidos?",
        "opciones": ["Thomas Jefferson", "John Adams", "George Washington", "Benjamin Franklin"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿En qué año se descubrió América?",
        "opciones": ["1492", "1490", "1495", "1500"],
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "¿Cuál es la lengua más hablada del mundo?",
        "opciones": ["Inglés", "Español", "Chino mandarín", "Hindi"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿Quién compuso la 'Novena Sinfonía'?",
        "opciones": ["Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Ludwig van Beethoven", "Franz Schubert"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿Cuál es el país más grande del mundo por superficie?",
        "opciones": ["China", "Estados Unidos", "Canadá", "Rusia"],
        "respuesta_correcta": "D"
    },
    {
        "pregunta": "¿En qué siglo vivió William Shakespeare?",
        "opciones": ["Siglo XV", "Siglo XVI", "Siglo XVII", "Siglo XVIII"],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Cuál es el metal más precioso del mundo?",
        "opciones": ["Platino", "Oro", "Rodio", "Paladio"],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Quién inventó la imprenta?",
        "opciones": ["Johannes Gutenberg", "Leonardo da Vinci", "Galileo Galilei", "Isaac Newton"],
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "¿Cuál es el océano más grande del mundo?",
        "opciones": ["Océano Atlántico", "Océano Índico", "Océano Pacífico", "Océano Ártico"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿En qué año terminó la Segunda Guerra Mundial?",
        "opciones": ["1944", "1945", "1946", "1943"],
        "respuesta_correcta": "B"
    }
]

def play():    
    print('🔍 Bienvenido al juego de preguntas y respuestas 🔍')
    print('A continuación te presentaremos una serie de 6 preguntas y respuestas')
    print('Las respuestas serán 4 opciones (A, B, C, D), y solo una será la correcta')
    print('Cada pregunta correcta te dará 1 punto')
    print('Cada pregunta incorrecta te restará 0.5 puntos')
    print('El juego terminará cuando respondas todas las preguntas')    
    print('==========================================================')
    repetir = True
    while repetir:
        puntaje = 0
        preguntas_aleatorias = random.sample(array_preguntas, 6)
        
        for pregunta in preguntas_aleatorias:
            print(pregunta['pregunta'])
            index = 0
            for opcion in pregunta['opciones']:
                if index == 0:
                    print(f"A. {opcion}")
                elif index == 1:
                    print(f"B. {opcion}")
                elif index == 2:
                    print(f"C. {opcion}")
                else:
                    print(f"D. {opcion}")
                index += 1
            respuesta = input('Ingresa la respuesta (A, B, C, D): ')
            if respuesta.upper() == pregunta['respuesta_correcta']:
                print('✅ Respuesta correcta')
                puntaje += 1
            else:
                print('❌ Respuesta incorrecta')
                puntaje -= 0.5
            print('==========================================================')

        print('Tu puntaje final es: ', puntaje)
        if puntaje >= 3:
            print('🎉 ¡Felicidades! Has ganado el juego')
        else:
            print('❌ 😭 Has perdido el juego')

        print('Quieres jugar de nuevo? (s/n)')
        repetir = input()
        if repetir == 's':
            print('🔍 Bienvenido al juego de preguntas y respuestas 🔍')
            repetir = True
        else:
            print('Gracias por jugar')
            repetir = False
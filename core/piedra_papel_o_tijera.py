import random

opciones = ("piedra", "papel", "tijera")

# Reglas: cada clave vence a la tupla de valores
prioridad = {
    "piedra": ("tijera",),
    "papel": ("piedra",),
    "tijera": ("papel",),
}

def determinar_ganador(jugador: str, bot: str) -> int:
    """
    Devuelve:
      1 si gana jugador
      0 si empate
     -1 si gana bot
    """
    if jugador == bot:
        return 0
    if bot in prioridad[jugador]:
        return 1
    return -1

def play_piedra_papel_o_tijera():
    print("Piedra, Papel o Tijera (vs Bot)")
    print("Opciones válidas: piedra, papel, tijera")
    rondas = 3  # cantidad fija de rondas

    puntos_jugador = 0
    puntos_bot = 0

    for i in range(1, rondas + 1):
        print(f"\n-- Ronda {i} de {rondas} --")
        eleccion_j = input("Tu elección (piedra/papel/tijera): ").strip().lower()

        if eleccion_j not in opciones:
            print("Entrada inválida. Se registra como empate y se pasa a la siguiente ronda.")
            print(f"Marcador: Vos {puntos_jugador} - {puntos_bot} Bot")
            continue

        eleccion_b = random.choice(opciones)
        print(f"Bot eligió: {eleccion_b}")

        resultado = determinar_ganador(eleccion_j, eleccion_b)
        if resultado == 1:
            puntos_jugador += 1
            print("Ganaste esta ronda.")
        elif resultado == -1:
            puntos_bot += 1
            print("Perdiste esta ronda.")
        else:
            print("Empate.")

        print(f"Marcador: Vos {puntos_jugador} - {puntos_bot} Bot")

    print("\nResultado final")
    if puntos_jugador > puntos_bot:
        print(f"Victoria. Ganaste {puntos_jugador} a {puntos_bot}.")
    elif puntos_jugador < puntos_bot:
        print(f"Derrota. Perdiste {puntos_jugador} a {puntos_bot}.")
    else:
        print(f"Empate final: {puntos_jugador} a {puntos_bot}.")

if __name__ == "__main__":
    play()

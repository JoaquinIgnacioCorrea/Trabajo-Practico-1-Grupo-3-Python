import os

#region Funciones programa
def select_character(jugador = 0, jugador_name = "1") :
    while (jugador != "1" and jugador != "2"):
        jugador = input(f"Seleccione el jugador {jugador_name} \n 1. X \n 2. O\n")
        os.system("cls")
    return "X" if jugador == "1" else "O"

def verificar_ganador(tablero, jugador):
    combinaciones = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),  
                     (0, 4, 8), (2, 4, 6)]
    for a, b, c in combinaciones:
        if tablero[a] == tablero[b] == tablero[c] and tablero[a] in ["X", "O"]:
            return jugador
    return None

def realizar_jugada(jugador, tablero, jugador_1, jugador_2):
    movimiento = 0
    while (movimiento not in range(1,10)):
        mostrar_tablero(jugador_1, jugador_2, tablero)
        movimiento = int(input("Ingrese su movimiento\n"))
        if(tablero[movimiento - 1] not in ["X", "O"]):
            tablero[movimiento - 1] = jugador
            return
        else:
            os.system("cls")
            print("Movimiento inválido. Intente nuevamente.\n")
            movimiento = 0

def mostrar_tablero(jugador_1, jugador_2, tablero):
    print(f"Jugador 1 = {jugador_1} \tJugador 2 = {jugador_2}\n")
    for i in range(0, 9, 3):
        fila = " | ".join(tablero[i:i+3])
        print(fila)

def reiniciar_juego ():
    reiniciar = ""
    while reiniciar not in ["s", "n"]:
        reiniciar = input("¿Querés reiniciar? (s/n): ").lower()
    if reiniciar == "n":
        print("¡Gracias por jugar!")
    return reiniciar
#endregion
def play_ta_te_ti():

    reiniciar = "s"

    while reiniciar == "s":
        os.system("cls")
        print("Bienvenido al juego de Ta-Te-Ti\n")

        jugador_1 = select_character()
        jugador_2 = "X" if jugador_1 == "O" else "O"
        jugadores = [jugador_1, jugador_2]
        tablero = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        ganador = None
        turno = 0

        print(f"\nJugador 1 es {jugador_1}\tJugador 2 es {jugador_2}\n")

        while ganador is None:
            print(f"Turno del jugador {jugadores[turno]}")
            realizar_jugada(jugadores[turno], tablero, jugador_1, jugador_2)
            os.system("cls")
            ganador = verificar_ganador(tablero, jugadores[turno])
            if ganador is None and all(pos in ["X", "O"] for pos in tablero):
                ganador = "e"
            turno = 1 if turno == 0 else 0

        os.system("cls")
        print("Hubo un empate") if ganador == "e"  else print(f"El ganador es: {ganador}")
        
        reiniciar = reiniciar_juego()
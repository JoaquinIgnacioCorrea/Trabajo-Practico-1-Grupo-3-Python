import os
import sys

#region Funciones programa
def SelectCharacter(jugador = 0, jugadorname = "1") :
    while (jugador != "1" and jugador != "2"):
        jugador = input(f"Seleccione el jugador {jugadorname} \n 1. X \n 2. O\n")
        os.system("cls")
    return "X" if jugador == "1" else "O"

def VerificarGanador(tablero, jugador):
    combinaciones = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),  
                     (0, 4, 8), (2, 4, 6)]
    for a, b, c in combinaciones:
        if tablero[a] == tablero[b] == tablero[c] and tablero[a] in ["X", "O"]:
            return jugador
    return None

def RealizarJugada(jugador, tablero):
    movimiento = 0
    while (movimiento not in range(1,10)):
        MostrarTablero(Jugador1, Jugador2, tablero)
        movimiento = int(input("Ingrese su movimiento\n"))
        if(tablero[movimiento - 1] not in ["X", "O"]):
            tablero[movimiento - 1] = jugador
            return
        else:
            os.system("cls")
            print("Movimiento inválido. Intente nuevamente.\n")
            movimiento = 0

def MostrarTablero(jugador1, jugador2, tablero):
    print(f"Jugador 1 = {jugador1} \tJugador 2 = {jugador2}\n")
    for i in range(0, 9, 3):
        fila = " | ".join(tablero[i:i+3])
        print(fila)

def ReiniciarJuego ():
    reiniciar = ""
    while reiniciar not in ["s", "n"]:
        reiniciar = input("¿Querés reiniciar? (s/n): ").lower()
    if reiniciar == "n":
        print("¡Gracias por jugar!")
    return reiniciar
#endregion

reiniciar = "s"

while reiniciar == "s":
    os.system("cls")
    print("Bienvenido al juego de Ta-Te-Ti\n")

    Jugador1 = SelectCharacter()
    Jugador2 = "X" if Jugador1 == "O" else "O"
    jugadores = [Jugador1, Jugador2]
    tablero = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ganador = None
    turno = 0

    print(f"\nJugador 1 es {Jugador1}\tJugador 2 es {Jugador2}\n")

    while ganador is None:
        print(f"Turno del jugador {jugadores[turno]}")
        RealizarJugada(jugadores[turno], tablero)
        os.system("cls")
        ganador = VerificarGanador(tablero, jugadores[turno])
        if ganador is None and all(pos in ["X", "O"] for pos in tablero):
            ganador = "e"
        turno = 1 if turno == 0 else 0

    os.system("cls")
    print("Hubo un empate") if ganador == "e"  else print(f"El ganador es: {ganador}")
    
    reiniciar = ReiniciarJuego()
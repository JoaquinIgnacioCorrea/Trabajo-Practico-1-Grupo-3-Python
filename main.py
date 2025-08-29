import os

def menu():
    menu = True
    games = obtain_games()
    while menu:
        print("\n--- Menú ---")
        for i, game in enumerate(games, 1):
            print(f"{i}. Jugar {(game.replace('_', ' ').title()).replace('.Py', '')}")
        print(f"{len(games) + 1}. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion in [str(i) for i in range(1, len(games) + 1)]:
            os.system(f"python {games[int(opcion) - 1]}")
        elif opcion == str(len(games) + 1):
            print("Saliendo...")
            menu = False
        else:
            print("Opción inválida. Intenta de nuevo.")

def obtain_games():
    obtained_games = []
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    return [
        "piedra_papel_o_tijera.py",
        "quiz_python.py",
        "ta_te_ti.py",
        "adivinar_el_numero.py"
    ]

menu()
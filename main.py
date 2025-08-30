import os

def clean_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    menu = True
    games = obtain_games()
    while menu:
        clean_console()
        print("\n--- Menú ---")
        for i, game in enumerate(games, 1):
            print(f"{i}. Jugar {(game.replace('_', ' ').title()).replace('.Py', '')}")
        print(f"{len(games) + 1}. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion in [str(i) for i in range(1, len(games) + 1)]:
            clean_console()
            os.system(f"python {games[int(opcion) - 1]}")
            input("\nPresiona Enter para volver al menú...")
        elif opcion == str(len(games) + 1):
            clean_console()
            print("Saliendo...")
            menu = False
        else:
            print("Opción inválida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")

def obtain_games():
    obtained_games = []
    for file in os.listdir("."):
        if file.endswith(".py") and file != "main.py":
            obtained_games.append(file)
    return obtained_games

menu()
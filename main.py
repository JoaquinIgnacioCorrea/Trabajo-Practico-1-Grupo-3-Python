import os

def clean_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    menu = True
    games = import_games(obtain_games())
    while menu:
        clean_console()
        print("\n--- Menú ---")
        for i, game in enumerate(games, 1):
            print(f"{i}. Jugar {(game.__name__.replace('_', ' ').title())}")
        print(f"{len(games) + 1}. Salir")
        option = input("Selecciona una opción: ")
        
        if option in [str(i) for i in range(1, len(games) + 1)]:
            clean_console()
            games[int(option) - 1].play()
            input("\nPresiona Enter para volver al menú...")
        elif option == str(len(games) + 1):
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

def import_games(games):
    imported_games = []
    for game in games:
        module = __import__(game.replace(".py", ""))
        imported_games.append(module)
    return imported_games

menu()
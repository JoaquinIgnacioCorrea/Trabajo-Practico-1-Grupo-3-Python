import os

import core.adivina_el_numero as adivina
import core.piedra_papel_o_tijera as ppt
import core.quiz_preguntas as quiz
import core.ta_te_ti as tateti

def clean_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    menu = True
    juegos = [
        ("Adivina El Número", adivina.play_adivina_el_numero),
        ("Piedra Papel O Tijera", ppt.play_piedra_papel_o_tijera),
        ("Quiz Preguntas", quiz.play_quiz_preguntas),
        ("Ta Te Ti", tateti.play_ta_te_ti),
    ]
    while menu:
        clean_console()
        print("\n--- Menú ---")
        for i, (nombre, _) in enumerate(juegos, 1):
            print(f"{i}. Jugar {nombre}")
        print(f"{len(juegos) + 1}. Salir")
        option = input("Selecciona una opción: ")
        
        if option in [str(i) for i in range(1, len(juegos) + 1)]:
            clean_console()
            _, fn = juegos[int(option) - 1]
            fn()
            input("\nPresiona Enter para volver al menú...")
        elif option == str(len(juegos) + 1):
            clean_console()
            print("Saliendo...")
            menu = False
        else:
            print("Opción inválida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")

menu()
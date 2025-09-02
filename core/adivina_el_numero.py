import random
import os
def clean_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def play_adivina_el_numero():
    number = random.randint(1, 10)
    print("¡Bienvenido al juego de adivinar el número!")
    print("Voy a elegir un numero entre 1 y 10...")
    print("Tenes 5 intentos para adivinarlo.")
    lives = 5
    win = False
    while lives > 0 and win == False:
        guess = int(input("¿Cuál es el número?: "))
        clean_console()
        if guess == number:
            print("¡Felicidades! Has adivinado el número.")
            win = True
        elif guess < number:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        lives -= 1
        if not win:
            print(f"Te quedan {lives} intentos.")
    if lives == 0:
        print(f"Lo siento, has perdido. El número era {number}.")
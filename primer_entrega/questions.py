import random
import string
categorias = {
    "programacion": ["python", "programa", "variable", "funcion"],
    "matematicas": ["suma", "resta", "multiplicacion", "division"],
    "geografia": ["pais", "capital", "continente", "oceano"]
}
guessed = []
attempts = 6
puntaje = 6
print("¡Bienvenido al Ahorcado!")
print()
categoria = input("Elija una categoria de palabras entre: [programacion, matematicas o geografia] ")
word = random.choice(categorias[categoria])
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        print("El puntaje es:", puntaje)
        break

    print(f"Intentos restantes: {attempts}")

    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")

    if letter.lower() in string.ascii_lowercase:
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -= 1
            print("Esa letra no está en la palabra.")
            print()
    else:
        print("Entrada no válida")
else:
    print(f"¡Perdiste! La palabra era: {word}")
    print("El puntaje es:", puntaje)
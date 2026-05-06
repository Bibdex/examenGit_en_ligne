import random

def jeu_devinette():
    nombre_secret = random.randint(1, 100)
    essais = 0

    print("Bienvenue dans le jeu de devinette !")
    print("Je pense à un nombre entre 1 et 100. Devinez-le !")

    while True:
        try:
            tentative = int(input("Votre proposition : "))
            essais += 1

            if tentative < nombre_secret:
                print("Trop petit !")
            elif tentative > nombre_secret:
                print("Trop grand !")
            else:
                print(f"Bravo ! Vous avez trouvé le nombre {nombre_secret} en {essais} essai(s).")
                break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

if __name__ == "__main__":
    jeu_devinette()

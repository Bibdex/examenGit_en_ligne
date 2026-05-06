
# Calcule la somme de deux nombres
def somme(a, b):
    return a + b

# Calcule la factorielle d'un entier non négatif
def factorielle(n):
    if n < 0:
        raise ValueError("Le nombre doit être non négatif")
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat

# Vérifie si un nombre est premier
def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Convertit Celsius en Fahrenheit
def celsius_en_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# Compte les voyelles dans une chaîne de caractères
def compter_voyelles(texte):
    voyelles = "aeiouyAEIOUY"
    return sum(1 for caractere in texte if caractere in voyelles)

# Retourne le plus grand élément d'une liste
def maximum(liste):
    if not liste:
        raise ValueError("La liste ne doit pas être vide")
    plus_grand = liste[0]
    for element in liste[1:]:
        if element > plus_grand:
            plus_grand = element
    return plus_grand

# Calcule la moyenne d'une liste de nombres
def moyenne(liste_nombres):
    if not liste_nombres:
        raise ValueError("La liste ne doit pas être vide")
    return sum(liste_nombres) / len(liste_nombres)

# Vérifie si une chaîne est un palindrome
def est_palindrome(texte):
    texte_sans_espace = "".join(texte.lower().split())
    return texte_sans_espace == texte_sans_espace[::-1]

# Convertit un nombre en une chaîne binaire
def entier_en_binaire(n):
    if n < 0:
        raise ValueError("Le nombre doit être non négatif")
    return bin(n)[2:]

# Génère une liste de nombres pairs jusqu'à une valeur donnée
def nombres_pairs(jusqua):
    return [i for i in range(2, jusqua + 1) if i % 2 == 0]


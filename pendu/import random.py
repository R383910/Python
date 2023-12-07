import random
import string

def mot_aleatoire(longueur):
    caracteres = string.ascii_letters  # Inclut toutes les lettres majuscules et minuscules
    mot = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot

longueur_du_mot = 8  # Vous pouvez spécifier la longueur souhaitée ici
mot_aleatoire_genere = mot_aleatoire(longueur_du_mot)
print(mot_aleatoire_genere)

import dictionnaire
import random
import sys

dico = dictionnaire.dictionnaire
nbVie = 7

nbLettreMax = int(input("Combien de lettres maximum voulez-vous ? "))

solution = random.choice(list(dico.values()))
solution = solution.upper()
solutionLength = len(solution)

while solutionLength > nbLettreMax:
    solution = random.choice(list(dico.values()))
    solution = solution.upper()
    solutionLength = len(solution)

base = "_" * solutionLength

#print("Mot aléatoire:", solution)

print(base)

while nbVie > 0:
    tentative = input("Donnez une lettre : ")
    tentative = tentative.upper()
    if tentative in solution:
        positions = [i for i, lettre in enumerate(solution) if lettre == tentative]
        for position in positions:
            liste_de_caracteres = list(base)
            liste_de_caracteres[position] = tentative
            base = ''.join(liste_de_caracteres)
        print(base)
    else:
        nbVie -= 1
        print("Mauvaise réponse, il vous reste", nbVie, "vies")
    
    if base == solution:  # Vérifiez la victoire à l'intérieur de la boucle
        print("Gagné ! La solution est " + solution)
        sys.exit(0)

print("Game Over")
print("La réponse été :", solution)

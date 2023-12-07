import sys

win = False
x = 0
y = 0
ligne1 = "---"
ligne2 = "---"
ligne3 = "---"
currentPlayer = "Joueur 1"
playerSymbole = ""

# Définition de la fonction update_board
def update_board(x, y, playerSymbole):
    global ligne1, ligne2, ligne3
    if x == 1:
        if y == 1:
            ligne1 = playerSymbole + ligne1[1:]
        elif y == 2:
            ligne2 = playerSymbole + ligne2[1:]
        elif y == 3:
            ligne3 = playerSymbole + ligne3[1:]
    elif x == 2:
        if y == 1:
            ligne1 = ligne1[0] + playerSymbole + ligne1[2:]
        elif y == 2:
            ligne2 = ligne2[0] + playerSymbole + ligne2[2:]
        elif y == 3:
            ligne3 = ligne3[0] + playerSymbole + ligne3[2:]
    elif x == 3:
        if y == 1:
            ligne1 = ligne1[:4] + playerSymbole + ligne1[4]
        elif y == 2:
            ligne2 = ligne2[:4] + playerSymbole + ligne2[4]
        elif y == 3:
            ligne3 = ligne3[:4] + playerSymbole + ligne3[4]
            
update_board(1, 1, "X")

nbPlayer = int(input("A combien voulez-vous jouer (1 ou 2) ? "))


def nextPlayer():
    global currentPlayer  # Declare currentPlayer as global
    if currentPlayer == "Joueur 1":
        currentPlayer = "Joueur 2"
    else:
        currentPlayer = "Joueur 1"

def board():
    print(ligne1)
    print(ligne2)
    print(ligne3)

def checkWin():
    global ligne1, ligne2, ligne3, win

    # Vérification des lignes horizontales
    for ligne in [ligne1, ligne2, ligne3]:
        if ligne == "XXX" or ligne == "OOO":
            win = True

    # Vérification des colonnes verticales
    for colonne in range(3):
        if ligne1[colonne] + ligne2[colonne] + ligne3[colonne] == "XXX" or \
           ligne1[colonne] + ligne2[colonne] + ligne3[colonne] == "OOO":
            win = True

    # Vérification des diagonales
    if ligne1[0] + ligne2[1] + ligne3[2] == "XXX" or ligne1[0] + ligne2[1] + ligne3[2] == "OOO":
        win = True
    if ligne1[2] + ligne2[1] + ligne3[0] == "XXX" or ligne1[2] + ligne2[1] + ligne3[0] == "OOO":
        win = True

def nextTurn():
    global ligne1, ligne2, ligne3, currentPlayer, playerSymbole
    if currentPlayer == "Joueur 1":
        playerSymbole = "X"
    else:
        playerSymbole = "O"
    print(board())
    print("Au ", currentPlayer, " de jouer")
    print("Votre symbole est ", playerSymbole)
    while True:
        try:
            x = int(input("Sur quelle colonne voulez-vous mettre votre signe ? (1, 2, 3) "))
            y = int(input("Sur quelle ligne voulez-vous mettre votre signe ? (1, 2, 3) "))
            if x not in [1, 2, 3] or y not in [1, 2, 3]:
                print("Coordonnées invalides. Veuillez choisir des valeurs parmi 1, 2 ou 3 pour la colonne et la ligne.")
            elif (x == 1 and y == 1 and ligne1[0] == ' ') or \
                 (x == 1 and y == 2 and ligne2[0] == ' ') or \
                 (x == 1 and y == 3 and ligne3[0] == ' ') or \
                 (x == 2 and y == 1 and ligne1[2] == ' ') or \
                 (x == 2 and y == 2 and ligne2[2] == ' ') or \
                 (x == 2 and y == 3 and ligne3[2] == ' ') or \
                 (x == 3 and y == 1 and ligne1[4] == ' ') or \
                 (x == 3 and y == 2 and ligne2[4] == ' ') or \
                 (x == 3 and y == 3 and ligne3[4] == ' '):
                break  # Sortir de la boucle si les coordonnées sont valides et la case est vide
            else:
                print("La case est déjà occupée. Veuillez choisir une case vide.")
        
        except ValueError:
            print("Veuillez entrer des nombres valides (1, 2, 3) pour la colonne et la ligne.")
    
    # Update the game board based on player's input
    if x == 1:
        if y == 1:
            ligne1 = playerSymbole + ligne1[1:]
        elif y == 2:
            ligne2 = playerSymbole + ligne2[1:]
        elif y == 3:
            ligne3 = playerSymbole + ligne3[1:]
    elif x == 2:
        if y == 1:
            ligne1 = ligne1[0] + playerSymbole + ligne1[2:]
        elif y == 2:
            ligne2 = ligne2[0] + playerSymbole + ligne2[2:]
        elif y == 3:
            ligne3 = ligne3[0] + playerSymbole + ligne3[2:]
    elif x == 3:
        if y == 1:
            ligne1 = ligne1[:4] + playerSymbole + ligne1[4]
        elif y == 2:
            ligne2 = ligne2[:4] + playerSymbole + ligne2[4]
        elif y == 3:
            ligne3 = ligne3[:4] + playerSymbole + ligne3[4]

    checkWin()
    nextPlayer()  # Call nextPlayer() to change the player

if nbPlayer == 2:
    while not win:
        nextTurn()
    board()
    print("La partie est terminée.")
    
else:
    print("Cette fonctionnalité n'est pas encore disponible.")

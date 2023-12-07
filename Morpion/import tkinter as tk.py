import tkinter as tk

win = False
x = 0
y = 0
lignes = [["", "", ""], ["", "", ""], ["", "", ""]]
currentPlayer = "Joueur 1"

def update_board(x, y):
    global lignes, currentPlayer
    if lignes[x][y] == "":
        if currentPlayer == "Joueur 1":
            lignes[x][y] = "X"
            currentPlayer = "Joueur 2"
        else:
            lignes[x][y] = "O"
            currentPlayer = "Joueur 1"

        check_win()
        update_ui()

def check_win():
    global lignes, win

    for i in range(3):
        if lignes[i][0] == lignes[i][1] == lignes[i][2] != "":
            win = True

    for i in range(3):
        if lignes[0][i] == lignes[1][i] == lignes[2][i] != "":
            win = True

    if lignes[0][0] == lignes[1][1] == lignes[2][2] != "":
        win = True
    if lignes[0][2] == lignes[1][1] == lignes[2][0] != "":
        win = True

def update_ui():
    for i in range(3):
        for j in range(3):
            labels[i][j].config(text=lignes[i][j])
    if win:
        label.config(text="La partie est terminée.")
        for i in range(3):
            for j in range(3):
                labels[i][j].unbind("<Button-1>")

root = tk.Tk()
root.title("Morpion")

labels = [[None, None, None], [None, None, None], [None, None, None]]

for i in range(3):
    for j in range(3):
        label = tk.Label(root, text="", font=("Helvetica", 48), width=3, height=1)
        label.grid(row=i, column=j)
        labels[i][j] = label
        label.bind("<Button-1>", lambda event, i=i, j=j: update_board(i, j))

label = tk.Label(root, text="", font=("Helvetica", 16))
label.grid(row=3, column=1)

canvas = tk.Canvas(root, width=300, height=300)
canvas.grid(row=0, column=0)

for i in range(1, 3):
    canvas.create_line(0, i * 100, 300, i * 100, fill="black", width=5)
    canvas.create_line(i * 100, 0, i * 100, 300, fill="black", width=5)

root.mainloop()

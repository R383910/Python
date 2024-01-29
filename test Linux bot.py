import os

def chercher_fichier(repertoire, nom_fichier):
    # Parcours récursif du répertoire et de ses sous-répertoires
    for dossier, sous_dossiers, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            # Vérifie si le nom du fichier correspond (sans tenir compte de l'extension)
            if nom_fichier in fichier:
                return os.path.join(dossier, fichier)
    return None

if __name__ == "__main__":
    # Chemin du répertoire racine où vous souhaitez commencer la recherche
    repertoire_racine = "/"  # Vous pouvez changer cela en fonction de votre besoin

    # Nom du fichier que vous cherchez (sans extension)
    nom_fichier_recherche = "cat"  # Remplacez cela par le nom de votre fichier sans extension

    # Chercher le fichier
    chemin_trouve = chercher_fichier(repertoire_racine, nom_fichier_recherche)

    if chemin_trouve:
        print(f"Le fichier {nom_fichier_recherche} a été trouvé à : {chemin_trouve}")
    else:
        print(f"Le fichier {nom_fichier_recherche} n'a pas été trouvé.")

import pandas as pd
import re  # sert pour séparer dans grammage : avoir d'un coté 100 et de l'autre 'g'

# import fichier recette.csv
CSV_FILE = r"C:\Users\virgi\Desktop\AGRAL\AGRAL4\Informatique\Projet base données2\recettes.csv"
SEPARATOR = " "
df = pd.read_csv(CSV_FILE, sep=SEPARATOR, header=(
    0))  # on a besoin de encoding??, encoding='utf_8')#latin-1')  # endocing permet éviter erreur ("UnicodeDecodeError: 'utf-8' codec...)"and to ignore the byte#dtype=np.dtype('unicode') inutile

# import fichier liste_alim
CSV_FILE2 = r"C:\Users\virgi\Desktop\AGRAL\AGRAL4\Informatique\Projet base données2\Table_CIQUAL_reduite.xlsx"
SEPARATOR2 = "\t"
df2 = pd.read_excel(CSV_FILE2)


# on crée un objet recette
class Recette():
    def __init__(self, nom_recette="", ingredient=[]):
        self.nom_recette = nom_recette
        self.ingredient = ingredient

    def __str__(self):
        return self.nom_recette #+ " [" + str(self.ingredient) + "] "


class Ingredient():
    def __init__(self, nom="", quantite="", unite=""):
        self.nom = nom
        self.quantite = quantite
        self.unite = unite

    def __str__(self):
        return self.nom + " (" + self.quantite + self.unite + ") "


# partie 1
# on crée une liste remplie de toutes les recettes
li = []  # liste vide qui prendra les recettes

# on veut reformater note fichier pour ensuite remplir li
# il faut mettre l'encodage encoding=uft8 pour avoir les accents normalement
with open(r'C:\Users\virgi\Desktop\AGRAL\AGRAL4\Informatique\Projet base données2\recettes.csv', 'r',
          encoding='utf_8') as fich:
    for i in range(len(df.index)):  # attention, on utilise la longueur du tableau de df!

        recette = Recette()

        lines = fich.readline()  # donne une seule ligne
        ligne_nom_recette = lines.split(sep='"')[1]  # donne le nom de la recette
        recette.nom_recette = ligne_nom_recette
        recette.ingredient = []

        ligne_ingredient = lines.split(sep='"')[3].split(",")  # va prendre la liste des ingrédients d'une recette
        ligne_grammageglob = lines.split(sep='"')[5].split(
            ",")  # prends la liste des grammages et de leur valeur pour la même recette
        ligne_grammage_sep = []
        if i >= 1:  # permet de ne pas tenir compte des noms des colonnes
            # liste qui contiendra d'un coté la valeur du grammage, d'un coté l'unité
            for i in range(len(ligne_grammageglob)):  # on fait une boucle sur le nombre de grammage dans le recette
                ingredient = Ingredient()
                ingredient.nom = ligne_ingredient[i]

                ligne_grammage_unite = re.split("[0-9]+", ligne_grammageglob[i])[
                    1]  # permet de séparer la virer la partie chiffre donc garder la partie lettre dong unite
                # print("grammi :"+ligne_grammageglob[i])
                ligne_grammage_valeur = re.split("[a-z]+", ligne_grammageglob[i])[
                    0]  # permet de séparer la virer la partie lettre donc garder la partie chiffre dont grammage
                # print("ligne unité" + ligne_grammage_valeur)

                ingredient.quantite = ligne_grammage_valeur
                ingredient.unite = ligne_grammage_unite

                recette.ingredient.append(ingredient)

            #    ligne_grammage_sep = [ligne_grammage_valeur,ligne_grammage_unite]

            li.append(recette)

for recette in li:
    print(recette.nom_recette, end=" ")
    for i in recette.ingredient:
        print(i, end=" ")

    print()
# print(str(li)) # permet d'afficher dans un language compréhensible l'élément 4 de la liste li

# attention, on n'a qu'un groupe pour les grammage, faut faire un boucle

# partie 2

# partie 2a :  description des régimes particuliers
# on crée une liste qui contient l'ensemble des éléments que le régime ne eput pas tolérer

from Part1 import donne_liste_recette

# après import de donne_liste_recette de Part1
li = donne_liste_recette()  # pour importer li

liste_ingre_issus_recette = []
def donne_liste_ingre_issus_recette():
    # on détermine la liste totale des ingrédients contenue dans les recettes
    for recette in li:
        for i in recette.ingredient:
            if i.nom not in liste_ingre_issus_recette:  # permet d'éviter d'avoir des doublons dans le liste totale des ingré des recettes
                liste_ingre_issus_recette.append(i.nom)
    return liste_ingre_issus_recette


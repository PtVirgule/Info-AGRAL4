import pandas as pd
import re
from Part1 import donne_liste_recette

# import fichier recette.csv
CSV_FILE = r"C:\Users\virgi\Desktop\AGRAL\AGRAL4\Informatique\Projet base données2\recettes.csv"
SEPARATOR = " "
df = pd.read_csv(CSV_FILE,sep=SEPARATOR)  # on a besoin de encoding??, encoding='utf_8')#latin-1')  # endocing permet éviter erreur ("UnicodeDecodeError: 'utf-8' codec...)"and to ignore the byte#dtype=np.dtype('unicode') inutile

# import fichier liste_alim
CSV_FILE2 = r"C:\Users\virgi\Desktop\AGRAL\AGRAL4\Informatique\Projet base données2\Table_CIQUAL_reduite2.7.xlsx"
SEPARATOR2 = "\t"
df2 = pd.read_excel(CSV_FILE2)

# après import de donne_liste_recette de Part1
li = donne_liste_recette()  # pour importer li

# objectif : regarder si les ingrédients des recettes sont dans la liste des ingré

liste_ingre_issus_recette = []
liste_alim_avec_s = ['champignon de paris', 'maïs', 'anchois', 'fromage frais', 'fois gras', 'fromage de chèvre frais',
                     'saumon frais']

# on détermine la liste totale des ingrédients contenue dans les recettes
def dic_alim_correspondance():
    for recette in li:
        for i in recette.ingredient:
            # print(vars(i)['nom'])
            # print(i.nom)
            if i.nom not in liste_ingre_issus_recette:  # permet d'éviter d'avoir des doublons dans le liste totale des ingré des recettes
                liste_ingre_issus_recette.append(i.nom)

    dic_alim_similaire = {}

    for i in range(len(liste_ingre_issus_recette) - 1):
        for j in range(len(df2['alim_nom_fr'])):
            # print(liste_ingre_issus_recette[i])
            # print(df2['alim_nom_fr'][j])
            # permet de regarder si les ingrédients sont rentrés avec un "s"
            nom_avec_s = False
            nom_avec_espace=False

            if liste_ingre_issus_recette[i][-1] == 's':
                # print(liste_ingre_issus_recette[i].lower())
                if liste_ingre_issus_recette[i].lower() not in liste_alim_avec_s:
                    nom_avec_s = False
                    # print("ok"+str(liste_ingre_issus_recette[i]))
                else:
                    # print(liste_ingre_issus_recette[i][:-1])
                    nom_avec_s = True
                    #print("non"+str(liste_ingre_issus_recette[i]))
            #permet de vérifier si les ingrédients ont un espace avant leur nom
            if liste_ingre_issus_recette[i][0] == " ":
                nom_avec_espace=True
                #print(liste_ingre_issus_recette[i])
            if nom_avec_s:
                if nom_avec_espace:
                    # print(liste_ingre_issus_recette[i].find(df2['alim_nom_fr'][j]))
                    if df2['alim_nom_fr'][j].lower().find(liste_ingre_issus_recette[i][
                                                              1:-1].lower()) != -1 or liste_ingre_issus_recette[i][1:-1].lower().find(df2['alim_nom_fr'][j].lower()) != -1:  # la fonction renvoit -1 si le premier string n'est aps compris dans l'autre
                        dic_alim_similaire[liste_ingre_issus_recette[i]] = df2['alim_nom_fr'][j]
                else :
                    # print(liste_ingre_issus_recette[i].find(df2['alim_nom_fr'][j]))
                    if df2['alim_nom_fr'][j].lower().find(liste_ingre_issus_recette[i][
                                                              :-1].lower()) != -1 or liste_ingre_issus_recette[i][:-1].lower().find(df2['alim_nom_fr'][j].lower()) != -1:  # la fonction renvoit -1 si le premier string n'est aps compris dans l'autre
                        dic_alim_similaire[liste_ingre_issus_recette[i]] = df2['alim_nom_fr'][j]

            else:  # quand nom_avec_s==False
                if nom_avec_espace:
                    if len(liste_ingre_issus_recette[i][1:]) <= len(df2['alim_nom_fr'][j]) or len(liste_ingre_issus_recette[i][1:]) > len(df2['alim_nom_fr'][j]):
                        if df2['alim_nom_fr'][j].lower().find(liste_ingre_issus_recette[
                                                                  i][1:].lower()) != -1 or liste_ingre_issus_recette[i][:-1].lower().find(df2['alim_nom_fr'][j].lower()) != -1 :  # la fonction renvoit -1 si le premier string n'est aps compris dans l'autre
                            dic_alim_similaire[liste_ingre_issus_recette[i]] = df2['alim_nom_fr'][j]
                else :
                    if len(liste_ingre_issus_recette[i][1:]) <= len(df2['alim_nom_fr'][j]) or len(liste_ingre_issus_recette[i][1:]) > len(df2['alim_nom_fr'][j]):
                        if df2['alim_nom_fr'][j].lower().find(liste_ingre_issus_recette[
                                                                  i].lower()) != -1 or liste_ingre_issus_recette[i].lower().find(df2['alim_nom_fr'][j].lower()) != -1 :  # la fonction renvoit -1 si le premier string n'est aps compris dans l'autre
                            dic_alim_similaire[liste_ingre_issus_recette[i]] = df2['alim_nom_fr'][j]

    return dic_alim_similaire


a=dic_alim_correspondance()
print(a)
# tomate crue ressort tomate
# pb : lait de chèvre ressort lait
# pb par rapport à béchamelle et vinaigrette : regarder quels sont les ingrédients dans les ingrédietns des recettes qui ne sont pas dans les clés de 'dic_alim_similaire'
# pb pourquoi olive ressort comme si n'était pas dans dic_alim_similaire
# importer le new fichier Table_ciqual__reduite_2.0



# vérifie que tous les ingrédients des recettes soient dans la liste d'ingrédients original
p=0
for i in range(len(liste_ingre_issus_recette) - 1):
    if liste_ingre_issus_recette[i] not in a:
        print(liste_ingre_issus_recette[i])
        p=p+1
print(p)


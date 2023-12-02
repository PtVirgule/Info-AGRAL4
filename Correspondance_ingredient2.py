import pandas as pd
import re
from Part1 import donne_liste_recette
from est_plus_proche import est_plus_proche
from Liste_ingre_recette import donne_liste_ingre_issus_recette
import jaro
#pip install jaro-winkler
from jaro import jaro_winkler_metric as jwm

# import fichier recette.csv
CSV_FILE = r"C:\Users\virgi\Desktop\AGRAL\AGRAL4\Informatique\Projet base données2\recettes.csv"
SEPARATOR = " "
df = pd.read_csv(CSV_FILE,sep=SEPARATOR)  # on a besoin de encoding??, encoding='utf_8')#latin-1')  # endocing permet éviter erreur ("UnicodeDecodeError: 'utf-8' codec...)"and to ignore the byte#dtype=np.dtype('unicode') inutile

# import fichier liste_alim
CSV_FILE2 = r"C:\Users\virgi\Desktop\AGRAL\AGRAL4\Informatique\Projet base données2\Table_CIQUAL_reduite2.10.xlsx"
SEPARATOR2 = "\t"
df2 = pd.read_excel(CSV_FILE2)

# après import de donne_liste_recette de Part1
li = donne_liste_recette()  # pour importer li

# objectif : regarder si les ingrédients des recettes sont dans la liste des ingré

liste_ingre_issus_recette = []
liste_alim_avec_s = ['champignon de paris', 'maïs', 'anchois', 'fromage frais', 'fois gras', 'fromage de chèvre frais',
                     'saumon frais']

#but de la fonction : créer un dictionnaire qui prend en clé le nom des ingrédients issus des recettes et en valeur le nom de ces ingrédients mais dans table_ciquel
def dic_alim_correspondance():
    # on récupère la liste totale des ingrédients contenue dans les recettes
    liste_ingre_issus_recette = donne_liste_ingre_issus_recette()

    dic_alim_similaire = {}
    # pour faire la liste des correspondandes entre ingrédients et les noms des aliments dans recettes
    for i in range(len(liste_ingre_issus_recette)):
        nom_plus_proche = '' #va prendre le nom de l'ingrédient le plus proche de celui liste_ingre_issus_recette[i] cad de l'ingré écris dans les recettes
        valeur_nom_plus_proche = 0
        for j in range(len(df2['alim_nom_fr'])):

            if est_plus_proche(valeur_nom_plus_proche, liste_ingre_issus_recette[i], df2['alim_nom_fr'][j])[0]:
                            valeur_nom_plus_proche= est_plus_proche(valeur_nom_plus_proche, liste_ingre_issus_recette[i], df2['alim_nom_fr'][j])[1]
                            nom_plus_proche = df2['alim_nom_fr'][j]

        dic_alim_similaire[liste_ingre_issus_recette[i]] = nom_plus_proche
    return dic_alim_similaire

dic_alim_corresp = dic_alim_correspondance()
print(dic_alim_corresp)

# vérifie que tous les ingrédients des recettes soient dans la liste d'ingrédients original
p=0
for i in range(len(liste_ingre_issus_recette)):
    if liste_ingre_issus_recette[i] not in dic_alim_corresp:
        print(liste_ingre_issus_recette[i])
        p=p+1
print(p)



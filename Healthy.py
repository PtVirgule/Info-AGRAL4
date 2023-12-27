import pandas as pd
from Part1 import donne_liste_recette
from Correspondance_ingredient2 import dic_alim_correspondance


# import fichier liste_alim
CSV_FILE2 = r"C:\Users\virgi\Desktop\AGRAL\AGRAL4\Informatique\Projet base données2\Table_CIQUAL_reduite2.10.xlsx"
SEPARATOR2 = "\t"
df2 = pd.read_excel(CSV_FILE2)


li = donne_liste_recette()
dic_alim_corresp = dic_alim_correspondance()
# remplir dictionnaire qui prend en valeur le nom des ingédients à ajouter en nombre ( 1 oeuf) et sa correspondance en poids : la velur en poids sera toujours pour une unite
dic_corresp_poids = {'Oeuf': 55, ' Oeuf': 55, 'Pain burger': 330, 'Pain de mie': 35, 'Citron': 90, 'Nori': 3,
                     ' Saucisse de Francfort': 70, 'Oeuf dur': 55, 'Vanille': 6,
                     'Tortilla souple (à garnir). à base de blé': 92, "Jaune d'oeuf": 20,
                     'Avocat': 200, 'Citron vert': 90, 'Jambon cru': 80, 'Banane': 120, 'Orange': 150, "Pomme": 145,
                     "Kiwi": 100, "Saucisse": 50, 'Pâte brisée': 250, 'Pâte sablée': 265, 'Escargots': 30,
                     'Escargot': 30,
                     'Pâte à pizza': 250, 'Pâte à pizza cuite': 250, 'Escalope de poulet': 170, 'Confit de canard': 260,
                     'Citron confit': 90,
                     'Pâte feuilletée': 250}


# les noms de certains ingédients dans dic_alim_correspondance ne vont pas
# !!!!
def est_healthy(nom_recette):
    index_recette = -1
    nombre_kcal_energie = 0
    #faut mettre +1 à len(li)??
    for i in range(1, len(li)):  # len(li) prend les valeur 1 à 271 pour correspondre aux valeur dans table_ciqual
        if nom_recette == li[i].nom_recette:
            index_recette = i
            break
    # print(index_recette)
    if index_recette != -1:
        for i in range(len(li[index_recette].ingredient)):
            # on définit quantite_energie une variable qui prend la quantité d'énergie pour 100g de l'aliment i
            quantite_energie = li[index_recette].ingredient[i].quantite
            if li[index_recette].ingredient[i].unite != 'g' and li[index_recette].ingredient[i].unite != 'ml' and \
                    li[index_recette].ingredient[i].unite != '.':
                # print(li[index_recette].ingredient[i].nom)
                # print(dic_alim_corresp[li[index_recette].ingredient[i].nom])
                # print(dic_corresp_poids[dic_alim_corresp[li[index_recette].ingredient[i].nom]])
                quantite_energie = dic_corresp_poids[dic_alim_corresp[li[index_recette].ingredient[i].nom]] * int(
                    li[index_recette].ingredient[i].quantite)
                # print(quantite_energie)
                # print(type(quantite_energie))
            nombre_kcal_energie = nombre_kcal_energie + float(quantite_energie) * (
                float(df2['Energie. Règlement UE N° 1169/2011 (kcal/100 g)'][i] / 100))
            # print(str(li[index_recette].ingredient[i]) + " quantite: " + str(li[index_recette].ingredient[i].quantite))
            # print(str(li[index_recette].ingredient[i]) + "   kcal  : " + str(df2['Energie. Règlement UE N° 1169/2011 (kcal/100 g)'][i]))
        # print(nombre_kcal_energie)
        if nombre_kcal_energie > 475:
            return False
        else:
            return True
    else:
        return "Cette recette n'existe pas"


# Faire les listes liste_recette_healthy et liste_recette_non_healthy
liste_recette_non_healthy = []
liste_recette_healthy = []
for i in range(len(li)):
    if est_healthy(li[i].nom_recette):
        liste_recette_healthy.append(li[i].nom_recette)
    else:
        liste_recette_non_healthy.append(li[i].nom_recette)
#print(liste_recette_non_healthy)
#print(liste_recette_healthy)

# Affichage et calcul du nombre de recette dans chaque catégorie
compte_helthy = 0
compte_non_healthy = 0
for i in range(len(li)):
    if est_healthy(li[i].nom_recette):
        compte_helthy += 1
    else:
        compte_non_healthy += 1
#print("Nb recette healthy : " + str(compte_helthy))
#print("Nb recette Normale / Non healthy : " + str(compte_non_healthy))

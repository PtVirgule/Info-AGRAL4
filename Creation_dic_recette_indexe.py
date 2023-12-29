from Part1 import donne_liste_recette
from Correspondance_ingredient2 import dic_alim_correspondance

# TODO créer ce fichier sur git

liste_ingre = [' Champignons', 'Tofu', 'Poulet', ' Riz basmati cuit']

li = donne_liste_recette()
dic_alim_corresp = dic_alim_correspondance()
dic_indexe = {}


def modif_liste_ingre(
        liste_ingre):  # liste qui a pour but de prendre la liste des ingré voulu par l'utilisateur et de lui ajouter l'ensemble des écritures possibles des ingrédients
    lis = liste_ingre
    for ingred in lis:
        for cle, val in dic_alim_corresp.items():
            if dic_alim_corresp[ingred] == val:
                if cle not in lis:
                    lis.append(cle)
    return lis


def donne_new_valeur_dic(valeur_dic, nom_recette):
    li_recette = []
    if len(valeur_dic) > 1:
        for i in valeur_dic:
            li_recette.append(i)
    else:
        li_recette.append(valeur_dic[0])
    li_recette.append(nom_recette)
    return li_recette

def donne_dico_index(liste_ingre, li):  # où li est la liste globale contenant toutes les recettes
    #print(liste_ingre)
    liste_ingre = modif_liste_ingre(liste_ingre)
    print(liste_ingre)
    for i in li:  # i est la recette n°i
        compte_ingre_compris = 0
        for j in i.ingredient:  # on regarde pour chaque ingrédient de la recette
            if j.nom in liste_ingre:  # s'il est dans dans la liste d'ingré voulu
                compte_ingre_compris = compte_ingre_compris + 1
                # print(compte_ingre_compris)
        # on ne veut garder que les recettes qui ont un compte_ingre_compris >0:
        if compte_ingre_compris > 0:
            # pour ajouter la recette à dic_indexe, il faut regarder si une recette avait déjà l'indice compte_ingre_compris comme clé dans dic_indexe
            if compte_ingre_compris in dic_indexe.keys():
                dic_indexe[compte_ingre_compris] = donne_new_valeur_dic(dic_indexe[compte_ingre_compris], i.nom_recette)
                # print(dic_indexe)
            else:
                dic_indexe[compte_ingre_compris] = [i.nom_recette]
    return dic_indexe


#donne_dico_index(liste_ingre, li)

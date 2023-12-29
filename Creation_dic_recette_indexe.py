from Part1 import donne_liste_recette
from Correspondance_ingredient2 import dic_alim_correspondance
from Regim_alim import regim_liste_alimentaire

liste_ingre = [' Courgette', ' Oeuf', ' Chorizo']
#liste_ingre = [' Champignons', 'Tofu', 'Poulet', ' Riz basmati cuit']
liste_intolerence=['Aubergine']

li = donne_liste_recette()
dic_alim_corresp = dic_alim_correspondance()
dic_indexe = {}


def modif_liste_ingre(liste_ingre):  # liste qui a pour but de prendre la liste des ingré voulu par l'utilisateur et de lui ajouter l'ensemble des écritures possibles des ingrédients

    lis = liste_ingre
    if len(liste_ingre) > 1:  # permet de tester si liste_ingre contient plus d'un element
        for ingred in lis:
            for cle, val in dic_alim_corresp.items():
                if dic_alim_corresp[ingred] == val :
                    #print(ingred)
                    if cle not in lis:
                        lis.append(cle)
    elif len(liste_ingre) == 1:  # si liste_ingre contient un unique element
        for cle, val in dic_alim_corresp.items():
            if dic_alim_corresp[liste_ingre[0]] == val:
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

def donne_dico_index(liste_ingre, li,list_intolerence):  # où li est la liste globale contenant toutes les recettes
    #print(liste_ingre)
    liste_ingre = modif_liste_ingre(liste_ingre)
    #print(liste_ingre)
    for i in li:  # i est la recette n°i
        print(i.nom_recette)
        print(regim_liste_alimentaire(list_intolerence))
        if i.nom_recette+',' not in regim_liste_alimentaire(list_intolerence) :##TODO supprimer les virgules et donc ','
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
        else :
            print('heyyyyy')
            print(i.nom_recette)
            print('heyyy')
    print(dic_indexe)
    return dic_indexe


#donne_dico_index(liste_ingre, li,liste_intolerence)

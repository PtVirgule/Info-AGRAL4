import random
from Healthy import est_healthy
from Creation_dic_recette_indexe2 import donne_dico_index
from Part1 import donne_liste_recette

# dic = {1: ['Salade', 'Pizza'], 2: ['Mayonnaise', 'Gnockie', 'Cookie'], 3: ['Repas']}
# dic2 = {1: ['Pizza Végétarienne'], 2: ['Salade', 'Pizza'], 3: ['Bruschetta', 'Quiche aux Légumes'], 4: ['Potage de Légumes']}


liste_ingre = [' Champignons', 'Tofu', 'Poulet', ' Riz basmati cuit','Quinoa']
li = donne_liste_recette()


def donne_liste_cle(cle_dico):
    li_cle = []
    for cle in cle_dico:
        li_cle.append(cle)
    return li_cle


def donne_cle_max(liste_cle):
    if not (liste_cle):  # cas où la liste est vide
        return -1
    else:
        # trouver l'élement max d'une liste
        max_liste = liste_cle[0]
        for i in liste_cle:
            if max_liste < i:
                max_liste = i
        return max_liste


def est_complet_liste_retour(lis):
    if len(lis) == 0:
        return False
    else:
        if len(lis[0]) == 0 or len(lis[1]) == 0: #cas où un des élements de la liste est vide donc qu'il n'y a pas de proposition d'un type de recette (healthy / non helthy)
            return False
        else:
            return True

# mettre à jour : donne_compte_recette + healthy
def donne_bon_compte_recette(dic):
    compte_recette = []
    liste_cle = donne_liste_cle(dic.keys())

    liste_recette_ingre_healthy = []
    liste_recette_ingre_non_healthy = []
    while est_complet_liste_retour(
            compte_recette) == False and donne_cle_max(liste_cle) != -1:  # tant qu'on n'a pas au moins 1 recette healthy et non healty
        # but récuperer liste des clé (pour ensuite trouver la clé max)
        # si il n'y a plus de clé cad le dictionnaire est à nouveau vide :
        if len(dic) == 0:
            return [0, 0]
        else:
            indice_max = donne_cle_max(liste_cle)

        # remplir la liste des recettes avec les recettes ayant l'indice indice_max
        for i in range(len(dic[indice_max])):
            if est_healthy(dic[indice_max][i]):
                liste_recette_ingre_healthy.append(dic[indice_max][i])
            else:
                liste_recette_ingre_non_healthy.append(dic[indice_max][i])
        liste_cle.remove(indice_max)  # permet de retirer la valeur clé la plus elevé
        print(liste_recette_ingre_healthy)
        print(liste_recette_ingre_non_healthy)
        # algo qui va remplir compte_recette
        if len(liste_recette_ingre_healthy) < 2:
            if len(liste_recette_ingre_non_healthy) < 2:
                compte_recette = (liste_recette_ingre_healthy, liste_recette_ingre_non_healthy)
            else:
                compte_recette = (liste_recette_ingre_healthy, random.sample(liste_recette_ingre_non_healthy, 2))
        else:
            if len(liste_recette_ingre_non_healthy) < 2:
                compte_recette = (random.sample(liste_recette_ingre_healthy, 2), liste_recette_ingre_non_healthy)
            else:
                compte_recette = (random.sample(liste_recette_ingre_healthy, 2),
                                  random.sample(liste_recette_ingre_non_healthy, 2))
        print('compte recette')
        print(compte_recette)
    return compte_recette


print(donne_bon_compte_recette(donne_dico_index(liste_ingre, li)))

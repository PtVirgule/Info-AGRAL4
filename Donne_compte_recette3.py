import random
from Healthy import est_healthy
from Creation_dic_recette_indexe4 import donne_dico_index
from Part1 import donne_liste_recette

liste_ingre = [' Courgette', ' Oeuf', ' Chorizo']
liste_intolerence=['Aubergine']



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
        if len(lis[0]) == 0 or len(lis[1]) == 0:  # cas où un des élements de la liste est vide donc qu'il n'y a pas de proposition d'un type de recette (healthy / non helthy)
            return False
        else:
            return True


def modif_compte_recette(compte_recette, liste_recette_ingre_healthy, liste_recette_ingre_non_healthy):
    if len(compte_recette) == 0:
        compte_recette = [[], []]
    for liste_recette in (liste_recette_ingre_healthy,
                          liste_recette_ingre_non_healthy):  # permet de ne faire qu'une boulce pour healthy et non healthy
        if liste_recette == liste_recette_ingre_healthy:
            index = 0
        else:
            index = 1
        if len(liste_recette) >= 2:
            if not compte_recette[index]:  # equivaut à faire == []
                compte_recette[index] = random.sample(liste_recette, 2)
            if len(compte_recette[index]) == 1:
                compte_recette[index].append(random.sample(liste_recette, 1)[0])

        elif len(liste_recette) == 1:
            if not compte_recette[index]:  # equivaut à faire == []
                compte_recette[index] = liste_recette[0]
            if len(compte_recette[index]) == 1:
                compte_recette[index].append(liste_recette[0])

    return compte_recette




def donne_bon_compte_recette(liste_ingre,liste_intolerence):
    li = donne_liste_recette()
    dic = donne_dico_index(liste_ingre, li,liste_intolerence)
    compte_recette = []
    liste_cle = donne_liste_cle(dic.keys())


    while est_complet_liste_retour(
            compte_recette) == False and donne_cle_max(
        liste_cle) != -1:  # tant qu'on n'a pas au moins 1 recette healthy et non healty

        liste_recette_ingre_healthy = []
        liste_recette_ingre_non_healthy = []

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
                print(dic[indice_max][i])
        liste_cle.remove(indice_max)  # permet de retirer la valeur clé la plus elevé

        # algo qui va remplir compte_recette
        compte_recette = modif_compte_recette(compte_recette,liste_recette_ingre_healthy,liste_recette_ingre_non_healthy)

    return compte_recette

print(donne_bon_compte_recette(liste_ingre,liste_intolerence))
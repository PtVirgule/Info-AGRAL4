import random
from Healthy import est_healthy

dic = {1: ['Salade', 'Pizza'], 2: ['Mayonnaise', 'Gnockie', 'Cookie'], 3: ['Repas']}
dic2 = {1: ['Pizza Végétarienne']}

# il faur prendre en compte que els recettes sont classées par quantité d'ingrédients souhaités : faut mettre dans
# liste tot_ingre_healthy que les recetees avec l'index max (et si le compte est trop faible prendre celui d'aant
# aussi))

#mettre à jour : donne_compte_recette + healthy
def donne_bon_compte_recette(dic):
    print(dic.keys())
    # Cas où le dictionnaire es vide
    if len(dic) == 0:
        return [0, 0]
    else:  # cas où le dictionnaire contient au moins 1 recette
        # On compte le nombre de recette totale dans le dictionnaire
        nombre_tot_recette_possible = 0
        for i in dic.keys():
            nombre_tot_recette_possible += len(dic[i])
        print(nombre_tot_recette_possible)
        liste_recette_ingre_healthy = []
        liste_recette_ingre_non_healthy = []
        for i in dic.keys():  # sachant que dans ce cas il y a une seule clé
            if est_healthy(dic[i]):
                liste_recette_ingre_healthy.append(dic[i])
            else:
                liste_recette_ingre_non_healthy.append(dic[i])
        if len(liste_recette_ingre_healthy) < 2:
            if len(liste_recette_ingre_non_healthy) < 2:
                return liste_recette_ingre_healthy, liste_recette_ingre_non_healthy
            else:
                return liste_recette_ingre_healthy, random.sample(liste_recette_ingre_non_healthy, 2)
        else:
            if len(liste_recette_ingre_non_healthy) < 2:
                return random.sample(liste_recette_ingre_healthy, 2), liste_recette_ingre_non_healthy
            else:
                return (
                random.sample(liste_recette_ingre_healthy, 2), random.sample(liste_recette_ingre_non_healthy, 2))


print(donne_bon_compte_recette(dic2))

import pandas as pd
from Creation_dic_recette_indexe2 import modif_liste_ingre

##TODO créer ce doc sur git
##TODO avancer fichier

# import fichier recette.csv
CSV_FILE = r"C:\Users\virgi\Desktop\AGRAL\AGRAL4\Informatique\Projet base données2\recettes.csv"
SEPARATOR = " "
df = pd.read_csv(CSV_FILE, sep=SEPARATOR, header=(
    0))  # on a besoin de encoding??, encoding='utf_8')#latin-1')  # endocing permet éviter erreur ("UnicodeDecodeError: 'utf-8' codec...)"and to ignore the byte#dtype=np.dtype('unicode') inutile

# import fichier liste_alim
CSV_FILE2 = r"C:\Users\virgi\Desktop\AGRAL\AGRAL4\Informatique\Projet base données2\Table_CIQUAL_reduite2.10.xlsx"
SEPARATOR2 = "\t"
df2 = pd.read_excel(CSV_FILE2)


# on veut que liste_intolerence contienne juste "Végé, lactose,oeuf, ingré précis ou ..
def regim_alim(liste_intolerence):
    liste_intolerence_modif = []
    print(liste_intolerence)
    print(type(liste_intolerence))
    # faire boucle sur liste_intolerence qui remplira une liste_intolerence selon si c'est fruit à coque ou directement oeuf
    for i in liste_intolerence:
        print(i)
        if i == 'Végé': # faut ajouter tous ce qui a de la viande, poisson
            liste_interdit_vege = ['autres produits à base de viande','substitus de produits carnés','viandes crues','viandes cuites','charcuteries et assimilés','poissons cuits','mollusques et crustacés crus','poissons crus']
            for categorie in liste_interdit_vege:
                liste_intolerence_modif.extend(df2.loc[(df2['alim_grp_nom_fr'] == categorie)]['alim_nom_fr'])
        if i == 'Oeuf':
            liste_intolerence_modif.extend(['Oeuf', ' Oeuf'])
        if i == 'Arachide':
            liste_intolerence_modif.append("cacahouète")
        if i == 'Fruits_a_coques':
            liste_intolerence_modif.extend([' Cacao', ' Noix', ' Amandes'])
        if i == 'Lactose':
            liste_intolerence_modif.extend([' Crème fraîche', ' Lait', 'Lait'])
            liste_intolerence_modif.extend(df2.loc[(df2['alim_ssssgrp_nom_fr'] == 'fromages blancs')]['alim_nom_fr'])
            liste_intolerence_modif.extend(
                df2.loc[(df2['alim_ssssgrp_nom_fr'] == 'fromages à pâte molle')]['alim_nom_fr'])
            liste_intolerence_modif.extend(
                df2.loc[(df2['alim_ssssgrp_nom_fr'] == 'autres fromages et spécialités')]['alim_nom_fr'])
            liste_intolerence_modif.extend(df2.loc[(df2['alim_ssssgrp_nom_fr'] == 'fromage fondus')]['alim_nom_fr'])
            liste_intolerence_modif.extend(
                df2.loc[(df2['alim_ssssgrp_nom_fr'] == 'fromages à pâte pressée')]['alim_nom_fr'])
        else : #cas d'un ingrédient précis
            print(i)
            liste_ecriture = modif_liste_ingre(i) # liste qui va prendre l'ensemble des écritures possibles de cet ingrédient
            liste_intolerence_modif.extend(liste_ecriture)

    #boucle qui va recencer toutes les recettes qui contiennent les ingrédients
    liste_recette_contenant_intolerance = []
    for ingre in liste_intolerence_modif:
        for i in range(len(df['Ingredients,'])):
            if ingre in df['Ingredients,'][i]:
                if df['Titre,'][i] not in liste_recette_contenant_intolerance : # permet d'ajouter de manière unique les recettes
                    liste_recette_contenant_intolerance.append(df['Titre,'][i])

    return liste_recette_contenant_intolerance


"""
       Végé?
       Oeuf
        if regime == 'cachuete':
            for j in range(len(df['Ingredients,'])):
                if "cachuete" in df['Ingredients,'][j]:
                    liste_recette_contenant_intolerance.append(df['Titre,'][j])
        if regime == 
    for k in range(len(df['Ingredients,'])):
        if "Cacao" in df['Ingredients,'][k] or "Amandes" in df['Ingredients,'][k] or "Noix" in df['Ingredients,'][k]:
            fruits_coques.append(df['Titre,'][k])
            # print(df['Titre,'][i])
    # print(fruits_coques)

    for l in range(len(df['Ingredients,'])):
        if "Crème fraîche" in df['Ingredients,'][l] or "Lait" in df['Ingredients,'][l] or "Fromage" in \
                df['Ingredients,'][
                    l] or "Mozzarella" in df['Ingredients,'][l] or "Gorgonzola" in df['Ingredients,'][
            l] or "Parmesan" in \
                df['Ingredients,'][l] or "Cheddar" in df['Ingredients,'][l] or "Crème liquide" in df['Ingredients,'][
            l] or "Beurre" in df['Ingredients,'][l] or "Emmental" in df['Ingredients,'][l]:
            lactose.append(df['Titre,'][l])

    # print(lactose)

    # il va falloir demander à l'utilisateur un ingrédient auquel il est allergique

"""

regim_alim(['Végé','Oeuf', ' Cheddar'])
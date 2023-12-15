# liste en fonction des régimes alimentaire
# Attention importer le doc ou changer le chemin

import pandas as pd

#CSV_FILE = "recettes.csv"
CSV_FILE = r"C:\Users\virgi\Desktop\AGRAL\AGRAL4\Informatique\Projet base données2\recettes.csv"
SEPARATOR = " "
df = pd.read_csv(CSV_FILE, sep=SEPARATOR)


# Création des listes avec allergènes
oeuf = []
arachide = []
fruits_coques = []
lactose = []
ingred_precis = []

for i in range(len(df['Ingredients,'])):
    if "Oeuf" in df['Ingredients,'][i]:
        oeuf.append(df['Titre,'][i])
# print(oeuf)

for j in range(len(df['Ingredients,'])):
    if "cachuete" in df['Ingredients,'][j]:
        arachide.append(df['Titre,'][j])
# print(arachide)

for k in range(len(df['Ingredients,'])):
    if "Cacao" in df['Ingredients,'][k] or "Amandes" in df['Ingredients,'][k] or "Noix" in df['Ingredients,'][k]:
        fruits_coques.append(df['Titre,'][k])
        # print(df['Titre,'][i])
# print(fruits_coques)


for l in range(len(df['Ingredients,'])):
    if "Crème fraîche" in df['Ingredients,'][l] or "Lait" in df['Ingredients,'][l] or "Fromage" in df['Ingredients,'][
        l] or "Mozzarella" in df['Ingredients,'][l] or "Gorgonzola" in df['Ingredients,'][l] or "Parmesan" in \
            df['Ingredients,'][l] or "Cheddar" in df['Ingredients,'][l] or "Crème liquide" in df['Ingredients,'][
        l] or "Beurre" in df['Ingredients,'][l] or "Emmental" in df['Ingredients,'][l]:
        lactose.append(df['Titre,'][l])


# print(lactose)

# il va falloir demander à l'utilisateur un ingrédient auquel il est allergique
def donne_liste_ingred_precis(nom_ingred):
    for m in range(len(df['Ingredients,'])):
        if nom_ingred in df['Ingredients,'][m]:
            ingred_precis.append(df['Titre,'][m])
    return ingred_precis


donne_liste_ingred_precis("")

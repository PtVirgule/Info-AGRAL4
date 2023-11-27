import pandas as pd

# import fichier liste_alim
CSV_FILE2 = r"C:\Users\virgi\Desktop\AGRAL\AGRAL4\Informatique\Projet base données2\Table_CIQUAL_reduite2.10.xlsx"
SEPARATOR2 = "\t"
df2 = pd.read_excel(CSV_FILE2)


def donne_liste_ingre_issus_CIQUAL():
    li_ingre_CIQUAL=[]
    for i in range(len(df2['alim_nom_fr'])):
        li_ingre_CIQUAL.append(df2['alim_nom_fr'][i])
    return li_ingre_CIQUAL


print(donne_liste_ingre_issus_CIQUAL())
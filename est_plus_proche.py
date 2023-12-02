#pip install jaro-winkler
from jaro import jaro_winkler_metric as jwm

def est_plus_proche(valeur_nom_plus_proche,nom1debase,nom2) :
    alors = False
    if valeur_nom_plus_proche < jwm(nom1debase, nom2):
        alors = True
        valeur_nom_plus_proche = jwm(nom1debase, nom2)


    return((alors, valeur_nom_plus_proche))

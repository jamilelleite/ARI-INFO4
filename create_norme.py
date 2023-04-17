# TP2, Exercice 7: Pour préparer le traitement des requêtes,
# il vous est demandé de rajouter, lors du traitement de 
# chaque document le calcul de la norme du vecteur suivant 
# la pondération tf.idf : il est calculé par la racine carrée 
# de la somme des carrées des valeurs (cest-à-dire tf.idf) 
# de chaque dimension du vecteur (se baser sur la question 5). 
# Ici encore, un dictionnaire est utilisable, avec comme clé 
# l'identifiant de document, et en valeur la norme calculée. 
# On calcule donc bien une valeur par document. Vous devrez 
# stocker ce fichier sur disque dans un autre fichier au 
# format json. Se baser sur la représentation construite en 
# question 5.

from create_vecteur import vecteur_doc
from math import sqrt
import json

def NormalisationVecteur(vecteur):
    vec_norm = {}
    # On boucle sur le vecteur orignal
    for doc, tokens in vecteur.items():
        count = 0
        # Pour chaque token, on increment le counter
        # avec la valeur carrée
        for value in tokens.values():
            count += value*value
        # On calcule la racine carrée
        count = sqrt(count)
        # On ajoute la valeur correspondante pour le fichier
        vec_norm[doc] = count

    return vec_norm

vec_norm = NormalisationVecteur(vecteur_doc)
json_object = json.dumps(vec_norm, indent=4)
with open("vecteur_normalise.json", "w") as outfile:
    outfile.write(json_object)
print(vec_norm)
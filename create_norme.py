from create_vecteur import vecteur_doc
from math import sqrt
import json

def NormalisationVecteur(vecteur):
    vec_norm = {}
    for doc, tokens in vecteur.items():
        count = 0
        for value in tokens.values():
            count += value*value
        count = sqrt(count)
        vec_norm[doc] = count

    return vec_norm

vec_norm = NormalisationVecteur(vecteur_doc)
json_object = json.dumps(vec_norm, indent=4)
with open("vecteur_normalise.json", "w") as outfile:
    outfile.write(json_object)
print(vec_norm)
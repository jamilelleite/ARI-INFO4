# TP2, Exercice 5: Écrire une fonction qui construit la 
# représentation vectorielle (au sens RI) de chaque 
# document, d'après le modèle vectoriel de Salton vu en 
# cours. Le type de représentation choisi est : tf.idf. 
# (on pose donc que nd=1 (cf. transparent 23)). Ici en 
# fait on modifie votre code de la question 5 du TP de 
# Zipf en générant un dictionnaire par document.
#
# La différence par rapport à la question 5 du TP Zipf est 
# que l'on stocke pour chaque document un dictionnaire de 
# couples (terme, tf.idf du terme dans d). Ici encore, 
# l'idée est de passer document par document : 1.) 
# calculer le tf de tous les termes présents (c'est la 
# question 5 du TP Zipf), et 2.) multiplier ces tf par 
# l'idf stockés dans le vocabulaire (cf. question 4').
# 
# Nous obtenons donc, un “gros” dictionnaire qui stocke 
# tous les “vecteurs” au sens recherche d'information 
# (des dictionnaires python) de documents, avec 
# l'identifiant de document comme clé et la représentation 
# de son vecteur comme valeur.

import os
import json
from create_dict import dict_freq

inppathname = "./files/collection_tokens/"
vocabpath = "./vocabulaire.json"

def RepresentationVectorielle(inpath, vocabpath, freq_dict):
    vecteur_doc = {}
    with open(vocabpath) as json_input:
        vocab = json.load(json_input)

    for doc_key, doc_value in freq_dict.items():
        vecteur_doc[doc_key] = {}
        for token in doc_value:
            vecteur_doc[doc_key][token] = vocab[token][1] * freq_dict[doc_key][token]

    # dict qui a comme clé le nom du document e comme valeur
    # un dict avec ses terms e le tf.idf
    return vecteur_doc

vecteur_doc = RepresentationVectorielle(inppathname, vocabpath, dict_freq)
if __name__ == "__main__":

    print("Affichage:")
    print(vecteur_doc)
    print(vecteur_doc["CACM-2439"])
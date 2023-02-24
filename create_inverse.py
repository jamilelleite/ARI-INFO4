# TP2, Exercice 6:   Indication : utiliser encore une fois 
# un dictionnaire pour stocker cet index en mémoire, et le
# sauver dans un fichier json (utiliser la fonction dump de
#  la library json). Dans ce cas, le dictionnaire a comme 
# clé le terme, et comme contenu un autre dictionnaire 
# ayant comme clé l'identifiant du document et la valeur 
# tf.idf du terme dans le documemt. On a donc un 
# dictionnaire de : [terme: [ document: valeur tf.idf]] .
# L'intérêt d'un tel dictionnaire est qu'il permet de se 
# passer du tri des paires (terme,doc) (cf. transparent 
# 28 du cours).


from create_vecteur import vecteur_doc
from create_vocabulaire import vocabulaire
import json

def IndexInverse(vecteur, vocab):
    ind_inv = {}
    for token in vocab:
        ind_inv[token] = {}
        for doc, terms in vecteur.items():
            if token in terms:
                ind_inv[token][doc] = vecteur[doc][token]

    # dict qui a comme clé le term e comme valeur les documents
    # avec le tf.idf
    return ind_inv

index_inverse = IndexInverse(vecteur_doc, vocabulaire)
print(index_inverse)
json_object = json.dumps(index_inverse, indent=4)
with open("index_inverse.json", "w") as outfile:
    outfile.write(json_object)
# TP2, Exercice 3: Construire le vocabulaire associé à 
# cette collection en considérant tous les termes (tronqués) 
# qui apparaissent au moins une fois dans le corpus de 
# documents. Le résultat sera stocké dans un fichier 
# “vocabulaire.json”. Utilisez encore un dictionnaire 
# python qui, pour chaque terme (la clé), stocke la 
# valeur 0 (on est ici assez proche du TP sur la loi de 
# Zipf). On a deux solutions pour ce problème : soit on 
# passe en revue les fichiers (comme pour le TP Zipf), 
# soit on reprend la structure générée à la question 2.

# TP2, Exercice 4: Calculer le df_i pour chaque terme t_i 
# du vocabulaire (en modifiant le code de la questuion 3) 
# et stocker le résultat dans le fichier “vocabulaire.json”. 
# Par rapport à la question précédente, il suffit de stocker 
# le df_i (c'est-à-dire le nombre de documents dans lequel il 
# apparaît) dans la valeur associée au terme dans le 
# dictionnaire au lieu de 0. Ici, une solution est de créer 
# un “petit” vocabulaire (dictionnaire python) lié au 
# document que l'on traite, en mettant uniquement 1 pour 
# valeur, puis une fois le document traité on passe en revue 
# ce petit dictionnaire et on met à jour le grand dictionnaire 
# créé en question 3.

# TP2, Exercice 4: A partir du dictionnaire qui contient 
# les df_i en question 4, on le met à jour pour stocker 
# les valeurs idf_i. Pour calculer l'idf_i, qui utilise 
# les df_i des termes c'est à dire qu'on applique la 
# formule “idf_i = ln(N/df_i)”.

import json
from math import *
from create_dict import dict_freq

def CreateVocab(freq_dict):
    vocab = {}
    n_doc = len(freq_dict)
    for file in freq_dict.values():
        freq = file
        for token in freq:
            if token not in vocab:
                vocab[token] = [0]
    
    for word in vocab:
        for freq in freq_dict.values():
            if word in freq:
                vocab[word][0] += 1
        vocab[word].append(log(n_doc/vocab[word][0]))

    # Vocabulaire du corpus, chaque couple dans le dict
    # a comme clé le mot e comme valeur une list avec
    # le df_i (document frequency, quantité de
    # documents dans lequel il apparait) et idf_i (inverse
    # document frequency, ln(N/df_i), avec N = taille vocab)
    return vocab
vocabulaire = CreateVocab(dict_freq)
json_object = json.dumps(vocabulaire, indent=4)
with open("vocabulaire.json", "w") as outfile:
    outfile.write(json_object)
if __name__ == "__main__":
    print(vocabulaire)
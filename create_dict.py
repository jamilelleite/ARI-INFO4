# Continuation Zipf.py

# TP1, Exercice 5: Générer dictionnaire python qui contient comme clé le 
# nom de fichier, et comme valeur un autre dictionnaire qui 
# contient, comme pour votre code Zipf, les mots qui 
# apparaissent dans ce fichier avec leur nombre d'occurrence.
# Afficher ce dictionnaire pour vérifier les calculs.

# TP2, Exercice 1: Écrire une fonction qui reprend la 
# question 5 du TP Zipf: il ouvre les fichiers CACM-XX.tok 
# un à un et qui applique l'anti-dictionnaire qui est dans 
# le fichier common-words (cf. TP Zipf) sur les mots “en 
# minuscule” (en ne prenant pas en compte les termes de 
# ces fichiers qui y apparaissent). Le résultat du filtrage 
# sera mis dans le dictionnaire créé en question 5 du 
# TP Zipf.

# TP2, Exercice 2: Reprendre la question 1 en ajoutant, à 
# la suite du traitement de l'anti-dictionnaire, le fait 
# que l'on tronque les termes en utilisant la troncature 
# de Porter de la librarie nltk.

import os
from nltk.stem.porter import *

tokenspathname = "./files/collection_tokens/"
antipathname = "./files/common_words"

stemmer = PorterStemmer()

def createAntiDict(antipath):
    anti_dict = {}
    fileHandler = open(antipath, "r")

    for word in fileHandler:
        if word not in anti_dict:
            anti_dict[word.strip()] = 1
    
    return anti_dict

def FreqWordsFile(tokenspath, anti_dict):
    dict_freq = {}
    for file in os.listdir(tokenspath):
        freq = {}
        fileHandler = open(tokenspath + file, "r")
        for line in fileHandler:
            line = stemmer.stem(line.strip())
            if line not in list(anti_dict.keys()):
                if line in freq:
                    freq[line] += 1
                else:
                    freq[line] = 1
        dict_freq[file[:-4]] = freq

    # Dictionnaire qui contient comme clé le nom de fichier,
    # et comme valeur un autre dictionnaire qui contient, comme
    # pour Zipf, les mots qui apparaissent dans ce fichier avec
    # leur nombre d'occurence
    return dict_freq

anti_dict = createAntiDict(antipathname)
dict_freq = FreqWordsFile(tokenspathname, anti_dict)

if __name__ == "__main__":

    for key in dict_freq:
        print(str(key) + ": " + str(dict_freq[key]))


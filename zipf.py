# TP1, Exercice 3: Écrire un programme python zipf.py qui, 
# à partir de tous les fichiers collection_tokens/CACM-XX.tok 
# créés à l'étape précédente : 1. calcule la fréquence 
# d'apparition de tous les termes de la collection 
# (utiliser un dictionnaire python avec la chaîne de 
# caractères comme clé et le nombre d'occurrences comme 
# valeur) et les affiche, 2. les affiche par nombre 
# d'apparition décroissant (affichage long, mais c'est 
# normal).

# TP1, Exercice 4: Modifier le code pour n'afficher QUE 
# les 10 termes les plus fréquents dans l'ordre décroissant, 
# puis ajouter a) l'affichage du nombre d'occurrences de 
# ces mots, b) la taille du vocabulaire (My du cours), et 
# c) la valeur lambda théorique calculée (cf. le cours). 
# (valeur de lambda attendue : +/- 18880).

import os

inppathname = "./files/collection_tokens/"

def FrequenceTokens(inpath):
    freq = {}

    # Calculus de la fréquence d'apparition de tous le termes
    # de la collection dans le corpus, sauvergadé dans dict
    # 'freq'
    for file in os.listdir(inpath):
        fileHandler = open(inpath + file, "r")
        for line in fileHandler:
            line = line.strip()
            if line in freq:
                freq[line] += 1
            else:
                freq[line] = 1
    # print("Affichage:")
    # for key in freq:
    #     print(key + ": " + str(freq[key]))

    # trie du dict par ordre decroissante de fréquence de mot
    sorted_freq = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))

    size = len(sorted_freq)
    count = 0
    # Affichage de frequence de termes avec leur valeur lambda
    # théorique calculée: 
    # lambda = fc(mot) * rang(mot)
    # fc: fréquence d'occurrence d'un mot
    # rang: position d'un mot dans ordonnance décroisssante
    for key in sorted_freq:
        count = count + 1
        if (count > 10):
            print("taille vocabulaire: " + str(size))
            break
        print(key + ": " + str(sorted_freq[key]))  
        lamb = sorted_freq[key]*count
        print("lambda: " + str(lamb))

FrequenceTokens(inppathname)



import json
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import *

stemmer = PorterStemmer()

tokenizer = RegexpTokenizer('[A-Za-z]\w{1,}')

with open("index_inverse.json") as file:
    index_inverse = json.load(file)
with open("vocabulaire.json") as file:
    vocabulaire = json.load(file)
with open("vecteur_normalise.json") as file:
    vecteur_normalise = json.load(file)


def ExtractionDesRequete(infile, antipath, vocab):
    fileHandler = open(infile, "r")
    #tokenization
    line = fileHandler.read()
    words = tokenizer.tokenize(line) #i think split works

    # anti dictionnaire
    anti_dict = {}
    dictHandler = open(antipath, "r")
    for word in dictHandler:
        if word not in anti_dict:
            anti_dict[word.strip()] = 1
    dictHandler.close()

    # vecteur requête avec pondération tf.idf
    vq = {}
    # calculus de tf - nombre d'occurrence du mot dans
    # la requête
    for word in words:
        if word not in anti_dict:
            word = stemmer.stem(word)
            if word not in vq:
                vq[word] = 1
            else:
                vq[word] += 1
    
    # Multiplier tf pour idf
    for term, tf in vq.items():
        # traiter les cas où le term n'est pas dans vocab:
        # enlever le mot de la requete, ajouter if else
        vq[term] = tf*vocab[term][1]

    fileHandler.close()

    return vq

vq = ExtractionDesRequete("requet.txt", "./files/common_words" , vocabulaire)
print(vq)

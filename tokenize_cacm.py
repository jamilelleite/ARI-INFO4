# TP 1, Exercice 2: Écrire un programme python tokenize_cacm.py, 
# qui ouvre un à un les fichiers CACM-XX du répertoire 
# “collection/” rempli à l'étape précédente (le répertoire 
# est passé en paramètre) et qui, pour chaque fichier, ne 
# garde que les mots qui commencent par une lettre et qui 
# ne contiennnent ensuite que des lettres ou des chiffres, 
# puis qui écrit le résultat (en minuscule, un mot par 
# ligne) dans un fichier portant le même nom que celui de 
# départ en y ajoutant l'extension .tok, dans un nouveau 
# répertoire (nom en paramètre), par exemple “collection_tokens/”, 
# à créer avant de lancer votre programme. Utiliser ici la 
# fonction Tokenizer décrite plus bas (partie 4).

from nltk.tokenize import RegexpTokenizer
import os

inppathname = "./files/collection/"
outpathname = "./files/collection_tokens/"

tokenizer = RegexpTokenizer('[A-Za-z]\w{1,}')

# Fonction qui prend chaque fichier CACM-XXX et ne garde que
# les mots, puis les écrit, chaque mot dans une ligne, dans 
# un noveau fichier correspondant "CACM-XXX.tok"
def TokenizeFichiers(inpath,outpath):
    for file in os.listdir(inpath):
        fileHandler = open(inpath +file, "r")

        text = fileHandler.read()

        words = tokenizer.tokenize(text)

        fileHandler.close()
        f = open(outpath + file + ".tok", "w+")
        for word in words:
            f.write(word.lower()+'\n')
        f.close()

TokenizeFichiers(inppathname, outpathname)

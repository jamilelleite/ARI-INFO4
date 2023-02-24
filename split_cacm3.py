# TP 1, Exercice 1: Repatriement et préparations des données:
# Vous devez commencer par rapatrier les données CACM et le 
# code fourni (cf. texte "La collection utilisée..." ci-dessous)
# puis modifier le programme cacm_splt.py qui contient la 
# fonction *ExtractionDesFichiers*, afin de découper le
# fichier cacm.all rapatriée en une liste de fichiers dans 
# un répertoire cible, par exemple "/...../collection/",
# que vous choisissez (il faut créer ce répertoire avant de
# lancer le code). Vérifier ensuite sur un ou deux fichiers
# exemples que le résultat est correct.

inpfilename = "./files/cacm.all"
outpathname = "./files/collection/"

# Fonction qui prend un fichier "cacm.all" et le découpe dans plusieurs fichers,
# chacun avec les données d'une publication "CACM-XXX"
def ExtractionDesFichiers(infile,outpath):
    fileHandler = open (infile, "r")
    debut = True
    # Boucle pour lire toutes lignes dans fichiet
    while True:
        # en lisant fichier ligne par ligne
        line = fileHandler.readline()
        # sortie du boucle quand plus de ligne à lire
        if not line :
            break
        #print 'XXXXX',line[:-1]
        if line[0:2] == '.I':
            if not debut:
                f.close()
            debut = False
            a,b = line.split(" ")
            print ('processing file CACM-',b[:-1],sep="")
            f = open(outpath+"CACM-"+b[:-1],"w+")
        if line[:-1] == '.T' or line[:-1] == '.A' or line[:-1] == '.W' or line[:-1] == '.B':
            out = True
            #print 'TOTO'
            while out:
                line = fileHandler.readline()
                #print line
                if not line :
                    break
                if line[:-1] == '.N' or line[:-1] == '.X' or line[:-1] == '.K' or line[:-1] == '.I':
                    out = False
                    #print 'OUT',line[:-1]
                    break
                elif line[:-1] != '.T' and line[:-1] != '.A' and line[:-1] != '.W' and line[:-1] != '.B':
                    f.write(line[:-1]+"\n")
    fileHandler.close()

ExtractionDesFichiers(inpfilename,outpathname)

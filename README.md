# ARI-INFO4

La requête traité est dans le fichier requete.txt

Il faut créer les répertoires /files/collection et /files/collection_tokens avant de lancer les programmes.


Lancer fichier split_cacm3.py qui répartit le fichier cacm.all en plusieurs fichiers dans /files/collection.

Lancer tokenize_cacm.py qui ouvre les fichiers précedents et n'écrit que les mots ciblés dans fichiers dans le répertoire /files/collection_token.

Lancer zipf.py pour afficher les mots et leurs fréquence d'apparition et lambda théorique en ordre décroissant.

create_dict.py crée un dictionnaire avec tous les fichiers et leurs mots avec le nombre d'occurrence. Il n'y a pas besoin de le lancer parce qu' il est appelé dans le programme suivant.

Lancer create_vocabulaire.py pour générer le vocabulaire du corpus dans le fichier vocabulaire.json.

create_vecteur.py transforme chaque document dans une représentation vectoriel. Il n'y a pas besoin de le lancer parce qu' il est appelé dans le programme suivant.

Lancer create_inverse.py pour générer l'index inversé du corpus.

Lancer create_norme.py pour calculer la norme des vecteurs.

Lancer create_modele_vectoriel.py pour traiter la requête dans le fichier requete.txt avec le corpus traité.
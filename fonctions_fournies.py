"""
Fonctions fournies à importer et à utiliser pour vous aider dans votre projet
"""
import re

#trie un dictionnaire par ordre décroissant suivant ses valeurs et le retourne
def sort_dict(x):
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse = True)}    


#Retourne sous forme d'entier (int) le premier numéro à 4 chiffres d'une chaine de caractères (pour la colonne 'year')
#retourne -1 si il n'y en a pas ou qu'il pose probème
def release_year(year):
    try:
        y = int(re.search(r"\d{4}", year).group())
    except:
        y = -1
    return y


# Graven exercice 03
# @author: Novitz Jean-Philippe <novitz@gmail.com>
# graven youtube url : https://www.youtube.com/watch?v=sgJt64iTOYM

# Une fonction pour calculer le nombre de voyelles dans un mot

# Définir une fonction get_vowels_numbers(mot)
# Créer un compteur de voyelles
# Pour chaque lettre du mot vérifier s’il s’agit d’une voyelle
# Si c’est le cas, on ajoute au compteur
# A la fin de la fonction, renvoyer le compteur.

def get_vowels_number(chaine):
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    nbr_voyelles = 0
    for i in range(len(chaine)):
        for y in range(len(voyelles)):
            if chaine[i] == voyelles[y]:
                nbr_voyelles += 1
                break
    return nbr_voyelles

mot = input("Entrez un mot: ")

print ("votre mot contient {} voyelles".format(get_vowels_number(mot)))

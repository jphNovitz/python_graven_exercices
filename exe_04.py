# Graven exercice 03
# @author: Novitz Jean-Philippe <novitz@gmail.com>
# graven youtube url : https://www.youtube.com/watch?v=BrknhzrHm8w


# Jeux du juste prix
#
# Choisir un nombre entre 1 et 1000
# Tant que le jeux n’est pas fini (le juste prix n'est pas trouvé)
# → demander à l’utilisateur "entrez un prix"
# → s’il trouve le juste pris ‘cest gagné’
# → sinon on affiche ‘c est moins’ ou ‘c est plus’

import random

prix = random.randint(1, 1000)
nombre = 0

while nombre != prix:
    nombre = int(input("Entrez un nombre: "))
    if nombre > prix:
        print("=> trop grand")
    elif nombre < prix:
        print('=> trop petit')
    else:
        print("== TROUVE ==")
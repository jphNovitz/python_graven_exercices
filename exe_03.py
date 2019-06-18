# Graven exercice 03
# @author: Novitz Jean-Philippe <novitz@gmail.com>
# graven youtube url : https://www.youtube.com/watch?v=kyxF5eH3Kic

# Générateur de phrases
# Demander en console une chaine de la forme ‘mot1/mot2/mot3’
# Transformer cette chaine en une liste
# La melanger
# Si le nombre d’éléments de cette liste est inférieure à 10
# → afficher les deux premiers mots
# Si le nombre d’élements de cette liste est supérieure ou égale à 10
# → afficher les trois derniers

import random
chaine = input("Entrez une chaîne de la forme mot1/mot2/mot3: ")
mots = chaine.split("/")
phrase = ""

print("je melange ...")

random.shuffle(mots)

if len(mots) < 10:
    i = 1
    for i in range(2):
        phrase = phrase + mots[i] + " "
else:
    y = len(mots)-3
    for i in range(3):
        phrase = phrase + mots[y] + " "
        y+=1

print("Votre phrase est: ", phrase)
# Graven exercice 02
# @author: Novitz Jean-Philippe <novitz@gmail.com>
# graven youtube url : https://www.youtube.com/watch?v=nvyX8JfoOWY

# Place de cinema
# Récolter l’age de la personne ‘Quel est votre age ‘
# Si la personne est mineure 7€
# Si la personne est majeure 12€
# Souhaitez-vous du popcorn
# Si oui + 5€
# Afficher ce prix total à payer


age = int(input("Quel est votre age ? "))

if age < 18:
    prix = 7
else:
    prix = 12

print("\nSous Total: ", prix)

pop_corn = input("Voulez-vous du popcorn ? ")

if pop_corn == 'O' or pop_corn == 'o' or pop_corn == 'oui':
    prix += 5

print("\nTOTAL:", prix)
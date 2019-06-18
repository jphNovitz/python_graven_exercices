
# Graven exercices
# @author: Novitz Jean-Philippe <novitz@gmail.com>
# graven youtube url : https://www.youtube.com/watch?v=nvyX8JfoOWY

# Recolter une valeur porte monnaie
# Créer un produit qui aura la valeur 50
# Afficher la nouvelle valeur du porte monnaie après son achat.

produit = 50
porte_monnaie = int(input("Combien y a-t-il dans votre porte monnaie ? "))
print("Vous aviez {}". format(porte_monnaie))
porte_monnaie -= produit
print("Le produit coûte {} eur". format(produit))
print("Il vous reste {} eur". format(porte_monnaie))

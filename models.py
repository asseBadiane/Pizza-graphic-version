

class Pizza:
    nom = ""
    ingredients = ""
    prix = 0
    vegetarian = False

    def __init__(self, nom, ingredients, prix, vegetarian):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix
        self.vegetarian = vegetarian

    def get_dictionnary_pizzas(self):
        return {"nom": self.nom, "ingredients": self.ingredients, "prix": self.prix, "vegetarian": self.vegetarian}
        
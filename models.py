

class Pizza:
    name = ""
    ingredients = ""
    prix = 0
    vegetarian = False

    def __init__(self, name, ingredients, prix, vegetarian):
        self.name = name
        self.ingredients = ingredients
        self.prix = prix
        self.vegetarian = vegetarian

    def get_dictionnary_pizzas(self):
        return {"name": self.name, "ingredients": self.ingredients, "prix": self.prix, "vegetarian": self.vegetarian}
        
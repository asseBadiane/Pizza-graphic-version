from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from models import Pizza
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ObjectProperty 

class PizzaWidget(BoxLayout):
    name = StringProperty()
    ingredients = StringProperty()
    price = NumericProperty()
    vegetarian = BooleanProperty()

class MainWidget(BoxLayout):
    recycleView = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.pizzas = [
            Pizza("4 fromages", "tomate, sucre, oeuf, huile d'olive", 10, True),
            Pizza("champignons", "tomate, sucre, oeuf, huile d'olive", 10, False),
            Pizza("Cerizone", "tomate, sucre, oeuf, huile d'olive", 10, True),
        ]

    def on_parent(self, widget, parent):
        self.recycleView.data = [pizza.get_dictionnary_pizzas() for pizza in self.pizzas]

class PizzaApp(App):
    pass

PizzaApp().run()
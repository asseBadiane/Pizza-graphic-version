from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from models import Pizza
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ObjectProperty 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior
from http_client import HttpClient
from storage_manager import StorageManager
class PizzaWidget(BoxLayout):
    name = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarian = BooleanProperty()

class MainWidget(FloatLayout):
    recycleView = ObjectProperty()
    error_str = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # self.pizzas = [

        #     Pizza("4 fromages", "tomate, sucre, oeuf, huile d'olive", 10, True),
        #     Pizza("champignons", "tomate, sucre, oeuf, huile d'olive", 10, False),
        #     Pizza("Cerizone", "tomate, sucre, oeuf, huile d'olive", 10, True),
        #     Pizza("4 fromages", "tomate, sucre, oeuf, huile d'olive", 10, True),
        #     Pizza("champignons", "tomate, sucre, oeuf, huile d'olive", 10, False),
        # ]

        HttpClient().get_pizzas(self.on_server_data, self.on_server_error, self.on_server_failure)

    # def on_parent(self, widget, parent):
    #     self.recycleView.data = [pizza.get_dictionnary_pizzas() for pizza in self.pizzas]

    def on_server_data(self, pizza):
        self.recycleView.data = pizza
        if StorageManager.load_data:
            StorageManager().save_data("pizzas", pizza)

    def on_server_error(self, error):
        print(f"Erreur: {error}")
        self.error_str = "Erreur: " + error

    def on_server_failure(self, failure):
        print(f"Failure: {failure}")
        self.error_str = "Erreur... " + failure

class PizzaApp(App):
    pass

PizzaApp().run()
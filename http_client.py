from kivy.network.urlrequest import UrlRequest
import json


class HttpClient:

    def get_pizzas(self, on_complete, on_error, on_failure):
        url = "http://assebadiane.pythonanywhere.com/api/get-pizzas"

        def data_received(req, result):
            data = json.loads(result)
            pizzas_dict = []
            for pizza in data:
                pizzas_dict.append(pizza["fields"])
            print("Data received")
            if on_complete:
                on_complete(pizzas_dict)

        # Pour des erreur de connexion réseaux
        def data_error(req, error):
            print("Data Erreur:", str(error))
            if error:
                on_error(str(error))
        
        # Pour les erreus au niveau du serveur
        def data_failure(req, result):
            print(f"Data Failure: {result}")
            if on_error:
                on_error(str(req.resp_status))


        req = UrlRequest(url, on_success=data_received, on_error=data_error, on_failure=data_failure) 
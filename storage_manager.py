import json

class StorageManager:
    def load_data(self, data_name):
        fileName = self.get_fileName(data_name)
        try:
            file = open(fileName, "r")
            data = file.read()
            file.close()
        except:
            return None
        return json.loads(data) # Ici on désarialize nos données

    def save_data(self, data_name, data_content):
        fileName = self.get_fileName(data_name)
        data_str = json.dumps(data_content) # Ici on serialize nos données
        file = open(fileName, "w")
        file.write(data_str)
        file.close()
        
    
    def get_fileName(self, fileName):
        return fileName  + ".json"
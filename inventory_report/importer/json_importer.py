import json
from .importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(caminho):
        if ".json" not in caminho:
            raise ValueError("Arquivo inválido")
        with open(caminho) as file:
            arquivo_json = json.loads(file.read())
        return arquivo_json

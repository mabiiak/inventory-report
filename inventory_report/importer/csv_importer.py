import csv
from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(caminho):
        if ".csv" not in caminho:
            raise ValueError("Arquivo inválido")
        with open(caminho) as file:
            arquivo_csv = list(csv.DictReader(file))
        return arquivo_csv

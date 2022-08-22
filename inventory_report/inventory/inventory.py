from inventory_report.importer.csv_importer import CsvImporter
from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport


class Inventory:
    def checa_tipo_do_arquivo(caminho):
        if "csv" in caminho:
            return CsvImporter.import_data(caminho)

    @classmethod
    def import_data(caminho, tipo):
        arquivo = Inventory.checa_tipo_do_arquivo(caminho)

        if tipo == "simples":
            return SimpleReport.generate(arquivo)
        if tipo == "completo":
            return CompleteReport.generate(arquivo)

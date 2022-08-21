from datetime import datetime
import statistics


class SimpleReport:
    @classmethod
    def checa_fabricacao(cls, lista):
        mais_antigo = sorted(
            lista, key=lambda x: x["data_de_fabricacao"]
        )[0]
        return mais_antigo["data_de_fabricacao"]

    @classmethod
    def checa_validade(cls, lista):
        mais_recente = sorted(
            lista, key=lambda x: x["data_de_validade"]
        )
        data_hoje = datetime.today().strftime("%Y-%m-%d")
        for item in mais_recente:
            if item["data_de_validade"] < data_hoje:
                mais_recente.remove(item)
        return mais_recente[0]["data_de_validade"]

    # https://docs.python.org/pt-br/3/library/statistics.html

    @classmethod
    def maior_fabricante(cls, lista):
        fabricante = statistics.mode(
            empresa["nome_da_empresa"] for empresa in lista
        )
        return fabricante

    @staticmethod
    def generate(lista):
        mais_antigo = SimpleReport.checa_fabricacao(lista)
        validade_recente = SimpleReport.checa_validade(lista)
        empresa = SimpleReport.maior_fabricante(lista)

        return(
              f"Data de fabricação mais antiga: {mais_antigo}\n"
              f"Data de validade mais próxima: {validade_recente}\n"
              f"Empresa com mais produtos: {empresa}"
        )

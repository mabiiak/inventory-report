from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def conta_produtos(cls, lista):
        return Counter(
            produto["nome_da_empresa"]
            for produto in lista
            if produto.get("nome_da_empresa")
        )

    @staticmethod
    def generate(lista):
        relatorio_simples = SimpleReport.generate(lista)
        relatorio_estoque = CompleteReport.conta_produtos(lista)
        relatorio_completo = (
            relatorio_simples + "\nProdutos estocados por empresa:\n"
        )
        for key, value in relatorio_estoque.items():
            relatorio_completo += f"- {key}: {value}\n"
        print(relatorio_completo)
        return relatorio_completo

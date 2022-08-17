from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        1,
        "coquinha",
        "cola-cola",
        "18-08-18",
        "18-09-28",
        "1556 1561 651 5561",
        "Manter gelada"
    )

    assert produto.__repr__() == (
        "O produto coquinha"
        " fabricado em 18-08-18"
        " por cola-cola com validade"
        " até 18-09-28"
        " precisa ser armazenado Manter gelada."
    )

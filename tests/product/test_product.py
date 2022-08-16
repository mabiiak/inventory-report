from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1,
        "coquinha",
        "cola-cola",
        "18-08-18",
        "18-09-28",
        "1556 1561 651 5561",
        "Manter gelada"
    )

    assert produto.id == 1
    assert produto.nome_do_produto == "coquinha"
    assert produto.nome_da_empresa == "cola-cola"
    assert produto.data_de_fabricacao == "18-08-18"
    assert produto.data_de_validade == "18-09-28"
    assert produto.numero_de_serie == "1556 1561 651 5561"
    assert produto.instrucoes_de_armazenamento == "Manter gelada"

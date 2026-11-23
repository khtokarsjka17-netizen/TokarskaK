from variants.variant_12 import solve


def test_first_example():
    assert solve("3", "1 2 3 4 5") == (
        "Суми блоків: 6, 9\n"
        "Максимальна сума у блоці: 2"
    )


def test_negative_numbers():
    assert solve("2", "-1 5 10 -20 3") == (
        "Суми блоків: 4, -10, 3\n"
        "Максимальна сума у блоці: 1"
    )


def test_one_block():
    assert solve("5", "2 3") == (
        "Суми блоків: 5\n"
        "Максимальна сума у блоці: 1"
    )
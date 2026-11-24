import student_starter as M


def test_parse_items():
    text = "d1: Кіт пес;;d2: КІТ ліс"
    assert M.parse_items(text) == [
        ("d1", "кіт"),
        ("d1", "пес"),
        ("d2", "кіт"),
        ("d2", "ліс")
    ]


def test_build_index():
    items = [
        ("d1", "кіт"),
        ("d2", "кіт"),
        ("d1", "пес")
    ]
    assert M.build_index(items) == {
        "кіт": ["d1", "d2"],
        "пес": ["d1"]
    }


def test_rank():
    index = {
        "пес": ["d1"],
        "кіт": ["d1", "d2"],
        "ліс": ["d2", "d3"]
    }
    assert M.rank(index, 2) == [
        ("кіт", ["d1", "d2"]),
        ("ліс", ["d2", "d3"])
    ]


def test_unique_sorted():
    items = [
        ("d1", "пес"),
        ("d1", "кіт"),
        ("d2", "пес")
    ]
    assert M.unique_sorted(items) == ["кіт", "пес"]


def test_solve():
    text = "d1: кіт пес;;d2: кіт ліс;;d3: Кіт"
    expected = (
        "Пар «документ-слово»: 5\n"
        "Унікальних слів: 3\n"
        "Слова за кількістю документів (топ-2):\n"
        "1. кіт: d1, d2, d3\n"
        "2. ліс: d2"
    )
    assert M.solve(text, "2") == expected
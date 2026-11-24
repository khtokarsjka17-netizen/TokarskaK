def parse_items(text):
    items = []

    if text is None:
        return items

    if not isinstance(text, str):
        return items

    for record in text.replace(";;", ";").split(";"):
        record = record.strip()
        if record.count(":") != 1:
            continue

        document, words_text = record.split(":")
        document = document.strip()
        if not document:
            continue

        for word in words_text.split():
            items.append((document, word.lower()))

    return items


def build_index(items):
    index = {}

    for document, word in items:
        if word not in index:
            index[word] = set()
        index[word].add(document)

    return {
        word: sorted(documents)
        for word, documents in index.items()
    }


def rank(index, n):
    if n <= 0:
        return []

    sorted_items = sorted(
        index.items(),
        key=lambda item: (-len(item[1]), item[0])
    )
    return sorted_items[:n]


def unique_sorted(items):
    return sorted({word for _, word in items})


def solve(text, n):
    n_text = str(n).strip()
    if not n_text or not n_text.isdigit():
        return "Помилка: n має бути цілим невід'ємним числом"

    n_value = int(n_text)
    items = parse_items(text)

    if not items:
        return "Помилка: немає даних"

    index = build_index(items)
    unique_words = unique_sorted(items)
    ranked = rank(index, n_value)

    lines = [
        "Пар «документ-слово»: " + str(len(items)),
        "Унікальних слів: " + str(len(unique_words)),
        "Слова за кількістю документів (топ-" + str(n_value) + "):"
    ]

    for position, (word, documents) in enumerate(ranked, start=1):
        lines.append(
            str(position) + ". " + word + ": " + ", ".join(documents)
        )

    return "\n".join(lines)


if __name__ == "__main__":
    text = input()
    n = input()
    print(solve(text, n))

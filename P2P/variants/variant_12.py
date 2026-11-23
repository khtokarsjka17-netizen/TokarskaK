def solve(k_str, seq_str):
    if not k_str.isdigit():
        return "Помилка: розмір блоку має бути додатним числом."

    k = int(k_str)

    if k <= 0:
        return "Помилка: розмір блоку має бути додатним числом."

    if seq_str.strip() == "":
        return "Помилка: послідовність не може бути порожньою."

    parts = seq_str.split()
    numbers = []

    for part in parts:
        if part.startswith("-"):
            if not part[1:].isdigit():
                return "Помилка: некоректні числа."
        elif not part.isdigit():
            return "Помилка: некоректні числа."

        numbers.append(int(part))

    sums = []
    i = 0

    while i < len(numbers):
        block_sum = 0
        j = i

        while j < i + k and j < len(numbers):
            block_sum += numbers[j]
            j += 1

        sums.append(block_sum)
        i += k

    max_sum = sums[0]
    max_block = 1

    for i in range(1, len(sums)):
        if sums[i] > max_sum:
            max_sum = sums[i]
            max_block = i + 1

    result = "Суми блоків: "

    for i in range(len(sums)):
        if i > 0:
            result += ", "
        result += str(sums[i])

    result += "\nМаксимальна сума у блоці: "
    result += str(max_block)

    return result
k_str = input("Введіть розмір блоку: ")
seq_str = input("Введіть послідовність чисел: ")

print(solve(k_str, seq_str))
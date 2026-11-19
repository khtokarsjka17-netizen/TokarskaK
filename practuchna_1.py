def solve(number: str) -> str:
    try:
        value = int(number)
    except (TypeError, ValueError):
        return "Помилка: некоректні дані"

    if value > 0:
        sign = "Додатне"
    elif value < 0:
        sign = "Від'ємне"
    else:
        sign = "Нуль"

    parity = "Парне" if value % 2 == 0 else "Непарне"

    if value % 15 == 0:
        multiple = "FizzBuzz"
    elif value % 3 == 0:
        multiple = "Fizz"
    elif value % 5 == 0:
        multiple = "Buzz"
    else:
        multiple = "Немає"

    return f"Знак: {sign}, Парність: {parity}, Кратність: {multiple}"


if __name__ == "__main__":
    try:
        number = input()
    except EOFError:
        number = ""

    print(solve(number))
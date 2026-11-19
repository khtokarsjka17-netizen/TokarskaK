number = int(input("Введіть число: "))
if number > 0:
    sign = "Додатне"
elif number < 0:
    sign = "Від'ємне"
else:
    sign = "Нуль"

if number % 2 == 0:
    parity = "Парне"
else:
    parity = "Непарне"

if number % 15 == 0:
    multiple = "FizzBuzz"
elif number % 3 == 0:
    multiple = "Fizz"
elif number % 5 == 0:
    multiple = "Buzz"
else:
    multiple = "Немає"

print(f"Знак: {sign}, Парність: {parity}, Кратність: {multiple}")

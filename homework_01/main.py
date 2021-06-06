"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """

    # Список квадратов целых чисел
    numbers_squared = [number * number for number in numbers]

    return numbers_squared


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    """
    функция, которая принимает целое число
    и возвращает наименьший целый делитель этого числа
    """
    counter = 2
    while counter * counter <= number and number % counter != 0:
        counter += 1

    return counter * counter > number


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """

    # Объект типа filter
    numbers_filtered = []

    if filter_type == ODD:
        numbers_filtered = filter(lambda number: (number % 2 != 0), numbers)
    elif filter_type == EVEN:
        numbers_filtered = filter(lambda number: (number % 2 == 0), numbers)
    elif filter_type == PRIME:

        numbers_filtered = filter(is_prime, numbers)

    return list(numbers_filtered)

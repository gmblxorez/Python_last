def average_num(list_num: list) -> float | str:
    converted_list = []
    for el in list_num:
        if isinstance(el, (int, float)):
            converted_list.append(el)
        else:
            try:
                # Пробуем преобразовать в float (чтобы работало и с "10.5", и с "3")
                converted_num = float(el)
                converted_list.append(converted_num)
            except (ValueError, TypeError):
                return "Bad request"
    return round(sum(converted_list) / len(converted_list), 2)


# Тесты для целых чисел
assert average_num([1, 1]) == 1
assert average_num([1, 2, 3, 4, 5]) == 3
assert average_num([-1, 1]) == 0
assert average_num([10, 20, 30, 40]) == 25

# Тесты для чисел с плавающей точкой
assert average_num([2.5, 3.5]) == 3.0
assert average_num([1.5, 2.5, 3.5]) == 2.5
assert average_num([0.1, 0.2, 0.3]) == 0.2

# Тесты для строк, которые можно преобразовать в числа
assert average_num(["1", "2", "3"]) == 2
assert average_num(["10.5", "20.5"]) == 15.5

# Тесты для некорректных данных
assert average_num(["a", "b", "c"]) == "Bad request"
assert average_num([1, 2, "three"]) == "Bad request"


print("Все тесты прошли успешно!")
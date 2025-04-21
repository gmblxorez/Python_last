import unittest
import sys

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFactorial(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_positive_numbers(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_negative_input(self):
        with self.assertRaises(ValueError) as context:
            factorial(-5)
        self.assertEqual(str(context.exception), "Факториал отрицательного числа не определен")

    def test_factorial_overflow(self):
        # Найдем порог, на котором factorial(n) > sys.maxsize
        n = 1
        while True:
            try:
                factorial(n)
                n += 1
            except ValueError:
                break
        # Проверяем, что n действительно вызывает переполнение
        with self.assertRaises(ValueError) as context:
            factorial(n)
        self.assertEqual(str(context.exception), f"Факториал для {n} не поддерживается типом int")

    def test_factorial_large_but_supported(self):
        # Проверяем максимальное n, которое не вызывает переполнение
        n = 1
        while True:
            try:
                res = factorial(n)
                n += 1
            except ValueError:
                n -= 1
                break
        # Убедимся, что для этого n исключение не возникает
        self.assertTrue(isinstance(factorial(n), int))

if __name__ == "__main__":
    unittest.main()
import re

def is_palindrome(text: str) -> bool:
    cleaned_text = re.sub(r'[^a-zA-Zа-яА-ЯёЁ0-9]', '', text.lower())
    return cleaned_text == cleaned_text[::-1]

# Тесты
assert is_palindrome("топот") == True
assert is_palindrome("А роза упала на лапу Азора!") == True
assert is_palindrome("Привет, мир!") == False
assert is_palindrome("LeV3l") == False  
assert is_palindrome("") == True
assert is_palindrome("Лёша на полке клопа нашёл") == True
assert is_palindrome("Я") == True

print("Все тесты прошли успешно!!")
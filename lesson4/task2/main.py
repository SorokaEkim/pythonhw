"""Задача 2. Шестнадцатеричные и десятичные числа"""

def hex2int(hex_char: str) -> int:
    try:
        decimal_num = int(hex_char, 16)
        if 0 <= decimal_num <= 15:
            return decimal_num
        else:
            print("Ошибка.Введенное значение выходит за допустимые границы (0-15).")
    except ValueError:
        print("Ошибка: Некорректный шестнадцатеричный символ.") 


def int2hex(decimal_num: int) -> str:
    try:
        if 0 <= decimal_num <= 15:
            hex_str = hex(decimal_num)[2:]  # Получение шестнадцатеричного эквивалента без префикса "0x"
            return hex_str.upper()  # Возвращаем шестнадцатеричный эквивалент в верхнем регистре
        else:
            print("Ошибка: Введенное число выходит за допустимые границы (0-15).")
    except ValueError:
        print("Ошибка: Некорректное десятичное число.")

print(hex2int('A'))

print(int2hex(10))
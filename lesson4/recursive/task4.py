"""Задача 4. Римские цифры"""

def roman_to_decimal(roman):
    if not roman:
        return 0
    
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    if len(roman) > 1 and roman_numerals[roman[0]] < roman_numerals[roman[1]]:
        return roman_numerals[roman[1]] - roman_numerals[roman[0]] + roman_to_decimal(roman[2:])
    else:
        return roman_numerals[roman[0]] + roman_to_decimal(roman[1:])


roman_numeral = input("Введите число, записанное римскими цифрами: ")
decimal_num = roman_to_decimal(roman_numeral)
print(f"Ответ: {decimal_num}")






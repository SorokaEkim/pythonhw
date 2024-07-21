"""Задача 2. Какого цвета клетка?"""

CHESSBOARD_NUMBERS = range(1,9)
CHESSBOARD_LETTERS = ['a','b','c','d','e','f','g','h']

while True:
    letter = input('Введите букву из шахматной доски: ')
    number = int(input('Введите цифру из шахматной доски: '))

    if letter not in CHESSBOARD_LETTERS:
        print('Допустимые буквы от "a" до "h"')
    elif number not in CHESSBOARD_NUMBERS:
        print('Допустимые цифры от "1" до "8"')
    else:
        letter_index = CHESSBOARD_LETTERS.index(letter)
        number_index = CHESSBOARD_NUMBERS.index(number)

        if letter_index % 2 == number_index %2:
            print("Черная клетка!")
        else:
            print("Белая клетка!")
"""" Задача 1. Собачий возраст. """

FIRST_TWO_YEAR_DOG = 10.5

while True:
    age_human = int(input('Укажите свой возраст: '))

    if FIRST_TWO_YEAR_DOG * 2 <= age_human:
        age_dog = ((age_human - FIRST_TWO_YEAR_DOG * 2) / 4) + 2
    else:
        age_dog = age_human / FIRST_TWO_YEAR_DOG

    print('Ваш собачий возраст: {:.1f} лет'.format(age_dog))
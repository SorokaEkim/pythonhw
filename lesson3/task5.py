"""Задача 5. Ниже и выше среднего."""
numbers = []

while True:
    num = input('Введите число ')
    
    if num == '':
        break
    else:
        numbers.append(int(num))
        
average = sum(numbers) / len(numbers)
print(f'Среднее число ряда чисел {average}')

print('Список чисел ниже среднего:')
for number in numbers:
    if number < average:
        print(number)

print('Список чисел выше среднего:')
for number in numbers:
    if number > average:
        print(number)

print('Числа равные среднему:')
for number in numbers:
    if number == average:
        print(number)


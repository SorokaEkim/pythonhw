""" Задача 1. Сумма значений """

total = 0.0

def addition(total):
    num = input('Введите число: ')

    if num == "":
        print(f"Конец: {total}")
    else:
        total = total + float(num)
        print(total)
        return addition(total)
    
addition(total)
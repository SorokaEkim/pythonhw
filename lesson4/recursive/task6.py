def can_assemble_sum(sum_value, num_coins):
    if sum_value == 0:
        return True
    if num_coins == 0 or sum_value < 1:
        return False

    # извлечь монету номиналом в 25 центов
    if sum_value >= 25 and can_assemble_sum(sum_value - 25, num_coins - 1):
        return True
    elif sum_value >= 10 and can_assemble_sum(sum_value - 10, num_coins - 1):
        return True
    elif sum_value >= 5 and can_assemble_sum(sum_value - 5, num_coins - 1):
        return True
    elif sum_value >= 1 and can_assemble_sum(sum_value - 1, num_coins - 1):
        return True

    return False

sum_value = int(input("Введите сумму в центах: "))
num_coins = int(input("Введите количество монет: "))

if can_assemble_sum(sum_value, num_coins):
    print("Сумму можно собрать при помощи заданного количества монет.")
else:
    print("Сумму нельзя собрать при помощи заданного количества монет.")
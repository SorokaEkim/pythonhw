""" Задача 7. Выравниваем список """

array = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]

def flatting(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatting(item))
        else:
            flat_list.append(item)
    return flat_list


result = flatting(array)

print(result)
    
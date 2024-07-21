""" Задача 8. Декодирование на основе длин серий """

def decode_rle(encoded_list, index=0, decoded_list=None):
    if decoded_list is None:
        decoded_list = []

    if index >= len(encoded_list):
        return decoded_list

    element = encoded_list[index]
    count = encoded_list[index + 1]

    decoded_list.extend([element] * count)

    return decode_rle(encoded_list, index + 2, decoded_list)


encoded_list = ["A", 12, "B", 4, "A", 6, "B", 1]
decoded_list = decode_rle(encoded_list)
print(decoded_list)
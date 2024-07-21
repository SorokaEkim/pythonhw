""" Задача 9. Кодирование на основе длин серий """

def rle_encode(data):
    def encode_recursive(data, index, current_char, count, result):
        if index == len(data):
            if count > 0:
                result.append((current_char, count))
            return result
        
        if data[index] == current_char:
            return encode_recursive(data, index + 1, current_char, count + 1, result)
        else:
            if count > 0:
                result.append((current_char, count))
            return encode_recursive(data, index + 1, data[index], 1, result)
    
    if not data:
        return []
    
    return encode_recursive(data, 1, data[0], 1, [])

if __name__ == "__main__":
    user_input = input("Введите строку для сжатия: ")
    encoded_data = rle_encode(user_input)
    print("Закодированный список:", encoded_data)
""" Задача 3. Фонетический алфавит """

def transcript(word):
    data = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
        'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 
        'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 
        'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 
        'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 
        'Y': 'Yankee', 'Z': 'Zulu',
    }

    word = word.upper()
    if word == '':
        return ''
    else:
        if word[0] in data:
            letter_code = data[word[0]]
        else:
            letter_code = ''

        return letter_code + ' ' + transcript(word[1:])

word = input('Введите слово: ')

print(transcript(word))


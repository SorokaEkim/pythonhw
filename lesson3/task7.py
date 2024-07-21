points = {
    'AEILNORSTU': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10
}

word = input('Введите слово: ')
word = word.upper()

result = []

for letter in word:
    for key, value in points.items():
        if letter in key:
            result.append(value)

print(f'Количество очков {sum(result)}')
            
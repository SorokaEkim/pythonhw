""" Задача 1. Книги без буквы E. """

forbidden_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '/', '-', '«', '–', '»', '(', ')', '!']
counts = {}

file = open("./lesson6/task1/text.txt", "r", encoding="utf-8")
words = file.read().split()

for word in words:
    for letter in word.upper().rstrip():
        if letter in forbidden_symbols:
            continue
        else:
            try:
                counts[letter] += 1
            except KeyError:
                counts[letter] = 1
            
file.close()

total = sum(counts.values())

for symbol in counts:
    print(f'{symbol} -> {round(counts[symbol] / (total / 100), 2)}%')

smallest_count = min(counts.values())

key = next(key for key, value in counts.items() if value == smallest_count)

print(f'Самая редкая буква "{key}"')




"""Задача 4. Избавляемся от дубликатов."""

word = True
words = []

while word != '':
    word = input('Введите слово: ')
    if word == '':
        continue
    elif word not in words:
        words.append(word)
    else:
        continue

if len(words) == 0:
    print('Вы ничего не ввели :(')
else:
    for word in words:
        print(word, sep='/n')


from neuron import Neuron

questions = [
    'У вас есть свободное время для игры в LOL? "Y"->Да, "N"->Нет\n',
    'Есть ли у вас настроение для игры в LOL? "Y"->Да, "N"->Нет\n',
    'Есть ли потребность в общении? "Y"->Да, "N"->Нет\n',
    'Кушали ли вы сегодня? "Y"->Да, "N"->Нет\n'
]

Xi = []
# Задаем входной вектор
for question in questions:
    while True:
        answer = input(question)
        if answer.upper() == 'Y':
            answer = 1
            break
        elif answer.upper() == 'N':
            answer = 0
            break
        else:
            print("Вы введи не корректные данные")
    Xi.append(answer)
        
bias = 9 # порог срабатывания
# Задаем вектор весов ('Свободное время; Настроение; Общение; Человеческие потребности')
Wi = [5, 4, 2, 2]
n = Neuron(Wi)
s = n.у(Xi) - bias

if n.onestep(s) == 1:
    print('Идем играть')
else:
    print('Не идем')
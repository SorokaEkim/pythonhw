while True:
    number = int(input('Назовите число от 1 до 100: '))

    if number > 100:
        print('Число больше 100')
    else:
        if number % 3 == 0:
            print('Fizz')
        if number % 5 == 0:
            print('Buzz')
        if (number % 3 == 0) and (number % 5 == 0):
            print('Fizz-Buzz')
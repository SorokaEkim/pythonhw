num = int(input('Введите число: '))
numbers = [i for i in range(num + 1)]
numbers[1] = 0

p = 2
print(numbers)
while p <= num:
    if numbers[p] != 0:
        j = p + p
        while j <= num:
            numbers[j] = 0
            j += p
    print(numbers)
    p += 1

numbers = [i for i in numbers if i != 0]


        
    
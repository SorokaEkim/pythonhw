""" Задача 2. Наибольший общий делитель """

def gcd_fun(a, b): 
    if(b == 0): 
        return a 
    else: 
        return gcd_fun(b, a % b) 
    

a =int(input("Введи первое число: ")) 
b =int(input("Введите второе чсисло: ")) 
num = gcd_fun(a, b)

print(num)

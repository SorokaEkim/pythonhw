import random
from data import LETTERS_LIST, NUMBERS_LIST

def buildNumber():
    #Старый формат
    letters = ''.join(random.choice(LETTERS_LIST) for letter in range(3))
    numbers = ''.join(random.choice(NUMBERS_LIST) for letter in range(random.choice((3,4))))

    return letters + numbers

if __name__ == "__main__":
    print(buildNumber())



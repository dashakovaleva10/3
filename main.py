import os
import random
#clear = lambda:os.system('clear')

print('Привет! Я загадал слово, твоя задача - угадать его по буквам.')
input('*Нажми Enter, чтобы продолжить*')
#clear()
print('Поехали!')

words = ['барышня','квокка','фламинго','грация','жемчужина','лакомство','мотылёк','параллель','прелесть']
word = random.choice(words)

letters = []
isWin = True
hp = 10

while hp > 0:
    isWin = True

    for symb in word:
        if symb in letters:
            print(symb, end=' ')
        else:
            print('*', end=' ')
            isWin = False
    print()

    if isWin:
        print('Ты выйграл(а). молодец!')
        break

    letter = input('Введите букву: ')
    letters.append(letter)
    print(letters)

    if letter not in word:
        hp -=1
        print(f'Осталось попыток: {hp}')

if hp == 0:
    print('Ты проиграл! У тебя закончились попытки.')


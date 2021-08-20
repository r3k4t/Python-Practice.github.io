#Problrm. This is not a correct solution

import random as r
sccret_age = r.randiant(1,10)
flag=False


def game_func(guessed_age,secret):
    if guessed_age < secret:
        return 'Tool low'
    elif guesses_age > secret:
        return "Too High"
    else:
        return 'CORRECT'


for i in range(1,6):
    print("Take a guess.You have "+str(6-i)+" guesses left.")
    guess = input()
    if game_func(int(guess),secret_age) == 'CORRECT !' :
        print("YOU WON THE GAME")
        flag = True
        break


if not flag:
    print('you lost the game!')
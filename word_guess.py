import random

list = ['cat', 'rat', 'mouse','rabbit','horse', 'chiwawa']

random_word = random.choice(list)

guess_limit = 8
guessed_word = ''


while guess_limit > 0:

    wrong_guess = 0
    #checking if guessed word is part of the random word generated
    for character in random_word:
        if character in guessed_word:
            print(f'correct: {character}')
        else:
            wrong_guess += 1
            print("_")

    #if all letters are guessed correctly
    if wrong_guess == 0:
        print("correct!")
        print(f"word = {random_word}")
        break

    guess = input("make a guess: ")
    guessed_word += guess

    if guess not in random_word:
        guess_limit -= 1
        print(f"wrong guess!, you have {guess_limit} chances more")


    if guess_limit == 0:
        print("Game Over")


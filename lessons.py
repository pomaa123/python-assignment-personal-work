from random import randint

### A function for calculating the average of exams score ###

def average_score():
    number = int(input("How many subjects did you take: "))
    list = []
    while True:
        scores = int(input("Enter score " + str(len(list) + 1) + ": "))
        list = list + [scores]
        #comparing the number of subjects to the number of scores to be provided by the user
        lenght = len(list)
        if lenght == number:
            break
    average = sum(list)/len(list)
    print("Your average score is: ",average)
    return average

average_score()


# finding the grade of the score provided by the student##
def grade_score(average_score):
    if average_score > 70:
        return 'A'
    elif 70 > average_score >=60:
        return 'B'
    elif 60 > average_score >=50:
        return 'C'
    elif 50 > average_score >=40:
        return 'D'
    else:
        return 'Trialled'


grade_score(60.5)


### A program that adds and multiply two numbers ###
def add_numbers():
    first_number = int(input("Enter your first number: "))
    second_number = int(input("Enter your second number: "))
    total = first_number + second_number
    mult = first_number * second_number
    return total,mult

a = add_numbers()
print("The sum and product of your numbers are: ", a)


def guess_game():
    #produce a random number
    secret_number = randint(1,20)
    user_entry = int(input("Guess a number: "))
    guesses = 0
    for number_of_guess in range(6):
        if secret_number < user_entry:
            print("Your guess is too high!!")
            user_entry = int(input("Guess another number: "))
             
        elif secret_number > user_entry:
            print("Your guess is too low!!")
            user_entry = int(input("Guess another number: "))

        elif secret_number == user_entry:
            print("Good job!\n you guessed right in " +str(number_of_guess + 1) + " guesses!")
            break
        else:
            print("The answer is: " ,secret_number)

guess_game()


##### the collaz problem from the python book ###########
def number():
    user_input = int(input("Enter any number: "))
    return user_input


def collaz(number):
    num = number()
    
    while num > 1:
        print(num)

        if num % 2 == 0:
            a = num//2
            # print(a)
            num = a
            if num == 1:
                print(num)
                continue  
        elif num % 2 == 1:
            b = 3*num + 1
            # print(b)
            num = b
        
        
collaz(number)




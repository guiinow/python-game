from random import randint

random_value = randint(1, 50)
print(random_value)

user_name = input("Hey there, my name is Boot, what is yours? ")
print(user_name, " this is how it's gonna work:")
print("You will have 5 chances to guess the secret number that I am thinking of in a range between 1 and 50, got it?")
print("Let's game \n")

user_attempts = 4

for i in range(5):
    user_guess = int(input("So wich number do you have in mind? "))

    won = (user_guess == random_value)
    guessBigger = (user_guess > random_value)

    if (won):
        print(user_name, "congrats, you've won!")
        break
    elif (guessBigger):
        print("Sorry, I though of a number a little bit smaller")
    else:
        print("Sorry, I though of a number a little bit bigger")

    if (user_attempts == 0):
        print("Unfortunately you ran out of chances, the correct answer was: ", random_value)
        break
    
    print("Attempts left: ", user_attempts)
    user_attempts-=1
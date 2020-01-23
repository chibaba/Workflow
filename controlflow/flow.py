# __author__ = "dev"
# name = input("please enter your name: ")
# age =  int(input("How old are you, {0}? ".format(name)))
# print(age)

# if age >= 18:
#     print("you are old enough to vote")
#     print("please put an x in the ballot box")
# else:
#     print("please come back in {0}".format(18 - age))

print("please guess a number between 1 and 10: ")
guess = int(input())

if guess < 5:
    print("please guess higher")
    guess = int(input())
    if guess == 5:
        print("well done, you guessed right")
elif guess > 5:
        print("please guess lower")
        guess = int(input())
        if guess == 5:
            print("well done, you guesses right")
        else:
            print("sorry you have not guessed right")
else:
    print("you guessed right the first time")
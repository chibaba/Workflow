# age = int(input("How old are you? "))
# if (age < 16) or (age < 65):
#     print("Enjoy your free time")
# else:
#     print("enjoy your day at work")

parrot = "Norwegian blue"

letter = input('enter a character: ')

if letter in parrot:
    print("Give me an {}, Bob".format(letter))
else:
    print('i dont need that letter')
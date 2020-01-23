name = input("please enter your name: ")
age =  int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("you are old enough to vote")
else:
    print("please come back in {0}".format(18 - age))
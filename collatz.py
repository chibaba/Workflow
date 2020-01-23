number = int(input("enter a number jor: "))
counter = 0
while number != 1:
    if number % 2 != 0:
        number = number * 3 + 1
    else:
        number = number / 2
    counter = counter + 1
    print(number)
print("counter=", counter)
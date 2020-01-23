number = int(input("please enter a number"))

sum_of_numbers=0

for i in range(1, number):
    if number % i == 0:
        print(i)
        sum_of_numbers = sum_of_numbers + i

print("total = ", sum_of_numbers)

if sum_of_numbers == number:
    print(number, "is a perfect number")
elif sum_of_numbers > number:
    print(number, "is an abundant number")
else:
    print(number, "is a deficient number")
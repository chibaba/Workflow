number = "9,234,765,987,023"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("the number is {}".format(newNumber))

for state in ["not pinin'","no more","a stiff","ereft of life"]:
    print("This parrot is "+ state)
    
for i in range(1, 20):
    print("i is now {}".format(i))
    
number2 = "6,548,924,874,784"
for i in range(0, len(number)):
    print(number2[i])
    
    for i in range(0, 100, 5):
        print("i is {}".format(i))
    
for i in range(1,13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i, j, i*j))
    print("===============")
    
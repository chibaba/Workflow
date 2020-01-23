shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == 'spam':
        continue
    print("buy " + item)
    
meal = ["egg", "bacon", "tomato", "sausage"]

nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("i'll have a plate of that, then chese please")   
if nasty_food_item == 'spam':
    print("cant i have anything without spam in it")

for i in range(2, 11):
    number_str = ''
    
    for j in range(1, i):
        number_str += str(j)
    number = int(number_str)
    ans = number * 9 + i
    #print(number, 'x', 9, '+', i, '=', ans)
    print("{0:>10} x 9 + {1} = {2}".format(number,i,ans))
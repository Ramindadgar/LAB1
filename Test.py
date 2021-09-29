import math

side = input('plz enter a number: ')
if side.isdigit():
    shape = input('plz enter a shape:1)a, 2)b ')
    if shape == '1':
        result = math.pow(int(side), 3)  
    else:
        result = math.pow(int(side), 3) // (6 * math.sqrt(2))
    print(f'your side is {side} and your result is: {result}')
else:
    print('wrong input')

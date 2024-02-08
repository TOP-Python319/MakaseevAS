number = int(input('enter 3-digit number '))
d3 = number % 10 
d2 = (number // 10) % 10
d1 = (number // 100) % 10
print(f'summ of {d1} {d2} {d3} = {d1 + d2 + d3}') 
print (f'multiplication of {d1} {d2} {d3} = {d1 * d2 * d3}')
number1 = int(input('введите первое число '))
number2 = int(input('введите второе число '))

if number1 % number2 == 0: 
    print(f'{number1} делится на {number2} нацело ')
    print(f'частное: {number1 // number2}')
elif number1 % number2 != 0:
    print(f'{number1} не делится на {number2} нацело ')
    print(f'неполное частное: {number1 // number2}')
    print(f'остаток: {number1 % number2}')

# введите первое число 8
# введите второе число 4
# 8 делится на 4 нацело
# частное 2
    
# введите первое число 10
# введите второе число 3
# 10 не делится на 3 нацело 
# неполное частное: 3
# остаток: 1

# комментарий преподавателя:
# всё чисто, вопросов нет. =)
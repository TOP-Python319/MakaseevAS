year = int(input('введите год чтобы узнать високостный ли он '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('да')
else :
    print('нет')

#введите год чтобы узнать високостный ли он 2023
#нет
    
#введите год чтобы узнать високостный ли он 2020
#да

# комментарий преподавателя:
# всё чисто, вопросов нет. =)
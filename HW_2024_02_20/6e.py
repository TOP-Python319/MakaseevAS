#Написать программу, которая проверяет транспортный билет.
#
#Отрывные билеты старого формата в наземном общественном транспорте содержали номер из шести цифр. Билетик считался «счастливым», если сумма первых трёх цифр совпадала с суммой последних трёх цифр.



#Пример ввода 1:
#    183534

#Пример вывода 1:
#    да

#Пример ввода 2:
#    401367

#Пример вывода 2:
#    нет
# Вариант 1 
number = (input('укажите номер вашего билета '))
if (int(number[0]) + int(number[1]) + int(number[2]) == (int(number[3]) + int(number[4]) + int(number[5]))) :
    print('да')
else :
    print('нет')
#укажите номер вашего билета 183534
#да
    
#укажите номер вашего билета 401367
#нет
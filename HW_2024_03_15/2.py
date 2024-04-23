#Написать программу, которая генерирует форматированную строку.
#
#Программа в цикле получает из stdin названия фруктов (цикл прерывается при вводе пустой строки).
#Программа выводит в stdout строку с перечислением всех фруктов, добавляя перед последним фруктом союз "и", а перед предыдущими (при их наличии) фруктами добавляя запятые (см. примеры вывода).
#
#Пример ввода 1:
#    яблоко
#
#Пример вывода 1:
#    яблоко
#
#Пример ввода 2:
#    яблоко
#    груша
#
#Пример вывода 2:
#    яблоко и груша
#
#Пример ввода 3:
#    яблоко
#    груша
#    апельсин
#
#Пример вывода 3:
#    яблоко, груша и апельсин
#
#Пример ввода 4:
#    яблоко
#    груша
#    апельсин
#   лимон
#
#Пример вывода 4:
#    яблоко, груша, апельсин и лимон

#fruits_list = []
#while True :
#    fruits = (input('введите названия фруктов '))
#    if not fruits :
#        break
#    else :
#        fruits_list.append(fruits)
#new_fruits_list = ", ".join(fruits_list[:-1])
#if len(fruits_list) > 1 :
#    new_fruits_list += ' и '
#new_fruits_list += fruits_list[-1]   
#print(new_fruits_list)

fruits = []
while True:
    fruit = input()
    if fruit:
        fruits.append(fruit)
    else:
        break
 
if len(fruits) == 1:
    print(fruits[0])
else:
    formatted_string = ", ".join(fruits[:-1]) + " и " + fruits[-1]
    print(formatted_string)
#введите названия фруктов яблоко
#введите названия фруктов апельсин
#введите названия фруктов мандарин
#введите названия фруктов 
#яблоко, апельсин и мандарин
#Написать программу, которая проверяет, является ли один список частью другого списка.
#
#Программа два раза получает из stdin произвольное количество целых чисел, разделённых пробелом. Из каждого ввода формируется отдельный список объектов int.
#
#Далее, программа определяет, можно ли из первого списка выбрать срез с шагом по умолчанию (единица) так, чтобы получился второй список.
#    В решении не обязательно использовать именно срезы, есть много разных способов.
#
#Программа выводит в stdout текстовый ответ.
#
#Примечание: пустой список является частью любого списка, включая пустой.
#
#Пример ввода 1:
#    1 2 3 4
#    1 2
#
#Пример вывода 1:
#    да
#
#Пример ввода 2:
#    1 2 3 4
#    2 4
#
#Пример вывода 2:
#    нет

# list_1 = list(map(int, input("введите числа первого списка ").split()))
# list_2 = list(map(int, input("введите числа второго списка ").split()))

# if str(list_2)[:] in str(list_1)[::1]:
#     print("да")
# else :
#     print("нет")



# list1 = list(map(int, input().split()))
# list2 = list(map(int, input().split()))
 
# # Проверяем, является ли list2 частью list1
# def is_subset(lst1, lst2):
#     if not lst2:
#         return True
#     for i in range(len(lst1) - len(lst2) + 1):
#         if lst1[i:i+len(lst2)] == lst2:
#             return True
#     return False
 
# if is_subset(list1, list2):
#     print("да")
# else:
#     print("нет")

list1 = list(input())
list2 = list(input())
del list1[1::2]
del list2[1::2]
x = 'да'
y = 'нет'
 
for i in range(len(list1) - len(list2) + 1):
       if list2[i] in list1[i]:
              print(x)
              break
       else:
              print(y)
              break
       
print(list1)
print(list2)

# 1 2 3 4
# 1 2
# да
# ['1', '2', '3', '4']
# ['1', '2']

# 1 2 3 4
# 2 4
# нет
# ['1', '2', '3', '4']
# ['2', '4']

# Комментарий преподавателя:
# всё верно
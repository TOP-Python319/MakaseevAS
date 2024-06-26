# Написать программу, которая подсчитывает количество простых чисел среди всех чисел одной разрядности.

# Программа получает из stdin натуральное число n — количество разрядов.
# Далее, с помощью вложенных циклов программа считает количество простых чисел среди всех n-значных чисел.
# Результат программа выводит в stdout.

# Примечание: простые числа делятся только на единицу и на само себя.

# Подсказка: конкатенация последовательностей может быть осуществлена посредством умножения на число:
#     >>> 'z' * 4
#     'zzzz'

# Пример ввода:
#     3

# Пример вывода:
#     143


# Пояснение задачи:

# Простое число - число, которое делится без остатка только на себя и на единицу
# 7 делится только на 7 и на 1, значит 7 простое число.
# 9 делится на 9, на 3 и на 1, значит 9 не является простым числом.
# 12 делится на 12, на 6, на 4, на 3, на 2 и на 1, значит 12 не является простым числом.
# 619 делится только на 619 и на 1, значит 619 простое число.

# n-значное число:
# подразумевается, что пользователь вводит количество разрядов в переменную n
# 2-значные числа: все числа в диапазоне от 10 до 99
# 3-значные числа: все числа в диапазоне от 100 до 999
# 4-значные числа: все числа в диапазоне от 1000 до 9999
# и т. д.

# таким образом:
# 1. пользователь вводит количество разрядов
# 2. программа строит диапазон n-значных чисел
# 3. программа ищет в этом диапазоне простые числа
# 4. программа подсчитывает количество простых чисел в этом диапазоне


# ввод пользователем количества разрядов
n = int(input())

# находим конец диапазона
# если пользователь ввёл 2, то int('1' + '0' * 2) -> int('1' + '00') -> int('100') -> 100
# если пользователь ввёл 4, то int('1' + '0' * 4) -> int('1' + '0000') -> int('10000') -> 10000
end_number = int('1' + '0' * n)

# находим начало диапазона
# так как конец диапазона нам уже известен, то просто делим его на 10
start_number = end_number // 10

# инициализируем переменную, в которой мы будем вести подсчёт простых чисел
count = 0

# создаём диапазон с помощью range()
# если пользователь ввёл в начале 3
# это будет значить, что start_number = 100, end_number = 1000
# а range(100, 1000) даст нам диапазон от 100 до 999, т. к. правая граница в range() не включается
for num in range(start_number, end_number):

    # внутри первого цикла запускаем второй цикл, в котором мы перебираем все возможные делители числа
    # то есть, для каждого num мы перебираем все числа от 2 до num-1
    for div in range(2, num):

        # проверяем делится ли num на какие-то числа из диапазона от 2 до num-1 без остатка
        # простое число по определению не может делится без остатка на что-то кроме себя самого (num) и 1
        # если же находится какой-то ещё делитель, то это означает, что число не является простым
        # и можно прервать выполнение второго цикла (внутреннего)
        if num % div == 0:
            # этот break прерывает выполнение только внутреннего цикла, внешний цикл переходит на следующую итерацию
            # с новым значением num и с новыми проверками на деление
            break

        # если не нашёлся делитель (div), на который число num разделилось без остатка,
        # значит мы нашли простое число
        # и можно увеличить значение переменной count на единицу
        elif num % div != 0 and div == num - 1:
            count += 1

# таким образом мы нашли все простые числа в заданном диапазоне
# и теперь можем вывести их количество
print(count)    


# решение двумя разными способами! Я доволен. =)
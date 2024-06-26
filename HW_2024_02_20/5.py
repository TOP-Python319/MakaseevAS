#Написать программу, которая подсчитывает стоимость отправки телеграммы.
#
#В прошлом веке для отправки коротких текстовых сообщений люди использовали телеграммы. В разное время их стоимость рассчитывалась по-разному. 
# Но при передаче телеграмм по ключу (морзянкой) стоимость отправки телеграммы зависит от количества знаков. 
#В нашей задаче примем, что один символ буквы или цифры стоит тридцать копеек.
#
#Программа получает из stdin строку с текстом телеграммы.
#Программа выводит в stdout стоимость в рублях и копейках, согласно формату в примере ниже.
#
#Пример ввода:
#    грузите апельсины бочках братья карамазовы

#Пример вывода:
#    11 руб. 40 коп.
message = (input('введите ваше сообщения для посчета стоимости телеграммы '))
kopeck = (len(message) - message.count(' ')) * 30
print(f'цена будет равна {kopeck // 100} рублей {kopeck % 100} копеек')

# введите ваше сообщения для посчета стоимости телеграммы грузите апельсины бочках братья карамазовы
#цена будет равна 11 рублей 40 копеек


# комментарий преподавателя:
# все верно
x = (input('введите координаты первой клетки '))
y = (input('введите координаты второй клетки '))
dif_1 = (ord(x[0]) - ord(y[0]))
dif_2 = (int(x[1]) - int(y[1]))
if abs(dif_1) and abs(dif_2) <= 1:
    print('да')
else :
    print('нет')
#введите координаты первой клетки g3
#введите координаты второй клетки f2
#да
    
#введите координаты первой клетки g4
#введите координаты второй клетки h7
#нет